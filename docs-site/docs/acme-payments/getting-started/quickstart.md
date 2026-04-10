---
title: Quickstart
sidebar_position: 2
description: This quickstart shows how to create your first payment using the Acme Payments API.
---

# Quickstart

This quickstart shows how to create your first payment using the Acme Payments API.

## 1. Prerequisites

**Get your API key**. Refer to [Get an API Key](/docs/acme-payments/quickstart/get-api-key).

## 2. Install the SDK

Install the SDK for your preferred language.

**Node.js**

```bash
npm install acme-payments@latest
```

**Python**

```bash
pip install acme-payments@latest
```

**JavaScript**

```javascript
import Acme from 'acme-payments';
```

## 3. Create a client
This task provides a basic example of how to create a client using the Acme Payments API.

prerequisites:

- Get your API key. Refer to [Get an API Key](/docs/acme-payments/quickstart/get-api-key).

To create a client, you need to provide the following parameters:

- api_key: The API key to be used.

```javascript
const client = new Acme('sk_test_123');
```
You have successfully created a client.

## 4. Create a payment
This task provides a basic example of how to create a payment using the Acme Payments API.

prerequisites:

- Get your API key. Refer to [Get an API Key](/docs/acme-payments/quickstart/get-api-key).
- Create a customer. Refer to [Create a Customer](/docs/acme-payments/quickstart/create-customer).

To create a payment, you need to provide the following parameters:

- amount: The amount to be charged.
- currency: The currency of the amount.
- customer_id: The ID of the customer.
- payment_method: The payment method to be used.

```javascript
const payment = await client.payments.create({
  amount: 5000,
  currency: 'INR',
  customer_id: 'cus_123',
  payment_method: 'pm_card_visa',
});
```
You have successfully created a payment.

## 5. Check status
This task provides a basic example of how to check the status of a payment using the Acme Payments API.

prerequisites:

- Get your API key. Refer to [Get an API Key](/docs/acme-payments/quickstart/get-api-key).
- Create a payment. Refer to [Create a Payment](/docs/acme-payments/quickstart/create-payment).

To check the status of a payment, you need to provide the following parameters:

- payment_id: The ID of the payment.

```javascript
console.log(payment.status);
```
You have successfully checked the status of a payment.

## 6. Handle Webhooks
This task provides a basic example of how to handle webhooks using the Acme Payments API.

prerequisites:

- Get your API key. Refer to [Get an API Key](/docs/acme-payments/quickstart/get-api-key).
- Create a payment. Refer to [Create a Payment](/docs/acme-payments/quickstart/create-payment).

To handle webhooks, you need to provide the following parameters:

- webhook_secret: The webhook secret to be used.

```javascript
const webhook = await client.webhooks.handle({
  webhook_secret: 'whsec_123',
});
```
You have successfully handled webhooks.

## 7. Next Steps

- Go to [**Introduction**](/docs/acme-payments/introduction) to learn more about the API.
- Explore [**Concepts**](/docs/acme-payments/concepts) to understand core objects.
- Use [**Guides**](/docs/acme-payments/guides) for real-world workflows.

