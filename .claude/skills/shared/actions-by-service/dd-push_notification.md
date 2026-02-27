# Datadog Push Notifications Actions
Bundle: `com.datadoghq.dd.push_notification` | 1 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Epush_notification)

## com.datadoghq.dd.push_notification.sendPushNotification
**Send mobile push notification message** — Send a push notification message to specified Datadog Mobile app user.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | userId | string | yes | The ID of the user. Warning: user must have already logged into the Datadog Mobile application and allowed the Datadog mobile application to receive push notifications: https://docs.datadoghq.com/s... |
  | body | string | yes | The body of the push notification. |
  | pushLink | any | no | The Datadog resource to open when opening the notification. |

