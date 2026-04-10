---
title: Introduction
sidebar_position: 1
description: This guide introduces the Acme Payments API, its key features, and how to get started.
---

# Introduction

Acme Payments API is a developer-first platform designed to help you accept and manage payments globally with speed, reliability, and simplicity.

If you are building an e-commerce platform, SaaS product, or mobile app, Acme Payments provides the tools you need to handle payments end-to-end.



## Features

With Acme Payments, you can:

- Accept one-time payments (cards, UPI, wallets)
- Store and manage customers
- Save payment methods for future use
- Handle refunds and failed transactions
- Receive real-time updates via webhooks



## Payment Flow

At a high level, the payment flow looks like this:

1. Create a customer.
2. Attach a payment method.
3. Create and confirm a payment.
4. Listen to webhooks for status updates.

This separation ensures flexibility, scalability, and clean system design.


## Key Features

### Global Payments
Support for multiple currencies and payment methods including cards and UPI.

### Security
- API key authentication
- No sensitive data stored on your servers
- Webhook signature verification

### Idempotent Requests
Prevent duplicate payments using idempotency keys.

### Real-Time Events
Stay updated with webhook notifications for all payment events.


## Base URL

https://api.acmepayments.com/v1


## Authentication

All API requests must include your secret API key:

```

Authorization: Bearer <YOUR_API_KEY>

```

### API Key Types

| Key Type | Usage |
|---------|------|
| sk_test | Testing environment |
| sk_live | Production environment |

> **Note:** Never expose your secret key in frontend or client-side code.


## Environments

### Test Mode
Use test keys to simulate payments without real transactions.

### Live Mode
Process real payments with live API keys.


## Design Principles

This API is built with:

- **Predictability** : Consistent request/response formats
- **Simplicity** : Minimal required parameters
- **Reliability** : Retry-safe operations
- **Scalability** : Works for startups to enterprise systems


## Next Steps

Start integrating in minutes:

- Go to [**Quickstart**](quickstart.md) to create your first payment
- Explore [**Concepts**](concepts.md) to understand core objects
- Use [**Guides**](guides.md) for real-world workflows


> **Note:** If you're new to payments APIs, begin with the [**Accept Payments guide**](accept-payments.md) — it walks you through a complete working flow.

```

