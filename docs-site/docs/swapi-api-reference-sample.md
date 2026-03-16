---
title: SWAPI API Reference Sample
description: API reference case study showing quickstart, conventions, and endpoint design.
---

# SWAPI API Reference Sample

This migrated sample shows how I design API documentation that supports both first-run success and deeper reference scanning.

## Documentation goal

Give developers a clean path from the first successful request to detailed endpoint usage without forcing them to infer conventions from raw examples.

## Quickstart

Send a basic `GET` request to confirm the API is reachable and that the response shape is understandable:

```bash
curl --request GET \
  --url https://swapi.dev/api/people/1/
```

## Key concepts and conventions

| Concept | Why it matters |
| --- | --- |
| Base URL | Consistent examples should use `https://swapi.dev/api/` to reduce confusion. |
| No authentication | Readers can focus on request structure instead of token setup. |
| Collection vs. detail endpoints | This separation makes pagination and single-resource retrieval easier to understand. |
| Query parameters | `page` and `search` are the fastest way to demonstrate pagination and filtering. |

## Reference patterns

### List people

`GET https://swapi.dev/api/people/`

Use this endpoint when you want a paginated people collection.

| Parameter | Type | Description |
| --- | --- | --- |
| `page` | integer | Returns a specific results page. |
| `search` | string | Filters results by a search term such as `luke`. |

### Get a person

`GET https://swapi.dev/api/people/{id}/`

Use this endpoint when you want one person resource by ID.

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | integer | Unique identifier for the person resource. |

## Why this sample works as documentation

- it pairs quickstart, conventions, and reference content on one path
- it standardizes examples so the reader is not forced to reconcile mixed environments
- it ends with troubleshooting and next-step guidance instead of stopping at the last endpoint

## Next steps

- test pagination with `?page=2`
- test filtering with `?search=luke`
- expand the same pattern to planets, films, and starships

Original HTML sample: [SWAPI API Reference](https://madaswamy14.github.io/My-Portfolio/Portfolio/swapi_API-docs.html)