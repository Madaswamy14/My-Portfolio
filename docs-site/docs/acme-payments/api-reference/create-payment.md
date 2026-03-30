---
title: Create a payment
description: Create a payment for an existing customer.
---

# Create a payment

`POST /payments`

Creates a new payment for an existing customer. Always include an `Idempotency-Key` header on this request to safely retry on network failures without double-charging.

## Request headers

| Header | Required | Description | Example |
| --- | --- | --- | --- |
| `Authorization` | Yes | Bearer token using your API key. | `Bearer sk_test_51ABC123XYZ` |
| `Content-Type` | Yes | Must be `application/json`. | `application/json` |
| `Idempotency-Key` | Recommended | Unique string per payment attempt. Safe to retry with the same key. | `order-8821-attempt-1` |

## Request body

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `amount` | integer | Yes | Payment amount in the smallest currency unit (cents for USD). Minimum: 50. | `1000` |
| `currency` | string | Yes | Three-letter ISO 4217 currency code, uppercase. | `USD` |
| `customerId` | string | Yes | ID of an existing customer. Create one first using [Create customer](./create-customer.md). | `cus_12345` |
| `description` | string | No | Human-readable description shown on the customer's receipt. | `Order #8821` |
| `metadata` | object | No | Arbitrary key-value pairs for your internal reference. | `{"orderId": "8821"}` |

## Example request

```bash
curl https://api.acmepayments.com/v1/payments \
  -H "Authorization: Bearer sk_test_51ABC123XYZ" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: order-8821-attempt-1" \
  -d '{
    "amount": 1000,
    "currency": "USD",
    "customerId": "cus_12345",
    "description": "Order #8821",
    "metadata": { "orderId": "8821" }
  }'
```

## Response

### 201 Created

Returns the created payment object.

| Field | Type | Description | Example |
| --- | --- | --- | --- |
| `id` | string | Unique payment identifier. Use this for refunds and lookups. | `pay_98765` |
| `amount` | integer | Payment amount in cents. | `1000` |
| `currency` | string | Three-letter ISO 4217 currency code. | `USD` |
| `status` | string | Payment status. One of `pending`, `succeeded`, `failed`. | `succeeded` |
| `customerId` | string | The customer this payment is associated with. | `cus_12345` |
| `description` | string | Receipt description, if provided. | `Order #8821` |
| `metadata` | object | Key-value pairs attached at creation. | `{"orderId": "8821"}` |
| `createdAt` | string (ISO 8601) | UTC timestamp when the payment was created. | `2026-03-09T12:00:00Z` |

```json
{
  "id": "pay_98765",
  "amount": 1000,
  "currency": "USD",
  "status": "succeeded",
  "customerId": "cus_12345",
  "description": "Order #8821",
  "metadata": { "orderId": "8821" },
  "createdAt": "2026-03-09T12:00:00Z"
}
```

## Error responses

| HTTP status | Error code | Cause |
| --- | --- | --- |
| `400 Bad Request` | `invalid_request` | Missing required field or malformed JSON. |
| `401 Unauthorized` | `invalid_api_key` | API key is missing, expired, or revoked. |
| `402 Payment Required` | `payment_failed` | Card was declined or funds were insufficient. |
| `404 Not Found` | `customer_not_found` | The `customerId` does not exist in this account. |
| `409 Conflict` | `idempotency_mismatch` | An `Idempotency-Key` was reused with a different request body. |
| `422 Unprocessable Entity` | `validation_error` | Amount is below the minimum, or the currency code is not supported. |

## Related docs

- [Idempotency](../concepts/idempotency.md)
- [Create refund](./create-refund.md)
- [Make Your First API Call](../quickstart/first-api-call.md)