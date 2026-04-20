---
title: Payments API
sidebar_position: 2
description: Reference documentation for creating and retrieving payments in the Acme Payments API.
---

# Payments API

The Payments API allows you to initiate and retrieve payment transactions. Payments are associated with a customer and processed using an attached payment method.

**Base URL:** `https://api.acmepayments.com/v1`

---

## Create a Payment

Initiates a new payment for a specified customer and amount.

**Endpoint**

```
POST /v1/payments
```

**Request Headers**

| Header | Value |
| --- | --- |
| `Authorization` | `Bearer <YOUR_API_KEY>` |
| `Content-Type` | `application/json` |
| `Idempotency-Key` | Optional. A unique string (UUID recommended) to safely retry requests without creating duplicate payments. |

**Request Body Parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `customer_id` | string | Required | The ID of an existing customer. |
| `amount` | integer | Required | Amount to charge, in the smallest currency unit (e.g., paise for INR, cents for USD). |
| `currency` | string | Required | Three-letter ISO 4217 currency code in uppercase (e.g., `INR`, `USD`). |
| `payment_method` | string | Required | ID of the payment method to charge (e.g., `pm_card_visa`). |
| `description` | string | Optional | An internal description of the payment. Not visible to the customer. |
| `metadata` | object | Optional | Set of key-value pairs for storing additional structured information. |

**Request Example**

```bash
curl -X POST https://api.acmepayments.com/v1/payments \
  -H "Authorization: Bearer sk_test_51ABC123XYZ" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
  -d '{
    "customer_id": "cus_ABC123",
    "amount": 5000,
    "currency": "INR",
    "payment_method": "pm_card_visa",
    "description": "Order #1042"
  }'
```

**Response Schema**

| Field | Type | Description |
| --- | --- | --- |
| `id` | string | Unique identifier for the payment. Prefixed with `pay_`. |
| `customer_id` | string | ID of the customer associated with this payment. |
| `amount` | integer | Payment amount in the smallest currency unit. |
| `currency` | string | Three-letter ISO 4217 currency code. |
| `status` | string | Current status of the payment. One of `pending`, `succeeded`, or `failed`. |
| `payment_method` | string | ID of the payment method used. |
| `description` | string | Internal description of the payment, if provided. |
| `metadata` | object | Additional key-value data attached to the payment. |
| `created_at` | string | ISO 8601 timestamp of when the payment was created. |

**Response Example**

```json
{
  "id": "pay_XYZ789",
  "customer_id": "cus_ABC123",
  "amount": 5000,
  "currency": "INR",
  "status": "succeeded",
  "payment_method": "pm_card_visa",
  "description": "Order #1042",
  "metadata": {},
  "created_at": "2026-04-10T05:30:00Z"
}
```

**Response Codes**

| HTTP Status | Description |
| --- | --- |
| `201 Created` | Payment was successfully created. |
| `400 Bad Request` | The request body is missing required fields or contains invalid values. |
| `401 Unauthorized` | The API key is missing or invalid. |
| `402 Payment Required` | The payment failed due to insufficient funds or a declined card. |
| `404 Not Found` | The specified `customer_id` or `payment_method` does not exist. |
| `429 Too Many Requests` | The request was rate-limited. See [Rate Limits](../reference/rate-limits.md). |

---

## Retrieve a Payment

Returns the details of an existing payment.

**Endpoint**

```
GET /v1/payments/{id}
```

**Path Parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Required | The unique identifier of the payment to retrieve. |

**Request Example**

```bash
curl -X GET https://api.acmepayments.com/v1/payments/pay_XYZ789 \
  -H "Authorization: Bearer sk_test_51ABC123XYZ"
```

**Response Schema**

| Field | Type | Description |
| --- | --- | --- |
| `id` | string | Unique identifier for the payment. |
| `customer_id` | string | ID of the customer associated with this payment. |
| `amount` | integer | Payment amount in the smallest currency unit. |
| `currency` | string | Three-letter ISO 4217 currency code. |
| `status` | string | Current status of the payment. One of `pending`, `succeeded`, or `failed`. |
| `payment_method` | string | ID of the payment method used. |
| `description` | string | Internal description of the payment, if provided. |
| `metadata` | object | Additional key-value data attached to the payment. |
| `created_at` | string | ISO 8601 timestamp of when the payment was created. |

**Response Example**

```json
{
  "id": "pay_XYZ789",
  "customer_id": "cus_ABC123",
  "amount": 5000,
  "currency": "INR",
  "status": "succeeded",
  "payment_method": "pm_card_visa",
  "description": "Order #1042",
  "metadata": {},
  "created_at": "2026-04-10T05:30:00Z"
}
```

**Response Codes**

| HTTP Status | Description |
| --- | --- |
| `200 OK` | Payment details returned successfully. |
| `401 Unauthorized` | The API key is missing or invalid. |
| `404 Not Found` | No payment exists with the specified ID. |

---

## Next:

For Refunds API, see [Refunds API](/acme-payments/api/refunds).
For Webhooks API, see [Webhooks API](/acme-payments/api/webhooks).
For Customers API, see [Customers API](/acme-payments/api/customers).