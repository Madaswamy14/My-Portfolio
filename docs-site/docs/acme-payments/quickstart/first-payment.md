---
title: Create a Payment
description: Complete the fastest path from sandbox credentials to a successful payment.
---

# Create a Payment

This quickstart shows how to create your first payment using the Acme Payments API.

## What you will do

1. Create an API key
2. Install the SDK or use raw HTTP
3. Create a customer
4. Create a payment
5. Issue a refund

## Get your API key

Get an API key from the Acme dashboard. You can use the sandbox key or create a new key.

Example test key:

`sk_test_51ABC123XYZ`

Send it in the `Authorization` header:

`Authorization: Bearer sk_test_51ABC123XYZ`

## Install the SDK

You can call the API directly or use an SDK.

### Node.js

```bash
npm install acme-payments
```

### Python

```bash
pip install acme-payments
```

## Create a customer

```bash
curl https://api.acmepayments.com/v1/customers \
  -H "Authorization: Bearer sk_test_51ABC123XYZ" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "customer@example.com",
    "name": "Jane Doe"
  }'
```

Example response:

```json
{
  "id": "cus_12345",
  "email": "customer@example.com",
  "name": "Jane Doe"
}
```

Save the `id` for the payment request.

## Create a payment

```bash
curl https://api.acmepayments.com/v1/payments \
  -H "Authorization: Bearer sk_test_51ABC123XYZ" \
  -H "Content-Type: application/json" \
  -d '{
    "amount": 1000,
    "currency": "USD",
    "customerId": "cus_12345"
  }'
```

Example response:

```json
{
  "id": "pay_98765",
  "amount": 1000,
  "currency": "USD",
  "status": "succeeded"
}
```

## Issue a refund

```bash
curl https://api.acmepayments.com/v1/refunds \
  -H "Authorization: Bearer sk_test_51ABC123XYZ" \
  -H "Content-Type: application/json" \
  -d '{
    "paymentId": "pay_98765",
    "amount": 1000
  }'
```

## What success looks like

You should have created a customer, completed a payment, and optionally exercised the refund workflow.

## Next steps

- [Authentication Overview](../authentication/overview.md)
- [Error Handling](../concepts/error-handling.md)
- [Handling Webhooks](../webhooks/handling-webhooks.md)
- [API Reference Overview](../api-reference/overview.md)