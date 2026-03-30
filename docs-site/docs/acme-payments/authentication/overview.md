---
title: Authentication Overview
description: Authentication pattern and key-handling guidance for Acme Payments integrations.
---

# Authentication Overview

Acme Payments uses API keys for server-to-server requests.

## How it works

Acme Payments authenticates API requests using API keys. If you do not include your key when making an API request, or use one that is incorrect or disabled, Acme Payments returns a `401 Unauthorized` error.

> [!IMPORTANT]  
> Your API keys carry many privileges. Keep them secure! Do not share your secret API keys in publicly accessible areas such as GitHub, client-side code, or mobile applications.

All API requests must be made over HTTPS. Calls made over plain HTTP will fail. API requests without authentication will also fail.

## Authenticating Requests

Authenticate your API requests by providing your API key in the `Authorization` header as a Bearer token.

### Examples

Here is how to authenticate in different environments:

**cURL**
```bash
curl https://api.acmepayments.com/v1/payments \
  -H "Authorization: Bearer sk_test_51ABC123XYZ..."
```

**Node.js**
```javascript
const response = await fetch('https://api.acmepayments.com/v1/payments', {
  headers: {
    'Authorization': 'Bearer sk_test_51ABC123XYZ...',
    'Content-Type': 'application/json'
  }
});
```

**Python**
```python
import requests

headers = {
    'Authorization': 'Bearer sk_test_51ABC123XYZ...',
    'Content-Type': 'application/json'
}
response = requests.get('https://api.acmepayments.com/v1/payments', headers=headers)
```

## Recommended patterns

1. **Keep secrets out of frontend code**: Never hardcode API keys in UI repositories.
2. **Proxy client requests**: Route requests through your backend service so your API key remains hidden from the browser.
3. **Use environment variables**: Inject your API key via `.env` files or a secret manager.

## Authentication errors

If credentials are missing or invalid, the API returns a `401 Unauthorized` response.

| HTTP Status | Error Type | Cause |
| :--- | :--- | :--- |
| `401` | `unauthorized` | The `Authorization` header was not provided. |
| `401` | `invalid_api_key` | The API key provided is invalid, revoked, or belongs to a different environment. |

## Related docs

- [Get an API Key](../quickstart/get-api-key.md)
- [Idempotency](../concepts/idempotency.md)
- [Error Handling](../concepts/error-handling.md)