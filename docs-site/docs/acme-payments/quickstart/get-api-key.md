---
title: Get an API Key
description: Generate sandbox credentials for your first Acme Payments integration.
---

# Get an API Key

Use a sandbox API key to test the Acme Payments API safely.

## 1. Before you begin

Before making API calls, ensure you have completed the following prerequisites:

1. **Create a Developer Account**: Sign up or log into the Acme Developer Dashboard.
2. **Switch to Sandbox Mode**: Toggle the environment switch at the top right of your dashboard to ensure you aren't using live production data.
3. **Create an Application**: In the dashboard, configure an application named `dev-portal-demo` to logically group your API keys and webhook endpoints.

## 2. Generate credentials

Acme Payments provides two types of API keys: **Secret Keys** (for backend servers) and **Publishable Keys** (for frontend integrations like Stripe Elements). For this quickstart, we need a Secret Key.

1. Open the Developer Dashboard and navigate to **Developers > API Keys**.
2. Select **Create secret key**.
3. Copy the secret key and store it securely in your secret manager or backend environment variables. For example, in a `.env` file.

> **Note:**
> Test mode secret keys look like this: `sk_test_51ABCxyz...`
> Live mode secret keys look like this: `sk_live_51ABCxyz...`

> **Warning:**
> You will only be able to view the secret API key once. If you lose it, you will need to roll the key and generate a new one.

## 3. What success looks like

You should have a sandbox secret key stored safely in your development environment, ready to send in the `Authorization` header of your API requests.

```bash
Authorization: Bearer sk_test_51ABC123XYZ
```

## 4. Next step

Use the key in [Accept Your First Payment](./first-payment.md) or [Make Your First API Call](./first-api-call.md).
