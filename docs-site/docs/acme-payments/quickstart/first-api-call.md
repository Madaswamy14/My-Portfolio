---
title: Make Your First API Call
description: Send a minimal payment request in the sandbox environment.
---

# Make Your First API Call

This example creates a test payment in the sandbox environment.

## Request

Send a request to the Acme Payments API using your terminal. This API call simulates charging a customer for a dummy product. Replace `YOUR_API_KEY` with the sandbox secret key you generated previously.

```bash
curl https://api.sandbox.acmepayments.dev/v1/payments \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: demo-payment-001" \
  -d '{
    "amount": 4200,
    "currency": "USD",
    "customerId": "cus_demo_123",
    "source": "tok_visa"
  }'
```

> **Note:** Notice the `amount` field. Acme Payments APIs generally expect amounts in the smallest currency unit. In the US, `4200` means $42.00, formatted in cents.

## Response

If the API call was successful, it returns a `201 Created` HTTP response and a JSON payload containing the new payment object. It should look like this:

```json
{
  "id": "pay_9876543210ABCxyz",
  "amount": 4200,
  "currency": "USD",
  "customerId": "cus_demo_123",
  "source": "tok_visa",
  "status": "succeeded",
  "createdAt": "2026-03-09T14:35:10Z"
}
```

## What to check

Verify that your integration works perfectly by checking the following details:

- **Authentication**: Ensure the request used the `Authorization: Bearer` header containing your test key.
- **Amounts**: Verify you sent the amount as the lowest integer denominator.
- **Idempotency**: Verify an `Idempotency-Key` was sent to safely decouple retries from network errors.
- **Status**: Look for `"status": "succeeded"` in the HTTP response body.

## Next step

Open the [Create Payment](../api-reference/create-payment.md) endpoint page to review the request fields and response shape in more detail.