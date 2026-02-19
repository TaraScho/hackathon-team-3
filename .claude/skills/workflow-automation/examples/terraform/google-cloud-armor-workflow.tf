resource "datadog_workflow_automation" "workflow" {
  name        = "Block IP with Cloud Armor"
  provider    = datadog.workflow
  description = ""
  tags        = []
  published   = true

  spec_json = jsonencode(
    {
      "triggers": [
        {
          "startStepNames": [
            "Add_rule"
          ],
          "securityTrigger": {}
        }
      ],
      "steps": [
        {
          "name": "Add_rule",
          "actionId": "com.datadoghq.gcp.armor.addRule",
          "connectionLabel": "INTEGRATION_GCP",
          "parameters": [
            {
              "name": "project",
              "value": "{{ Source.securitySignal.custom.project_id }}"
            },
            {
              "name": "securityPolicy",
              "value": "dogstore-policy"
            },
            {
              "name": "securityPolicyRuleResource",
              "value": {
                "action": "deny(403)",
                "description": "Block specific IP address",
                "match": {
                  "config": {
                    "srcIpRanges": [
                      "{{ Trigger.attacker_ip }}"
                    ]
                  },
                  "versionedExpr": "SRC_IPS_V1"
                },
                "preview": false,
                "priority": 1001
              }
            }
          ],
          "display": {
            "bounds": {
              "x": 0,
              "y": 228
            }
          }
        }
      ],
      "handle": "block-ip-with-cloud-armor",
      "connectionEnvs": [
        {
          "env": "default",
          "connections": [
            {
              "connectionId": "d8531e71-0523-449a-bc4f-22d877b518ac",
              "label": "INTEGRATION_GCP"
            }
          ]
        }
      ],
      "inputSchema": {
        "parameters": [
          {
            "name": "attacker_ip",
            "type": "STRING"
          }
        ]
      }
    }
  )
}