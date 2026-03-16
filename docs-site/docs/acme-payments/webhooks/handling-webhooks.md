---
title: Handling Webhooks
description: Receive and process asynchronous payment state changes safely.
---

# Handling Webhooks

Use webhooks to receive asynchronous updates when payment state changes in Acme Payments.

## Recommended event flow

1. receive the webhook request on your server
2. verify the webhook signature before parsing the payload
3. store the event ID so retries are idempotent
4. update your application state
5. return a `2xx` response quickly

## Example events

- `payment.succeeded`
- `payment.failed`
- `refund.processed`

## Example payload

```json
{
  "id": "evt_12345",
  "type": "payment.succeeded",
  "createdAt": "2026-03-09T12:00:00Z",
  "data": {
    "paymentId": "pay_98765",
    "customerId": "cus_12345",
    "amount": 1000,
    "currency": "USD",
    "status": "succeeded"
  }
}
```

## Implementation guidance

- verify the request signature before trusting the payload
- treat every delivery as retryable and safe to process more than once
- persist the event ID and processing result
- queue long-running work instead of doing it inline in the webhook handler

## Failure handling

If your endpoint returns a non-`2xx` response, the event should be retried. Design your handler so repeated deliveries do not create duplicate emails, refunds, or internal state changes.

## Related guides

- [Accept Your First Payment](../quickstart/first-payment.md)
- [Error Handling](../concepts/error-handling.md)
- [Developer Portal Architecture](../architecture/developer-portal-architecture.md)