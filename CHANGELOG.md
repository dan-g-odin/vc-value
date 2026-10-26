# Changelog

All notable changes to the dataset are recorded here. Versions follow the policy in [CONTRIBUTING.md](CONTRIBUTING.md#versioning).

## [1.1.0] - 2026-10-26

- **Data correction, Initialized Capital fund split (changes values and ranks, so the next release is a minor version).** In 1.0.0 the holder-name rule credited all of Initialized's Coinbase shares to Initialized II, L.P. The Coinbase investors' rights agreement (S-1/A Ex4.2, 15 March 2021) names three Initialized vehicles: Initialized Capital Special Opportunities Fund I, L.P. among the earliest investors, and Initialized II, L.P. and Initialized Annex L.P. next to the 2018 Series E investors. The book's note abbreviated the first as "SOF I", so the rule matched only "Initialized II".
  - **Special Opportunities Fund I is Initialized's debut fund** (generation `initialized-capital--initialized-i`): the only 2012-era Initialized entity on EDGAR (Form D 0001542689-12-000001), and listed in Initialized Capital Management's Form ADV of 27 March 2026. Its display name in `fund_metrics.csv` is now the full legal name.
  - **Coinbase (`COIN`):** the $300k seed went in during 2012 and January 2013, before Initialized II's first sale on 24 May 2013 (Form D/A 0001577804-13-000002), and is about 0.66 points of the 0.8% stake. The seed share, 82.5%, now goes to Fund I (`A01143`); the Series C and E follow-ons, 17.5%, are split equally between Initialized II (`A00642`) and the Annex, which belongs to the Initialized III generation (`A01144`). No filing gives per-fund share counts; the fund ranges use 55%–91% for Fund I.
  - **Instacart (`CART`):** moved from Initialized III to Fund I (`A00641`). No filing names Initialized; the book records a 2012 seed cheque, when only Fund I existed, but the entry year was not in `entry_year`, so the no-entry rule had used the listing year less six.
  - **Weave (`WEAV`):** basis corrected to the holder name (the IRA names Initialized Capital II, L.P.); same fund, no value change.
  - **Blend (`BLND`):** holding added as known but unsized (`H2313`, allocation `A01145` to Initialized II, named in Blend's IRA of 11 January 2021). No value, so no figure changes.
  - **Effect:** Initialized Capital Special Opportunities Fund I moves from 118th to **8th** of 408 funds (34.3x consistency-adjusted, 59.3x plain; range 14.0x–57.5x). Initialized II moves from 76th to 245th and Initialized III from 377th to 366th; 206 other funds move by one place. Firm figures and the firm ranking are unchanged (Initialized stays 103rd), as is the stage-weighted companion ranking. Report version 8 (§4) still shows the old fund figures.
  - **Files:** `holdings.csv` (+1 row), `fund_allocations.csv` (3 rows changed, 3 added), `listings.csv` (`BLND` holder lines), `firms.csv` (Initialized `n_listings`), `holding_stage_weights.csv` (+1 row), `fund_metrics.csv` (Initialized rows and fund ranks).
- **Documentation:** Zenodo DOI added to the README (badge and citation), CITATION.cff and datapackage.json (all versions: 10.5281/zenodo.23455286; version 1.0.0: 10.5281/zenodo.23455287). Issue links in the README and CONTRIBUTING.md open the issue forms; the README links to Discussions; one limitations bullet reworded; the release procedure covers browser uploads of hidden files and Zenodo set-up. No data changed.

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
