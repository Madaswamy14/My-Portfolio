---
title: Production Checklist
description: Verify that the integration is secure, observable, and resilient before launch.
---

# Production Checklist

Before going live, verify that your integration is secure, observable, and resilient.

## Credentials and environments

- [ ] Switch from sandbox to production API keys.
- [ ] Keep secret keys only on the server side.
- [ ] Separate test and production configuration clearly.

## Request safety

- [ ] Implement idempotency for payment creation workflows.
- [ ] Validate request payloads before sending them.
- [ ] Handle retries with backoff for transient failures.

## Webhooks

- [ ] Verify webhook signatures.
- [ ] Deduplicate events using stored event IDs.
- [ ] Return `2xx` quickly and move long-running work to background jobs.

## Monitoring and support

- [ ] Capture request IDs for failed API calls.
- [ ] Monitor API error rates and webhook delivery failures using the [Monitoring and Observability Guide](./monitoring-observability.md)
- [ ] Create support workflows for refunds and payment investigation.

## Launch readiness

- [ ] Run end-to-end tests in a staging environment.
- [ ] Document rollback and incident response steps.
- [ ] Review [Build a Payment App](../tutorials/build-payment-app.md), [Developer Journey Overview](./overview.md), and [Monitoring and Observability Guide](./monitoring-observability.md).