# Datadog IP Ranges Actions
Bundle: `com.datadoghq.dd.ip_ranges` | 2 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Eip_ranges)

## com.datadoghq.dd.ip_ranges.getIPAllowlist
**Get IP allowlist** — Returns the IP allowlist and its enabled or disabled state.
- Stability: stable
- Access: read
- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | IP allowlist data. |


## com.datadoghq.dd.ip_ranges.getIPRanges
**Get IP ranges** — Get Datadog IP ranges.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | site | string | no | The Datadog site to get the IP ranges for. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | version | number |  |
  | modified | string |  |
  | ips | object |  |

