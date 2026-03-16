---
title: List payments
description: Return a list of payment objects.
---

# List payments

`GET /payments`

Return a list of payment objects.

## Example request

```bash
curl https://api.acmepayments.com/v1/payments \
  -H "Authorization: Bearer sk_test_51ABC123XYZ"
```

## Success response

```json
[
  {
    "id": "pay_98765",
    "amount": 1000,
    "currency": "USD",
    "status": "succeeded",
    "createdAt": "2026-03-09T12:00:00Z"
  }
]
```

## Use this endpoint when

- you need to review recent payment activity
- support or operations teams need to inspect payment state quickly
- you are verifying the output of a new integration

## Related docs

- [Retrieve payment](./retrieve-payment.md)
- [Monitoring and Observability Guide](../developer-journey/monitoring-observability.md)