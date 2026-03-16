---
sidebar_position: 4
---

# API Reference Pattern

This page shows the reference structure I use for endpoint documentation: a fast scanning path, clear request shape, readable parameter detail, and examples that feel implementation-ready.

## Reference principles

- start with the smallest successful request
- separate collection endpoints from single-resource endpoints
- explain query or path parameters close to the request example
- keep errors and next steps visible so troubleshooting does not require a second page

## List people

`GET https://swapi.dev/api/people/`

Returns a paginated collection of people resources.

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `page` | integer | Returns a specific results page. |
| `search` | string | Filters results by a search term such as a character name. |

## Get a person

`GET https://swapi.dev/api/people/{id}/`

Returns a single resource by ID.

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `id` | integer | Unique identifier for the person resource. |

### Example request

```bash
curl --request GET \
  --url https://swapi.dev/api/people/1/
```

### Example response

```json
{
  "name": "Luke Skywalker",
  "height": "172",
  "mass": "77",
  "birth_year": "19BBY"
}
```

## Error responses

- `400` for malformed identifiers
- `404` when the resource does not exist
- `5xx` when the public API is temporarily unavailable

For the fuller migrated case study, review the [SWAPI API Reference Sample](./swapi-api-reference-sample.md).
Good reference content helps developers scan quickly while still giving them enough context to implement confidently.