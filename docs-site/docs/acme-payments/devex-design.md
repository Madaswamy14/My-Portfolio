---
title: Designing the Acme Developer Portal
description: Explain the DevEx strategy behind the Acme Payments documentation system.
---

# Designing the Acme Developer Portal

This page explains the developer experience strategy behind the portal, not just the content inside it.

## Documentation strategy

The portal is organized around the developer journey:

- Discover the API.
- Get authenticated quickly.
- Make the first successful call.
- Handle errors and webhooks.
- Monitor integration health and support incidents.
- Prepare for production use.

## API documentation

The standalone source project originally generated endpoint docs from an OpenAPI contract. In the main portfolio portal, those endpoints are represented as integrated Markdown reference pages so the information architecture remains visible without a second Docusaurus app.

## Tutorials and conceptual docs

Quickstarts, tutorials, and concept pages complement the reference by showing realistic integration tasks and operational concerns.

## System design perspective

This portal section is meant to demonstrate DevEx thinking:

- Content architecture.
- Onboarding design.
- Reference strategy.
- Request safety and webhook guidance.
- Production-readiness guidance.
- Observability guidance across the developer lifecycle.

## Related sections

- [Developer Journey Overview](./developer-journey/overview.md)
- [Monitoring and Observability Guide](./developer-journey/monitoring-observability.md)
- [Developer Portal Architecture](./architecture/developer-portal-architecture.md)
- [Build a Payment App](./tutorials/build-payment-app.md)