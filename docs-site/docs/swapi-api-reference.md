---
title: SWAPI API Reference Documentation
description: A complete API reference for SWAPI, including endpoints, schemas, parameters, and code examples.
---

# SWAPI API Reference Documentation

**URL:** https://swapi.dev

**Version:** 1.0  
**Audience:** Developers & Technical Writers  

## 1. Introduction
SWAPI (The Star Wars API) is an open-source, read-only REST API that provides structured data from the Star Wars universe. It provides data on various entities including characters, films, planets, species, vehicles, and starships. It is widely used as a learning resource for REST API consumption, documentation practice, and front-end prototyping.
This document provides a complete API reference including endpoint descriptions, request/response schemas, query parameters, error codes, and code examples.

## 2. Quick Reference
### 2.1 API Specifications
| Property | Value |
| --- | --- |
| Base URL | `https://swapi.dev/api/` |
| Protocol | HTTPS only |
| Data Format | JSON (`application/json`) |
| Authentication | None |
| Rate Limit | 10,000 requests per day per IP |
| Pagination | 10 results per page (configurable) |
| HTTP Methods | `GET` only (read-only API) |
| CORS | Enabled for all origins |
| Versioning | Version embedded in URL: `/api/v1/` (current) |
| Status Codes | 200, 400, 404, 500 |

### 2.2 Available Endpoints

| Method | Endpoint Path | Description |
| --- | --- | --- |
| GET | `/api/` | Root — lists all available resource URLs |
| GET | `/api/people/` | List all people (paginated) |
| GET | `/api/people/{id}/` | Retrieve a specific person by ID |
| GET | `/api/films/` | List all films (paginated) |
| GET | `/api/films/{id}/` | Retrieve a specific film by ID |
| GET | `/api/planets/` | List all planets (paginated) |
| GET | `/api/planets/{id}/` | Retrieve a specific planet by ID |
| GET | `/api/species/` | List all species (paginated) |
| GET | `/api/species/{id}/` | Retrieve a specific species by ID |
| GET | `/api/vehicles/` | List all vehicles (paginated) |
| GET | `/api/vehicles/{id}/` | Retrieve a specific vehicle by ID |
| GET | `/api/starships/` | List all starships (paginated) |
| GET | `/api/starships/{id}/` | Retrieve a specific starship by ID |

## 3. Root Endpoint
### 3.1 GET /api/
The root endpoint returns a JSON object containing the URLs for all six resource collections. This is the recommended starting point for API exploration.

**Request**
```http
GET https://swapi.dev/api/
```

**Response — 200 OK**
```json
{
  "people": "https://swapi.dev/api/people/",
  "planets": "https://swapi.dev/api/planets/",
  "films": "https://swapi.dev/api/films/",
  "species": "https://swapi.dev/api/species/",
  "vehicles": "https://swapi.dev/api/vehicles/",
  "starships": "https://swapi.dev/api/starships/"
}
```

## 4. People Endpoint
The People resource returns data about individual characters in the Star Wars universe.

### 4.1 `GET /api/people/{id}/`
Returns a single person resource identified by their integer ID.

**Path Parameter**
| Parameter | Description |
| --- | --- |
| `{id}` | Integer. The unique identifier for the person. Range: 1–83. |

**Response Schema**
| Field | Type & Description |
| --- | --- |
| `name` | string — Full name of the character |
| `height` | string — Height in centimetres |
| `mass` | string — Weight in kilograms |
| `hair_color` | string — Hair colour(s) separated by commas |
| `skin_color` | string — Skin colour(s) separated by commas |
| `eye_color` | string — Eye colour(s) separated by commas |
| `birth_year` | string — Birth year using BBY or ABY notation |
| `gender` | string — 'male', 'female', 'hermaphrodite', 'none', or 'n/a' |
| `homeworld` | string — URL of the planet resource for their home planet |
| `films` | array[string] — URLs of film resources this character appears in |
| `species` | array[string] — URLs of species resources |
| `vehicles` | array[string] — URLs of vehicle resources piloted |
| `starships` | array[string] — URLs of starship resources piloted |
| `created` | string — ISO 8601 datetime when this record was created |
| `edited` | string — ISO 8601 datetime when this record was last modified |
| `url` | string — The canonical URL of this resource |

**Example Request**
```http
GET https://swapi.dev/api/people/1/
```

**Example Response**
```json
{
  "name": "Luke Skywalker",
  "height": "172",
  "mass": "77",
  "hair_color": "blond",
  "skin_color": "fair",
  "eye_color": "blue",
  "birth_year": "19BBY",
  "gender": "male",
  "homeworld": "https://swapi.dev/api/planets/1/",
  "films": [
    "https://swapi.dev/api/films/1/",
    "https://swapi.dev/api/films/2/",
    "https://swapi.dev/api/films/3/",
    "https://swapi.dev/api/films/6/"
  ],
  "url": "https://swapi.dev/api/people/1/"
}
```

## 5. Films Endpoint
The Films resource provides metadata for each of the seven Star Wars theatrical films covered by SWAPI (Episodes I–VII).

### 5.1 `GET /api/films/{id}/`

**Response Schema**
| Field | Type & Description |
| --- | --- |
| `title` | string — The title of the film |
| `episode_id` | integer — The episode number (1–7) |
| `opening_crawl` | string — The full opening crawl text |
| `director` | string — Name of the film director |
| `producer` | string — Comma-separated list of producers |
| `release_date` | string — Release date in YYYY-MM-DD format |
| `characters` | array[string] — URLs of people resources appearing in this film |
| `planets` | array[string] — URLs of planet resources featured |
| `starships` | array[string] — URLs of starship resources featured |
| `vehicles` | array[string] — URLs of vehicle resources featured |
| `species` | array[string] — URLs of species resources featured |
| `created` | string — ISO 8601 creation datetime |
| `edited` | string — ISO 8601 last-modified datetime |
| `url` | string — Canonical URL of this resource |

## 6. Planets Endpoint
The Planets resource provides environmental and geographical data for planets featured in the Star Wars films.

### 6.1 `GET /api/planets/{id}/`

**Response Schema**
| Field | Type & Description |
| --- | --- |
| `name` | string — Planet name |
| `rotation_period` | string — Hours to complete one rotation on its axis |
| `orbital_period` | string — Days to complete one orbit of its local star |
| `diameter` | string — Diameter in kilometres |
| `climate` | string — Comma-separated climate types (e.g., 'arid', 'temperate') |
| `gravity` | string — Gravitational force relative to standard (e.g., '1 standard') |
| `terrain` | string — Comma-separated terrain types |
| `surface_water` | string — Percentage of planet surface covered in water |
| `population` | string — Average population (or 'unknown') |
| `residents` | array[string] — URLs of people who are residents |
| `films` | array[string] — URLs of films this planet appears in |
| `url` | string — Canonical URL of this resource |

## 7. Starships Endpoint
The Starships resource describes spacecraft capable of atmospheric and interstellar travel featured in the Star Wars films.

### 7.1 `GET /api/starships/{id}/`

**Response Schema**
| Field | Type & Description |
| --- | --- |
| `name` | string — Common name of the starship |
| `model` | string — Model or official name |
| `manufacturer` | string — Manufacturer(s) |
| `cost_in_credits` | string — Cost in Galactic Credits |
| `length` | string — Length in metres |
| `max_atmosphering_speed` | string — Maximum speed in atmosphere (km/h), or 'n/a' |
| `crew` | string — Minimum crew required to operate |
| `passengers` | string — Maximum passengers (excluding crew) |
| `cargo_capacity` | string — Cargo capacity in kilograms |
| `consumables` | string — Duration of consumables (e.g., '2 years') |
| `hyperdrive_rating` | string — Class of hyperdrive (lower = faster) |
| `MGLT` | string — Megalight per hour speed rating |
| `starship_class` | string — Type classification (e.g., 'Star Destroyer') |
| `pilots` | array[string] — URLs of people resources who pilot this ship |
| `films` | array[string] — URLs of films this ship appears in |
| `url` | string — Canonical URL of this resource |

## 8. Query Parameters
All list endpoints support the following query parameters for searching and paginating results.

### 8.1 Search and Pagination
| Parameter | Description & Usage |
| --- | --- |
| `search` | string — Case-insensitive partial match on the `name` field. Example: `?search=luke` |
| `page` | integer — Page number (1-indexed). Default: 1. Each page returns 10 results. Example: `?page=2` |
| `format` | string — Response format. Supported: 'json' (default) or 'api' (browsable). Example: `?format=json` |

### 8.2 Paginated Response Envelope
All list endpoints wrap results in a standard pagination envelope:
```json
{
  "count": 82,
  "next": "https://swapi.dev/api/people/?page=2",
  "previous": null,
  "results": [ ... ]
}
```
> **Tip:** To retrieve all records, start at page 1 and keep following the 'next' URL until it returns `null`. Each page contains up to 10 results.

## 9. Error Responses
SWAPI uses standard HTTP status codes to communicate success and failure. All error responses return a JSON object with a `detail` field describing the error.

| HTTP Status | Meaning & When It Occurs |
| --- | --- |
| `200 OK` | Request succeeded. Response body contains the requested data. |
| `400 Bad Request` | The request was malformed. Common cause: invalid page number or unsupported parameter. |
| `404 Not Found` | The requested resource does not exist. Example: `/api/people/9999/` |
| `500 Internal Server Error` | An unexpected server-side error occurred. Retry after a short delay. |

**Error Response Body**
```json
{
  "detail": "Not found"
}
```

## 10. Code Examples
### 10.1 JavaScript / Fetch API
```javascript
// Fetch Luke Skywalker's data
fetch("https://swapi.dev/api/people/1/")
  .then(response => {
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    return response.json();
  })
  .then(data => console.log(data.name, data.birth_year))
  .catch(error => console.error("Error:", error));
```

### 10.2 Python (requests)
```python
import requests

BASE = "https://swapi.dev/api/"

# Get all films
response = requests.get(f"{BASE}films/")
response.raise_for_status()

films = response.json()["results"]
for film in films:
    print(f"Episode {film['episode_id']}: {film['title']} ({film['release_date'][:4]})")
```

### 10.3 cURL
```bash
# Retrieve Tatooine (planet ID 1)
curl -X GET "https://swapi.dev/api/planets/1/" -H "Accept: application/json"

# Search for characters named 'Vader'
curl -X GET "https://swapi.dev/api/people/?search=Vader" -H "Accept: application/json"

# Get page 2 of starships
curl -X GET "https://swapi.dev/api/starships/?page=2" -H "Accept: application/json"
```

## 11. Best Practices
*   Cache responses locally when building applications to avoid hitting the 10,000 req/day rate limit.
*   Always check the `next` field in paginated responses to determine if more pages exist.
*   Use the `?search=` parameter server-side rather than fetching all records and filtering client-side.
*   Handle `null` and `'unknown'` values gracefully — many fields return these for incomplete data.
*   All URLs in response bodies are fully-qualified and can be used directly for linked-resource lookups.
*   Use HTTPS exclusively. The API does not support plain HTTP.

> **Read-only API:** SWAPI supports `GET` requests only. `POST`, `PUT`, `PATCH`, and `DELETE` requests will return a `405 Method Not Allowed` response.

---
