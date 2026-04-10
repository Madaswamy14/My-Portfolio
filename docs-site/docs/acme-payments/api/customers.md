---
title: Customers API
sidebar_position: 1
description: Reference documentation for creating, retrieving, and updating customer records in the Acme Payments API.
---

# Customers API

The Customers API allows you to create and manage customer records. A customer object stores contact information and serves as a reference point for payment methods and transaction history.

**Base URL:** `https://api.acmepayments.com/v1`

---

## Create a Customer

Creates a new customer record.

**Endpoint**

```
POST /v1/customers
```

**Request Headers**

| Header | Value |
| --- | --- |
| `Authorization` | `Bearer <YOUR_API_KEY>` |
| `Content-Type` | `application/json` |

**Request Body Parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Required | Full name of the customer. |
| `email` | string | Required | Email address of the customer. Must be a valid email format. |
| `phone` | string | Optional | Phone number of the customer, including country code. |
| `metadata` | object | Optional | Set of key-value pairs for storing additional structured information. |

**Request Example**

```bash
curl -X POST https://api.acmepayments.com/v1/customers \
  -H "Authorization: Bearer sk_test_51ABC123XYZ" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Jane Smith",
    "email": "jane.smith@example.com",
    "phone": "+919876543210"
  }'
```

**Response Schema**

| Field | Type | Description |
| --- | --- | --- |
| `id` | string | Unique identifier for the customer. Prefixed with `cus_`. |
| `name` | string | Full name of the customer. |
| `email` | string | Email address of the customer. |
| `phone` | string | Phone number of the customer. |
| `metadata` | object | Additional key-value data attached to the customer. |
| `created_at` | string | ISO 8601 timestamp of when the customer was created. |

**Response Example**

```json
{
  "id": "cus_ABC123",
  "name": "Jane Smith",
  "email": "jane.smith@example.com",
  "phone": "+919876543210",
  "metadata": {},
  "created_at": "2026-04-10T05:00:00Z"
}
```

**Response Codes**

| HTTP Status | Description |
| --- | --- |
| `201 Created` | Customer was successfully created. |
| `400 Bad Request` | The request body is missing required fields or contains invalid values. |
| `401 Unauthorized` | The API key is missing or invalid. |
| `409 Conflict` | A customer with the provided email already exists. |

---

## Retrieve a Customer

Returns the details of an existing customer.

**Endpoint**

```
GET /v1/customers/{id}
```

**Path Parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Required | The unique identifier of the customer. |

**Request Example**

```bash
curl -X GET https://api.acmepayments.com/v1/customers/cus_ABC123 \
  -H "Authorization: Bearer sk_test_51ABC123XYZ"
```

**Response Schema**

| Field | Type | Description |
| --- | --- | --- |
| `id` | string | Unique identifier for the customer. |
| `name` | string | Full name of the customer. |
| `email` | string | Email address of the customer. |
| `phone` | string | Phone number of the customer. |
| `metadata` | object | Additional key-value data attached to the customer. |
| `created_at` | string | ISO 8601 timestamp of when the customer was created. |

**Response Example**

```json
{
  "id": "cus_ABC123",
  "name": "Jane Smith",
  "email": "jane.smith@example.com",
  "phone": "+919876543210",
  "metadata": {},
  "created_at": "2026-04-10T05:00:00Z"
}
```

**Response Codes**

| HTTP Status | Description |
| --- | --- |
| `200 OK` | Customer details returned successfully. |
| `401 Unauthorized` | The API key is missing or invalid. |
| `404 Not Found` | No customer exists with the specified ID. |

---

## Update a Customer

Updates one or more fields on an existing customer record. Only the fields included in the request body are modified.

**Endpoint**

```
PATCH /v1/customers/{id}
```

**Path Parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Required | The unique identifier of the customer to update. |

**Request Headers**

| Header | Value |
| --- | --- |
| `Authorization` | `Bearer <YOUR_API_KEY>` |
| `Content-Type` | `application/json` |

**Request Body Parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Optional | Updated full name of the customer. |
| `email` | string | Optional | Updated email address. Must be a valid email format. |
| `phone` | string | Optional | Updated phone number, including country code. |
| `metadata` | object | Optional | Updated key-value metadata. Replaces the existing metadata entirely. |

**Request Example**

```bash
curl -X PATCH https://api.acmepayments.com/v1/customers/cus_ABC123 \
  -H "Authorization: Bearer sk_test_51ABC123XYZ" \
  -H "Content-Type: application/json" \
  -d '{
    "phone": "+919999900000"
  }'
```

**Response Schema**

| Field | Type | Description |
| --- | --- | --- |
| `id` | string | Unique identifier for the customer. |
| `name` | string | Full name of the customer. |
| `email` | string | Email address of the customer. |
| `phone` | string | Updated phone number of the customer. |
| `metadata` | object | Additional key-value data attached to the customer. |
| `created_at` | string | ISO 8601 timestamp of when the customer was created. |

**Response Example**

```json
{
  "id": "cus_ABC123",
  "name": "Jane Smith",
  "email": "jane.smith@example.com",
  "phone": "+919999900000",
  "metadata": {},
  "created_at": "2026-04-10T05:00:00Z"
}
```

**Response Codes**

| HTTP Status | Description |
| --- | --- |
| `200 OK` | Customer was updated successfully. |
| `400 Bad Request` | The request body contains invalid values. |
| `401 Unauthorized` | The API key is missing or invalid. |
| `404 Not Found` | No customer exists with the specified ID. |