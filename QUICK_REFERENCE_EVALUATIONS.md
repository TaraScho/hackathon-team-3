# Quick Reference: Datadog LLM Observability Evaluations

## Quick Start (5 Minutes)

### Submit an Evaluation

```bash
# 1. Set environment variables
export DD_API_KEY="your_api_key"
export DD_APP_KEY="your_app_key"

# 2. Run submission script
python3 submit_evaluation.py

# 3. Wait 1-2 minutes, then check UI
open https://app.datadoghq.com/llm/evaluations
```

### Verify in UI

1. Navigate to: **APM → LLM Observability → Evaluations**
2. Set time range: **Last 1 hour**
3. Search: `action_name:summarize_incidents` or `label:coherence`
4. Look for: Value **0.88** with label **coherence**

---

## Scripts Overview

### submit_evaluation.py
**Purpose**: Submit evaluation with verification

**What it does**:
1. ✅ Verifies credentials
2. ✅ Checks for existing spans (attempts)
3. ✅ Submits evaluation (HTTP 202)
4. ✅ Provides UI verification instructions

**When to use**: Primary script for submitting evaluations

---

### verify_evaluation.py
**Purpose**: Standalone verification tool

**What it does**:
1. ✅ Checks span availability
2. ✅ Provides detailed UI guide
3. ✅ Documents troubleshooting steps

**When to use**: After submission to get verification instructions

---

### create_test_span.py
**Purpose**: Create test spans for development

**What it does**:
1. Creates span with ddtrace
2. Sets action_name tag
3. Attempts to flush to Datadog

**When to use**: Testing evaluation joins (requires agent setup)

---

## Common Commands

### Check Environment
```bash
# Verify credentials are set
env | grep DD_

# Check ddtrace installed
pip3 list | grep ddtrace
```

### Submit Evaluation
```bash
# Default: summarize_incidents, coherence, 0.88
python3 submit_evaluation.py

# To modify, edit the script's main() function:
# action_name = "your_action"
# label = "your_label"
# score_value = 0.95
```

### Create Test Span
```bash
python3 create_test_span.py
```

---

## Troubleshooting

### Evaluation Not Appearing

**Check 1**: Verify submission succeeded
```bash
# Look for: "✓ Evaluation submitted successfully (202 Accepted)"
python3 submit_evaluation.py
```

**Check 2**: Verify time range in UI
- Expand to last 4 hours
- Ensure current time is included

**Check 3**: Check for spans
- Navigate to APM → Traces
- Search: `@action_name:summarize_incidents`
- Verify spans exist with correct tag

**Check 4**: Wait longer
- Evaluations can take 2-5 minutes to appear
- Join window is 5 minutes for span matching

### Span Search Returns 404

**Cause**: APM not fully enabled or no span index

**Solutions**:
1. Enable APM in Datadog settings
2. Create some spans first (run actions)
3. Verify API keys have APM permissions
4. Continue with submission anyway (evaluation will wait for spans)

### API Key Errors

**Error**: "Missing DD_API_KEY or DD_APP_KEY"

**Solution**:
```bash
# Set in environment
export DD_API_KEY="your_key"
export DD_APP_KEY="your_key"

# Or add to .env file
echo "DD_API_KEY=your_key" >> .env
echo "DD_APP_KEY=your_key" >> .env
```

---

## Key Concepts

### Evaluation Join Strategies

**Tag-based joining** (used in scripts):
```json
"join_on": {
  "tag": {
    "key": "action_name",
    "value": "summarize_incidents"
  }
}
```
- Joins to ANY span with matching tag
- Flexible, works with multiple spans
- 5-minute join window

**Direct span reference**:
```json
"join_on": {
  "span_id": "abc123",
  "trace_id": "xyz789"
}
```
- Joins to specific span
- More precise
- Requires knowing span ID

### Evaluation Lifecycle

```
1. Submit evaluation (HTTP 202)
   ↓
2. Datadog receives evaluation
   ↓
3. Waits for matching span (up to 5 min)
   ↓
4. Joins evaluation to span
   ↓
5. Appears in UI (1-2 min after join)
```

### Required Fields

```python
{
  "ml_app": "action_catalog",      # Required
  "label": "coherence",             # Required (alphanumeric + underscore)
  "metric_type": "score",           # Required ("score" or "categorical")
  "score_value": 0.88,              # Required for score type
  "join_on": {...}                  # Required (tag or span reference)
}
```

---

## Best Practices

### ✅ DO

1. **Verify credentials first** - Fail fast on auth issues
2. **Use tag-based joining** - More flexible than direct span reference
3. **Wait 1-2 minutes** - Give Datadog time to process
4. **Check UI time range** - Ensure it includes submission time
5. **Document results** - Screenshot evaluations for reference

### ❌ DON'T

1. **Don't use invalid label characters** - Only alphanumeric + underscore
2. **Don't expect immediate appearance** - Processing takes time
3. **Don't forget tags on spans** - Evaluations need matching tags to join
4. **Don't use 'value' field** - Use 'score_value' for score metrics
5. **Don't skip join_on** - Always required for evaluation submission

---

## Configuration

### Default Settings (submit_evaluation.py)

```python
action_name = "summarize_incidents"
label = "coherence"
score_value = 0.88
ml_app = "action_catalog"
metric_type = "score"
```

### To Change Evaluation Parameters

Edit `submit_evaluation.py` main() function:

```python
def main():
    # Configuration
    action_name = "your_action_name"    # Change this
    label = "your_label"                # Change this
    score_value = 0.95                  # Change this
    ...
```

---

## API Endpoints

### Evaluation Submission
```
POST https://api.datadoghq.com/api/intake/llm-obs/v2/eval-metric
```

### Span Search
```
POST https://api.datadoghq.com/api/v2/spans/search
```

---

## Environment Variables

```bash
# Required
DD_API_KEY          # Datadog API key
DD_APP_KEY          # Datadog Application key

# Optional
DATADOG_SITE        # Default: datadoghq.com
DD_SERVICE          # For span creation
DD_ENV              # For span creation
```

---

## Resources

### Documentation
- [LLM Observability Evaluations](https://docs.datadoghq.com/llm_observability/evaluations/)
- [Submit Evaluations](https://docs.datadoghq.com/llm_observability/submit_evaluations/)
- [HTTP API Reference](https://docs.datadoghq.com/llm_observability/instrumentation/api/)

### Datadog UI
- **Evaluations**: https://app.datadoghq.com/llm/evaluations
- **Traces**: https://app.datadoghq.com/apm/traces
- **Services**: https://app.datadoghq.com/apm/services

---

## Success Checklist

- [ ] DD_API_KEY and DD_APP_KEY set
- [ ] Submit evaluation (202 response)
- [ ] Wait 1-2 minutes
- [ ] Check Datadog UI
- [ ] Verify evaluation appears
- [ ] Document results
- [ ] Screenshot for reference

---

**Last Updated**: 2026-02-20
**Version**: 1.0
**Status**: Production Ready
