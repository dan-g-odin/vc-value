# Changelog

All notable changes to the dataset are recorded here. Versions follow the policy in [CONTRIBUTING.md](CONTRIBUTING.md#versioning).

## [Unreleased]

## [1.0.0] - 2026-10-18

First public release.

- **Data:** 424 listings, 792 firms and other institutional holders, 1,955 holder lines, 3,422 fund vehicles in 1,789 fund generations, 1,142 fund allocations, and benchmark prices; derived firm and fund metrics, robustness checks, company summaries and the companion stage-weighted ranking; reference tables for the method.
- **Basis:** holdings book v17 and fund files v17, the inputs to analysis report version 8 (18 October 2026). Performance end date: the close on 2 October 2026.
- **Left out of the public release:** 358 holder lines of natural persons (founders, executives and individual investors). They enter no figure.
- **Formats:** CSV tables with Frictionless Table Schemas and a Data Package descriptor; a consolidated SQLite database.
- **Tooling:** validation with recomputation of the headline figures, SQLite build, data-dictionary generation, release-metadata script, continuous integration, examples.
- **Known issues:** see [docs/limitations.md](docs/limitations.md#known-data-issues-in-version-100).

## History before the public release

The data were built in eight internal report versions between 4 and 18 October 2026: the holdings book grew from a census of prospectus holder tables (book v2) through accuracy audits, SPAC mergers and omitted listings (v13–v15), a coverage check of investor agreements and 13F filings (v16) and fund-level attribution (v17). The fund histories were built from Form D filings, fund announcements and public reports. Appendix D of the [analysis report](docs/report/value_per_dollar_report_v8.md) lists every change since report version 5.
