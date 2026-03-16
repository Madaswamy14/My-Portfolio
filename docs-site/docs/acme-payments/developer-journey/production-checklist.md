---
title: Production Checklist
description: Verify that the integration is secure, observable, and resilient before launch.
---

# Production Checklist

Before going live, verify that your integration is secure, observable, and resilient.

## Credentials and environments

- [ ] switch from sandbox to production API keys
- [ ] keep secret keys only on the server side
- [ ] separate test and production configuration clearly

## Request safety

- [ ] implement idempotency for payment creation workflows
- [ ] validate request payloads before sending them
- [ ] handle retries with backoff for transient failures

## Webhooks

- [ ] verify webhook signatures
- [ ] deduplicate events using stored event IDs
- [ ] return `2xx` quickly and move long-running work to background jobs

## Monitoring and support

- [ ] capture request IDs for failed API calls
- [ ] monitor API error rates and webhook delivery failures using the [Monitoring and Observability Guide](./monitoring-observability.md)
- [ ] create support workflows for refunds and payment investigation

## Launch readiness

- [ ] run end-to-end tests in a staging environment
- [ ] document rollback and incident response steps
- [ ] review [Build a Payment App](../tutorials/build-payment-app.md), [Developer Journey Overview](./overview.md), and [Monitoring and Observability Guide](./monitoring-observability.md)