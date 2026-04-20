---
title: Introduction
sidebar_position: 1
description: This guide introduces the Acme Payments API, its key features, and how to get started.
---

# Introduction

Acme Payments API is a developer-first platform designed to help you accept and manage payments globally with speed, reliability, and simplicity.

If you are building an e-commerce platform, SaaS product, or mobile app, Acme Payments provides the tools you need to handle payments end-to-end.

**Key Features**

- **Global Payments**: Support for multiple currencies and payment methods including cards and UPI.
- **Security**: API key authentication, No sensitive data stored on your servers, Webhook signature verification
- **Idempotent Requests**: Prevent duplicate payments using idempotency keys.
- **Real-Time Events**: Stay updated with webhook notifications for all payment events.

## Base URL

https://api.acmepayments.com/v1


## Authentication

Acme Payments API uses Bearer Token authentication. All API requests must include your secret API key:

**API Key Types**

| Key Type | Usage |
|---------|------|
| sk_test | Testing environment |
| sk_live | Production environment |

> **Note:** Never expose your secret key in frontend or client-side code.

**Authenticated Requests**

```
curl https://api.acmepayments.com/v1/customers \
  -u sk_test_51Kz83eLwQ987....3210987
```

```
curl https://api.acmepayments.com/v1/customers \
  -u sk_live_51Kz83eLwQ987....3210987
```

## Error Handling

Acme Payments API returns standard HTTP status codes and JSON error responses.

**HTTP Status Code Summary**

| Status Code | Meaning |
|------------|--------|
| 200 | OK |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 404 | Not Found |
| 500 | Internal Server Error |

**Error Response Format**

```json
{
  "error": {
    "code": "invalid_request_error",
    "message": "Invalid request parameters",
    "param": "amount"
  }
}
```

**Error Types**

| Error Type | Meaning |
|------------|--------|
| invalid_request_error | Invalid request parameters |
| invalid_api_key | Invalid API key |
| invalid_payment_method | Invalid payment method |
| invalid_payment | Invalid payment |
| invalid_customer | Invalid customer |

## Handling errors
Our API follows RESTful error handling conventions. When an error occurs, the API returns an HTTP status code and a JSON error response.

## Expanding Responses
Many API responses include nested objects. You can expand these objects by using the `expand` parameter.

**Request**

```
curl https://api.acmepayments.com/v1/customers?expand=payment_methods
```

**Response**

```json
{
  "id": "cus_123",
  "name": "John Doe",
  "email": "[EMAIL_ADDRESS]",
  "payment_methods": [
    {
      "id": "pm_123",
      "type": "card",
      "card": {
        "brand": "visa",
        "last4": "4242"
      }
    }
  ]
}
```

## Idempotency

Idempotency allows you to safely retry requests without causing duplicate charges. Use the `Idempotency-Key` header to ensure requests are processed only once.

**Request**

```
curl https://api.acmepayments.com/v1/customers \
  -H "Idempotency-Key: 8a7b6c5d4e3f2a1b0c9d8e7f6a5b4c3d"
```

**Response**

```json
{
  "id": "cus_123",
  "name": "John Doe",
  "email": "[EMAIL_ADDRESS]"
}
```


## Metadata

Metadata allows you to store custom information about objects. Metadata is stored as key-value pairs and can be used to store any information that you want to associate with an object.

**Request**

```
curl https://api.acmepayments.com/v1/customers \
  -H "Idempotency-Key: 8a7b6c5d4e3f2a1b0c9d8e7f6a5b4c3d"
```

**Response**

```json
{
  "id": "cus_123",
  "name": "John Doe",
  "email": "[EMAIL_ADDRESS]"
}
```

## Pagination
All list endpoints support pagination. Use the `limit` and `offset` parameters to control the number of items returned.

**Request**

```
curl https://api.acmepayments.com/v1/customers?limit=10&offset=0
```

**Response**

```json
{
  "id": "cus_123",
  "name": "John Doe",
  "email": "[EMAIL_ADDRESS]"
}
```
## Search
Some list endpoints support search. Use the `search` parameter to search for items.

**Request**

```
curl https://api.acmepayments.com/v1/customers?search=John
```

**Response**

```json
{
  "id": "cus_123",
  "name": "John Doe",
  "email": "[EMAIL_ADDRESS]"
}
```

## Versioning
Each API version is backward compatible with the previous versions. 


## Payment Flow

At a high level, the payment flow looks like this:

1. Create a customer.
2. Attach a payment method.
3. Create and confirm a payment.
4. Listen to webhooks for status updates.

This separation ensures flexibility, scalability, and clean system design.

## Next Steps

Start integrating in minutes:

- Go to [**Quickstart**](/acme-payments/getting-started/quickstart.md) to create your first payment
- Explore [**Concepts**](/acme-payments/concepts/concepts.md) to understand core objects
- Use [**Guides**](/acme-payments/guides/guides.md) for real-world workflows


> **Note:** If you're new to payments APIs, begin with the [**Accept Payments guide**](/acme-payments/guides/accept-payments.md) — it walks you through a complete working flow.

```

