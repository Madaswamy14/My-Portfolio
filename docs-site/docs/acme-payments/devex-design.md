---
title: Designing the Acme Developer Portal
description: Explain the DevEx strategy behind the Acme Payments documentation system.
---

# Designing the Acme Developer Portal

This page explains the developer experience strategy behind the portal, not just the content inside it.

## Documentation strategy

The portal is organized around the developer journey:

- discover the API
- get authenticated quickly
- make the first successful call
- handle errors and webhooks
- monitor integration health and support incidents
- prepare for production use

## API documentation

The standalone source project originally generated endpoint docs from an OpenAPI contract. In the main portfolio portal, those endpoints are represented as integrated Markdown reference pages so the information architecture remains visible without a second Docusaurus app.

## Tutorials and conceptual docs

Quickstarts, tutorials, and concept pages complement the reference by showing realistic integration tasks and operational concerns.

## System design perspective

This portal section is meant to demonstrate DevEx thinking:

- content architecture
- onboarding design
- reference strategy
- request safety and webhook guidance
- production-readiness guidance
- observability guidance across the developer lifecycle

## Related sections

- [Developer Journey Overview](./developer-journey/overview.md)
- [Monitoring and Observability Guide](./developer-journey/monitoring-observability.md)
- [Developer Portal Architecture](./architecture/developer-portal-architecture.md)
- [Build a Payment App](./tutorials/build-payment-app.md)