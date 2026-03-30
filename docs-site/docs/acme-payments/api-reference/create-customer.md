---
title: Create a customer
description: Create a customer record before charging them. Use the returned id in all subsequent payment requests for this customer. Always include an Idempotency-Key header on this request to safely retry on network failures without creating duplicate customers.
---

# Create a customer

Creates a new customer object. Use the returned `id` in all subsequent payment requests for this customer. Always include an `Idempotency-Key` header on this request to safely retry on network failures without creating duplicate customers.

**Endpoint:** `POST /customers`

## Parameters

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `email` | string | Yes | Customer email address. Must be a valid format and unique per account. |
| `name` | string | No | Customer's full name. Used for receipts and dashboard display. |
| `phone` | string | No | E.164-formatted phone number for SMS receipts. |
| `metadata` | object | No | Arbitrary key-value pairs for your internal reference. Not returned in list views. |
| `Idempotency-Key` | string | Recommended | Unique string per customer creation attempt. Safe to retry with the same key. |

## Sample request

```bash
curl https://api.acmepayments.com/v1/customers \
  -H "Authorization: Bearer sk_test_51ABC123XYZ" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: customer-jane-doe" \
  -d '{
    "email": "jane.doe@example.com",
    "name": "Jane Doe",
    "phone": "+14155552671",
    "metadata": { "plan": "pro", "region": "us-east" }
  }'
```

## Response body

Returns the created customer object.

| Field | Type | Description | Example |
| --- | --- | --- | --- |
| `id` | string | Unique customer identifier. Pass this as `customerId` when creating payments. | `cus_12345` |
| `email` | string | The customer's email address. | `jane.doe@example.com` |
| `name` | string | The customer's full name. | `Jane Doe` |
| `phone` | string | E.164-formatted phone number, if provided. | `+14155552671` |
| `metadata` | object | Key-value pairs attached at creation. | `{"plan": "pro"}` |
| `createdAt` | string (ISO 8601) | UTC timestamp when the customer was created. | `2026-03-09T12:00:00Z` |

## Sample response

```json
{
  "id": "cus_12345",
  "email": "jane.doe@example.com",
  "name": "Jane Doe",
  "phone": "+14155552671",
  "metadata": { "plan": "pro", "region": "us-east" },
  "createdAt": "2026-03-09T12:00:00Z"
}
```

## Error codes

| HTTP status | Error code | Description |
| --- | --- | --- |
| `400 Bad Request` | `invalid_request` | Request body is missing or malformed JSON. |
| `401 Unauthorized` | `invalid_api_key` | API key is missing, expired, or revoked. |
| `409 Conflict` | `customer_exists` | A customer with this email already exists in the account. |
| `422 Unprocessable Entity` | `validation_error` | A field value did not pass validation, for example an invalid email format or phone number. |

## Related docs

- [Idempotency](../concepts/idempotency.md)
- [Create refund](./create-refund.md)
- [Make Your First API Call](../quickstart/first-api-call.md)