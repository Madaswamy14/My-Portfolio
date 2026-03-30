---
title: Create refund
description: Refund a previously created payment.
---

# Create refund

`POST /refunds`

Create a refund for a previously created payment.

## Request body

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `paymentId` | string | Yes | The identifier of the charge to refund. | `pay_98765` |
| `amount` | integer | No | A positive integer in cents representing how much to refund. If not provided, the entire remaining amount is refunded. | `500` |
| `reason` | string | No | String indicating the reason for the refund. One of `duplicate`, `fraudulent`, or `requested_by_customer`. | `requested_by_customer` |
| `metadata` | object | No | Arbitrary key-value pairs for your internal reference. | `{"ticket_id": "12345"}` |

## Example request

```bash
curl https://api.acmepayments.com/v1/refunds \
  -H "Authorization: Bearer sk_test_51ABC123XYZ" \
  -H "Content-Type: application/json" \
  -d '{
    "paymentId": "pay_98765",
    "amount": 500,
    "reason": "requested_by_customer",
    "metadata": { "ticket_id": "12345" }
  }'
```

## Response

### 201 Created

Returns the created refund object.

| Field | Type | Description | Example |
| --- | --- | --- | --- |
| `id` | string | Unique refund identifier. | `ref_45678` |
| `paymentId` | string | ID of the payment that was refunded. | `pay_98765` |
| `amount` | integer | Refunded amount in cents. | `500` |
| `status` | string | Refund status. One of `pending`, `processed`, `failed`. | `processed` |
| `reason` | string | Reason for the refund, if provided. | `requested_by_customer` |
| `metadata` | object | Key-value pairs attached during creation. | `{"ticket_id": "12345"}` |
| `createdAt` | string (ISO 8601) | UTC timestamp when the refund was created. | `2026-03-09T14:30:00Z` |

```json
{
  "id": "ref_45678",
  "paymentId": "pay_98765",
  "amount": 500,
  "status": "processed",
  "reason": "requested_by_customer",
  "metadata": { "ticket_id": "12345" },
  "createdAt": "2026-03-09T14:30:00Z"
}
```

## Error responses

| HTTP status | Error code | Cause |
| --- | --- | --- |
| `400 Bad Request` | `invalid_request` | Missing required field or malformed JSON. Amount exceeds the remaining charge balance. |
| `401 Unauthorized` | `invalid_api_key` | API key is missing, expired, or revoked. |
| `404 Not Found` | `payment_not_found` | The `paymentId` does not exist in this account. |

## Related docs

- [Retrieve payment](./retrieve-payment.md)
- [Handling Webhooks](../webhooks/handling-webhooks.md)