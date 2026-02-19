#=============================================================================
# DATADOG WORKFLOW AUTOMATION
# Creates a workflow to create security cases for AWS security signals
#=============================================================================

resource "datadog_workflow_automation" "create_security_case" {
  name        = "Investigate and Block Malicious IPs in AWS WAF [TERRAFORM]"
  description = "Creates an investigative notebook to allow security responders to kickstart their investigation and notified the security responder in Slack. The Workflow also gives them the options to block the IP or raise an incident."
  tags        = ["security", "appsec", "aws", "terraform"]
  published   = true
  
  spec_json = templatefile("${path.module}/workflow-spec.json", {
    connection_id = datadog_action_connection.aws_waf.id
  })
  
  depends_on = [datadog_action_connection.aws_waf]
}