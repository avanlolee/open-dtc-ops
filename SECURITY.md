# Security Policy

`open-dtc-ops` is a local CSV analysis toolkit. It does not store private seller data, run scraping, or automate marketplace logins.

## Supported Versions

Security fixes are considered for the latest released version and the current `main` branch.

| Version | Supported |
| --- | --- |
| 0.1.x | Yes |

## Reporting a Vulnerability

Please report suspected security issues privately by emailing the primary maintainer listed in `MAINTAINERS.md`.

Include:

- A short description of the issue.
- Steps to reproduce.
- The affected command or module.
- Whether private CSV data could be exposed or modified.

The maintainer will acknowledge reports within 7 days when possible and will coordinate a fix before public disclosure.

## Security Scope

In scope:

- Unsafe file handling.
- Accidental private data exposure.
- Dependency vulnerabilities that affect normal CLI usage.
- Formula or validation bugs that could materially mislead operators.

Out of scope:

- Requests to add scraping, credential handling, browser automation, or private data storage.
- Issues caused by modified local environments outside the project.
