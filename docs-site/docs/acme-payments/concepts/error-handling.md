---
title: Error Handling
description: Handle validation, authentication, and transient platform errors gracefully.
---

# Error Handling

Design your integration to handle validation, authentication, and transient platform errors gracefully.

## Error categories

- `400 Bad Request` for malformed or invalid input
- `401 Unauthorized` for missing or invalid credentials
- `409 Conflict` for idempotency mismatches or request collisions
- `429 Too Many Requests` for rate limiting
- `500` and `502` for transient platform failures

## Integration guidance

1. retry only safe, transient failures
2. never retry validation errors without changing the request
3. store the `requestId` from every failed response

## Developer experience note

Well-structured errors make support faster and reduce integration time for partner teams.