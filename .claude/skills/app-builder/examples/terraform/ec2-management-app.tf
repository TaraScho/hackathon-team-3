#=============================================================================
# DATADOG APP BUILDER APPS
# Creates App Builder applications for EC2 management
#=============================================================================

# App Builder: EC2 Instance Management
# Allows users to view, filter, and manage EC2 instances with tagging operations
resource "datadog_app_builder_app" "ec2_management" {
  count    = var.create_workflows ? 1 : 0

  name        = "Modify EC2 instance tags"
  description = "View and manage EC2 instances with team-based filtering and tagging operations"
  published   = true

  # Load the app definition from the JSON template file
  app_json = file("${path.module}/app_builder.json")

  # Map the query names to connection IDs
  # This tells the app which connection to use for each action query
  action_query_names_to_connection_ids = {
    for query in [
      "listTeams",
      "listInstances",
      "applyPRODTag",
      "applyDEVTag",
      "applyTESTTag"
    ] :
    query => datadog_action_connection.aws_ec2_appbuilder[0].id
  }

  depends_on = [datadog_action_connection.aws_ec2_appbuilder]
}
