# Quick Start - Datadog LLM Observability Evaluation Submission

## Overview

This project contains a Python script to submit LLM Observability evaluations to Datadog for the `query_datadog_metrics` action in the Action Catalog.

## Files

- `submit_evaluation.py` - Main script to submit evaluations
- `EVALUATION_SUBMISSION_REPORT.md` - Detailed report with findings and learnings
- `QUICK_START.md` - This file

## Prerequisites

1. Datadog API Key (DD_API_KEY or DATADOG_API_KEY)
2. Datadog Application Key (DD_APP_KEY or DATADOG_APP_KEY)
3. Python 3.x with `requests` library

## Setup

Configure credentials in the `.env` file:
```bash
DATADOG_API_KEY=your_api_key_here
DATADOG_APP_KEY=your_app_key_here
DATADOG_SITE=datadoghq.com
```

## Usage

Simply run the script:

```bash
python3 submit_evaluation.py
```

## What It Does

The script submits an evaluation to Datadog's LLM Observability platform with:

- **ml_app**: `action_catalog`
- **label**: `accuracy`
- **metric_type**: `score`
- **score_value**: `0.85`
- **join_on**: Tag-based joining with `action_name=query_datadog_metrics`

## Example Output

```
Submitting evaluation to Datadog LLM Observability...
Endpoint: https://api.datadoghq.com/api/intake/llm-obs/v2/eval-metric
Payload: {
  "data": {
    "type": "evaluation_metric",
    "attributes": {
      "metrics": [
        {
          "ml_app": "action_catalog",
          "label": "accuracy",
          "metric_type": "score",
          "score_value": 0.85,
          ...
        }
      ]
    }
  }
}

Response Status Code: 202
✓ Evaluation submitted successfully!
```

## API Details

- **Endpoint**: `POST https://api.datadoghq.com/api/intake/llm-obs/v2/eval-metric`
- **Authentication**:
  - Header: `DD-API-KEY: <your_api_key>`
  - Header: `DD-APPLICATION-KEY: <your_app_key>`
- **Content-Type**: `application/json`
- **Success Response**: HTTP 202 Accepted

## Key Implementation Details

### Tag-Based Joining

The evaluation uses tag-based joining to associate with spans:

```python
"join_on": {
    "tag": {
        "key": "action_name",
        "value": "query_datadog_metrics"
    }
}
```

This means the evaluation will be joined to any span that has the tag `action_name=query_datadog_metrics`.

### Score Value Field

For score-type metrics, use `score_value` (not `value`):

```python
"metric_type": "score",
"score_value": 0.85
```

## Customization

You can customize the evaluation by modifying the function parameters:

```python
submit_evaluation(
    ml_app="your_app_name",
    label="your_metric_label",
    score_value=0.95,
    action_name="your_action_name"
)
```

## Troubleshooting

### Error: DD_API_KEY and DD_APP_KEY environment variables must be set

Make sure the `.env` file exists and contains the required keys, or export them:

```bash
export DD_API_KEY="your_api_key"
export DD_APP_KEY="your_app_key"
```

### Error: 400 Bad Request

Check that your payload includes:
- `join_on` field (required)
- `score_value` field for score metrics (not `value`)
- Valid `ml_app`, `label`, and `metric_type`

## Next Steps

1. Verify the evaluation appears in the Datadog LLM Observability UI
2. Create spans tagged with `action_name=query_datadog_metrics` to join with this evaluation
3. Set up automated evaluation submission for production use

## Resources

- [Datadog LLM Observability Evaluations](https://docs.datadoghq.com/llm_observability/evaluations/)
- [Submit Evaluations Documentation](https://docs.datadoghq.com/llm_observability/submit_evaluations/)
- [HTTP API Reference](https://docs.datadoghq.com/llm_observability/instrumentation/api/)
