---
title: Create customer
description: Create a customer record before charging them.
---

# Create customer

`POST /customers`

Create a customer record before you create a payment.

## Request body

| Field | Type | Required | Example |
| --- | --- | --- | --- |
| `email` | string | Yes | `customer@example.com` |
| `name` | string | No | `Jane Doe` |

## Example request

```bash
curl https://api.acmepayments.com/v1/customers \
  -H "Authorization: Bearer sk_test_51ABC123XYZ" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "customer@example.com",
    "name": "Jane Doe"
  }'
```

## Success response

```json
{
  "id": "cus_12345",
  "email": "customer@example.com",
  "name": "Jane Doe"
}
```

## Common errors

- `400 Bad Request` if the request body is malformed
- `401 Unauthorized` if the API key is missing or invalid

## Next step

Use the returned customer ID with [Create payment](./create-payment.md).