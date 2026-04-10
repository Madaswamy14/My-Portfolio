---
title: Errors
sidebar_position: 1
description: Reference documentation for error response format and HTTP status codes returned by the Acme Payments API.
---

# Errors

The Acme Payments API uses conventional HTTP status codes to indicate the outcome of a request. Codes in the `2xx` range indicate success. Codes in the `4xx` range indicate a client-side error. Codes in the `5xx` range indicate a server-side error.

**Base URL:** `https://api.acmepayments.com/v1`

---

## Error Response Format

All error responses include a JSON body with the following structure:

| Field | Type | Description |
| --- | --- | --- |
| `type` | string | Category of the error. See [Error Types](#error-types) for possible values. |
| `code` | integer | HTTP status code. |
| `message` | string | Human-readable description of what went wrong. |
| `param` | string | The specific request parameter that caused the error, if applicable. |
| `request_id` | string | A unique identifier for the request. Include this when contacting support. |

**Error Response Example**

```json
{
  "error": {
    "type": "invalid_request_error",
    "code": 400,
    "message": "The 'amount' field must be a positive integer.",
    "param": "amount",
    "request_id": "req_A1B2C3D4E5"
  }
}
```

---

## Error Types

| Type | Description |
| --- | --- |
| `authentication_error` | The API key is missing, expired, or invalid. |
| `invalid_request_error` | The request is malformed or missing required parameters. |
| `payment_error` | The payment failed due to card decline, insufficient funds, or similar. |
| `rate_limit_error` | Too many requests were sent in a short period. |
| `api_error` | An unexpected error occurred on the server. If this persists, contact support. |

---

## HTTP Status Codes

| HTTP Status | Error Type | Description |
| --- | --- | --- |
| `400 Bad Request` | `invalid_request_error` | The request body is missing a required field or contains an invalid value. |
| `401 Unauthorized` | `authentication_error` | The `Authorization` header is missing or the API key is invalid. |
| `402 Payment Required` | `payment_error` | The payment was declined by the card network or issuer. |
| `403 Forbidden` | `authentication_error` | The API key does not have permission to perform the requested action. |
| `404 Not Found` | `invalid_request_error` | The specified resource does not exist. |
| `409 Conflict` | `invalid_request_error` | A resource with the provided identifier already exists. |
| `422 Unprocessable Entity` | `invalid_request_error` | The resource is not in a valid state for the requested operation. |
| `429 Too Many Requests` | `rate_limit_error` | The request was rate-limited. See [Rate Limits](rate-limits.md). |
| `500 Internal Server Error` | `api_error` | An unexpected error occurred on the server. |

---

## Handling Errors

### Authentication Errors

Verify that the `Authorization` header is present and uses the correct API key for the target environment (`sk_test_` for test mode, `sk_live_` for live mode).

### Invalid Request Errors

Check the `param` field in the error response to identify which field caused the issue. Review the corresponding endpoint's parameter documentation.

### Payment Errors

A `402` status indicates a payment failure at the issuer level. The `message` field provides additional detail. Prompt the customer to use a different payment method.

### Rate Limit Errors

Implement exponential backoff before retrying requests. See [Rate Limits](rate-limits.md) for limit thresholds.

### Server Errors

If a `5xx` error persists, include the `request_id` from the error response when contacting support.

---

## Related

- [Rate Limits](rate-limits.md) — Request volume limits and retry strategies.
- [Payments API](../api/payments.md) — Create and retrieve payments.
