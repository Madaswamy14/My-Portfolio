---
title: API Reference Overview
description: Human-readable endpoint reference for the Acme Payments portfolio sample.
---

# API Reference Overview

The original standalone Acme portal generated endpoint docs from an OpenAPI source. In this integrated portfolio portal, the same endpoint coverage is presented as clean Markdown reference pages so it works natively inside the main Docusaurus site.

## Base request pattern

- base URL: `https://api.acmepayments.com/v1`
- authentication: `Authorization: Bearer <token>`
- content type: `application/json`
- write safety: send an `Idempotency-Key` header on create operations

## Core endpoints

- [Create customer](./create-customer.md)
- [Create payment](./create-payment.md)
- [List payments](./list-payments.md)
- [Retrieve payment](./retrieve-payment.md)
- [Create refund](./create-refund.md)

## Suggested reading order

1. [Create customer](./create-customer.md)
2. [Create payment](./create-payment.md)
3. [Retrieve payment](./retrieve-payment.md)
4. [Create refund](./create-refund.md)

For the fastest hands-on path, start with [Accept Your First Payment](../quickstart/first-payment.md).