---
title: Accept Payments
sidebar_position: 2
description: This guide explains how to accept payments.
---

# Accept Payments

This guide describes how to create and confirm a payment and verify its final status.

## Steps

1. Create a customer
2. Create a payment
3. Confirm the payment (optional if `confirm=true`)
4. Verify status via API or webhook

---

## Create a customer

```http
POST /v1/customers
```

```json
{
  "name": "Jane Doe",
  "email": "jane@example.com"
}
```

## Create a payment

```http
POST /v1/payments
```

```json
{
  "amount": 1500,
  "currency": "INR",
  "customer_id": "cus_123",
  "payment_method": "pm_card_visa",
  "confirm": true
}
```

## Check Payment Status

```http
GET /v1/payments/{id}
```

## Possible Status Values

- Requires_payment_method
- Processing
- Succeeded
- Failed

## Handle Result

- If succeeded: fulfill the order
- If failed: prompt retry with a different payment method

## Notes

- Use idempotency keys to prevent duplicate charges
- Do not assume immediate success; verify via webhook
