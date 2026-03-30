---
title: Retrieve payment
description: Fetch a single payment by ID.
---

# Retrieve payment

`GET /payments/{paymentId}`

Fetch a single payment object by ID.

## Path parameter

| Parameter | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `paymentId` | string | Yes | Unique payment identifier. | `pay_98765` |

## Example request

```bash
curl https://api.acmepayments.com/v1/payments/pay_98765 \
  -H "Authorization: Bearer sk_test_51ABC123XYZ"
```

## Response

### 200 OK

Returns the payment object if a valid identifier was provided.

| Field | Type | Description | Example |
| --- | --- | --- | --- |
| `id` | string | Unique payment identifier. Use this for refunds and lookups. | `pay_98765` |
| `amount` | integer | Payment amount in cents. | `1000` |
| `currency` | string | Three-letter ISO 4217 currency code. | `USD` |
| `status` | string | Payment status. One of `pending`, `succeeded`, `failed`. | `succeeded` |
| `createdAt` | string (ISO 8601) | UTC timestamp when the payment was created. | `2026-03-09T12:00:00Z` |

```json
{
  "id": "pay_98765",
  "amount": 1000,
  "currency": "USD",
  "status": "succeeded",
  "createdAt": "2026-03-09T12:00:00Z"
}
```

## Error responses

| HTTP status | Error code | Cause |
| --- | --- | --- |
| `401 Unauthorized` | `invalid_api_key` | API key is missing, expired, or revoked. |
| `404 Not Found` | `payment_not_found` | The `paymentId` does not exist in this account. |

## Related docs

- [List payments](./list-payments.md)
- [Create refund](./create-refund.md)