---
title: Create a payment
description: Create a payment for an existing customer.
---

# Create a payment

`POST /payments`

Create a payment for an existing customer.

## Request body

| Field | Type | Required | Example | Notes |
| --- | --- | --- | --- | --- |
| `amount` | integer | Yes | `1000` | Payment amount in cents |
| `currency` | string | Yes | `USD` | Three-letter currency code |
| `customerId` | string | Yes | `cus_12345` | Existing customer identifier |

## Example request

```bash
curl https://api.acmepayments.com/v1/payments \
  -H "Authorization: Bearer sk_test_51ABC123XYZ" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: demo-payment-001" \
  -d '{
    "amount": 1000,
    "currency": "USD",
    "customerId": "cus_12345"
  }'
```

## Success response

```json
{
  "id": "pay_98765",
  "amount": 1000,
  "currency": "USD",
  "status": "succeeded",
  "createdAt": "2026-03-09T12:00:00Z"
}
```

## Common errors

- `400 Bad Request` for invalid input
- `401 Unauthorized` for missing or invalid credentials
- `409 Conflict` for idempotency mismatches

## Related docs

- [Make Your First API Call](../quickstart/first-api-call.md)
- [Idempotency](../concepts/idempotency.md)
- [Create refund](./create-refund.md)