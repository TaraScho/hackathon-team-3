#=============================================================================
# DATADOG WORKFLOW AUTOMATION
# Creates workflows for automated remediation and response
#=============================================================================

# Workflow: Remove Insecure Ingress Rules - Simple
# Automatically removes security group rules that expose sensitive ports to the internet
resource "datadog_workflow_automation" "remove_insecure_ingress" {
  count       = var.create_workflows ? 1 : 0
  name        = "Remove insecure ingress rules"
  description = "Automatically removes insecure security group rules that expose EC2 instances to the internet"
  tags        = ["security", "remediation", "ec2", "automated", "terraform"]
  published   = true
  depends_on  = [datadog_action_connection.aws_ec2_workflow]

  spec_json = jsonencode({
    "triggers" : [
      {
        "startStepNames" : [
          "Revoke_security_group_ingress"
        ],
        "securityTrigger" : {}
      }
    ],
    "steps" : [
      {
        "name" : "Revoke_security_group_ingress",
        "actionId" : "com.datadoghq.aws.ec2.revoke_security_group_ingress",
        "connectionLabel" : "WORKFLOW_EC2",
        "parameters" : [
          {
            "name" : "region",
            "value" : var.aws_region
          },
          {
            "name" : "ipPermissions",
            "value" : [
              {
                "FromPort" : 80,
                "IpProtocol" : "TCP",
                "IpRanges" : [
                  {
                    "CidrIp" : "0.0.0.0/0"
                  }
                ],
                "ToPort" : 80
              }
            ]
          },
          {
            "name" : "dryRun",
            "value" : false
          },
          {
            "name" : "groupId",
            "value" : "{{ Source.securityFinding.resourceConfiguration.group_id }}"
          }
        ],
        "display": {
          "bounds": {
            "x": 0,
            "y": 252
          }
        }
      }
    ],
    "handle" : "remove-rules-simple",
    "connectionEnvs" : [
      {
        "env" : "default",
        "connections" : [
          {
            "connectionId" : datadog_action_connection.aws_ec2_workflow[0].id,
            "label" : "WORKFLOW_EC2"
          }
        ]
      }
    ]
  })
}

# Workflow: Update EC2 Env scorecard
# Verifies EC2 instances have ENV tag and updates scorecard
resource "datadog_workflow_automation" "update_ec2_env_scorecard" {
  count       = var.create_workflows ? 1 : 0
  name        = "Update EC2 Env scorecard"
  description = ""
  tags        = []
  published   = true
  depends_on  = [datadog_action_connection.aws_ec2_workflow]

  spec_json = jsonencode({
    "triggers" : [
      {
        "startStepNames" : [
          "List_ec2_instances"
        ],
        "workflowTrigger" : {}
      }
    ],
    "steps" : [
      {
        "name" : "List_ec2_instances",
        "actionId" : "com.datadoghq.aws.ec2.describe_ec2_instances",
        "connectionLabel" : "WORKFLOW_EC2",
        "parameters" : [
          {
            "name" : "region",
            "value" : var.aws_region
          },
          {
            "name" : "filters",
            "value" : [
              {
                "Name" : "tag:Team",
                "Values" : [
                  "Milliways",
                  "Magrathea"
                ]
              }
            ]
          }
        ],
        "outboundEdges" : [
          {
            "nextStepName" : "For_each_instance",
            "branchName" : "main"
          }
        ]
      },
      {
        "name" : "For_each_instance",
        "actionId" : "com.datadoghq.core.forLoop",
        "parameters" : [
          {
            "name" : "inputList",
            "value" : "{{ Steps.List_ec2_instances.instances }}"
          },
          {
            "name" : "parentExecContext",
            "value" : "{{ InstanceId }}"
          },
          {
            "name" : "startStepNames",
            "value" : [
              "For each instance"
            ]
          },
          {
            "name" : "workflowId",
            "value" : "{{ WorkflowId }}"
          }
        ],
        "outboundEdges" : [
          {
            "nextStepName" : "check_env",
            "branchName" : "loopStart"
          }
        ]
      },
      {
        "name" : "If_env_missing",
        "actionId" : "com.datadoghq.core.if",
        "parameters" : [
          {
            "name" : "conditions",
            "value" : [
              {
                "comparisonOperator" : "nonnull",
                "value" : "{{ Steps.check_env.data.env }}"
              }
            ]
          },
          {
            "name" : "joinOperator",
            "value" : "and"
          }
        ],
        "outboundEdges" : [
          {
            "nextStepName" : "Update_scorecard_rule",
            "branchName" : "true"
          },
          {
            "nextStepName" : "Update_scorecard_rule_1",
            "branchName" : "false"
          }
        ]
      },
      {
        "name" : "Update_scorecard_rule",
        "actionId" : "com.datadoghq.dd.service_catalog.updateScorecardRuleOutcome",
        "parameters" : [
          {
            "name" : "serviceName",
            "value" : "simple-app-1"
          },
          {
            "name" : "state",
            "value" : "pass"
          },
          {
            "name" : "scorecardRuleId",
            "value" : var.ec2_scorecard_rule_id
          }
        ]
      },
      {
        "name" : "Update_scorecard_rule_1",
        "actionId" : "com.datadoghq.dd.service_catalog.updateScorecardRuleOutcome",
        "parameters" : [
          {
            "name" : "serviceName",
            "value" : "simple-app-1"
          },
          {
            "name" : "state",
            "value" : "fail"
          },
          {
            "name" : "scorecardRuleId",
            "value" : var.ec2_scorecard_rule_id
          }
        ]
      },
      {
        "name" : "check_env",
        "actionId" : "com.datadoghq.datatransformation.func",
        "parameters" : [
          {
            "name" : "script",
            "value" : "const data = $.Current.Value;\n\nconsole.log(data)\n\nconst tags = data.Tags || [];\n\nconsole.log(tags)\n\nconst findTag = (key) =>\n  tags.find(tag => tag.Key.toLowerCase() === key.toLowerCase())?.Value ?? null;\n\nconst result = {\n  team: findTag(\"Team\"),\n  env: findTag(\"Env\")\n};\n\nreturn result;"
          }
        ],
        "outboundEdges" : [
          {
            "nextStepName" : "If_env_missing",
            "branchName" : "main"
          }
        ]
      }
    ],
    "handle" : "workflow-update-ec2-env-scorecard",
    "connectionEnvs" : [
      {
        "env" : "default",
        "connections" : [
          {
            "connectionId" : datadog_action_connection.aws_ec2_workflow[0].id,
            "label" : "WORKFLOW_EC2"
          }
        ]
      }
    ]
  })
}
