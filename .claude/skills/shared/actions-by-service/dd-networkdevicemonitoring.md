# Datadog Network Device Monitoring Actions
Bundle: `com.datadoghq.dd.networkdevicemonitoring` | 4 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Enetworkdevicemonitoring)

## com.datadoghq.dd.networkdevicemonitoring.getDevice
**Get device** — Get the device details.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | device_id | string | yes | The id of the device to fetch. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Get device response data. |


## com.datadoghq.dd.networkdevicemonitoring.getInterfaces
**Get interfaces** — Get the list of interfaces of the device.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | device_id | string | yes | The ID of the device to get interfaces from. |
  | get_ip_addresses | boolean | no | Whether to get the IP addresses of the interfaces. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Get Interfaces response. |


## com.datadoghq.dd.networkdevicemonitoring.listDeviceUserTags
**List device user tags** — Get the list of tags for a device.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | device_id | string | yes | The id of the device to fetch tags for. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The list tags response data. |


## com.datadoghq.dd.networkdevicemonitoring.listDevices
**List devices** — Get the list of devices.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | filter_tag | any | no | Filter devices by tags. |
  | page_size | number | no | Size for a given page. |
  | page_number | number | no | Specific page number to return. |
  | sort | string | no | The field to sort the devices by. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | The list devices response data. |
  | meta | object | Object describing meta attributes of response. |

