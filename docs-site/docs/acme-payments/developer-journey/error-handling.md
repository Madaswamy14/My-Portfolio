---
title: Error Handling Journey
description: Build resilience into the integration, not only the happy path.
---

# Error Handling Journey

Reliable integrations are built on clear error handling, not only successful responses.

## Common categories

- `400 Bad Request` — request validation failed
- `401 Unauthorized` — credentials are missing or invalid
- `409 Conflict` — the request is colliding with previous state or idempotency expectations
- `429 Too Many Requests` — back off and retry later
- `5xx` — treat as transient and retry carefully when safe

## Integration practices

### Capture request metadata

Store request IDs and relevant response data so support and debugging workflows are easier later.

### Distinguish retryable and non-retryable failures

Only retry requests when the failure is transient and the operation is safe to repeat.

### Pair errors with webhooks

If a client times out but the API later processes the request, your webhook flow should help reconcile the final state.

## Detailed guide

See [Error Handling](../concepts/error-handling.md) for the canonical guidance.