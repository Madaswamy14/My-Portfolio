---
title: First Payment Journey
description: Validate the first successful payment flow end to end.
---

# First Payment Journey

After onboarding, the first milestone is a successful payment flow that proves authentication, request formatting, and response handling all work.

## Recommended flow

1. Create a customer with `POST /customers`.
2. Create a payment with `POST /payments`.
3. Inspect the returned payment `status`.
4. Optionally issue a refund with `POST /refunds`.

## Canonical guides

- [Accept Your First Payment](../quickstart/first-payment.md)
- [Create customer](../api-reference/create-customer.md)
- [Create a payment](../api-reference/create-payment.md)
- [Create refund](../api-reference/create-refund.md)

## What to verify

- request bodies match the schema
- customer and payment IDs are stored for follow-up requests
- the frontend or test client displays the response clearly
- failed requests surface actionable errors

## Next step

Once the synchronous payment flow works, support asynchronous updates with [Webhooks Journey](./webhooks.md).