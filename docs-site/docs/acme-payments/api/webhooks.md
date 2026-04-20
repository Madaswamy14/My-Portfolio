---
title: Webhooks
sidebar_position: 3
description: This guide explains how to receive real-time updates about payments.
---

# Webhooks

You can configure webhooks to receive real-time notifications about payment lifecycle changes.

**Endpoints**

```http
POST https://api.acmepayments.com/v1/webhook
GET https://api.acmepayments.com/v1/webhook
DELETE https://api.acmepayments.com/v1/webhook
```

---

## The Webhook Endpoint object

```json
{
  "id": "wh_123",
  "url": "https://example.com/webhook",
  "events": [
    "payment.succeeded",
    "payment.failed",
    "refund.processed"
  ]
}
```

**Webhook Endpoint Object**

| Field | Type | Description |
|-------|------|-------------|
| id | string | The ID of the webhook endpoint |
| url | string | The URL of the webhook endpoint |
| events | array | The events that the webhook endpoint will receive |

---

## Create a webhook
Creates a webhook endpoint.

**Endpoint**
```http
POST https://api.acmepayments.com/v1/webhook
```

**Request**

```json
{
  "url": "https://example.com/webhook",
  "events": [
    "payment.succeeded",
    "payment.failed",
    "refund.processed"
  ]
}
```

**Response**

```json
{
  "id": "wh_123",
  "url": "https://example.com/webhook",
  "events": [
    "payment.succeeded",
    "payment.failed",
    "refund.processed"
  ]
}
```
## Update a webhook
Updates a webhook endpoint.

**Endpoint**
```http
PUT https://api.acmepayments.com/v1/webhook/{id}
```

**Request**

```json
{
  "url": "https://example.com/webhook",
  "events": [
    "payment.succeeded",
    "payment.failed",
    "refund.processed"
  ]
}
```

**Response**

```json
{
  "id": "wh_123",
  "url": "https://example.com/webhook",
  "events": [
    "payment.succeeded",
    "payment.failed",
    "refund.processed"
  ]
}
```

## Retrieve a webhook
Returns a webhook endpoint.

**Endpoint**
```http
GET https://api.acmepayments.com/v1/webhook/{id}
```

**Request**

```json
{
  "id": "wh_123"
}
```

**Response**

```json
{
  "id": "wh_123",
  "url": "https://example.com/webhook",
  "events": [
    "payment.succeeded",
    "payment.failed",
    "refund.processed"
  ]
}
```

## List all webhook endpoints
Returns a list of your webhook endpoints.

**Endpoint**
```http
GET https://api.acmepayments.com/v1/webhook
```

**Request**

```json
{
  "id": "wh_123"
}
```

**Response**

```json
{
  "id": "wh_123",
  "url": "https://example.com/webhook",
  "events": [
    "payment.succeeded",
    "payment.failed",
    "refund.processed"
  ]
}
```

## Delete a webhook
Deletes a webhook endpoint.

**Endpoint**
```http
DELETE https://api.acmepayments.com/v1/webhook/{id}
```

**Request**

```json
{
  "id": "wh_123"
}
```

**Response**

```json
{
  "id": "wh_123",
  "url": "https://example.com/webhook",
  "events": [
    "payment.succeeded",
    "payment.failed",
    "refund.processed"
  ]
}
```

## Next:

For Payments API, see [Payments API](/acme-payments/api/payments).
For Refunds API, see [Refunds API](/acme-payments/api/refunds).
For Customers API, see [Customers API](/acme-payments/api/customers).
