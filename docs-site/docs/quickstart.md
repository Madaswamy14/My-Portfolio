---
sidebar_position: 2
---

# Quickstart

This quickstart shows the first-run path I use when documenting a public REST API with the smallest successful request possible.

## Before you begin

- Confirm the base URL: `https://swapi.dev/api/`
- Use a tool such as `curl`, PowerShell, Postman, or your preferred HTTP client.
- No authentication is required for the request in this sample.

## Make your first request

```bash
curl --request GET \
  --url https://swapi.dev/api/people/1/
```

## What success looks like

A successful first request should help the user answer three questions quickly:

1. Did I reach the correct endpoint?
2. Did the API return `200 OK` and valid JSON?
3. Can I recognize a useful response shape immediately?

## Why this pattern works

- It proves the base URL and endpoint format first.
- It removes unnecessary auth friction from the first-run flow.
- It gives the reader a clean handoff into conventions and detailed reference content.

Next, review the [SWAPI API Reference Sample](./swapi-api-reference-sample.md) for the full migrated case study or open [API Reference](./api-reference.md) to see the reusable reference pattern.