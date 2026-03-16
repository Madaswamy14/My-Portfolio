import type {ReactNode} from 'react';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';

import styles from './index.module.css';

const capabilityCards = [
  {
    title: 'Quickstart flow',
    description:
      'A first-run setup sequence designed to help developers reach value with minimal friction.',
  },
  {
    title: 'Authentication guidance',
    description:
      'Clear token, header, and security patterns written in the style hiring teams expect from DevEx writers.',
  },
  {
    title: 'API reference model',
    description:
      'Endpoint structure, request examples, response detail, and error handling organized like a real platform reference.',
  },
];

const docCards = [
  {
    title: 'Quickstart',
    description: 'Start here for the fastest path from account setup to a successful first request.',
    to: '/docs/quickstart',
  },
  {
    title: 'Authentication',
    description: 'See how bearer tokens, headers, and security guidance are documented for implementation use.',
    to: '/docs/authentication',
  },
  {
    title: 'API Reference',
    description: 'Review endpoint patterns, parameters, example payloads, and error responses.',
    to: '/docs/api-reference',
  },
  {
    title: 'SDK Guide',
    description: 'Show how SDK onboarding, install flows, and reusable examples can be structured.',
    to: '/docs/sdk-guide',
  },
];

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();

  return (
    <header className={styles.heroBanner}>
      <div className={`container ${styles.heroInner}`}>
        <div>
          <p className={styles.eyebrow}>Developer Platform Documentation System</p>
          <Heading as="h1" className={styles.heroTitle}>
            {siteConfig.title}
          </Heading>
          <p className={styles.heroSubtitle}>{siteConfig.tagline}</p>

          <div className={styles.buttonRow}>
            <Link className="button button--primary button--lg" to="/docs/intro">
              View portal overview
            </Link>
            <Link className="button button--secondary button--lg" to="/docs/quickstart">
              Open quickstart
            </Link>
            <Link
              className="button button--secondary button--lg"
              href="https://madaswamy14.github.io/My-Portfolio/index.html">
              Back to portfolio
            </Link>
          </div>
        </div>

        <div className={styles.heroPanel}>
          <p className={styles.panelLabel}>Included documentation surfaces</p>
          <ul className={styles.panelList}>
            <li>API reference architecture</li>
            <li>Authentication guidance</li>
            <li>SDK onboarding examples</li>
            <li>Tutorial-style implementation flow</li>
          </ul>
        </div>
      </div>
    </header>
  );
}

export default function Home(): ReactNode {
  const {siteConfig} = useDocusaurusContext();

  return (
    <Layout
      title={siteConfig.title}
      description="Docusaurus-based developer portal portfolio with quickstarts, auth docs, API reference structure, and SDK documentation examples.">
      <HomepageHeader />
      <main className={styles.mainContent}>
        <section className="container">
          <div className={styles.sectionHeader}>
            <p className={styles.sectionKicker}>Portal proof</p>
            <Heading as="h2">A docs system built for DevEx hiring managers</Heading>
            <p>
              This portal demonstrates how I structure developer documentation products: landing experience,
              task-based docs, reference architecture, and implementation-oriented writing.
            </p>
          </div>

          <div className={styles.cardGrid}>
            {capabilityCards.map((card) => (
              <article key={card.title} className={styles.surfaceCard}>
                <Heading as="h3">{card.title}</Heading>
                <p>{card.description}</p>
              </article>
            ))}
          </div>
        </section>

        <section className={`container ${styles.docsSection}`}>
          <div className={styles.sectionHeader}>
            <p className={styles.sectionKicker}>Core docs</p>
            <Heading as="h2">Explore the initial documentation set</Heading>
          </div>

          <div className={styles.cardGrid}>
            {docCards.map((doc) => (
              <article key={doc.title} className={styles.surfaceCard}>
                <Heading as="h3">{doc.title}</Heading>
                <p>{doc.description}</p>
                <Link className={styles.inlineLink} to={doc.to}>
                  Open {doc.title}
                </Link>
              </article>
            ))}
          </div>
        </section>
      </main>
    </Layout>
  );
}
