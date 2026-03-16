---
title: Monitoring and Observability Guide
description: Observability guidance for payments and webhook integrations.
---

# Monitoring and Observability Guide

Observability is part of the product experience. Developers need to understand what happened, why it happened, and what to do next when payments or webhooks fail.

## What to capture on every API request

- log the Acme `request_id` returned with each response
- capture the endpoint, HTTP status, latency, and environment
- store idempotency keys for write operations so retries can be traced safely
- correlate failed requests to customer, payment, or refund identifiers

## Monitor webhook delivery health

- store every webhook `event.id` before processing
- record signature verification results and delivery timestamps
- alert on repeated delivery failures or growing retry backlogs
- separate acknowledgement latency from downstream business logic time

## Build dashboards for the developer lifecycle

At minimum, create dashboards for:

1. authentication failures and `401` spikes
2. validation and `4xx` trends by endpoint
3. `5xx` errors and latency regressions
4. webhook retry counts and dead-letter events
5. refunds and payment investigations opened by support

## Launch checklist

- [ ] request IDs appear in API error logs and support tickets
- [ ] webhook delivery failures trigger an alert
- [ ] dashboards distinguish sandbox from production traffic
- [ ] developers can trace a payment from request to webhook completion
- [ ] incident runbooks link to [Webhooks Journey](./webhooks.md) and [Production Checklist](./production-checklist.md)