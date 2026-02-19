resource "datadog_action_connection" "aws_connection" {
  name = "Disable IAM Users connection"

  aws {
    assume_role {
      account_id = var.aws_account_id
      role       = var.aws_role_name
    }
  }
}

resource "datadog_workflow_automation" "workflow" {
  name        = "AWS IAM Disable User"
  description = "Disable an IAM User by removing any active access keys, login profile, and MFA devices."
  tags        = ["security"]
  published   = true

  spec_json = jsonencode(
    {
      "triggers": [
        {
          "startStepNames": [
            "Disable_User"
          ],
          "securityTrigger": {}
        },
        {
          "startStepNames": [
            "Disable_User"
          ],
          "dashboardTrigger": {}
        }
      ],
      "steps": [
        {
          "name": "Disable_User",
          "actionId": "com.datadoghq.aws.iam.disable_user",
          "connectionLabel": "INTEGRATION_AWS",
          "parameters": [
            {
              "name": "userName",
              "value": "{{ Trigger.userName }}"
            }
          ],
          "outboundEdges": [
            {
              "nextStepName": "Create_case",
              "branchName": "main"
            }
          ],
          "display": {
            "bounds": {
              "x": 192,
              "y": 264
            }
          }
        },
        {
          "name": "Create_case",
          "actionId": "com.datadoghq.dd.casem.createCase",
          "parameters": [
            {
              "name": "project_id",
              "value": var.case_project_id
            },
            {
              "name": "status",
              "value": "OPEN"
            },
            {
              "name": "title",
              "value": "{{ Trigger.userName }} disabled from cloud security"
            },
            {
              "name": "type",
              "value": "SECURITY"
            },
            {
              "name": "description",
              "value": "{{ Trigger.userName }} AWS IAM user was disabled from a Cloud Security finding or dashboard. Investigate {{ Trigger.userName }} and determine if user should be permanently deleted."
            }
          ],
          "display": {
            "bounds": {
              "x": 192,
              "y": 456
            }
          }
        }
      ],
      "handle": "AWS-IAM-Disable-User",
      "connectionEnvs": [
        {
          "env": "default",
          "connections": [
            {
              "connectionId": datadog_action_connection.aws_connection.id,
              "label": "INTEGRATION_AWS"
            }
          ]
        }
      ],
      "inputSchema": {
        "parameters": [
          {
            "name": "userName",
            "label": "IAM User Name",
            "type": "STRING"
          }
        ]
      }
    }
  )
}