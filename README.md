# My Portfolio — Madaswamy

> **Technical Writer & Developer Experience Engineer**
> A curated portfolio showcasing documentation samples, developer portal architecture, API references, onboarding guides, and documentation tooling — all built and deployed as a live GitHub Pages site.

🌐 **Live Site:** [madaswamy14.github.io/My-Portfolio](https://madaswamy14.github.io/My-Portfolio/portfolio.html)
📚 **Developer Portal:** [madaswamy14.github.io/docs-site](https://madaswamy14.github.io/My-Portfolio/developer-portal/)

---

## Overview

This repository is a professional portfolio for a Technical Writer and Developer Experience (DevEx) engineer. It demonstrates the full range of skills involved in building, publishing, and maintaining developer documentation products — from writing individual API references to architecting multi-product documentation portals with tooling and automation.

The portfolio is structured in two layers:

| Layer | Description |
|---|---|
| **Portfolio site** | A static HTML/CSS/JS site with a homepage, resume, case study cards, and freelance page |
| **Developer portal** | A Docusaurus-powered documentation product with real writing samples, structured information architecture, and a sidebar-driven navigation system |

---

## Repository Structure

```
My-Portfolio/
├── index.html                    # Portfolio landing page
├── portfolio.html                # Case study gallery
├── resume.html                   # Interactive resume
├── freelance.html                # Freelance services page
├── architecture-docs.html        # Architecture documentation page
├── styleindex.css                # Main stylesheet
├── script.js                     # Site interactivity
│
├── docs-site/                    # Docusaurus source (developer portal)
│   ├── docs/
│   │   ├── intro.md              # Developer portal overview
│   │   ├── documentation-samples.md
│   │   ├── facebook-events-quickstart.md
│   │   ├── jira-getting-started.md
│   │   ├── swapi-api-reference.md
│   │   └── acme-payments/        # Full multi-section doc case study
│   │       ├── getting-started/
│   │       ├── api/
│   │       └── concepts/
│   ├── sidebars.ts               # Navigation configuration
│   └── docusaurus.config.ts      # Site configuration
│
├── developer-portal/             # Built static output (deployed to GitHub Pages)
│
├── Portfolio/                    # Standalone HTML writing samples
│   ├── jira-getting-started.html
│   ├── swapi_API-docs.html
│   └── facebookevents_quick-start-guide.html
│
├── doc_quality_checker.py        # Automated documentation quality checker
├── openapi_docs_generator.py     # OpenAPI documentation generator
├── release_notes_generator.py    # Release notes automation script
├── screenshot_generator.py       # Screenshot automation utility
└── tests/                        # Test suite for tooling scripts
```

---

## Documentation Samples

All writing samples are available in the Docusaurus developer portal and as standalone HTML pages.

### Acme Payments Developer Platform
A full-scale developer portal case study for a fictional payments API platform. Demonstrates real-world documentation architecture across multiple sections:

- **Getting Started** — Introduction and quickstart onboarding flow
- **API Reference** — Customers, Payments, Refunds, and Webhooks endpoints with parameters, request/response schemas, and code examples
- **Concepts** — Conceptual framing to support complex integrations

### Facebook Events Quickstart Guide
A workflow-based tutorial covering the complete lifecycle of a Facebook event — from planning and publishing to promotion and post-event follow-up. Demonstrates task-based, quickstart-first documentation structure.

### Jira Getting Started Guide
A first-day onboarding guide for new Jira users covering projects, issues, and boards. Optimized for a new-user reading path with progressive disclosure and actionable next steps.

### SWAPI API Reference
A REST API reference for the Star Wars API (SWAPI). Covers endpoint definitions, URL parameters, response schemas, code examples, conventions, and troubleshooting guidance. Demonstrates structured API documentation that matches developer workflows.

---

## Developer Portal Architecture

The developer portal (`docs-site/`) is built with **Docusaurus** and deployed as a static site to GitHub Pages. Key design decisions:

- **Dark mode default** with `respectPrefersColorScheme` for accessibility
- **Sidebar-driven navigation** configured via `sidebars.ts` for scannable, hierarchical content
- **Multi-product structure** — top-level docs for standalone samples and a nested category for the Acme Payments platform
- **Edit on GitHub** deep-links on every page for transparency and open-source contribution
- **Custom CSS** for brand consistency across the portal

---

## Documentation Tooling

This repository also demonstrates tooling skills through a set of Python utility scripts:

| Script | Purpose |
|---|---|
| `doc_quality_checker.py` | Audits documentation files for quality issues — missing sections, broken links, style violations |
| `openapi_docs_generator.py` | Generates structured API reference documentation from OpenAPI specs |
| `release_notes_generator.py` | Automates release note generation from structured input |
| `screenshot_generator.py` | Automates screenshot capture for documentation use |

Each script is covered by a test suite in the `tests/` directory.

---

## Tech Stack

| Category | Technology |
|---|---|
| Portfolio site | HTML, CSS (Vanilla), JavaScript |
| Developer portal | [Docusaurus](https://docusaurus.io/) (TypeScript config) |
| Deployment | GitHub Pages |
| Tooling | Python 3 |
| Version control | Git / GitHub |

---

## Live Links

- 🏠 [Portfolio Homepage](https://madaswamy14.github.io/My-Portfolio/portfolio.html)
- 📄 [Resume](https://madaswamy14.github.io/My-Portfolio/resume.html)
- 📚 [Developer Portal](https://madaswamy14.github.io/My-Portfolio/developer-portal/)
- 💼 [Freelance Services](https://madaswamy14.github.io/My-Portfolio/freelance.html)
- 🐙 [GitHub Profile](https://github.com/madaswamy14)

---

## About

This portfolio is maintained by **Madaswamy**, a Technical Writer and Developer Experience engineer focused on API documentation, developer onboarding, and documentation system design. The repository is open for review as part of the job application process.

---

*Built with Docusaurus · Deployed on GitHub Pages · © 2026 Madaswamy*
