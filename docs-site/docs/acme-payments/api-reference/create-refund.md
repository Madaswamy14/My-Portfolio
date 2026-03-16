---
title: Create refund
description: Refund a previously created payment.
---

# Create refund

`POST /refunds`

Create a refund for a previously created payment.

## Request body

| Field | Type | Required | Example |
| --- | --- | --- | --- |
| `paymentId` | string | Yes | `pay_98765` |
| `amount` | integer | No | `500` |

## Example request

```bash
curl https://api.acmepayments.com/v1/refunds \
  -H "Authorization: Bearer sk_test_51ABC123XYZ" \
  -H "Content-Type: application/json" \
  -d '{
    "paymentId": "pay_98765",
    "amount": 500
  }'
```

## Success response

```json
{
  "id": "ref_45678",
  "paymentId": "pay_98765",
  "amount": 500,
  "status": "processed"
}
```

## Common errors

- `400 Bad Request` for invalid request bodies
- `401 Unauthorized` for missing or invalid credentials
- `404 Not Found` if the payment does not exist

## Related docs

- [Retrieve payment](./retrieve-payment.md)
- [Handling Webhooks](../webhooks/handling-webhooks.md)