# Datadog Notebooks Actions
Bundle: `com.datadoghq.dd.notebooks` | 8 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Enotebooks)

## com.datadoghq.dd.notebooks.cloneNotebook
**Clone notebook** — Clone the specified notebook.
- Stability: stable
- Access: read, create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | notebookId | ['number', 'string'] | yes | The ID of the notebook to be cloned. |
  | name | string | no | Replace the cloned notebook name. |
  | cell | string | no | An optional Markdown field which adds a new Markdown cell at the top of the notebook. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | id | ['number', 'string'] | Unique notebook ID, assigned when you create the notebook. |
  | type | string | Type of the Notebook resource. |
  | cells | array<object> | List of cells to display in the notebook. |
  | time | any | Notebook global timeframe. |
  | url | string |  |
  | status | string | Publication status of the notebook. |
  | metadata | object | Metadata associated with the notebook. |
  | name | string | The name of the notebook. |
  | author | object | Attributes of user object returned by the API. |
  | created | string | UTC time stamp for when the notebook was created. |
  | modified | string | UTC time stamp for when the notebook was last modified. |
  | template_variables | any |  |
  | tags | array<string> |  |


## com.datadoghq.dd.notebooks.createFromTemplate
**Create notebook from template** — Create a new notebook from the given template.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | templateId | ['number', 'string'] | yes | The ID of the notebook template to be used to create a new notebook. |
  | name | string | no | Replace the created notebook's name. |
  | cell | string | no | An optional markdown field which will add a new Markdown cell at the top of the notebook. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | id | ['number', 'string'] | Unique notebook ID, assigned when you create the notebook. |
  | type | string | Type of the Notebook resource. |
  | cells | array<object> | List of cells to display in the notebook. |
  | time | any | Notebook global timeframe. |
  | url | string |  |
  | status | string | Publication status of the notebook. |
  | metadata | object | Metadata associated with the notebook. |
  | name | string | The name of the notebook. |
  | author | object | Attributes of user object returned by the API. |
  | created | string | UTC time stamp for when the notebook was created. |
  | modified | string | UTC time stamp for when the notebook was last modified. |
  | template_variables | any |  |
  | tags | array<string> |  |


## com.datadoghq.dd.notebooks.createNotebook
**Create notebook** — Create a notebook using the specified options.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | time | any | yes | Notebook global timeframe |
  | cells | array<object> | yes | List of cells to display in the notebook. |
  | status | string | no | Publication status of the notebook. |
  | metadata | object | no | Metadata associated with the notebook. |
  | name | string | yes | The name of the notebook. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | id | ['number', 'string'] | Unique notebook ID, assigned when you create the notebook. |
  | type | string | Type of the Notebook resource. |
  | cells | array<object> | List of cells to display in the notebook. |
  | time | any | Notebook global timeframe. |
  | url | string |  |
  | status | string | Publication status of the notebook. |
  | metadata | object | Metadata associated with the notebook. |
  | name | string | The name of the notebook. |
  | author | object | Attributes of user object returned by the API. |
  | created | string | UTC time stamp for when the notebook was created. |
  | modified | string | UTC time stamp for when the notebook was last modified. |
  | template_variables | any |  |
  | tags | array<string> |  |


## com.datadoghq.dd.notebooks.deleteNotebook
**Delete notebook** — Delete a notebook using the specified ID.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | notebook_id | ['number', 'string'] | yes | Unique ID, assigned when you create the notebook. |


## com.datadoghq.dd.notebooks.getNotebook
**Get notebook details** — Get a notebook using the specified notebook ID with the cells' information.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | notebook_id | ['number', 'string'] | yes | If you're dynamically passing in a Notebook using a variable, then ensure that you pass in a Notebook ID value. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | id | ['number', 'string'] | Unique notebook ID, assigned when you create the notebook. |
  | type | string | Type of the Notebook resource. |
  | cells | array<object> | List of cells to display in the notebook. |
  | time | any | Notebook global timeframe. |
  | url | string |  |
  | status | string | Publication status of the notebook. |
  | metadata | object | Metadata associated with the notebook. |
  | name | string | The name of the notebook. |
  | author | object | Attributes of user object returned by the API. |
  | created | string | UTC time stamp for when the notebook was created. |
  | modified | string | UTC time stamp for when the notebook was last modified. |
  | template_variables | any |  |
  | tags | array<string> |  |


## com.datadoghq.dd.notebooks.getNotebookWithoutCells
**Get notebook** — Get a notebook using the specified notebook ID.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | notebook_id | ['number', 'string'] | yes | If you're dynamically passing in a Notebook using a variable, then ensure that you pass in a Notebook ID value. |
  | templateVariables | object | no | Provided template variables will be used to create the Notebook link this action outputs. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | numberOfCells | number |  |
  | id | ['number', 'string'] | Unique notebook ID, assigned when you create the notebook. |
  | type | string | Type of the Notebook resource. |
  | time | any | Notebook global timeframe. |
  | url | string |  |
  | status | string | Publication status of the notebook. |
  | metadata | object | Metadata associated with the notebook. |
  | name | string | The name of the notebook. |
  | author | object | Attributes of user object returned by the API. |
  | created | string | UTC time stamp for when the notebook was created. |
  | modified | string | UTC time stamp for when the notebook was last modified. |
  | template_variables | any |  |
  | tags | array<string> |  |


## com.datadoghq.dd.notebooks.listNotebooks
**List notebooks** — Get all notebooks.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | start | number | no | The index of the first notebook you want returned. |
  | count | number | no | The number of notebooks to be returned. The default is 50 notebooks. |
  | sort_field | string | no | Sort by field `modified`, `name`, or `created`. |
  | sort_dir | string | no | Sort by direction `asc` or `desc`. |
  | query | string | no | Return only notebooks with `query` string in notebook name or author handle. |
  | is_template | boolean | no | True value returns only template notebooks. |
  | author_handle | string | no | Return notebooks created by the given `author_handle`. |
  | exclude_author_handle | string | no | Return notebooks not created by the given `author_handle`. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | notebooks | array<object> | List of notebook definitions. |
  | meta | object | Searches metadata returned by the API. |


## com.datadoghq.dd.notebooks.updateNotebook
**Update notebook** — Update a notebook using the specified ID.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | timeframe | any | yes | Notebook global timeframe |
  | notebook_id | ['number', 'string'] | yes | Unique ID, assigned when you create the notebook. |
  | cells | array<object> | yes | List of cells to display in the notebook. |
  | status | string | no | Publication status of the notebook. |
  | metadata | object | no | Metadata associated with the notebook. |
  | name | string | yes | The name of the notebook. |
  | tags | any | no | Tags to be associated with the notebook. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The data for a notebook. |

