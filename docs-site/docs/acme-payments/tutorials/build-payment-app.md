---
title: Build a Payment App
description: Assemble a simple payment workflow around the Acme Payments API.
---

# Build a Payment App

This tutorial shows how to assemble a simple payment app around the Acme Payments API.

## What you will build

- a checkout form in your frontend
- a server route that creates customers
- a server route that creates payments
- a refund action for support workflows
- a webhook handler for asynchronous updates

## Step 1 — Create your API key

Start with [Get an API Key](../quickstart/get-api-key.md) and store the secret in your backend environment variables.

## Step 2 — Create a customer endpoint

Your server should collect customer data from the frontend and call `POST /customers` using the secret key.

## Step 3 — Create a payment endpoint

After the customer exists, create a payment with `POST /payments` and return the resulting payment object to the frontend.

## Step 4 — Show payment state in the UI

Display the payment `status`, amount, and currency in your application so users can confirm the result immediately after checkout.

## Step 5 — Add refund support

Use `POST /refunds` from an internal support workflow or admin screen to reverse completed payments when needed.

## Step 6 — Handle webhooks

Read [Handling Webhooks](../webhooks/handling-webhooks.md) and update your internal order or billing state when events arrive asynchronously.

## Suggested project structure

```text
app/
  frontend/
  backend/
    routes/customers.js
    routes/payments.js
    routes/refunds.js
    routes/webhooks.js
```

## Related docs

- [Accept Your First Payment](../quickstart/first-payment.md)
- [API Reference Overview](../api-reference/overview.md)
- [Production Checklist](../developer-journey/production-checklist.md)