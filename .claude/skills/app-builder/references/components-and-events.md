# App Builder Components and Events Reference

Complete reference for all component types, event types, reaction types, and component state functions available in Datadog App Builder.

---

## Component Types

App Builder provides 22 component types organized into five categories. Every component shares this base structure:

```json
{
  "type": "componentType",
  "name": "uniqueName",
  "properties": { "...type-specific..." },
  "events": []
}
```

### Layout Components

Layout components control how other components are arranged on screen.

#### Grid

The root component of every app. All other components are nested inside a grid's `children` array.

```json
{
  "type": "grid",
  "name": "grid0",
  "properties": {
    "children": [],
    "columns": 12,
    "isVisible": true
  }
}
```

- `columns`: Number of grid columns (default 12)
- `children`: Array of child components with layout metadata
- Every app must have exactly one root grid named in `rootInstanceName`

#### Container

Groups related components with an optional title and border.

```json
{
  "type": "container",
  "name": "instanceDetails",
  "properties": {
    "title": "Instance Details",
    "isCollapsible": true,
    "isCollapsed": false,
    "isVisible": "{{ ui.instanceTable.selectedRow !== undefined }}",
    "children": []
  }
}
```

- `isCollapsible`: Allows the user to collapse/expand the container
- `isVisible`: Expression controlling conditional rendering

#### Modal

An overlay dialog triggered by an event reaction. Not placed in the grid directly -- opened via an `openModal` reaction.

```json
{
  "type": "modal",
  "name": "confirmDialog",
  "properties": {
    "title": "Confirm Action",
    "size": "medium",
    "children": []
  }
}
```

- `size`: `"small"`, `"medium"`, `"large"`
- Opened with `openModal` reaction, closed with `closeModal` reaction or the built-in close button

#### Tabs

Organizes content into switchable tab panels.

```json
{
  "type": "tabs",
  "name": "serviceTabs",
  "properties": {
    "tabs": [
      { "label": "EC2 Instances", "children": [] },
      { "label": "ECS Tasks", "children": [] },
      { "label": "Lambda Functions", "children": [] }
    ],
    "defaultTabIndex": 0
  }
}
```

### Input Components

Input components collect user data and expose their current value via component state.

#### TextInput

```json
{
  "type": "textInput",
  "name": "regionInput",
  "properties": {
    "label": "AWS Region",
    "defaultValue": "us-east-1",
    "placeholder": "Enter region...",
    "isRequired": false,
    "isDisabled": false
  }
}
```

State: `ui.regionInput.value`

#### NumberInput

```json
{
  "type": "numberInput",
  "name": "desiredCapacity",
  "properties": {
    "label": "Desired Capacity",
    "defaultValue": 2,
    "min": 0,
    "max": 100,
    "step": 1
  }
}
```

State: `ui.desiredCapacity.value`

#### Select

Single-value dropdown.

```json
{
  "type": "select",
  "name": "regionSelect",
  "properties": {
    "label": "Region",
    "options": [
      { "label": "US East (N. Virginia)", "value": "us-east-1" },
      { "label": "US West (Oregon)", "value": "us-west-2" },
      { "label": "EU (Ireland)", "value": "eu-west-1" }
    ],
    "defaultValue": "us-east-1",
    "isSearchable": true,
    "isClearable": true
  }
}
```

State: `ui.regionSelect.value`

#### MultiSelect

Multiple-value dropdown. Same properties as Select, plus returns an array.

```json
{
  "type": "multiSelect",
  "name": "tagFilter",
  "properties": {
    "label": "Filter by Tags",
    "options": "{{ queries.listTags.data.tags.map(t => ({label: t, value: t})) }}",
    "defaultValue": []
  }
}
```

State: `ui.tagFilter.value` (array)

#### Checkbox

```json
{
  "type": "checkbox",
  "name": "autoRefresh",
  "properties": {
    "label": "Auto-refresh every 30s",
    "defaultValue": false
  }
}
```

State: `ui.autoRefresh.value` (boolean)

#### RadioGroup

```json
{
  "type": "radioGroup",
  "name": "instanceState",
  "properties": {
    "label": "Filter by State",
    "options": [
      { "label": "Running", "value": "running" },
      { "label": "Stopped", "value": "stopped" },
      { "label": "All", "value": "all" }
    ],
    "defaultValue": "all",
    "direction": "horizontal"
  }
}
```

State: `ui.instanceState.value`

#### DatePicker

```json
{
  "type": "datePicker",
  "name": "startDate",
  "properties": {
    "label": "Start Date",
    "defaultValue": "",
    "minDate": "",
    "maxDate": "",
    "includeTime": true
  }
}
```

State: `ui.startDate.value` (ISO 8601 string)

#### TextArea

Multi-line text input.

```json
{
  "type": "textArea",
  "name": "policyDocument",
  "properties": {
    "label": "IAM Policy JSON",
    "defaultValue": "",
    "rows": 10,
    "placeholder": "Paste policy document..."
  }
}
```

State: `ui.policyDocument.value`

#### FileUpload

```json
{
  "type": "fileUpload",
  "name": "configFile",
  "properties": {
    "label": "Upload Configuration",
    "accept": ".json,.yaml,.yml",
    "maxFileSizeMB": 5,
    "multiple": false
  }
}
```

State: `ui.configFile.files` (array of file objects with `name`, `content`, `size`)

### Display Components

Display components render data but do not accept user input.

#### Text

Renders markdown or plain text. Supports expression interpolation.

```json
{
  "type": "text",
  "name": "statusText",
  "properties": {
    "value": "**Status:** {{ queries.describeInstance.data.state }}",
    "format": "markdown"
  }
}
```

- `format`: `"markdown"` or `"plain"`

#### Table

The most commonly used display component. Renders tabular data with sorting, searching, and row selection.

```json
{
  "type": "table",
  "name": "instanceTable",
  "properties": {
    "data": "{{ queries.listInstances.data.instances }}",
    "columns": [
      { "header": "Instance ID", "accessor": "instanceId", "width": 200 },
      { "header": "State", "accessor": "state" },
      { "header": "Type", "accessor": "instanceType" }
    ],
    "isSearchable": true,
    "isSortable": true,
    "isPaginated": true,
    "pageSize": 25,
    "isRowSelectable": true
  }
}
```

State: `ui.instanceTable.selectedRow`, `ui.instanceTable.selectedRows`, `ui.instanceTable.searchText`, `ui.instanceTable.page`

#### Image

```json
{
  "type": "image",
  "name": "logo",
  "properties": {
    "src": "https://example.com/logo.png",
    "alt": "Company Logo",
    "width": 120,
    "height": 40
  }
}
```

#### Stat

Displays a single metric value with optional label and trend indicator.

```json
{
  "type": "stat",
  "name": "runningCount",
  "properties": {
    "value": "{{ queries.listInstances.data.instances.filter(i => i.state === 'running').length }}",
    "label": "Running Instances",
    "prefix": "",
    "suffix": "",
    "color": "green"
  }
}
```

#### CodeEditor

Read-only or editable code block with syntax highlighting.

```json
{
  "type": "codeEditor",
  "name": "jsonViewer",
  "properties": {
    "value": "{{ JSON.stringify(queries.describeInstance.data, null, 2) }}",
    "language": "json",
    "isReadOnly": true,
    "height": 300
  }
}
```

- `language`: `"json"`, `"python"`, `"javascript"`, `"yaml"`, `"bash"`, `"sql"`, `"hcl"`

State: `ui.jsonViewer.value` (when editable)

### Action Components

Action components trigger behavior when interacted with.

#### Button

```json
{
  "type": "button",
  "name": "refreshButton",
  "properties": {
    "label": "Refresh",
    "variant": "primary",
    "isDisabled": "{{ queries.listInstances.isLoading }}",
    "isLoading": "{{ queries.listInstances.isLoading }}"
  },
  "events": [
    {
      "name": "click",
      "type": "custom",
      "reactions": [
        { "type": "triggerQuery", "queryName": "listInstances" }
      ]
    }
  ]
}
```

- `variant`: `"primary"`, `"secondary"`, `"danger"`, `"ghost"`

#### Link

Navigational link. Opens a URL or triggers a reaction.

```json
{
  "type": "link",
  "name": "consoleLink",
  "properties": {
    "label": "Open in AWS Console",
    "href": "https://console.aws.amazon.com/ec2/home?region={{ ui.regionSelect.value }}#Instances:instanceId={{ ui.instanceTable.selectedRow.instanceId }}"
  }
}
```

#### CallToAction

A prominent action block with title, description, and button. Used for empty states or primary actions.

```json
{
  "type": "callToAction",
  "name": "noInstancesCTA",
  "properties": {
    "title": "No instances found",
    "description": "Try changing your region or filters",
    "buttonLabel": "Reset Filters",
    "isVisible": "{{ queries.listInstances.data.instances.length === 0 }}"
  },
  "events": [
    {
      "name": "click",
      "type": "custom",
      "reactions": [
        { "type": "setComponentState", "target": "regionSelect", "value": "us-east-1" },
        { "type": "triggerQuery", "queryName": "listInstances" }
      ]
    }
  ]
}
```

### Visualization Components

#### Chart

Renders line, bar, area, pie, or scatter charts from query data.

```json
{
  "type": "chart",
  "name": "cpuChart",
  "properties": {
    "chartType": "line",
    "data": "{{ queries.getMetrics.data.series }}",
    "xAxis": { "field": "timestamp", "label": "Time" },
    "yAxis": { "field": "value", "label": "CPU %" },
    "seriesField": "instanceId",
    "height": 300,
    "showLegend": true
  }
}
```

- `chartType`: `"line"`, `"bar"`, `"area"`, `"pie"`, `"scatter"`

---

## Event Types

Events are triggered by user interactions or lifecycle hooks. Each event has a `name`, `type`, and array of `reactions`.

| Event Name | Fired When | Common Components |
|------------|------------|-------------------|
| `click` | User clicks a button, link, or CTA | Button, Link, CallToAction |
| `change` | Input value changes | TextInput, NumberInput, Select, MultiSelect, Checkbox, RadioGroup, DatePicker, TextArea |
| `submit` | User presses Enter in a text input | TextInput, TextArea |
| `tableRowClick` | User clicks a table row | Table |
| `pageChange` | Table page changes | Table |
| `toggle` | Checkbox or collapsible is toggled | Checkbox, Container |
| `openModal` | A modal is opened (lifecycle) | Modal |
| `closeModal` | A modal is closed (lifecycle) | Modal |
| `load` | Component first renders | Any (typically Grid) |
| `custom` | Programmatically triggered | Any |

### Event Structure

```json
{
  "name": "click",
  "type": "custom",
  "reactions": [
    { "type": "triggerQuery", "queryName": "stopInstance" },
    { "type": "triggerQuery", "queryName": "listInstances" }
  ]
}
```

Events execute their reactions array sequentially. Multiple reactions in the same event run in order.

---

## Reaction Types

Reactions define what happens when an event fires.

### triggerQuery

Executes a named query.

```json
{ "type": "triggerQuery", "queryName": "listInstances" }
```

### setComponentState

Sets a component's state value.

```json
{
  "type": "setComponentState",
  "target": "regionSelect",
  "value": "us-west-2"
}
```

### openModal

Opens a modal component by name.

```json
{ "type": "openModal", "modalName": "confirmDialog" }
```

### closeModal

Closes a modal component by name.

```json
{ "type": "closeModal", "modalName": "confirmDialog" }
```

### openUrl

Opens a URL in a new browser tab.

```json
{
  "type": "openUrl",
  "url": "https://console.aws.amazon.com/ec2/home?region={{ ui.regionSelect.value }}"
}
```

### downloadFile

Triggers a file download.

```json
{
  "type": "downloadFile",
  "filename": "instances.json",
  "content": "{{ JSON.stringify(queries.listInstances.data, null, 2) }}",
  "mimeType": "application/json"
}
```

### setStateVariableValue

Sets the value of a stateVariable query.

```json
{
  "type": "setStateVariableValue",
  "variableName": "selectedRegion",
  "value": "{{ ui.regionSelect.value }}"
}
```

### custom

Executes a JavaScript expression.

```json
{
  "type": "custom",
  "expression": "console.log('Row selected:', ui.instanceTable.selectedRow.instanceId)"
}
```

---

## Component State Functions

Every component exposes state via the `ui` namespace. Access patterns:

### Common State Accessors

| Component Type | State Path | Returns |
|----------------|------------|---------|
| TextInput | `ui.{name}.value` | string |
| NumberInput | `ui.{name}.value` | number |
| Select | `ui.{name}.value` | string (selected option value) |
| MultiSelect | `ui.{name}.value` | array of strings |
| Checkbox | `ui.{name}.value` | boolean |
| RadioGroup | `ui.{name}.value` | string |
| DatePicker | `ui.{name}.value` | ISO 8601 string |
| TextArea | `ui.{name}.value` | string |
| FileUpload | `ui.{name}.files` | array of file objects |
| Table | `ui.{name}.selectedRow` | object (single row) |
| Table | `ui.{name}.selectedRows` | array (multi-select) |
| Table | `ui.{name}.searchText` | string |
| Table | `ui.{name}.page` | number |
| CodeEditor | `ui.{name}.value` | string |

### Query State Accessors

Queries also expose state via the `queries` namespace:

| Path | Returns |
|------|---------|
| `queries.{name}.data` | The query response data |
| `queries.{name}.isLoading` | boolean (true while executing) |
| `queries.{name}.error` | Error object or null |
| `queries.{name}.lastRunAt` | ISO timestamp of last execution |

### Expression Usage in Properties

Component properties accept template expressions using `{{ }}` syntax:

```json
{
  "isVisible": "{{ queries.listInstances.data.instances.length > 0 }}",
  "label": "{{ ui.instanceTable.selectedRow ? 'Edit ' + ui.instanceTable.selectedRow.instanceId : 'Select an instance' }}",
  "isDisabled": "{{ queries.stopInstance.isLoading }}",
  "data": "{{ queries.listInstances.data.instances.filter(i => i.state === ui.stateFilter.value || ui.stateFilter.value === 'all') }}"
}
```

Expressions have full access to `ui`, `queries`, `state` (state variables), and standard JavaScript functions.
