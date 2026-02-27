# Datadog Logs Archives Actions
Bundle: `com.datadoghq.dd.logsarchives` | 8 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Elogsarchives)

## com.datadoghq.dd.logsarchives.addReadRoleToArchive
**Add read role to archive** — Adds a read role to an archive.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | archive_id | string | yes | The ID of the archive. |
  | id | string | yes | The unique identifier of the role. |


## com.datadoghq.dd.logsarchives.deleteLogsArchive
**Delete logs archive** — Delete a given archive from your organization.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | archive_id | string | yes | The ID of the archive. |


## com.datadoghq.dd.logsarchives.getLogsArchive
**Get logs archive** — Get a specific archive from your organization.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | archive_id | string | yes | The ID of the archive. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The definition of an archive. |


## com.datadoghq.dd.logsarchives.getLogsArchiveOrder
**Get logs archive order** — Get the current order of your archives.
- Stability: stable
- Access: read
- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The definition of an archive order. |


## com.datadoghq.dd.logsarchives.listArchiveReadRoles
**List archive read roles** — Returns all read roles a given archive is restricted to.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | archive_id | string | yes | The ID of the archive. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Array of returned roles. |
  | meta | object | Object describing meta attributes of response. |


## com.datadoghq.dd.logsarchives.listLogsArchives
**List logs archives** — Get the list of configured logs archives with their definitions.
- Stability: stable
- Access: read
- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | A list of archives. |


## com.datadoghq.dd.logsarchives.removeRoleFromArchive
**Remove role from archive** — Removes a role from an archive.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | archive_id | string | yes | The ID of the archive. |
  | id | string | yes | The unique identifier of the role. |


## com.datadoghq.dd.logsarchives.updateLogsArchiveOrder
**Update logs archive order** — Update the order of your archives.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | archive_ids | array<string> | yes | An ordered array of `<ARCHIVE_ID>` strings, the order of archive IDs in the array define the overall archives order for Datadog. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The definition of an archive order. |

