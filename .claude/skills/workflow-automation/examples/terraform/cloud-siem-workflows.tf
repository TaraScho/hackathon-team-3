#=============================================================================
# DATADOG WORKFLOW AUTOMATION - CASE CREATION
# Conditionally creates workflow to create cases for AWS security signals
#=============================================================================

provider "datadog" {
  alias   = "scoped"
  api_key = var.datadog_api_key
  app_key = var.datadog_scoped_app_key
}

# AWS Action Connection for Workflow Automation
# This connection allows workflows to assume the IAM role for AWS operations
resource "datadog_action_connection" "aws_iam_connection" {
  provider = datadog.scoped
  count    = var.create_case_workflow && var.datadog_scoped_app_key != "" ? 1 : 0
  name     = "AWS IAM Management Connection [LAB EXAMPLE]"
  
  aws {
    assume_role {
      account_id = var.aws_account_id
      role       = var.datadog_iam_management_role_name
    }
  }
}

resource "datadog_workflow_automation" "create_case_for_aws_security_signal" {
  provider    = datadog.scoped
  count       = var.create_case_workflow && var.datadog_scoped_app_key != "" ? 1 : 0
  name        = "Create case for AWS security signal [LAB EXAMPLE]"
  description = "Automatically creates security cases and investigates AWS security signals"
  tags        = ["security", "aws", "terraform"]
  published   = true
  depends_on = [datadog_action_connection.aws_iam_connection]

  spec_json = jsonencode(
    {
      "triggers": [
        {
          "startStepNames": [
            "Get_security_signal"
          ],
          "securityTrigger": {}
        }
      ],
      "steps": [
        {
          "name": "Get_security_signal",
          "actionId": "com.datadoghq.dd.cloudsecurity.getSecuritySignal",
          "parameters": [
            {
              "name": "signalId",
              "value": "{{ Source.securitySignal.id }}"
            }
          ],
          "outboundEdges": [
            {
              "nextStepName": "Get_User_or_Role_Name",
              "branchName": "main"
            }
          ],
          "display": {
            "bounds": {
              "x": 0,
              "y": 216
            }
          }
        },
        {
          "name": "Get_User_or_Role_Name",
          "actionId": "com.datadoghq.datatransformation.func",
          "parameters": [
            {
              "name": "script",
              "value": "/**\n* The code extracts the userIdentityArn from the security signal\n* and returns either the IAM Role or IAM User name for later use in the workflow.\n*/\n\nvar identityArn = $.Steps.Get_security_signal.securitySignal.custom.userIdentity.arn;\nconsole.log(identityArn)\n\n// Split the ARN and return the user or role name\nvar arnParts = identityArn.split('/');\nreturn arnParts[arnParts.length - 1]; // Returns the last part after the final '/'"
            },
            {
              "name": "description",
              "value": ""
            }
          ],
          "outboundEdges": [
            {
              "nextStepName": "Set_workflow_variables",
              "branchName": "main"
            }
          ],
          "display": {
            "bounds": {
              "x": 0,
              "y": 432
            }
          }
        },
        {
          "name": "Set_workflow_variables",
          "actionId": "com.datadoghq.core.setVariables",
          "parameters": [
            {
              "name": "variables",
              "value": [
                {
                  "name": "detection_rule_name",
                  "value": "{{ Steps.Get_security_signal.detectionRule.name }}"
                },
                {
                  "name": "iam_entity_name",
                  "value": "{{ Steps.Get_User_or_Role_Name.data }}"
                },
                {
                  "name": "cloud_siem_investigator_link",
                  "value": "https://app.datadoghq.com/security/investigator/aws?filter=&id={{ Steps.Get_User_or_Role_Name.data }}"
                }
              ]
            }
          ],
          "outboundEdges": [
            {
              "nextStepName": "Map_signal_severity_to_case_priority",
              "branchName": "main"
            }
          ],
          "display": {
            "bounds": {
              "x": 0,
              "y": 576
            }
          }
        },
        {
          "name": "Map_signal_severity_to_case_priority",
          "actionId": "com.datadoghq.datatransformation.expression",
          "parameters": [
            {
              "name": "script",
              "value": "`P$${5 - $.Steps.Get_security_signal.securitySignal.severity}`"
            },
            {
              "name": "description",
              "value": "Maps the signal severity (medium, high, critical) with the appropriate case priority (P3, P2, P1)."
            }
          ],
          "outboundEdges": [
            {
              "nextStepName": "Create_security_case",
              "branchName": "main"
            }
          ],
          "display": {
            "bounds": {
              "x": 0,
              "y": 768
            }
          }
        },
        {
          "name": "Create_security_case",
          "actionId": "com.datadoghq.dd.casem.createCase",
          "parameters": [
            {
              "name": "project_id",
              "value": "cc541359-56c4-4ac7-be5e-7d99151813df"
            },
            {
              "name": "status",
              "value": "OPEN"
            },
            {
              "name": "title",
              "value": "Investigate actions for {{ Steps.Get_security_signal.securitySignal.custom.userIdentity.arn }}"
            },
            {
              "name": "type_id",
              "value": "00000000-0000-0000-0000-000000000003"
            },
            {
              "name": "priority",
              "value": "{{ Steps.Map_signal_severity_to_case_priority.data }}"
            },
            {
              "name": "description",
              "value": "Identity {{ Variables.iam_entity_name }} generated security signal for {{ Variables.detection_rule_name }}.\n\nActions to take: \n- Review the [signal]({{ Source.securitySignal.url }}) \n- Investigate entity with [Cloud SIEM Investigator]({{ Variables.cloud_siem_investigator_link }}) \n- Review logs attached and active access keys available in case comments"
            }
          ],
          "outboundEdges": [
            {
              "nextStepName": "Search_logs_by_IAM_arn",
              "branchName": "main"
            },
            {
              "nextStepName": "Check_for_IAM_user",
              "branchName": "main"
            }
          ],
          "display": {
            "bounds": {
              "x": 0,
              "y": 1008
            }
          }
        },
        {
          "name": "Search_logs_by_IAM_arn",
          "actionId": "com.datadoghq.dd.logs.listLogsV2",
          "parameters": [
            {
              "name": "time_range",
              "value": "1d"
            },
            {
              "name": "query",
              "value": "@userIdentity.arn:\"{{ Steps.Get_security_signal.securitySignal.custom.userIdentity.arn }}\""
            }
          ],
          "outboundEdges": [
            {
              "nextStepName": "Get_AWS_API_events_from_logs",
              "branchName": "main"
            }
          ],
          "display": {
            "bounds": {
              "x": -252,
              "y": 1200
            }
          }
        },
        {
          "name": "Check_for_IAM_user",
          "actionId": "com.datadoghq.core.if",
          "parameters": [
            {
              "name": "joinOperator",
              "value": "and"
            },
            {
              "name": "conditions",
              "value": [
                {
                  "comparisonOperator": "eq",
                  "leftValue": "{{ Steps.Get_security_signal.securitySignal.custom.userIdentity.type }}",
                  "rightValue": "IAMUser"
                }
              ]
            }
          ],
          "outboundEdges": [
            {
              "nextStepName": "List_access_keys",
              "branchName": "true"
            }
          ],
          "display": {
            "bounds": {
              "x": 228,
              "y": 1200
            }
          }
        },
        {
          "name": "List_access_keys",
          "actionId": "com.datadoghq.aws.iam.listAccessKeys",
          "connectionLabel": "INTEGRATION_AWS",
          "parameters": [
            {
              "name": "userName",
              "value": "{{ Variables.iam_entity_name }}"
            }
          ],
          "outboundEdges": [
            {
              "nextStepName": "Add_access_key_summary_to_case",
              "branchName": "main"
            }
          ],
          "display": {
            "bounds": {
              "x": 228,
              "y": 1392
            }
          }
        },
        {
          "name": "Add_access_key_summary_to_case",
          "actionId": "com.datadoghq.dd.casem.addComment",
          "parameters": [
            {
              "name": "id",
              "value": "{{ Steps.Create_security_case.key }}"
            },
            {
              "name": "comment",
              "value": "Access key data for user {{ Variables.iam_entity_name }}: {{ Steps.List_access_keys.accessKeyMetadata }}"
            }
          ],
          "display": {
            "bounds": {
              "x": 228,
              "y": 1608
            }
          }
        },
        {
          "name": "Get_AWS_API_events_from_logs",
          "actionId": "com.datadoghq.datatransformation.func",
          "parameters": [
            {
              "name": "script",
              "value": "/**\n * The code extracts the eventName from the logs associated with the security signal\n * and returns an array of event names.\n */\n\nlet logs = $.Steps.Search_logs_by_IAM_arn.data;\n\nconsole.log(logs)\nconsole.log(logs.length)\n\nif (!logs || logs.length === 0) {\nreturn [];\n}\n\nconst eventNames = logs.map(log => {\nreturn log.attributes?.attributes?.eventName;\n}).filter(eventName => eventName !== undefined);\n\nreturn eventNames;//"
            },
            {
              "name": "description",
              "value": "Extract AWS API events from logs associated with security signal"
            }
          ],
          "outboundEdges": [
            {
              "nextStepName": "Add_AWS_actions_summary_to_case",
              "branchName": "main"
            }
          ],
          "display": {
            "bounds": {
              "x": -252,
              "y": 1392
            }
          }
        },
        {
          "name": "Add_AWS_actions_summary_to_case",
          "actionId": "com.datadoghq.dd.casem.addComment",
          "parameters": [
            {
              "name": "id",
              "value": "{{ Steps.Create_security_case.id }}"
            },
            {
              "name": "comment",
              "value": "AWS API actions found in logs: {{ Steps.Get_AWS_API_events_from_logs.data }}"
            }
          ],
          "display": {
            "bounds": {
              "x": -252,
              "y": 1584
            }
          }
        }
      ],
      "handle": "8yv52qw2ix-Aug-12-2025-1436",
      "connectionEnvs": [
        {
          "env": "default",
          "connections": [
            {
              "connectionId": datadog_action_connection.aws_iam_connection[0].id,
              "label": "INTEGRATION_AWS"
            }
          ]
        }
      ]
    }
  )
}