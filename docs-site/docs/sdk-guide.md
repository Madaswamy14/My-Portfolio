---
sidebar_position: 5
---

# SDK Guide

SDK documentation should help developers move from installation to a working implementation with as little friction as possible.

## Install

```bash
npm install swapi-sdk-example
```

## Initialize the client

```ts
import {createClient} from 'swapi-sdk-example';

const client = createClient({
  apiToken: process.env.SWAPI_API_TOKEN,
});
```

## Make a call

```ts
const person = await client.people.getById(1);

console.log(person.name);
```

## What a strong SDK guide includes

- install and environment setup
- authentication handoff
- first successful request
- error-handling expectations
- links back to the API reference for deeper detail