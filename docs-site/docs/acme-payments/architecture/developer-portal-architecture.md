---
title: Developer Portal Architecture
description: Content and publishing model for the Acme Payments developer portal case study.
---

# Developer Portal Architecture

This portal section is structured to reflect a realistic developer experience platform.

## Content model

- `docs/acme-payments/` holds onboarding, reference, tutorial, concept, and architecture content
- quickstart pages create the fastest path to first success
- API reference pages document the core payments, customers, and refunds endpoints
- developer-journey pages extend the docs from first call to production readiness

## Publishing flow

1. update docs or API contract
2. refresh endpoint examples and reference content
3. review changes in preview
4. publish the static site

## Why this structure works

It mirrors real DevEx teams that separate conceptual docs, onboarding, and API reference while keeping one cohesive portal experience.