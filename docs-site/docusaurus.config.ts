import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: 'Madaswamy Developer Portal',
  tagline:
    'A Stripe-style documentation portfolio showing onboarding case studies, workflow tutorials, API reference systems, and developer portal architecture.',
  favicon: 'img/favicon.ico',
  future: {
    v4: true,
  },
  url: 'https://madaswamy14.github.io',
  baseUrl: '/My-Portfolio/developer-portal/',
  trailingSlash: false,
  organizationName: 'madaswamy14',
  projectName: 'My-Portfolio',
  onBrokenLinks: 'throw',
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },
  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          exclude: [
            '**/_*.{js,jsx,ts,tsx,md,mdx}',
            '**/*.test.{js,jsx,ts,tsx}',
            '**/__tests__/**',
            '**/node_modules/**',
          ],
          editUrl:
            'https://github.com/madaswamy14/My-Portfolio/tree/main/docs-site/',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],
  themeConfig: {
    image: 'img/docusaurus-social-card.jpg',
    colorMode: {
      defaultMode: 'dark',
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'Developer Portal',
      logo: {
        alt: 'Developer Portal Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          to: '/docs/intro',
          position: 'left',
          label: 'Overview',
        },
        {
          href: 'https://madaswamy14.github.io/My-Portfolio/portfolio.html',
          label: 'Portfolio',
          position: 'right',
        },
        {
          href: 'https://github.com/madaswamy14',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Overview',
              to: '/docs/intro',
            },
            {
              label: 'Documentation Samples',
              to: '/docs/documentation-samples',
            },
            {
              label: 'Jira Getting Started',
              to: '/docs/jira-getting-started',
            },
            {
              label: 'Facebook Quickstart Guide',
              to: '/docs/facebook-events-quickstart',
            },
            {
              label: 'SWAPI API Reference',
              to: '/docs/swapi-api-reference',
            },
          ],
        },
        {
          title: 'More',
          items: [
            {
              label: 'Portfolio Homepage',
              href: 'https://madaswamy14.github.io/My-Portfolio/portfolio.html',
            },
            {
              label: 'GitHub Profile',
              href: 'https://github.com/madaswamy14',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Madaswamy. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
