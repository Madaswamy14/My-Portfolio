---
title: Make Your First API Call
description: Send a minimal payment request in the sandbox environment.
---

# Make Your First API Call

This example creates a test payment in the sandbox environment.

## Request

```bash
curl --request POST https://api.sandbox.acmepayments.dev/v1/payments \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --header "Content-Type: application/json" \
  --header "Idempotency-Key: demo-payment-001" \
  --data '{
    "amount": 4200,
    "currency": "USD",
    "customerId": "cus_demo_123",
    "source": "tok_visa"
  }'
```

## Success response

Expect a `201 Created` response with a payment object that includes its `id`, `status`, and `createdAt` timestamp.

## What to check

- the request includes a bearer token
- the body uses the smallest currency unit
- an idempotency key is sent for safe retries

## Next step

Open the [Create Payment](../api-reference/create-payment.md) endpoint page to review the request fields and response shape in more detail.