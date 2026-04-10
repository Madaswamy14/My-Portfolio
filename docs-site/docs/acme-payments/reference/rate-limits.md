---
title: Rate Limits
sidebar_position: 1
description: This guide explains the rate limits for the Acme Payments API.
---

# Rate Limits

This guide explains the rate limits for the Acme Payments API.

## What are rate limits?

Rate limits are a way to prevent abuse and ensure a fair and stable experience for all developers. They restrict the number of requests you can make to the API within a certain time period.

Rate limits are applied to each API key. If you exceed the rate limit, you will receive a 429 Too Many Requests response.


## Rate Limits Table
| Plan | Rate Limit |
| --- | --- |
| Free | 60 req/min |
| Pro | 1000 req/min |

## Best Practices

- Use retries with backoff
- Avoid unnecessary polling

## Next Steps

Start integrating in minutes:

- Go to **Quickstart** to create your first payment
- Explore **Concepts** to understand core objects
- Use **Guides** for real-world workflows
