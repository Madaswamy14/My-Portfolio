---
title: Retrieve payment
description: Fetch a single payment by ID.
---

# Retrieve payment

`GET /payments/{paymentId}`

Fetch a single payment object by ID.

## Path parameter

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `paymentId` | string | Yes | Payment identifier, such as `pay_98765` |

## Example request

```bash
curl https://api.acmepayments.com/v1/payments/pay_98765 \
  -H "Authorization: Bearer sk_test_51ABC123XYZ"
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

- `401 Unauthorized` if credentials are missing or invalid
- `404 Not Found` if the payment ID does not exist

## Related docs

- [List payments](./list-payments.md)
- [Create refund](./create-refund.md)