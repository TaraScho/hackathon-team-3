# Datadog Slack Integration Actions
Bundle: `com.datadoghq.dd.integration.slack` | 5 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Eintegration%2Eslack)

## com.datadoghq.dd.integration.slack.createSlackIntegrationChannel
**Create Slack integration channel** — Add a channel to your Datadog-Slack integration.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | account_name | string | yes | The name/label given to the Slack account in your Datadog account. View [docs](https://docs.datadoghq.com/integrations/slack/?tab=datadogforslack) for more information. |
  | message | boolean | no | Show the main body of the alert event. |
  | mute_buttons | boolean | no | Show interactive buttons to mute the alerting monitor. |
  | notified | boolean | no | Show the list of |
  | snapshot | boolean | no | Show the alert event's snapshot image. |
  | tags | boolean | no | Show the scopes on which the monitor alerted. |
  | name | string | no | Your channel name. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | display | object | Configuration options for what is shown in an alert event message. |
  | name | string | Your channel name. |


## com.datadoghq.dd.integration.slack.getSlackIntegrationChannel
**Get Slack integration channel** — Get a channel configured for your Datadog-Slack integration.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | account_name | string | yes | Your Slack account name. |
  | channel_name | string | yes | The name of the Slack channel being operated on. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | display | object | Configuration options for what is shown in an alert event message. |
  | name | string | Your channel name. |


## com.datadoghq.dd.integration.slack.getSlackIntegrationChannels
**Get Slack integration channels** — Get a list of all channels configured for your Datadog-Slack integration.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | account_name | string | yes | Your Slack account name. |


## com.datadoghq.dd.integration.slack.removeSlackIntegrationChannel
**Remove Slack integration channel** — Remove a channel from your Datadog-Slack integration.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | account_name | string | yes | Your Slack account name. |
  | channel_name | string | yes | The name of the Slack channel being operated on. |


## com.datadoghq.dd.integration.slack.updateSlackIntegrationChannel
**Update Slack integration channel** — Update a channel used in your Datadog-Slack integration.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | account_name | string | yes | The name/label given to the Slack account in your Datadog account. View [docs](https://docs.datadoghq.com/integrations/slack/?tab=datadogforslack) for more information. |
  | channel_name | string | yes | The name of the Slack channel being operated on. |
  | message | boolean | no | Show the main body of the alert event. |
  | mute_buttons | boolean | no | Show interactive buttons to mute the alerting monitor. |
  | notified | boolean | no | Show the list of |
  | snapshot | boolean | no | Show the alert event's snapshot image. |
  | tags | boolean | no | Show the scopes on which the monitor alerted. |
  | name | string | no | Your channel name. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | display | object | Configuration options for what is shown in an alert event message. |
  | name | string | Your channel name. |

