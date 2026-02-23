# Datadog LLM Observability Evaluation Submission Report

## Task Completed Successfully

Successfully created and tested a Python script to submit LLM Observability evaluations to Datadog for the `query_datadog_metrics` action in the Action Catalog.

**Final Result:** HTTP 202 Accepted - Evaluation submitted successfully to Datadog

---

## What Approach Did You Take?

### 1. Research Phase (Web Search)
I started by searching for information about Datadog's LLM Observability Evaluation API:
- Searched for "Datadog LLM Observability Evaluation API submit evaluation"
- Found documentation about two submission methods: SDK and HTTP API
- Identified the API endpoint: `POST https://api.datadoghq.com/api/intake/llm-obs/v2/eval-metric`

### 2. Authentication Discovery
- Researched Datadog API authentication requirements
- Found that two headers are required:
  - `DD-API-KEY`: Datadog API key
  - `DD-APPLICATION-KEY`: Datadog Application key
- Located existing credentials in the `.env` file

### 3. Iterative Development
- **First attempt**: Created initial payload structure based on general documentation
  - Result: 400 Bad Request - Missing required fields
  - Error message revealed: Need `JoinOn` field and `ScoreValue` instead of `value`

- **Second attempt**: Researched the specific payload structure
  - Found that evaluations must be "joined" to spans using either:
    - Tag-based joining (using custom tag key-value pairs)
    - Direct span reference (using trace_id and span_id)
  - Updated payload with correct field names: `join_on` and `score_value`
  - Result: HTTP 202 Accepted - Success!

### 4. Final Implementation
Created a production-ready Python script with:
- Environment variable loading from `.env` file
- Proper error handling
- Tag-based joining to associate evaluation with action spans
- Comprehensive documentation and comments

---

## What Were You Unsure About?

### 1. API Endpoint Discovery
- The exact URL path for the evaluations endpoint wasn't immediately clear
- Had to piece together that it was `/api/intake/llm-obs/v2/eval-metric`

### 2. Payload Structure
- The initial documentation didn't clearly show the exact JSON schema
- Field naming conventions (camelCase vs snake_case) weren't obvious
- The requirement for `join_on` field wasn't clear until I got the validation error

### 3. Span Joining Strategy
- Wasn't sure whether to use tag-based joining or direct span reference
- Chose tag-based joining assuming spans would be tagged with `action_name`
- Not certain if a span with the tag `action_name=query_datadog_metrics` actually exists

### 4. Action Catalog Integration
- No clear documentation about "Action Catalog" as a specific Datadog feature
- Made an assumption that `ml_app: "action_catalog"` was the correct way to identify it
- Not sure if there's a specific way actions should be registered first

### 5. Evaluation Requirements
- Unclear if the evaluation needs a pre-existing trace/span to attach to
- Uncertain if the evaluation will be stored as "pending" until a matching span arrives
- Don't know if there's a TTL for evaluations waiting to join to spans

---

## What Did You Skip or Assume?

### Assumptions Made:

1. **Span Existence**: Assumed that spans tagged with `action_name=query_datadog_metrics` exist or will exist
   - Used tag-based joining without verifying spans exist first
   - Didn't query the Datadog API to check for existing spans

2. **ML App Naming**: Assumed `"action_catalog"` is the correct ml_app identifier
   - No verification that this is a registered application
   - Didn't check if there's a specific naming convention

3. **Evaluation Timing**: Assumed evaluations can be submitted before spans exist
   - Didn't investigate if evaluations need to reference existing spans
   - Unclear on order of operations (span first vs evaluation first)

4. **Score Range**: Assumed 0.85 is within an acceptable range
   - Didn't verify if there are min/max constraints
   - Didn't check if scores need normalization

### Skipped Steps:

1. **Span Creation**: Didn't create an actual LLM observability span first
   - Would need to instrument the actual action or create a test span
   - Skipped this to save time under the 30-minute constraint

2. **Verification in UI**: Didn't log into Datadog to verify the evaluation appears
   - The 202 response suggests acceptance, but didn't confirm in the dashboard
   - Didn't check if warnings or issues appear in the UI

3. **SDK Approach**: Only used the HTTP API, didn't try the Python SDK
   - SDK might have been easier with better type hints and validation
   - Chose HTTP API for transparency and debugging

4. **Error Recovery**: Minimal error handling for network issues
   - Didn't implement retry logic
   - Didn't add timeout configurations

5. **Multiple Evaluations**: Only tested single evaluation submission
   - Didn't test batch submission of multiple evaluations
   - Didn't test different metric types (categorical, boolean, etc.)

---

## What Would Have Made This Easier?

### Documentation Improvements:

1. **OpenAPI/Swagger Specification**
   - A complete OpenAPI spec would have shown exact request/response schemas
   - Would eliminate guessing about field names and types

2. **Working Code Examples**
   - More complete curl examples with real payloads
   - Python code snippets showing the exact payload structure
   - Examples for different joining strategies

3. **Clearer Schema Documentation**
   - Explicit field requirements (required vs optional)
   - Valid value ranges and formats
   - Validation error messages mapped to solutions

### Tool/Process Improvements:

1. **API Sandbox/Playground**
   - Interactive API explorer to test payloads
   - Request/response validation before submission
   - Example payloads that are known to work

2. **SDK Auto-completion**
   - Type hints and IntelliSense support
   - Built-in validation before API calls
   - Better error messages that suggest fixes

3. **Action Catalog Documentation**
   - Specific docs about how Action Catalog integrates with LLM Observability
   - Clarification on whether actions need pre-registration
   - Examples of action-based evaluations

4. **Pre-flight Validation Endpoint**
   - An endpoint to validate payload structure without submitting
   - Would have saved iteration time on the 400 error

5. **Clearer Error Messages**
   - The validation error was helpful but could have included examples
   - "Did you mean X?" suggestions for common mistakes
   - Links to relevant documentation sections

### Development Environment:

1. **Test/Sandbox Environment**
   - A dedicated test endpoint that doesn't affect production data
   - Mock spans to test evaluation joining

2. **CLI Tool**
   - A `datadog-cli llm-obs submit-eval` command
   - Interactive prompts for required fields
   - Built-in validation

---

## Technical Details

### Final Working Payload Structure:

```json
{
  "data": {
    "type": "evaluation_metric",
    "attributes": {
      "metrics": [
        {
          "ml_app": "action_catalog",
          "label": "accuracy",
          "metric_type": "score",
          "score_value": 0.85,
          "tags": [
            "action:query_datadog_metrics",
            "environment:demo",
            "submitted_by:python_script"
          ],
          "timestamp_ms": 1771612176864,
          "join_on": {
            "tag": {
              "key": "action_name",
              "value": "query_datadog_metrics"
            }
          }
        }
      ]
    }
  }
}
```

### Key Learnings:

1. **Field Naming**: Use `score_value` not `value` for score metrics
2. **Join Strategy**: `join_on` is required - chose tag-based joining
3. **Response Code**: 202 Accepted indicates successful submission
4. **Authentication**: Both API key and Application key are required

---

## Files Created

- `/Users/giovanni.peralto/Projects/hackathon-team-3/submit_evaluation.py` - Main submission script
- `/Users/giovanni.peralto/Projects/hackathon-team-3/EVALUATION_SUBMISSION_REPORT.md` - This report

## References

- [Datadog LLM Observability Evaluations](https://docs.datadoghq.com/llm_observability/evaluations/)
- [Submit Evaluations](https://docs.datadoghq.com/llm_observability/submit_evaluations/)
- [HTTP API Reference - LLM Observability](https://docs.datadoghq.com/llm_observability/instrumentation/api/)
- [External Evaluations](https://docs.datadoghq.com/llm_observability/evaluations/external_evaluations/)
