# App Builder Queries and Expressions Reference

Complete reference for query types, execution lifecycle, advanced options, and JavaScript expression syntax in Datadog App Builder.

---

## Query Types

App Builder supports three query types, each serving a distinct purpose.

### ActionQuery

Calls an AWS action or Datadog API via an action connection. This is the primary query type for interacting with cloud services.

```json
{
  "name": "listInstances",
  "type": "action",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "properties": {
    "fqn": "com.datadoghq.aws.ec2.describe_ec2_instances",
    "connectionId": "aaaabbbb-cccc-dddd-eeee-ffffffffffff",
    "inputs": {
      "region": "{{ ui.regionSelect.value }}",
      "filters": [
        {
          "name": "instance-state-name",
          "values": ["running", "stopped"]
        }
      ]
    }
  },
  "events": [
    {
      "name": "onSuccess",
      "type": "custom",
      "reactions": []
    },
    {
      "name": "onError",
      "type": "custom",
      "reactions": []
    }
  ]
}
```

**Key fields:**

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Unique identifier used to reference the query (`queries.{name}`) |
| `type` | Yes | Must be `"action"` |
| `id` | Yes | UUID (generate with `uuid.uuid4()` or `crypto.randomUUID()`) |
| `fqn` | Yes | Fully qualified action name (e.g., `com.datadoghq.aws.ec2.describe_ec2_instances`) |
| `connectionId` | Yes | UUID of the action connection to use |
| `inputs` | Yes | Object whose keys match the action's input parameters |

**Finding the FQN:** Look up actions in `.claude/skills/shared/actions-by-service/{service}.md`. Each file lists the FQN, required inputs, and output schema for every action.

**Input expressions:** Input values can use `{{ }}` expressions to reference component state or other query results. These are evaluated at query execution time.

### DataTransform

Runs a JavaScript expression to transform, filter, or combine data from other queries. Does not make network calls.

```json
{
  "name": "runningInstances",
  "type": "dataTransform",
  "id": "660e8400-e29b-41d4-a716-446655440001",
  "properties": {
    "expression": "return queries.listInstances.data.instances.filter(i => i.state === 'running').map(i => ({ id: i.instanceId, type: i.instanceType, az: i.placement.availabilityZone, launchTime: i.launchTime }))"
  },
  "events": []
}
```

**Key fields:**

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Unique identifier |
| `type` | Yes | Must be `"dataTransform"` |
| `expression` | Yes | JavaScript expression. Must `return` a value. |

**Use cases:**
- Filtering query results by component state
- Joining data from multiple queries
- Reshaping data for table columns or chart series
- Computing aggregate values (counts, sums, averages)

**Execution:** DataTransforms re-execute automatically whenever any referenced `queries.*` or `ui.*` value changes.

### StateVariable

Stores persistent state across the app session. Unlike component state (which is tied to a specific component), state variables are global and can be read/written from any component or query.

```json
{
  "name": "selectedInstanceId",
  "type": "stateVariable",
  "id": "770e8400-e29b-41d4-a716-446655440002",
  "properties": {
    "defaultValue": ""
  },
  "events": []
}
```

**Key fields:**

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Unique identifier. Accessed via `state.{name}` |
| `type` | Yes | Must be `"stateVariable"` |
| `defaultValue` | Yes | Initial value (string, number, boolean, object, or array) |

**Setting values:** Use the `setStateVariableValue` reaction:
```json
{
  "type": "setStateVariableValue",
  "variableName": "selectedInstanceId",
  "value": "{{ ui.instanceTable.selectedRow.instanceId }}"
}
```

**Reading values:** Use `state.selectedInstanceId` in any expression:
```json
{
  "isVisible": "{{ state.selectedInstanceId !== '' }}",
  "label": "Selected: {{ state.selectedInstanceId }}"
}
```

---

## Query Execution Order

When a query is triggered (by a button click, page load, or reaction chain), the execution follows these 9 steps:

1. **Evaluate inputs** -- All `{{ }}` expressions in the query's `inputs` are resolved against current component state and query data
2. **Check conditional execution** -- If `runCondition` is set, evaluate it. Skip execution if it returns falsy
3. **Apply debounce** -- If `debounceMs` is set, wait for the debounce window before executing
4. **Set loading state** -- `queries.{name}.isLoading` becomes `true`
5. **Execute the query** -- For ActionQuery, send the request via the connection. For DataTransform, evaluate the expression. For StateVariable, set the value
6. **Store response** -- The result is stored in `queries.{name}.data`
7. **Apply post-query transformation** -- If `postTransform` is defined, run it on the response
8. **Fire success/error event** -- Execute `onSuccess` reactions if the query succeeded, or `onError` reactions if it failed
9. **Clear loading state** -- `queries.{name}.isLoading` becomes `false`

If a reaction in step 8 triggers another query, that query goes through the same 9-step cycle. Chains of query triggers execute sequentially.

---

## Advanced Query Options

These optional properties can be added to any query's `properties` object.

### Debounce

Prevents rapid re-execution when inputs change frequently (e.g., as a user types in a text input).

```json
{
  "name": "searchInstances",
  "type": "action",
  "properties": {
    "fqn": "com.datadoghq.aws.ec2.describe_ec2_instances",
    "connectionId": "...",
    "inputs": {
      "filters": [{ "name": "tag:Name", "values": ["*{{ ui.searchInput.value }}*"] }]
    },
    "debounceMs": 300
  }
}
```

The query waits 300ms after the last input change before executing. If the input changes again within that window, the timer resets.

### Conditional Execution

Skip query execution unless a condition is met.

```json
{
  "properties": {
    "runCondition": "{{ ui.regionSelect.value !== '' && ui.regionSelect.value !== undefined }}",
    "fqn": "...",
    "inputs": { "region": "{{ ui.regionSelect.value }}" }
  }
}
```

Useful for queries that depend on a selection being made first.

### Polling Interval

Automatically re-execute the query at a fixed interval.

```json
{
  "properties": {
    "pollingIntervalMs": 30000,
    "fqn": "com.datadoghq.aws.ec2.describe_ec2_instances",
    "connectionId": "...",
    "inputs": { "region": "us-east-1" }
  }
}
```

- `pollingIntervalMs`: Re-execute every N milliseconds (minimum 5000)
- Polling pauses when the browser tab is not visible and resumes when it becomes visible again
- Combine with a checkbox component to let the user toggle polling on/off:
  ```json
  "pollingIntervalMs": "{{ ui.autoRefresh.value ? 30000 : 0 }}"
  ```

### Mocked Outputs for Testing

During development, you can provide mock data so the app renders without making real API calls.

```json
{
  "properties": {
    "fqn": "com.datadoghq.aws.ec2.describe_ec2_instances",
    "connectionId": "...",
    "inputs": { "region": "us-east-1" },
    "mockOutput": {
      "instances": [
        { "instanceId": "i-mock001", "state": "running", "instanceType": "t3.micro" },
        { "instanceId": "i-mock002", "state": "stopped", "instanceType": "t3.medium" }
      ]
    },
    "useMock": true
  }
}
```

- `mockOutput`: The data object to return instead of calling the real action
- `useMock`: Set to `true` to use mock data, `false` for real API calls
- Remove or set `useMock: false` before publishing to production

### Run on Page Load

Control whether a query executes automatically when the app loads.

```json
{
  "properties": {
    "runOnPageLoad": true,
    "fqn": "com.datadoghq.aws.ec2.describe_ec2_instances",
    "connectionId": "...",
    "inputs": { "region": "us-east-1" }
  }
}
```

- `runOnPageLoad`: Defaults to `false`. Set to `true` for queries that should populate data on initial render (e.g., list queries)
- Mutating queries (stop, start, delete) should always have `runOnPageLoad: false`

---

## JavaScript Expression Syntax

App Builder uses a template expression syntax throughout component properties and query inputs.

### Template Syntax

All expressions are wrapped in `{{ }}` double curly braces:

```
{{ expression }}
```

The expression inside the braces is evaluated as JavaScript. The return value is used as the property value.

### Available Globals

Inside `{{ }}` expressions, you have access to:

| Global | Description |
|--------|-------------|
| `ui` | Component state namespace. `ui.{componentName}.value`, `ui.{tableName}.selectedRow`, etc. |
| `queries` | Query results namespace. `queries.{queryName}.data`, `queries.{queryName}.isLoading`, etc. |
| `state` | State variable namespace. `state.{variableName}` |
| `global` | Global context. Contains `global.user` (current user info) and `global.dashboard` (when embedded) |
| `_` | Lodash utility library (full lodash API available) |
| `moment` | Moment.js for date/time manipulation |
| `JSON` | Standard JSON object (`JSON.stringify`, `JSON.parse`) |
| `Math` | Standard Math object |
| `Array` | Standard Array constructor and methods |
| `Object` | Standard Object constructor and methods |
| `console` | Console object for debugging (`console.log` output appears in browser dev tools) |

### Expression Examples

**Simple value reference:**
```
{{ ui.regionSelect.value }}
```

**Conditional rendering:**
```
{{ queries.listInstances.data.instances.length > 0 }}
```

**Ternary expression:**
```
{{ ui.instanceTable.selectedRow ? 'Selected: ' + ui.instanceTable.selectedRow.instanceId : 'No selection' }}
```

**Array filtering:**
```
{{ queries.listInstances.data.instances.filter(i => i.state === 'running') }}
```

**Array mapping:**
```
{{ queries.listInstances.data.instances.map(i => ({ label: i.instanceId + ' (' + i.state + ')', value: i.instanceId })) }}
```

**Lodash usage:**
```
{{ _.groupBy(queries.listInstances.data.instances, 'instanceType') }}
```

**Moment.js usage:**
```
{{ moment(ui.instanceTable.selectedRow.launchTime).fromNow() }}
```

**Computed string:**
```
{{ 'Found ' + queries.listInstances.data.instances.length + ' instances in ' + ui.regionSelect.value }}
```

### Multi-line Expressions in DataTransform

DataTransform `expression` fields support multi-line JavaScript. Use `return` to specify the output:

```javascript
const instances = queries.listInstances.data.instances;
const running = instances.filter(i => i.state === 'running');
const grouped = _.groupBy(running, 'instanceType');
const summary = Object.entries(grouped).map(([type, items]) => ({
  instanceType: type,
  count: items.length,
  instanceIds: items.map(i => i.instanceId)
}));
return summary;
```

---

## Post-Query Transformations

Apply a JavaScript transformation to query results after execution but before storing in `queries.{name}.data`.

```json
{
  "name": "listInstances",
  "type": "action",
  "properties": {
    "fqn": "com.datadoghq.aws.ec2.describe_ec2_instances",
    "connectionId": "...",
    "inputs": { "region": "us-east-1" },
    "postTransform": "return data.instances.map(i => ({ ...i, displayName: i.tags?.find(t => t.key === 'Name')?.value || i.instanceId }))"
  }
}
```

- The transform receives the raw response as `data`
- Must `return` the transformed value
- The returned value replaces `queries.{name}.data`
- Useful for flattening nested structures, computing derived fields, or normalizing data shapes across different actions

### Chaining Transforms

For complex transformations, use a DataTransform query that depends on the action query:

```json
[
  {
    "name": "rawInstances",
    "type": "action",
    "properties": {
      "fqn": "com.datadoghq.aws.ec2.describe_ec2_instances",
      "connectionId": "...",
      "inputs": { "region": "us-east-1" },
      "runOnPageLoad": true
    }
  },
  {
    "name": "enrichedInstances",
    "type": "dataTransform",
    "properties": {
      "expression": "const instances = queries.rawInstances.data.instances; return instances.map(i => ({ ...i, name: i.tags?.find(t => t.key === 'Name')?.value || 'unnamed', uptime: moment(i.launchTime).fromNow(), isProduction: i.tags?.some(t => t.key === 'env' && t.value === 'production') }))"
    }
  }
]
```

The DataTransform automatically re-evaluates whenever `queries.rawInstances.data` changes.
