---
title: Webhooks
sidebar_position: 3
description: This guide explains how to receive real-time updates about payments.
---

# Webhooks

Webhooks provide event notifications for payment lifecycle changes.

---

## Supported Events

- payment.succeeded
- payment.failed
- refund.processed

---

## Endpoint Setup

```http
POST /webhook
```

## Example Payload

```json
{
  "type": "payment.succeeded",
  "data": {
    "id": "pay_123",
    "amount": 1500
  }
}
```

## Handling Events

```javascript
switch (event.type) {
  case "payment.succeeded":
    fulfillOrder();
    break;
  case "payment.failed":
    notifyUser();
    break;
}
```

## Reliability Considerations

- Webhooks may be retried on failure
- Ensure idempotent handling
- Always return HTTP 200 after processing

## Security

- Validate webhook signatures
- Reject unknown sources