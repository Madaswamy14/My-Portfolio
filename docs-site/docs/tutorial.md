---
sidebar_position: 6
---

# Tutorial

Tutorials are where documentation becomes outcome-oriented. This example shows how to take a developer from setup into a simple integration story.

## Goal

Build a small character lookup flow that fetches one person and renders the returned name.

## Steps

1. Authenticate with a bearer token.
2. Request a person resource by ID.
3. Parse the response payload.
4. Render the returned value in your UI or console.

## Example flow

```ts
async function loadCharacter(id: number) {
  const response = await fetch(`https://swapi.dev/api/people/${id}`, {
    headers: {
      Authorization: `Bearer ${process.env.SWAPI_API_TOKEN}`,
    },
  });

  return response.json();
}
```

## Documentation outcome

This kind of tutorial is useful because it connects the portal's other content types:

- quickstart for initial setup
- authentication for secure requests
- API reference for endpoint detail
- SDK guide for reusable implementation patterns