---
title: Refunds
sidebar_position: 2
description: Reference documentation for issuing full or partial refunds on payments in the Acme Payments API.
---

# Refunds

The Refunds API allows you to issue a full or partial refund on a previously succeeded payment. Refunds are applied to the same payment method used in the original transaction.

**Base URL:** `https://api.acmepayments.com/v1`

---

## Issue a Refund

Issues a refund against an existing payment.

**Endpoint**

```
POST /v1/payments/{id}/refunds
```

**Path Parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Required | The unique identifier of the payment to refund. |

**Request Headers**

| Header | Value |
| --- | --- |
| `Authorization` | `Bearer <YOUR_API_KEY>` |
| `Content-Type` | `application/json` |

**Request Body Parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `amount` | integer | Optional | Amount to refund, in the smallest currency unit. Defaults to the full payment amount if omitted. |
| `reason` | string | Optional | Reason for the refund. Accepted values: `duplicate`, `fraudulent`, `customer_request`. |
| `metadata` | object | Optional | Set of key-value pairs for storing additional structured information about the refund. |

**Request Example**

```bash
curl -X POST https://api.acmepayments.com/v1/payments/pay_XYZ789/refunds \
  -H "Authorization: Bearer sk_test_51ABC123XYZ" \
  -H "Content-Type: application/json" \
  -d '{
    "amount": 2500,
    "reason": "customer_request"
  }'
```

**Response Schema**

| Field | Type | Description |
| --- | --- | --- |
| `id` | string | Unique identifier for the refund. Prefixed with `rf_`. |
| `payment_id` | string | ID of the payment that was refunded. |
| `amount` | integer | Refunded amount in the smallest currency unit. |
| `currency` | string | Three-letter ISO 4217 currency code of the original payment. |
| `reason` | string | Reason provided for the refund, if any. |
| `status` | string | Current status of the refund. One of `pending` or `succeeded`. |
| `metadata` | object | Additional key-value data attached to the refund. |
| `created_at` | string | ISO 8601 timestamp of when the refund was created. |

**Response Example**

```json
{
  "id": "rf_DEF456",
  "payment_id": "pay_XYZ789",
  "amount": 2500,
  "currency": "INR",
  "reason": "customer_request",
  "status": "succeeded",
  "metadata": {},
  "created_at": "2026-04-10T06:00:00Z"
}
```

**Response Codes**

| HTTP Status | Description |
| --- | --- |
| `201 Created` | Refund was successfully issued. |
| `400 Bad Request` | The request body contains invalid values or the refund amount exceeds the original payment amount. |
| `401 Unauthorized` | The API key is missing or invalid. |
| `404 Not Found` | No payment exists with the specified ID. |
| `422 Unprocessable Entity` | The payment is not in a refundable state (e.g., already fully refunded or failed). |

---

> **Note:** Refunds are typically processed within 5–7 business days, depending on the customer's bank or card issuer. The refund `status` transitions from `pending` to `succeeded` when the funds have been returned.

## Next:

For Webhooks API, see [Webhooks API](/acme-payments/api/webhooks).
For Payments API, see [Payments API](/acme-payments/api/payments).
For Customers API, see [Customers API](/acme-payments/api/customers).


