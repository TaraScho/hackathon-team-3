# Flow Control and Expressions

This reference covers all flow control actions, error handling configuration, expression languages, and variable management in Datadog Workflow Automation.

---

## Flow Control Actions

### If (Conditional Branch)

Routes execution to one of two paths based on a boolean condition.

**Action ID:** `com.datadoghq.core.if`

```json
{
  "name": "Check_severity",
  "actionId": "com.datadoghq.core.if",
  "parameters": [
    {
      "name": "condition",
      "value": "{{ Source.securityFinding.severity == 'critical' }}"
    }
  ],
  "outboundEdges": [
    { "nextStepName": "Immediate_remediation", "branchName": "true" },
    { "nextStepName": "Create_ticket", "branchName": "false" }
  ]
}
```

**Condition syntax:** The `condition` parameter accepts a Datadog template expression that evaluates to a boolean. Supported operators:

| Operator | Example |
|---|---|
| Equality | `{{ Steps.Check.status == 'ACTIVE' }}` |
| Inequality | `{{ Steps.Count.value != 0 }}` |
| Greater/Less than | `{{ Steps.Metric.value > 100 }}` |
| Logical AND | `{{ Steps.A.result == 'ok' && Steps.B.result == 'ok' }}` |
| Logical OR | `{{ Steps.A.result == 'fail' \|\| Steps.B.result == 'fail' }}` |
| Contains | `{{ Steps.List.data.includes('target') }}` |
| Negation | `{{ !Steps.Flag.enabled }}` |

**Branch names:** Must be exactly `"true"` and `"false"` (strings, lowercase).

---

### Switch (Multiple Branches)

Routes execution to one of many paths based on matching a value against multiple cases. More readable than nested If steps.

**Action ID:** `com.datadoghq.core.switch`

```json
{
  "name": "Route_by_severity",
  "actionId": "com.datadoghq.core.switch",
  "parameters": [
    {
      "name": "value",
      "value": "{{ Source.securityFinding.severity }}"
    }
  ],
  "outboundEdges": [
    { "nextStepName": "Critical_path", "branchName": "critical" },
    { "nextStepName": "High_path", "branchName": "high" },
    { "nextStepName": "Medium_path", "branchName": "medium" },
    { "nextStepName": "Default_path", "branchName": "default" }
  ]
}
```

**Branch matching:** The `branchName` of each outbound edge is compared to the evaluated `value`. The `"default"` branch is taken when no other branch matches.

---

### Sleep (Wait/Delay)

Pauses workflow execution for a specified duration before continuing to the next step.

**Action ID:** `com.datadoghq.core.sleep`

```json
{
  "name": "Wait_for_propagation",
  "actionId": "com.datadoghq.core.sleep",
  "parameters": [
    {
      "name": "duration",
      "value": "30s"
    }
  ],
  "outboundEdges": [
    { "nextStepName": "Verify_change", "branchName": "main" }
  ]
}
```

**Duration format:** A string with a numeric value and unit suffix:
- `"30s"` -- 30 seconds
- `"5m"` -- 5 minutes
- `"1h"` -- 1 hour
- `"1d"` -- 1 day

The duration can also use template expressions: `"{{ Steps.Calculate_wait.duration }}s"`.

---

### For Loop

Iterates over a list, executing one or more child steps for each element.

**Action ID:** `com.datadoghq.core.forLoop`

```json
{
  "name": "Process_each_instance",
  "actionId": "com.datadoghq.core.forLoop",
  "parameters": [
    {
      "name": "list",
      "value": "{{ Steps.List_instances.Reservations }}"
    }
  ],
  "outboundEdges": [
    { "nextStepName": "Tag_instance", "branchName": "loop" },
    { "nextStepName": "Summary_step", "branchName": "after_loop" }
  ]
}
```

**Inside the loop body:**
- `{{ Current.Value }}` -- The current element in the iteration
- `{{ Current.Index }}` -- The zero-based index of the current iteration
- `{{ Current.Value.fieldName }}` -- Access nested fields on the current element

**Branch names:**
- `"loop"` -- Points to the first step of the loop body
- `"after_loop"` -- Points to the step executed after all iterations complete

**Maximum iterations:** 2,000 per loop invocation. If the list has more than 2,000 items, the loop stops at the 2,000th element and proceeds to `after_loop`. Consider batching or filtering the list before the loop if this limit might be reached.

**Loop results:** After the loop completes, step outputs from within the loop are available as arrays indexed by iteration.

---

### While Loop

Repeats a set of steps as long as a condition evaluates to true.

**Action ID:** `com.datadoghq.core.whileLoop`

```json
{
  "name": "Poll_until_ready",
  "actionId": "com.datadoghq.core.whileLoop",
  "parameters": [
    {
      "name": "condition",
      "value": "{{ Steps.Check_status.status != 'ACTIVE' }}"
    }
  ],
  "outboundEdges": [
    { "nextStepName": "Check_status", "branchName": "loop" },
    { "nextStepName": "Proceed", "branchName": "after_loop" }
  ]
}
```

**Maximum iterations:** 2,000. The loop exits automatically if this limit is reached, proceeding to `after_loop`. Always include a Sleep step inside the loop body to avoid rapid polling.

---

## Error Handling

### Retry Configuration

Any step can be configured with automatic retries on failure.

```json
{
  "name": "Call_aws_api",
  "actionId": "com.datadoghq.aws.ecs.describeTaskDefinition",
  "connectionLabel": "INTEGRATION_AWS",
  "parameters": [ "..." ],
  "retries": {
    "count": 3,
    "interval": "10s",
    "backoff": "exponential"
  }
}
```

**Retry fields:**

| Field | Type | Description |
|---|---|---|
| `count` | int | Number of retry attempts (1-5) |
| `interval` | string | Base wait time between retries (e.g., `"5s"`, `"30s"`) |
| `backoff` | string | `"constant"` (same interval each time) or `"exponential"` (doubles each retry) |

With exponential backoff and `interval: "10s"`, retry waits are: 10s, 20s, 40s.

### Error Paths

Steps can define an error branch that executes when the step fails (after all retries are exhausted).

```json
{
  "name": "Revoke_ingress",
  "actionId": "com.datadoghq.aws.ec2.revoke_security_group_ingress",
  "connectionLabel": "INTEGRATION_AWS",
  "parameters": [ "..." ],
  "outboundEdges": [
    { "nextStepName": "Next_step", "branchName": "main" },
    { "nextStepName": "Handle_failure", "branchName": "error" }
  ]
}
```

**Branch names:** `"main"` for the success path, `"error"` for the failure path. In the error handler step, access the error details via `{{ Steps.Revoke_ingress.error }}`.

### Wait-Until Conditions

Some steps support a `waitUntil` configuration that polls a condition before considering the step complete.

```json
{
  "name": "Update_service",
  "actionId": "com.datadoghq.aws.ecs.updateEcsService",
  "connectionLabel": "INTEGRATION_AWS",
  "parameters": [ "..." ],
  "waitUntil": {
    "condition": "{{ Steps.Update_service.service.deployments[0].rolloutState == 'COMPLETED' }}",
    "timeout": "600s",
    "pollInterval": "30s"
  }
}
```

This causes the step to poll the condition at the specified interval until it evaluates to true or the timeout elapses.

---

## Expressions

Workflow expressions allow data transformation and logic within step parameters using template syntax `{{ ... }}`.

### JavaScript Expressions

#### Inline Expressions

Short one-line JavaScript expressions embedded directly in a parameter value:

```
{{ Steps.Get_instances.Reservations.length }}
{{ Steps.Get_data.result.map(item => item.name).join(', ') }}
{{ new Date().toISOString() }}
```

#### JavaScript Function Steps (Data Transformation)

Full JavaScript functions for complex transformations. Uses the `com.datadoghq.datatransformation.func` action.

**Action ID:** `com.datadoghq.datatransformation.func`

```json
{
  "name": "Transform_image_tag",
  "actionId": "com.datadoghq.datatransformation.func",
  "parameters": [
    {
      "name": "script",
      "value": "function main(args) {\n  const containers = args.Steps.Describe_task_definition.taskDefinition.containerDefinitions;\n  return containers.map(c => ({\n    ...c,\n    image: c.image.replace(/:.*$/, ':' + args.Trigger.image_tag)\n  }));\n}"
    }
  ]
}
```

**Function contract:**
- Must define a `function main(args)` that returns a value
- `args` contains the full workflow context: `args.Steps.*`, `args.Trigger.*`, `args.Source.*`
- Return value is available in subsequent steps as `{{ Steps.Transform_image_tag.data }}`
- Maximum script size: 10 KB

**Available libraries:**
- **Lodash** (`_`): Full Lodash library is available globally. Use `_.get()`, `_.groupBy()`, `_.flatten()`, etc.
- Standard JavaScript built-ins: `JSON`, `Date`, `Math`, `Array`, `Object`, `RegExp`, `String`, `Map`, `Set`

**Examples:**

```javascript
// Extract unique tags from a list of resources
function main(args) {
  const resources = args.Steps.List_resources.data;
  return _.uniq(_.flatMap(resources, r => r.tags));
}

// Build a summary report
function main(args) {
  const instances = args.Steps.Describe_instances.Reservations
    .flatMap(r => r.Instances);
  return {
    total: instances.length,
    running: instances.filter(i => i.State.Name === 'running').length,
    stopped: instances.filter(i => i.State.Name === 'stopped').length,
    ids: instances.map(i => i.InstanceId)
  };
}
```

#### Expression Steps

For simpler transformations that do not need a full function, use an expression step:

**Action ID:** `com.datadoghq.datatransformation.expression`

```json
{
  "name": "Extract_count",
  "actionId": "com.datadoghq.datatransformation.expression",
  "parameters": [
    {
      "name": "expression",
      "value": "{{ Steps.List_items.data.length }}"
    }
  ]
}
```

The result is available as `{{ Steps.Extract_count.data }}`.

---

### Python Expressions

Python 3.12.8 runtime for more complex data processing. Uses the `com.datadoghq.datatransformation.pythonFunction` action.

**Action ID:** `com.datadoghq.datatransformation.pythonFunction`

```json
{
  "name": "Analyze_findings",
  "actionId": "com.datadoghq.datatransformation.pythonFunction",
  "parameters": [
    {
      "name": "script",
      "value": "def main(ctx):\n    findings = ctx['Steps']['List_findings']['data']\n    critical = [f for f in findings if f['severity'] == 'critical']\n    return {\n        'total': len(findings),\n        'critical_count': len(critical),\n        'critical_resources': [f['resource'] for f in critical]\n    }"
    }
  ]
}
```

**Function contract:**
- Must define a `def main(ctx)` function that returns a serializable value
- `ctx` is a dictionary with the full workflow context: `ctx['Steps']`, `ctx['Trigger']`, `ctx['Source']`
- Return value is available as `{{ Steps.Analyze_findings.data }}`

**Available libraries:**
- `rsa` -- RSA encryption/decryption
- `python-dateutil` -- Advanced date parsing and manipulation
- Standard library: `json`, `re`, `datetime`, `collections`, `itertools`, `math`, `hashlib`, `base64`, `urllib.parse`

**Example with dateutil:**

```python
def main(ctx):
    from dateutil import parser, relativedelta
    from datetime import datetime

    created_str = ctx['Steps']['Get_resource']['createdAt']
    created = parser.parse(created_str)
    age_days = (datetime.utcnow() - created).days

    return {
        'created': created.isoformat(),
        'age_days': age_days,
        'is_stale': age_days > 90
    }
```

---

## Custom Mutable Variables (Set Variable Action)

The **Set Variable** action lets you create or update mutable variables that persist across steps within a single workflow execution.

**Action ID:** `com.datadoghq.core.setVariable`

```json
{
  "name": "Initialize_counter",
  "actionId": "com.datadoghq.core.setVariable",
  "parameters": [
    { "name": "variableName", "value": "processed_count" },
    { "name": "variableValue", "value": "0" }
  ]
}
```

**Accessing the variable in subsequent steps:**
```
{{ Variables.processed_count }}
```

**Updating inside a loop:**
```json
{
  "name": "Increment_counter",
  "actionId": "com.datadoghq.core.setVariable",
  "parameters": [
    { "name": "variableName", "value": "processed_count" },
    { "name": "variableValue", "value": "{{ Variables.processed_count + 1 }}" }
  ]
}
```

**Use cases:**
- Accumulating counts or results across loop iterations
- Building a summary string step by step
- Tracking state across conditional branches
- Setting flags for downstream conditional logic

---

## Output Parameters

Output parameters define the values a workflow exposes to callers, particularly important for child workflows (workflow-to-workflow trigger).

**Configured in the workflow spec:**

```json
{
  "outputParameters": [
    {
      "name": "remediation_result",
      "label": "Remediation Result",
      "type": "OBJECT",
      "value": "{{ Steps.Final_step.result }}"
    },
    {
      "name": "affected_resources",
      "label": "Affected Resources",
      "type": "ARRAY",
      "value": "{{ Steps.Collect_resources.data }}"
    }
  ]
}
```

**In the parent workflow accessing child outputs:**
```
{{ Steps.Run_child_workflow.outputs.remediation_result }}
{{ Steps.Run_child_workflow.outputs.affected_resources }}
```

Output parameters are also visible in the workflow execution details in the Datadog UI and via the `GET /api/v2/workflows/{id}/instances/{instance_id}` API response in `attributes.outputs`.
