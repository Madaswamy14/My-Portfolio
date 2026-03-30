---
title: Monitoring and Observability Guide
description: Observability guidance for payments and webhook integrations.
---

# Monitoring and Observability Guide

Observability is part of the product experience. Developers need to understand what happened, why it happened, and what to do next when payments or webhooks fail.

## What to capture on every API request

- Log the Acme `request_id` returned with each response.
- Capture the endpoint, HTTP status, latency, and environment.
- Store idempotency keys for write operations so retries can be traced safely.
- Correlate failed requests to customer, payment, or refund identifiers.

## Monitor webhook delivery health

- Store every webhook `event.id` before processing.
- Record signature verification results and delivery timestamps.
- Alert on repeated delivery failures or growing retry backlogs.
- Separate acknowledgement latency from downstream business logic time.

## Build dashboards for the developer lifecycle

At minimum, create dashboards for:

1. Authentication failures and `401` spikes.
2. Validation and `4xx` trends by endpoint.
3. `5xx` errors and latency regressions.
4. Webhook retry counts and dead-letter events.
5. Refunds and payment investigations opened by support.

## Launch checklist

- [ ] Request IDs appear in API error logs and support tickets.
- [ ] Webhook delivery failures trigger an alert.
- [ ] Dashboards distinguish sandbox from production traffic.
- [ ] Developers can trace a payment from request to webhook completion.
- [ ] incident runbooks link to [Webhooks Journey](./webhooks.md) and [Production Checklist](./production-checklist.md)