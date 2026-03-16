---
sidebar_position: 3
---

# Authentication

Authentication documentation should remove ambiguity, not create it. This example models the kind of concise implementation guidance a developer portal needs.

## Auth model

- **Scheme:** Bearer token
- **Transport:** HTTPS only
- **Header:** `Authorization: Bearer YOUR_API_TOKEN`

## Example request

```http
GET /api/people/1 HTTP/1.1
Host: swapi.dev
Authorization: Bearer YOUR_API_TOKEN
Accept: application/json
```

## Common errors

| Status | Meaning | Recommended guidance |
| --- | --- | --- |
| `401` | Missing or invalid token | Ask the user to verify the header format and token scope. |
| `403` | Token valid but insufficient | Document required permissions or environment limits. |
| `429` | Rate limit reached | Explain retry timing and backoff behavior. |

Authentication pages work best when they pair security rules with copy-paste-ready examples.