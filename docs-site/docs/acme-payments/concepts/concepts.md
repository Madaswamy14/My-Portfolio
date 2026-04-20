---
title: Concepts
sidebar_position: 1
description: A Customer represents a user in the system.
---

# Concepts

This section explains the core concepts of the Acme Payments API.

## Customers

A **Customer** represents a user in the system. It stores user identity and payment history.

### Customer Object

```json
{
  "id": "cus_123",
  "name": "John Doe",
  "email": "[EMAIL_ADDRESS]"
}
```

## Payments

A **Payment** represents a transaction between a customer and the system.

### Payment Object

```json
{
  "id": "pay_123",
  "amount": 1500,
  "currency": "INR",
  "status": "succeeded",
  "customer": "cus_123",
  "payment_method": "pm_card_visa"
}
```

## Payment Methods

A **Payment Method** represents a payment instrument, such as a credit card.

### Payment Method Object

```json
{
  "id": "pm_123",
  "type": "card",
  "card": {
    "brand": "visa",
    "last4": "4242"
  }
}
```
