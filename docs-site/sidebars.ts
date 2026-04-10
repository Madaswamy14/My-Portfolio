import type { SidebarsConfig } from '@docusaurus/plugin-content-docs';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const sidebars: SidebarsConfig = {
  portalSidebar: [
    'intro',
    'facebook-events-quickstart',
    'jira-getting-started',
    'swapi-api-reference',
    'documentation-samples',
    {
      type: 'category',
      label: 'Acme Payments Developer Platform',
      items: [
        {
          type: 'category',
          label: 'Getting Started',
          items: [
            'acme-payments/getting-started/introduction',
            'acme-payments/getting-started/quickstart',
          ],
        },
        {
          type: 'category',
          label: 'API Reference',
          items: [
            'acme-payments/api/customers',
            'acme-payments/api/payments',
          ],
        },
        {
          type: 'category',
          label: 'Guides',
          items: [
            'acme-payments/guides/accept-payments',
            'acme-payments/guides/refunds',
            'acme-payments/guides/webhooks',
          ],
        },
        {
          type: 'category',
          label: 'Concepts',
          items: [
            'acme-payments/concepts/customers',
            'acme-payments/concepts/payment-methods',
            'acme-payments/concepts/payments',
          ],
        },
        {
          type: 'category',
          label: 'Reference',
          items: [
            'acme-payments/reference/errors',
            'acme-payments/reference/rate-limits',
          ],
        },
      ],
    },
  ],
};

export default sidebars;
