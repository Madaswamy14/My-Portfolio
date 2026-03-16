---
title: Authentication Overview
description: Authentication pattern and key-handling guidance for Acme Payments integrations.
---

# Authentication Overview

Acme Payments uses API keys for server-to-server requests.

## How it works

- send your key in the `Authorization` header as `Bearer <token>`
- use sandbox keys in test environments only
- rotate keys regularly and store them in a secret manager

## Recommended pattern

1. keep secrets out of frontend code
2. proxy client requests through your backend
3. restrict production keys to only the services that need them

## Authentication errors

If credentials are missing or invalid, the API returns `401 Unauthorized` with an error code and request identifier.

## Related docs

- [Get an API Key](../quickstart/get-api-key.md)
- [Idempotency](../concepts/idempotency.md)
- [Error Handling](../concepts/error-handling.md)