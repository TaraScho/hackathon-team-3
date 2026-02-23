# Quick Start: Submit Datadog LLM Observability Evaluation

This guide helps you quickly submit an evaluation for the "analyze_logs" action.

## Prerequisites

- Python 3.x installed
- Datadog API and APP keys set in `.env` file
- `requests` library installed

## Setup

1. **Verify your .env file has the required credentials:**
   ```bash
   cat .env | grep DATADOG
   ```

   Should show:
   ```
   DATADOG_API_KEY=your_api_key_here
   DATADOG_APP_KEY=your_app_key_here
   DATADOG_SITE=datadoghq.com
   ```

2. **Install dependencies (if needed):**
   ```bash
   pip3 install requests
   ```

## Submit Evaluation

### Option 1: Use Default Values (Recommended for Demo)

Simply run:
```bash
python3 submit_evaluation.py
```

This will submit an evaluation with:
- Action: `analyze_logs`
- Label: `relevance`
- Score: `0.91`
- ML App: `action_catalog`

### Option 2: Customize Values in Code

Edit `submit_evaluation.py` and modify the defaults in the function signature:

```python
def submit_evaluation(
    ml_app="action_catalog",      # Change if needed
    label="relevance",             # Change to other labels like "accuracy", "quality"
    score_value=0.91,              # Change score (0.0 to 1.0)
    action_name="analyze_logs"     # Change action name if needed
):
```

Then run:
```bash
python3 submit_evaluation.py
```

### Option 3: Import and Use Programmatically

In your Python code:
```python
from submit_evaluation import submit_evaluation

# Submit with defaults
success = submit_evaluation()

# Or customize
success = submit_evaluation(
    label="accuracy",
    score_value=0.88,
    action_name="analyze_logs"
)

if success:
    print("Evaluation submitted!")
else:
    print("Submission failed")
```

## Expected Output

On success, you should see:
```
Submitting evaluation to Datadog LLM Observability...
Endpoint: https://api.datadoghq.com/api/intake/llm-obs/v2/eval-metric
Payload: {
  "data": {
    "type": "evaluation_metric",
    ...
  }
}

Response Status Code: 202
Response Body: {"data": {"id": "...", ...}}

✓ Evaluation submitted successfully!
```

## Verify in Datadog UI

1. Navigate to **APM → LLM Observability → Evaluations**
2. Wait 1-2 minutes for processing
3. Look for evaluation with:
   - Label: `relevance`
   - Score: `0.91`
   - Tags: `action:analyze_logs`

## Troubleshooting

### Error: Missing DD_API_KEY and DD_APP_KEY
**Solution**: Check your `.env` file has `DATADOG_API_KEY` and `DATADOG_APP_KEY` set.

### Error: 403 Forbidden
**Solution**: Verify your APP key is valid. APP key is different from API key.

### Error: 400 Bad Request
**Solution**: Check the error message in the response. Common issues:
- Invalid label format (use only letters, numbers, underscore)
- Invalid score value (must be between 0.0 and 1.0)

### Evaluation doesn't appear in UI
**Possible causes**:
1. No matching spans exist with `action_name=analyze_logs` tag
2. Need to wait longer (allow up to 5 minutes)
3. Check you're looking at the correct time range in Datadog

**Solution**: Ensure your action creates spans with the `action_name` tag before submitting evaluations.

## What's Next?

1. **Create spans for your action**: Ensure the `analyze_logs` action creates spans with `action_name=analyze_logs` tag
2. **Automate evaluation submission**: Integrate this into your action execution workflow
3. **Add more evaluation types**: Submit multiple evaluations (accuracy, quality, latency, etc.)
4. **Monitor trends**: Use Datadog dashboards to track evaluation scores over time

## Quick Reference

| Parameter | Default Value | Description |
|-----------|---------------|-------------|
| ml_app | action_catalog | Application name in Datadog |
| label | relevance | Evaluation metric name |
| score_value | 0.91 | Evaluation score (0.0-1.0) |
| action_name | analyze_logs | Action to evaluate |

## Documentation

For more details, see:
- `EVALUATION_IMPLEMENTATION_REPORT.md` - Full implementation report
- `submit_evaluation.py` - Source code with inline comments

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the implementation report for common mistakes
3. Verify API credentials and permissions in Datadog
