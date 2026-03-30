---
title: Create a Payment
description: Complete the fastest path from sandbox credentials to a successful payment.
---

# Create a Payment

This quickstart shows how to create your first payment using the Acme Payments API.

## 1. Prerequisites

Before you begin, you must:
1. Get your API key. Refer to [Get an API Key](./get-api-key.md).

## 2. Install the SDK
Install the SDK for your preferred language.

**Node.js**
```bash
npm install acme-payments
```

**Python**
```bash
pip install acme-payments
```

> **Note:** The examples below use raw `cURL` commands so you can copy and run them instantly from any terminal.

---

## 3. Create a customer
Create a customer before charging them.

**Endpoint:** `POST /customers`

**Request**

```bash
curl https://api.acmepayments.com/v1/customers \
  -u sk_test_51ABC123XYZ: \
  -H "Content-Type: application/json" \
  -d '{
    "email": "jane.doe@example.com",
    "name": "Jane Doe"
  }'
```

**Response**
The API responds with the newly created customer object. Save the `id` for the next step.
```json
{
  "id": "cus_12345",
  "email": "jane.doe@example.com",
  "name": "Jane Doe",
  "createdAt": "2026-03-09T14:30:00Z"
}
```

---

## 4. Create a payment
Create a payment to charge the customer you just created. Pass the `cus_12345` into the `customerId` property.

> **Warning:** Amounts must be provided in the lowest common denominator of the currency. For USD (`usd`), `$10.00` is represented as `1000` (cents).

**Endpoint:** `POST /payments`

**Request**
```bash
curl https://api.acmepayments.com/v1/payments \
  -u sk_test_51ABC123XYZ: \
  -H "Content-Type: application/json" \
  -d '{
    "amount": 1000,
    "currency": "USD",
    "customerId": "cus_12345"
  }'
```

**Response**
If the test card succeeds, the payment status returns `succeeded`.
```json
{
  "id": "pay_98765",
  "amount": 1000,
  "currency": "USD",
  "customerId": "cus_12345",
  "status": "succeeded",
  "createdAt": "2026-03-09T14:35:10Z"
}
```

---

## 5. Issue a refund
Create a refund to undo the payment.

Endpoint: `POST /refunds`

**Request**

```bash
curl https://api.acmepayments.com/v1/refunds \
  -u sk_test_51ABC123XYZ: \
  -H "Content-Type: application/json" \
  -d '{
    "paymentId": "pay_98765",
    "amount": 1000
  }'
```

**Response**
```json
{
  "id": "ref_88291",
  "paymentId": "pay_98765",
  "amount": 1000,
  "status": "processed",
  "createdAt": "2026-03-09T14:40:22Z"
}
```

---

## 7. What success looks like
You have successfully completed a full payment lifecycle without touching any real money. If you check your Developer Dashboard now, you will see a customer, a successful payment, and a processed refund in your sandbox events logged for today.

## 8. Next steps

Now that you understand the basic flow, consider looking at:

- **[Authentication Overview](../authentication/overview.md)**: Deep dive into securely managing API keys
- **[Error Handling](../concepts/error-handling.md)**: How to programmatically react to declines and issues
- **[Handling Webhooks](../webhooks/handling-webhooks.md)**: Receive real-time push notifications of events
- **[API Reference Overview](../api-reference/overview.md)**: View all endpoints and schemas