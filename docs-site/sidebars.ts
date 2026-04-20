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
            'acme-payments/api/refunds',
            'acme-payments/api/webhooks',
          ],
        },
        {
          type: 'category',
          label: 'Concepts',
          items: [
            'acme-payments/concepts/concepts',
          ],
        },
      ],
    },
  ],
};

export default sidebars;
