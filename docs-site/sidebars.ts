import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */
const sidebars: SidebarsConfig = {
  portalSidebar: [
    'intro',
    'documentation-samples',
    {
      type: 'category',
      label: 'Acme Payments Developer Platform',
      items: [
        'acme-payments/intro',
        {
          type: 'category',
          label: 'Quickstart',
          items: [
            'acme-payments/quickstart/get-api-key',
            'acme-payments/quickstart/first-payment',
            'acme-payments/quickstart/first-api-call',
          ],
        },
        {
          type: 'category',
          label: 'Authentication',
          items: ['acme-payments/authentication/overview'],
        },
        {
          type: 'category',
          label: 'API Reference',
          items: [
            'acme-payments/api-reference/overview',
            'acme-payments/api-reference/create-customer',
            'acme-payments/api-reference/create-payment',
            'acme-payments/api-reference/list-payments',
            'acme-payments/api-reference/retrieve-payment',
            'acme-payments/api-reference/create-refund',
          ],
        },
        {
          type: 'category',
          label: 'Tutorials',
          items: ['acme-payments/tutorials/build-payment-app'],
        },
        {
          type: 'category',
          label: 'Developer Journey',
          items: [
            'acme-payments/developer-journey/overview',
            'acme-payments/developer-journey/onboarding',
            'acme-payments/developer-journey/first-payment',
            'acme-payments/developer-journey/webhooks',
            'acme-payments/developer-journey/error-handling',
            'acme-payments/developer-journey/monitoring-observability',
            'acme-payments/developer-journey/production-checklist',
          ],
        },
        {
          type: 'category',
          label: 'Webhooks',
          items: ['acme-payments/webhooks/handling-webhooks'],
        },
        {
          type: 'category',
          label: 'Concepts',
          items: [
            'acme-payments/concepts/idempotency',
            'acme-payments/concepts/error-handling',
          ],
        },
        {
          type: 'category',
          label: 'Architecture',
          items: ['acme-payments/architecture/developer-portal-architecture'],
        },
        'acme-payments/devex-design',
      ],
    },
    {
      type: 'category',
      label: 'Documentation Case Studies',
      items: [
        'facebook-events-quickstart',
        'jira-getting-started',
        'swapi-api-reference-sample',
      ],
    },
    {
      type: 'category',
      label: 'Developer Portal System',
      items: ['quickstart', 'authentication', 'api-reference', 'sdk-guide', 'tutorial'],
    },
  ],
};

export default sidebars;
