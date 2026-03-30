---
title: SWAPI API Reference Documentation
description: A complete API reference for SWAPI, including endpoints, schemas, parameters, and code examples.
---

# SWAPI API Reference Documentation

**URL:** https://swapi.dev/api/  
**Version:** 1.0  
**Audience:** Developers & Technical Writers  

## 1. Introduction
SWAPI (The Star Wars API) is an open-source, read-only REST API that provides structured data from the Star Wars universe. It provides data on various entities, including characters, films, planets, species, vehicles, and starships. It is widely used as a learning resource for REST API consumption, documentation practice, and front-end prototyping.
This document provides a complete API reference including endpoint descriptions, request/response schemas, query parameters, error codes, and code examples.

## 2. Quick Reference

### 2.1 Base URL
The base address of Web API is "https://swapi.dev/api/".

### 2.2 Authorization
No authentication required.

### 2.3 Requests
All requests are made using the `GET` HTTP method.

### 2.4 Responses
SWAPI uses standard HTTP status codes to communicate success and failure. All responses return a JSON object with a `detail` field describing the error.

**Response Status Codes**

| Status Code | Description |
| --- | --- |
| `200` | OK - Request succeeded. Response body contains the requested data. |
| `400` | Bad Request - The request was malformed. Common causes include invalid page number or unsupported parameter. |
| `404` | Not Found -The requested resource does not exist. For example, `/api/people/9999/` |
| `500` | Internal Server Error - An unexpected server-side error occurred. Retry after a short delay. |

### 2.5 Rate Limits
The SWAPI API has a rate limit of 10,000 requests per day per IP address. If you exceed this limit, you will receive a 429 Too Many Requests response. You can check the `X-RateLimit-Remaining` header in the response to see how many requests you have left before the limit resets.

### 2.6 Pagination
Large result sets (such as listing all characters) are paginated. By default, SWAPI returns 10 records per page. A collection response includes a `count`, a `next` URL, and a `previous` URL.

## 3. Endpoints

### 3.1 Available Endpoints

| Method | Endpoint Path | Description |
| --- | --- | --- |
| GET | `/api/` | Root - lists all available resource URLs |
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

### 3.2 The Root Endpoint

The root endpoint lists all available resource URLs. It acts as the primary directory for navigation.

**Endpoint**

`GET /api/`

**Request sample**
```bash
curl -X GET "https://swapi.dev/api/" -H "Accept: application/json"
```

**Response Sample**

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

---

### 3.3 People

Retrieve data about individual characters from the Star Wars universe.

**Endpoint**

`GET /api/people/{id}/`

**Path Parameters**

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `id` | `integer` | Yes | The unique identifier for the person. For example, `1` for Luke Skywalker. |

**Query Parameters**

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `search` | `string` | No | Case-insensitive partial match on the `name` field. |
| `page` | `integer` | No | Page number for paginated list. List 10 results per page. |

**Request sample**
```bash
curl -X GET "https://swapi.dev/api/people/1/" -H "Accept: application/json"
```

**Response Schema**

| Field | Type | Description |
| :--- | :--- | :--- |
| `name` | `string` | Full name of the character |
| `height` | `string` | Height in centimetres |
| `mass` | `string` | Weight in kilograms |
| `hair_color` | `string` | Hair colour(s) separated by commas |
| `skin_color` | `string` | Skin colour(s) separated by commas |
| `eye_color` | `string` | Eye colour(s) separated by commas |
| `birth_year` | `string` | Birth year using BBY or ABY notation |
| `gender` | `string` | 'male', 'female', 'hermaphrodite', 'none', or 'n/a' |
| `homeworld` | `string` | URL of the planet resource for their home planet |
| `films` | `array[string]` | URLs of film resources this character appears in |
| `species` | `array[string]` | URLs of species resources |
| `vehicles` | `array[string]`| URLs of vehicle resources piloted |
| `starships` | `array[string]`| URLs of starship resources piloted |

**Response Sample**
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

---

### 3.4 Planets

Retrieve environmental and geographical data for Star Wars planets.

**Endpoint**

`GET /api/planets/{id}/`

**Path Parameters**

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `id` | `integer` | Yes | The unique identifier for the planet. |

**Query Parameters**

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `search` | `string` | No | Case-insensitive partial match on the `name` field. |
| `page` | `integer` | No | Page number for paginated list. List 10 results per page. |

**Request sample**
```bash
curl -X GET "https://swapi.dev/api/planets/1/" -H "Accept: application/json"
```

**Response Schema**

| Field | Type | Description |
| :--- | :--- | :--- |
| `name` | `string` | Planet name |
| `rotation_period` | `string` | Hours to complete one rotation on its axis |
| `orbital_period` | `string` | Days to complete one orbit of its local star |
| `diameter` | `string` | Diameter in kilometres |
| `climate` | `string` | Comma-separated climate types. For example, 'arid', 'temperate' |
| `gravity` | `string` | Gravitational force relative to standard. For example, '1 standard' |
| `terrain` | `string` | Comma-separated terrain types |
| `surface_water` | `string` | Percentage of planet surface covered in water |
| `population` | `string` | Average population or 'unknown' |

**Response Sample**
```json
{
  "name": "Tatooine",
  "rotation_period": "23",
  "orbital_period": "304",
  "diameter": "10465",
  "climate": "arid",
  "gravity": "1 standard",
  "terrain": "desert",
  "surface_water": "1",
  "population": "200000",
  "url": "https://swapi.dev/api/planets/1/"
}
```
---

### 3.5 Films

Metadata for Star Wars theatrical films from Episodes I–VII.

**Endpoint**

`GET /api/films/{id}/`

**Path Parameters**

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `id` | `integer` | Yes | The film episode ID or resource ID. |

**Query Parameters**

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `search` | `string` | No | Case-insensitive partial match on the `title` field. |
| `page` | `integer` | No | Page number for paginated list. List 10 results per page. |

**Request sample**
```bash
curl -X GET "https://swapi.dev/api/films/1/" -H "Accept: application/json"
```

**Response Schema**

| Field | Type | Description |
| :--- | :--- | :--- |
| `title` | `string` | The title of the film |
| `episode_id` | `integer` | The episode number from 1–7 |
| `opening_crawl` | `string` | The full opening crawl text |
| `director` | `string` | Name of the film director |
| `producer` | `string` | Comma-separated list of producers |
| `release_date` | `string` | Release date in YYYY-MM-DD format |

**Response Sample**
```json
{
  "title": "A New Hope",
  "episode_id": 4,
  "opening_crawl": "It is a period of civil war.\r\nRebel spaceships, striking\r\nfrom a hidden base, have won\r\ntheir first victory against\r\nthe evil Galactic Empire.\r\n\r\nDuring the battle, Rebel\r\nspies managed to steal secret\r\nplans to the Empire's\r\nultimate weapon, the DEATH\r\nSTAR, an armored space\r\nstation with enough power to\r\ndestroy an
  entire planet.\r\n\r\nPursued by the Empire's\r\nsinister agents, Princess\r\nLeia races home aboard her\r\nstarship, custodian of the\r\nstolen plans that can save her\r\npeople and restore\r\nfreedom to the galaxy....",
  "director": "George Lucas",
  "producer": "Gary Kurtz, Rick McCallum",
  "release_date": "1977-05-25",
  "url": "https://swapi.dev/api/films/1/"
}
```
---

### 3.6 Starships

Spacecraft capable of atmospheric and interstellar travel.

**Endpoint**

`GET /api/starships/{id}/`

**Path Parameters**

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `id` | `integer` | Yes | The unique identifier for the starship. |

**Query Parameters**

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `search` | `string` | No | Case-insensitive partial match on the `name` field. |
| `page` | `integer` | No | Page number for paginated list. List 10 results per page. |

**Request sample**
```bash
curl -X GET "https://swapi.dev/api/starships/9/" -H "Accept: application/json"
```

**Response Schema**

| Field | Type | Description |
| :--- | :--- | :--- |
| `name` | `string` | Common name of the starship |
| `model` | `string` | Model or official name |
| `manufacturer` | `string` | Manufacturer(s) |
| `cost_in_credits` | `string` | Cost in Galactic Credits |
| `length` | `string` | Length in metres |
| `max_atmosphering_speed`| `string` | Maximum speed in atmosphere (km/h), or 'n/a' |
| `hyperdrive_rating` | `string` | Class of hyperdrive (lower = faster) |
| `starship_class` | `string` | Type classification. For example, 'Star Destroyer' |

**Response Sample**
```json
{
  "name": "Death Star",
  "model": "DS-1 Orbital Battle Station",
  "manufacturer": "Imperial Department of Military Research, Sienar Fleet Systems",
  "cost_in_credits": "1000000000000",
  "length": "120000",
  "max_atmosphering_speed": "n/a",
  "hyperdrive_rating": "4.0",
  "starship_class": "Deep Space Mobile Battlestation",
  "url": "https://swapi.dev/api/starships/9/"
}
```
---

## 4. Best Practices
*   Cache responses locally when building applications to avoid hitting the 10,000 req/day rate limit.
*   Always check the `next` field in paginated responses to determine if more pages exist.
*   Use the `?search=` parameter server-side rather than fetching all records and filtering client-side.
*   Handle `null` and `'unknown'` values gracefully — many fields return these for incomplete data.
*   All URLs in response bodies are fully-qualified and can be used directly for linked-resource lookups.
*   Use HTTPS exclusively. The API does not support plain HTTP.

> **Read-only API:** SWAPI supports `GET` requests only. `POST`, `PUT`, `PATCH`, and `DELETE` requests will return a `405 Method Not Allowed` response.

---
