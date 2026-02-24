# Data Transformation Actions
Bundle: `com.datadoghq.datatransformation` | 5 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edatatransformation)

## com.datadoghq.datatransformation.expression
**Expression** — Use JavaScript expression to apply transformations on data or objects. An *expression* is any valid unit of code that resolves to a value.

**Examples**:
- `1 + 2`
- `[1, 2, 3].filter(x => x < 3)`

**Note**: Lodash is available through the variable `_`.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | context | any | no | This value should be a JSON-serializable value, which will be made available in the expression as `$`. This can be a hard-coded value, or composed from the workflow execution context using templating. |
  | script | string | yes | A JavaScript expression which applies a transformation to your data. An *expression* usually contains one line of JavaScript code that can be reformatted into multiple lines. **Variable assignments... |
  | description | string | no | A description for the expression. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | any |  |


## com.datadoghq.datatransformation.func
**JavaScript** — Use JavaScript to apply transformations on data or objects. The code entered into the script area represents the body of the function to be executed.

**Notes**:
- Network and file system access is restricted.
- Lodash is available through the variable `_`.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | context | any | no | This value should be a JSON-serializable value, which will be made available in the script as `$`. This can be a hard-coded value, or composed from the workflow execution context using templating. |
  | script | string | yes | A JS script which applies a transformation and returns a JSON-serializable value. |
  | description | string | no | A description for the script. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | any |  |


## com.datadoghq.datatransformation.funcPy
**Python** — Use Python to apply transformations on data or objects.

**Notes**:
- See Python version and available libraries at https://docs.datadoghq.com/actions/workflows/expressions/python/#python-environment

- Network access is restricted.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | context | object | no | This value should be a JSON-serializable value, which will be made available in the script as `$`. This can be a hard-coded value, or composed from the workflow execution context using templating. |
  | script | string | no | A Python script which applies a transformation and returns a JSON-serializable value. |
  | description | string | no | A description for the script. |
  | runtimeVersion | string | no |  |
  | wrapperScript | string | no | An optional Python script that wraps the user script. It should define a function `wrapper` that takes the user-defined `main` function as an argument and returns a new function to be executed. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | any | The JSON-serializable value returned by the Python script execution |


## com.datadoghq.datatransformation.inlineExpression
**Inline expression** — Use JavaScript expression to apply transformations on data or objects. An *expression* is any valid unit of code that resolves to a value.

**Examples**:
- `1 + 2`
- `[1, 2, 3].filter(x => x < 3)`

**Note**: Lodash is available through the variable `_`.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | context | any | no | This value should be a JSON-serializable value, which will be made available in the expression as `$`. This can be a hard-coded value, or composed from the workflow execution context using templating. |
  | script | string | yes | A JavaScript expression which applies a transformation to your data. An *expression* usually contains one line of JavaScript code that can be reformatted into multiple lines. **Variable assignments... |
  | description | string | no | A description for the expression. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | any |  |


## com.datadoghq.datatransformation.xmlToJSON
**Convert XML to JSON** — Convert XML string into a JSON object.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | xml | string | yes | A valid XML string to be converted to JSON. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | json | any | The converted JSON object from the provided XML string. |

