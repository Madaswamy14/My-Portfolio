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
    title: 'Getting Started Guide',
    description:
      'A task-based onboarding guide that helps new users set up Jira, learn key workflows, and reach first success faster.',
  },
  {
    title: 'API reference model',
    description:
      'Endpoint structure, request examples, response detail, and error handling organized like a real platform reference.',
  },
];

const docCards = [
  {
    title: 'Getting Started Guide',
    description: 'See how a task-based onboarding guide helps new users set up Jira, navigate workflows, and reach first success faster.',
    to: '/docs/jira-getting-started',
  },
  {
    title: 'Facebook Quickstart Guide',
    description: 'Follow a workflow-based guide for setting up Facebook, creating a profile, and managing pages and events with clear step-by-step instructions.',
    to: '/docs/facebook-events-quickstart',
  },
  {
    title: 'API Reference Overview',
    description: 'Review the Acme Payments reference overview for endpoint structure, authentication context, and implementation-ready guidance.',
    to: '/docs/acme-payments/api-reference/overview',
  },
  {
    title: 'SWAPI API Reference',
    description: 'Explore a structured REST API reference with resources, parameters, responses, and example-driven developer guidance.',
    to: '/docs/swapi-api-reference',
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
            <li>Task-based getting started guides</li>
            <li>Workflow-based quickstarts</li>
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
      description="Docusaurus-based developer portal portfolio with quickstarts, getting started guides, API reference structure, and workflow-based documentation examples.">
      <HomepageHeader />
      <main className={styles.mainContent}>
        <section className="container">
          <div className={styles.sectionHeader}>
            <p className={styles.sectionKicker}>Portal proof</p>
            <Heading as="h2">Built for DevEx hiring managers</Heading>
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
            <Heading as="h2">Explore the documentation</Heading>
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
