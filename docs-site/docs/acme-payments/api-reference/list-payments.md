---
title: List payments
description: Return a list of payment objects.
---

# List payments

`GET /payments`

Return a list of payment objects.

## Query parameters

| Parameter | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `limit` | integer | No | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. | `20` |
| `startingAfter` | string | No | A cursor for use in pagination. `startingAfter` is an object ID that defines your place in the list. | `pay_98765` |

## Example request

```bash
curl -G https://api.acmepayments.com/v1/payments \
  -H "Authorization: Bearer sk_test_51ABC123XYZ" \
  -d limit=20 \
  -d startingAfter=pay_88888
```

## Response

### 200 OK

Returns a dictionary with a `data` property that contains an array of up to `limit` payments. Each entry in the array is a separate payment object.

| Field | Type | Description |
| --- | --- | --- |
| `data` | array | An array of payment objects. |
| `hasMore` | boolean | `true` if more payments are available beyond this page. |

#### Payment object

| Field | Type | Description | Example |
| --- | --- | --- | --- |
| `id` | string | Unique payment identifier. Use this for refunds and lookups. | `pay_98765` |
| `amount` | integer | Payment amount in cents. | `1000` |
| `currency` | string | Three-letter ISO 4217 currency code. | `USD` |
| `status` | string | Payment status. One of `pending`, `succeeded`, `failed`. | `succeeded` |
| `createdAt` | string (ISO 8601) | UTC timestamp when the payment was created. | `2026-03-09T12:00:00Z` |

```json
{
  "data": [
    {
      "id": "pay_98765",
      "amount": 1000,
      "currency": "USD",
      "status": "succeeded",
      "createdAt": "2026-03-09T12:00:00Z"
    }
  ],
  "hasMore": false
}
```

## Error responses

| HTTP status | Error code | Cause |
| --- | --- | --- |
| `400 Bad Request` | `invalid_request` | Invalid pagination parameters. |
| `401 Unauthorized` | `invalid_api_key` | API key is missing, expired, or revoked. |

## Use this endpoint when

- you need to review recent payment activity
- support or operations teams need to inspect payment state quickly
- you are verifying the output of a new integration

## Related docs

- [Retrieve payment](./retrieve-payment.md)
- [Monitoring and Observability Guide](../developer-journey/monitoring-observability.md)