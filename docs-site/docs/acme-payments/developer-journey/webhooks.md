---
title: Webhooks Journey
description: Extend the integration from request/response into event-driven workflows.
---

# Webhooks Journey

Webhooks move the integration from a one-request demo into a realistic event-driven workflow.

## Why webhooks matter

Payment status can change outside the immediate request cycle. Your integration should consume events so internal order, billing, and support systems stay in sync.

## Core responsibilities

1. receive webhook events on a server endpoint
2. verify the signature before trusting the payload
3. store the event ID for deduplication
4. update your internal state
5. retry safely when downstream work fails

## Example event types

- `payment.succeeded`
- `payment.failed`
- `refund.processed`

## Detailed guide

Use [Handling Webhooks](../webhooks/handling-webhooks.md) for payload examples and delivery recommendations.