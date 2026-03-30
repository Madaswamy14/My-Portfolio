---
title: Idempotency
description: Prevent duplicate writes during retries.
---

# Idempotency

Idempotency ensures that retrying the same request does not create duplicate payments.

## Why it matters

Network failures and timeouts happen. Without idempotency, a client retry could charge a customer twice.

## How to use it

- Send a unique `Idempotency-Key` header on each create request.
- Reuse the same key only when retrying the exact same operation.
- Generate keys in your application layer, not manually.

## Best practice

Use business identifiers, such as an order number plus operation type, to make retries traceable and predictable.