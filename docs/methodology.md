# Methodology

This page explains how the dataset was built and how the derived figures are computed. It reproduces the method section of the [analysis report](report/value_per_dollar_report_v8.md) (version 8, 18 October 2026), adds the mapping from concepts to columns, and summarises the robustness checks. The judgments behind specific firms' figures are in the report's sections on [how firm the order is](report/value_per_dollar_report_v8.md#7-how-firm-is-the-order) and on [coverage and attribution checks](report/value_per_dollar_report_v8.md#8-coverage-and-attribution-checks-versions-7-and-8).

## From concepts to columns

| Concept | Where it is in the data |
|---|---|
| Value V (primary value at the end date) | `holdings.primary_value_counted_usd_bn`, summed in `firm_metrics.value_primary_usd_bn` |
| Stake | `holdings.stake_pct` (with `stake_pct_low`, `stake_pct_high`) |
| Primary share | `holdings.primary_share` (with low and high cases, `primary_evidence`) |
| Vehicles outside capital at risk | `holdings.inside_capital_at_risk_share` |
| Company value at the end date | `listings.value_end_usd_bn` = shares × split factor × price ÷ ADS ratio |
| Capital at risk K | `fund_vehicles.capital_at_risk_usd_m` = `committed_usd_m` × `timing_weight` (in-scope vehicles), summed in `firm_metrics.capital_at_risk_usd_bn` |
| Timing weight w(vintage, strategy) | `timing_weights.csv`, built from `lag_distributions.csv` and `strategy_parameters.csv` |
| Headline and its components | `firm_metrics`: `value_per_dollar`, `value_per_dollar_beyond_largest`, `consistency_adjusted_value_per_dollar` |
| Ranges and rank ranges | `firm_metrics`: `adjusted_low`, `adjusted_high`, `rank_range_best`, `rank_range_worst` |
| Alternative specifications | `firm_robustness.csv` with `specifications.csv` |
| Annualised measure | `firm_metrics`: `direct_alpha_vs_qqq_adjusted`, `pme_vs_qqq_adjusted`, `direct_alpha_vs_median_firm`; prices in `benchmark_prices.csv` |
| Fund-level split of a stake | `fund_allocations.csv` (`share_of_firm_stake`, `primary_fraction`, `basis`) |
| Fund-level measure | `fund_metrics.csv`, generations in `fund_generations.csv` |
| Venture funds' stake in a company | `listing_venture_summary.csv`, using `firms.counts_as_venture_fund` |
| Stage-weighted companion ranking | `holding_stage_weights.csv`, `stage_weighted_rankings.csv` |

The headline figures (V, K, value per dollar, value beyond the largest company and the consistency-adjusted figure) can be recomputed from the core tables: `scripts/validate.py` and `examples/recompute_headline.py` do so for every measured firm and fund generation. Ranges, robustness checks and the annualised measures come from the analysis code and are published as results.

## Report files and dataset tables

The analysis report refers to working files that the open dataset replaces:

| Report file | Dataset table(s) |
|---|---|
| `vc_value_creation_book_v17.csv` | `data/core/holdings.csv`, `data/derived/holding_stage_weights.csv`, `data/core/listings.csv` |
| `vc_fund_histories_v7.csv` | `data/core/fund_vehicles.csv`, `data/core/fund_generations.csv` |
| `vc_value_per_dollar_ranking_v8.csv` | `data/derived/firm_metrics.csv`, `data/derived/firm_robustness.csv` |
| `vc_fund_ranking_v8.csv` | `data/derived/fund_metrics.csv` |
| `vc_fund_attribution_v8.csv` | `data/core/fund_allocations.csv` |
| `vc_top20_companies_v8.csv` | `data/derived/listing_venture_summary.csv` (ranks 1 to 20) |
| `vc_conviction_weighted_ranking_v17.csv` | `data/derived/stage_weighted_rankings.csv` |
| `vc_gap_register_v16_final.csv` | `data/reference/coverage_register.csv` |

Differences from the working files: stable identifiers replace names as keys; yes/no codes are normalised (`led_round`, `board_seat_at_listing`, `secondary_noted`, with the original wording in `*_detail` columns); the internal change-code column is dropped and references to internal research files are removed (some notes still name the book version in which a value changed, such as "v14 G1"); capital at risk and timing weights are recomputed at full precision; holder lines of natural persons are left out.

## Robustness checks in brief

`firm_robustness.csv` gives each ranked firm's rank and headline under 21 specifications: the main one, 19 alternatives and the ex-SpaceX view (`main`, `depth_weight_one_fifth`, `depth_weight_half`, `depth_beyond_two_largest`, `weight_value_by_entry_stage`, `lags_two_years_longer`, `box_weights_2004_2020`, `no_weight_floor`, `pooled_lag_distribution`, `lags_one_year_shorter`, `include_sensitivity_funds`, `deduct_life_sciences_share`, `slower_deployment`, `low_confidence_sizes_x0_7`, `low_confidence_sizes_x1_3`, `us_and_global_funds_only`, `ipo_market_timing`, `faster_deployment`, `sequoia_global_growth_half`, `keep_sequoia_global_equities_heritage`, `ex_spacex`). Three test the form of the consistency adjustment, sixteen test capital at risk and the numerator, and the ex-SpaceX view answers a different question. `specifications.csv` gives each one's rank correlation with the main ranking (0.947 or more for the 19 alternatives). The rank range in `firm_metrics` is the best and worst rank across a firm's input range and the 19 alternatives.

## The method in full

### 10.1 The measure

`adjusted value per dollar = (1 + V ÷ K)^(2/3) × (1 + (V − V_top) ÷ K)^(1/3) − 1`

where:
- `V = Σ (stake % × company value at 2 October 2026 × primary share)` over the firm's listings;
- `V_top` is the value of its largest company;
- `K = Σ (fund commitment × w(vintage, strategy))` is its capital at risk.

1. **The stake.** These are the shares each firm's funds held going into the listing, as a percentage of all shares outstanding after the offering (for SPAC mergers, after the closing).
2. **Held in perpetuity to a fixed end date.** The stake is valued at the close on 2 October 2026, restated for every split since listing. Sales at or after the listing do not reduce it, and nothing after the end date is reflected.
3. **Primary capital only.** Only shares the firm bought from the company count, because only that money went to building it. Excluded:
   - shares bought from founders, employees or other investors;
   - shares received in mergers.
4. **Capital at risk.** The commitments of the firm's in-scope funds, each weighted by the share of its eventual listings expected to fall in the window ([§10.7](#107-capital-at-risk)).
5. **The consistency adjustment.**
   - The headline is a weighted geometric mean of (1 + value per dollar) and (1 + value per dollar beyond the largest company), minus 1, with weights of two-thirds and one-third. It counts mainly how much value the firm created per dollar, and partly how much it created beyond its single biggest success.
   - Version 5 weighted the two equally. Odin judged that too harsh, because in venture one outstanding company often carries a firm, while still wanting the measure to recognise firms that rest on one company. A one-company firm keeps (1 + value per dollar)^(2/3) − 1 instead of √(1 + value per dollar) − 1: 25x becomes 7.8x rather than 4.1x.
   - Adding 1 keeps a one-company record above zero, so a concentrated bet that works is still rewarded.
   - The adjustment is measured on companies rather than funds, because a firm's funds often hold the same company. Lowercase's second fund, for example, also held Uber.
   - The weight on depth and the definition of depth are tested in [report §7](report/value_per_dollar_report_v8.md#7-how-firm-is-the-order).
   - The same measure ranks individual funds in [report §4](report/value_per_dollar_report_v8.md#4-the-20-funds-with-the-most-value-per-dollar) ([§10.12](#1012-fund-level-measure)).

No entry-stage weight is applied; weighting by stage is one of the robustness checks ([report §7](report/value_per_dollar_report_v8.md#7-how-firm-is-the-order)).

### 10.2 Universe

- **Listings (unchanged since version 5).** The universe is 424 US venture-backed listings between 24 January 2014 and 12 June 2026, excluding life sciences (biotech and pharma, medical devices, healthcare services):
  - the 396 in Odin's IPO inputs dataset;
  - 11 SPAC mergers added in version 4;
  - 17 omitted listings added in version 5.
- **The version 5 additions** are every venture-backed, non-life-sciences listing (IPO, ADR offering or direct listing) in the window that the dataset omits and that is worth $2bn or more on its listing-day share count at the 2 October 2026 close or its takeout price:
  - Pinduoduo ($83.5bn), Anaplan ($7.8bn), Luckin ($7.7bn), CAVA ($6.2bn), Avalara ($6.1bn), MuleSoft ($5.6bn), EquipmentShare ($4.6bn), Atour ($4.2bn) and Coupa ($3.9bn);
  - NIO ($3.5bn), Pluralsight ($3.0bn), RLX ($2.7bn), SendGrid ($2.2bn), GigaCloud ($2.2bn), Ethos ($2.1bn), Cloudera ($2.0bn) and Chagee ($2.0bn).
- **How they were found.**
  - An EDGAR full-text search of final prospectuses (424B4 and 424B1) from January 2014 to June 2026, run period by period with SPACs filtered out.
  - A candidate list from earlier work, and published lists of the largest venture-backed and Chinese ADR offerings.
  - A check of each name against the dataset by ticker and company name.
  - The search misses some prospectuses (it missed Avalara, which was on the candidate list), so a few omitted listings may remain.
- **Not added:**
  - **Below $2bn:** Peloton ($1.4bn), Sprinklr ($1.3bn), Sumo Logic, SurveyMonkey, ForeScout and Sweetgreen, and the SPAC mergers below the version 4 line (QuantumScape, D-Wave, Rigetti and others).
  - **No or doubtful venture backing:** listings worth $2bn or more backed only or mainly by buyout, growth-equity, family or corporate investors, such as Carvana, GoDaddy, BBB Foods, Zeta and Sportradar.
- **Coverage.** 418 listings have at least one identified holder in the book, 325 of them a core venture firm. Together they are worth about $5.7 trillion at 2 October 2026 prices, on their listing-day share counts.
- **Share counts.** Post-offering share counts (all economic classes) come from the dataset, reconciled to each prospectus, or for added listings from the final prospectus or closing filing.

### 10.3 How stakes are measured

- **Source:** the shares held going into the IPO, as-converted, from the final prospectus (424B4, 424B1) principal-holder table.
  - Forms 3 and 4, Schedules 13G and 13D, Form 13F and investors' rights agreements fill gaps.
  - For the version 5 listings, whose prospectuses are too long to read in full by machine, the stakes come from Forms 3 filed at pricing (US issuers), Schedules 13G and 13D, Form 13F, share-purchase, shareholders' and investors' rights agreements, and press. Where possible, exact counts were confirmed by full-text search of the prospectus.
- **Version 7 additions ([report §8](report/value_per_dollar_report_v8.md#8-coverage-and-attribution-checks-versions-7-and-8)),** in order of preference:
  - **Directors' Form 3s** filed at the listing, which give exact counts for funds tied to a director (Revel in The Trade Desk, Walden in Credo, RPM in Firefly).
  - **13F counts inside the lock-up,** when locked-up shares were reported, or the first 13F after an early release, grossed up for the shares released (IA Ventures in Datadog).
  - **Investor-agreement schedules,** which name the share series each holder bought.
  - **Residuals by series:** the shares of a series not held by named holders, shared among the remaining investors.
  - **Round arithmetic:** cheque sizes at each series' issue price, with low and high cases.
- **SPAC mergers:** the shares held immediately after closing, as a percentage of all shares then outstanding.
  - Shares bought in the closing placement or in the SPAC's IPO are excluded.
  - Unvested or unissued earnout and sponsor shares are excluded from both the holding and the share count.
- **Not adjusted:** shares sold into the offering and distributions to fund investors around the listing.
- **Excluded:** shares bought in the IPO or a concurrent placement.
- **Funds only:** partners' personal holdings are excluded wherever the filings separate them (in version 7, Tim Draper's Box and Twilio shares, Steve Jang's Coinbase shares and Mitch Kapor's Twilio shares; in version 8, Peter Thiel's Affirm shares). Shares of other investors filed with a firm's block are removed too (in version 8, Stanford's shares in Emergence's Zoom block and the shares of Tim Draper's separate Draper Associates vehicles in DFJ's Redfin and PubMatic blocks).
- **Stakes below the 5% disclosure threshold.** 255 positions known from filings or press (205 in ranked firms) are sized with a low and a high estimate. They supply 9% of the ranked firms' primary value.

### 10.4 Valuation and the end date

- **Performance end date.** Every value is measured at the close on Friday 2 October 2026 and held there. The end date is the same for every firm, listing and benchmark, and later versions keep it unless Odin decides otherwise ([report §13](report/value_per_dollar_report_v8.md#13-decisions)).
- **Company value at the end date** = the listing-day share count × the split factor × the 2 October 2026 close. For ADS issuers, the price per ADS is converted by the ADS ratio.
- **Acquired companies** are valued at the consideration per share at completion, cash or stock. Version 5 corrected four takeout values:
  - **GrubHub:** $60.12 (0.6710 Just Eat Takeaway shares), not the price of one ADS.
  - **Hortonworks:** $13.53 (1.305 Cloudera shares on the completion date).
  - **Markit:** $106.62 (0.2838 S&P Global shares when S&P acquired IHS Markit).
  - **Coupons.com:** $4.00 (taken private in 2023). It had carried Coupa Software's $81 takeout, because both used the ticker COUP.
- **Luckin,** delisted from Nasdaq in 2020, is valued at its over-the-counter close. Payoneer, whose sale to Nuvei had not closed on 2 October, is valued at its $7.15 close.
- There is no adjustment for dilution or distributions after listing.

### 10.5 Primary versus secondary capital

- **Grading.** Each position is graded from filings and press:
  - primary confirmed (a filing names the firm as a buyer of newly issued stock);
  - primary likely (reliable press names it as a round investor);
  - mostly secondary;
  - not established.
- **Quantified secondary portions are removed:**
  - Altos Ventures: 43.5% of its Roblox stake (tender-offer SPVs).
  - Quiet Capital: 29.4% of its Reddit stake.
  - OMERS Ventures: about 50% of its Shopify stake.
  - Lowercase: 25% of its Uber stake (Industry Fund II-A, see [report §7](report/value_per_dollar_report_v8.md#7-how-firm-is-the-order)).
  - Pinduoduo: Banyan 43% and HongShan 31% (shares transferred from or issued against the founder's holding).
  - Version 5 listings: Meritech 56% and NEA 28% of MuleSoft (NEA's Series A shares were bought from Morgenthaler); Foundry 10.5%, Bessemer 11.8% and Bain Capital Ventures 7.3% of SendGrid; Battery 6% of Coupa and 5% of Avalara. Greenspring's MuleSoft stake and Coatue's Anaplan block were mostly or wholly bought from holders.
  - **Version 7:** DFJ 20% of SpaceX (60%–90% primary); Index 12.8% of ServiceTitan (common and Series A-1 bought from holders); Redpoint 5% of Twilio; Inspiration Ventures 50% of UserTesting (33%–100% primary). General Catalyst's GitLab block (bought in the 2020–21 employee tender), K5 Global's SpaceX shares outside its four named vehicles, Battery's Airbnb and Confluent lots, IVP's Uber lot, Kaszek's later Nubank block and Glynn's later Dropbox and Tenable purchases score zero, and March Capital's KnowBe4 shares are excluded.
  - **Version 8** (from the fund-level filings, [report §8](report/value_per_dollar_report_v8.md#8-coverage-and-attribution-checks-versions-7-and-8)): Pelion 10.5% of Cloudflare; Index 7.5% of Datadog and 5.5% of Figma; Andreessen Horowitz 18.6% of Coinbase and 6.8% of Navan (5.0% before); Lightspeed 10.2% of Rubrik; Benchmark 8.8% of Uber; Accel 34.6% of Etsy, 10.3% of UiPath and 0.9%–10.5% of its CrowdStrike, Tenable, ForgeRock, Couchbase and Varonis stakes; Union Square Ventures 5.1% of Etsy; Sequoia 1.0% of Airbnb, 8.0% of Instacart and 33% of Figma (6.7% and 30% before). JVP's CyberArk primary share is raised from 50% to 83% (66%–100%).
- **SpaceX.** Each holder's June 2026 13F or 13G stake was split into blocks by vehicle and matched to SpaceX's primary rounds, tender offers and the xAI merger. Each block counts by its probability of having been bought from SpaceX; merger stock counts zero (version 4). DFJ's stake, for which no filing exists, is treated as in [report §7](report/value_per_dollar_report_v8.md#7-how-firm-is-the-order).
- **Zero scores.** Positions that came from a merger score zero, as do positions whose origin could not be established. Some of these count in the high case only (Mithril's December 2012 Palantir shares, HongShan's Didi stake).

### 10.6 Attributing holdings and firm types

- **Combining vehicles.** All funds and vehicles a firm controls are combined: flagship, growth, opportunity and select funds, SPVs and evergreen vehicles.
  - DFJ Growth's stakes (Anaplan, SpaceX, Coinbase, Unity) and DFJ Fund X's Twilio stake belong to DFJ, whose fund file holds the DFJ venture, DFJ Growth and Threshold funds.
  - Gaorong Capital is Banyan Partners under a later name and is merged with it. Version 7 merges Bullet Time Ventures into Techstars Ventures, Sherpa Capital into ACME Capital and Pacven Walden into Walden International.
- **Separate firms.**
  - **Separately managed franchises:** Sequoia, HongShan and Peak XV; Lightspeed and Lightspeed China; Matrix Partners and Matrix China; GV and CapitalG.
  - **Corporate vehicles:** mFund, which held Pinduoduo, is a NetDragon-run vehicle, not part of IDG Capital.
  - **Personal vehicles:** Tim Draper's Draper Associates L.P. and Riskmasters are kept apart from DFJ and from Draper Associates, the fund manager.
- **Who is ranked.** Independent venture managers: firms that invest pooled capital from outside investors through limited-partnership funds, mainly in private technology companies, including managers that also use single-company vehicles alongside pooled funds (Romulus). Gigafund, whose vehicles are concentrated in SpaceX, is kept pending review.
- **Listed separately ([report §6](report/value_per_dollar_report_v8.md#6-firms-not-ranked)):**
  - family offices and individuals;
  - corporate and pension venture arms;
  - the thirteen firms Odin identified;
  - firms that fail the same test, whether energy private equity, regional generalist syndicates, consumer investors, public economic-development funds, single-company syndicates or sponsor-funded vehicles.
- **Not scored:** holders with no fund history, either because they invest their principals' or members' own money (angel groups, family vehicles, personal trusts) or because their fund sizes could not be found ([report §6](report/value_per_dollar_report_v8.md#6-firms-not-ranked), [§10.8](#108-coverage-and-screening)).
- **Not measured per dollar:** growth, crossover and hedge funds. They appear in the companion stage-weighted file (Layer 2).

### 10.7 Capital at risk

- **Fund histories.** 3,422 vehicles for 180 firms, of which 3,041 are in scope.
  - **Sources:** EDGAR Form D filings, Form ADV private-fund data, firm and press announcements of final closes, public pension reports, SEC filings that name funds, and database profiles checked against press.
  - **Fields:** each vehicle records vintage, committed capital, strategy, mandate, geography, scope, estimated life-sciences share, source and confidence.
  - **New in version 7:** fund histories for 51 firms, and RPM's BGW Ventures IV ($40m).
  - **New in version 8:** Lowercase's RT fund in scope and its sidecar counted at its Slack cheque ($7.5m, low confidence); the corrected fund sizes and added vehicles listed in [report §8](report/value_per_dollar_report_v8.md#8-coverage-and-attribution-checks-versions-7-and-8).
- **In scope:** closed-end venture and growth funds under the firm's brand and their side vehicles, including non-US funds of the same brand.
- **Excluded:**
  - dedicated life-sciences funds;
  - public-equity, crossover, hedge and public/private hybrid funds;
  - fund-of-funds and wealth vehicles;
  - feeders, credit funds and continuation vehicles;
  - vehicles that hold only merger stock.
- **Sensitivity only:**
  - renminbi funds and crypto funds;
  - vehicles whose purpose is unclear;
  - vehicles that bought existing shares (secondaries), such as Lowercase's two Industry Fund vehicles.
- **Estimated deployment.** Capital without a fund series is measured as estimated capital deployed per year.
  - **Firms concerned:** Sutter Hill (revised in version 5, [report §7](report/value_per_dollar_report_v8.md#7-how-firm-is-the-order)), RTP's proprietary capital, SAP Ventures before it became Sapphire, Y Combinator's standard deals, EPIC Ventures, Zeev Ventures' early years, SV Angel's partner-money vehicles and the family offices in [report §6](report/value_per_dollar_report_v8.md#6-firms-not-ranked).
  - **Ranges:** low-confidence rows carry a low-to-high range.
- **Timing weights:**
  - **Lags.** Lags from a firm's entry to listing were estimated from 554 entry-to-listing pairs in the book, corrected for observing listings only in 2014–2026 (Efron–Petrosian double-truncation estimator, smoothed with gamma and lognormal fits). Median lags are 7 years for seed and Series A entries, 5 for Series B and C, and 3 for Series D and later. Later additions were not used to re-estimate the lags.
  - **Deployment.** Funds are assumed to deploy over 5–6 years (venture) or 4 years (growth) on a typical pacing curve.
  - **Floor.** No dollar invested in 2004 or earlier by a fund of vintage 1995 or later counts at less than 25%. Without the floor, an old fund whose one company listed late would count at only 2–10%, and a single long-lag success would produce an extreme ratio.
  - **The weight** is the share of a fund's eventual listings expected to fall inside the window:

| Vintage | 1997 | 2000 | 2003 | 2005 | 2008 | 2011 | 2014 | 2017 | 2020 | 2022 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Early-stage fund | 25% | 25% | 32% | 47% | 79% | 92% | 83% | 57% | 25% | 9% |
| Growth fund | 25% | 25% | 20% | 16% | 38% | 78% | 94% | 86% | 65% | 41% |

- **Totals.** In-scope commitments are $764bn and capital at risk $311bn, of which $291bn belongs to the ranked firms.
- **Numerator consistency.** Positions held by vehicles outside the denominator are removed from the numerator: Sequoia Capital Global Equities and Sequoia Heritage, IDG's XPeng stake held through renminbi vehicles, Glynn's Emerging Opportunity funds, and the Li Auto stakes of Matrix China and Source Code held through renminbi vehicles.

### 10.8 Coverage and screening

- **Coverage.** The book has 396 core venture firms, of which 307 hold primary value ($848.2bn in total at 2 October 2026). The 180 firms with fund histories hold 97.1% of it.
- **Earlier versions:**
  - Version 2 covered 72 firms: the 50 largest by value created plus 22 large firms with little value in the window.
  - Version 3 screened every other firm with value against Form D totals and known fund sizes.
  - Version 4 screened the firms that gained value from the SPAC mergers and the SpaceX 13F filings.
  - Versions 5 and 6 screened the firms that gained value from the 17 added listings and wrote full fund histories for the contenders (Granite Ventures, Cathay Innovation, Romulus Capital, Highway 12 Ventures, Bay Partners, El Dorado Ventures and SWaN & Legend).
- **Version 7** searched for stakes the holder tables miss ([report §8](report/value_per_dollar_report_v8.md#8-coverage-and-attribution-checks-versions-7-and-8)) and wrote fund histories for the 51 firms whose new stakes could matter to the ranking. Smaller pooled-fund holders were screened instead (below).
- **Firms without fund histories.** 127 firms with value remain without them. They hold 2.9% of core value ($25.0bn).
  - **Screened against the top-50 line (1.38x in versions 7 and 8).** A firm whose value comes from one company reaches the line only if its value is at least 2.66 times its capital at risk. None of the pooled-fund managers without histories passes on its known fund sizes: the closest remain Origin Ventures (GrubHub; 1.0x on its documented funds) and Morgenthaler (about 0.8x), and three firms cleared in version 6 on announced fund sizes (83North, Shunwei and Northzone) stay below.
  - **Holders and candidates screened out on fund sizes:** Delta-V Capital (its 2011 fund alone puts about $32m at risk, more than the $19m that would let its Zayo stake reach the line), Liquid 2 Ventures (whose GitLab stake also sits in vehicles that predate its funds), Inspiration Ventures (central case), C&B Capital, TeleSoft Partners, Torch Capital, Four Rivers Group, Tru Arrow Partners and L1 Capital.
  - **Not scored by type:** principals', members' or family money (A-Grade, Youniversity, Amidzad, QueensBridge, SciFi, Three Kingdoms, Egan-Managed Capital, GlobalLink1, Pioneer Venture Partners, TEEC Angel Fund, Tim Draper's personal vehicles), a single-deal platform (FundersClub) and corporate capital (Seed Capital Partners, eValue). Two of these would score highly if counted: Pioneer's Avalara stake cost about $4m and TEEC's angel-club fund held $3.5m.
  - **Open:** Centillion, whose fund sizes are unknown, and the renminbi-only managers ([report §6](report/value_per_dollar_report_v8.md#6-firms-not-ranked)). Amicus Capital and IT-Farm were set aside by Odin ([report §8](report/value_per_dollar_report_v8.md#8-coverage-and-attribution-checks-versions-7-and-8)).
  - Two firms have no fund records at all: Luminari Capital (fuboTV, $30m of value; first fund 2015) and Stratim Capital (EverQuote, $41m).

### 10.9 Ranges

- **Range from estimated inputs:**
  - estimated stakes at their low and high values;
  - uncertain primary shares at their low and high cases;
  - low-confidence fund sizes doubled (low end) and halved (high end).
- **Where better ranges exist,** they replace that rule: Sutter Hill's deployment path, Contour, Altos, Celesta and Y Combinator (verification), and the screened firms' documented capital ranges. The adjusted figure is recomputed in each case, including which company is largest.
- **Gigafund:** the three readings of its SpaceX vehicles, each with matching capital at risk.
- **DFJ:** its SpaceX stake at 1.15% and 1.85%, with 60% and 90% bought from SpaceX.
- **Fund ranges ([report §4](report/value_per_dollar_report_v8.md#4-the-20-funds-with-the-most-value-per-dollar))** add the estimated splits of a firm's stake between its funds, at their low and high cases.
- **Rank range:** the best and worst of two things:
  - the firm's rank when its own figure is moved to the ends of its range and the others stay central;
  - its ranks under the 19 specifications in [report §7](report/value_per_dollar_report_v8.md#7-how-firm-is-the-order) (the ex-SpaceX view is excluded).

### 10.10 Annualised measure

- **Cash flows:** capital at risk drawn at mid-year over each fund's deployment. The terminal value is the consistency-adjusted value (headline figure × capital at risk) at the 2 October 2026 close; the unadjusted value is shown for comparison.
- **Measures:** Direct Alpha against the Nasdaq-100 price index (Gredil, Griffiths and Stucke, 2014) and the Kaplan–Schoar public market equivalent.
- **Benchmark:** Nasdaq-100 year-end closes before 2017, interpolated geometrically to mid-year, and QQQ monthly closes from 2017, ending at the 2 October 2026 close.
- **Presentation:** each firm's Direct Alpha relative to the median of the ranked firms with value.

### 10.11 Verification

- **Book.**
  - Principal-holder tables were swept for every listing with a findable prospectus, with 13F and 13G sweeps.
  - The October 2026 accuracy audit replaced 129 share counts, added 50 missing 5% holders and made 32 valuation fixes.
  - Of the ranked firms' primary value, 68% rests on high-confidence stakes, 24% on medium and 8% on low. 28% sits in positions whose primary share is a range: SpaceX (16%), positions corrected in version 8 with a range (10%, mainly Accel's CrowdStrike), Pinduoduo and smaller estimates.
  - Version 7's new stakes are graded by the width of their documented range: high when the range spans no more than 30% of the central figure, medium up to 60%, low beyond. DFJ's SpaceX stake is graded low because no filing stands behind it.
- **Version 5:** fourteen large stakes held by leading firms were re-checked against Forms 3 and 13G (all matched at the share level); Lowercase's Uber and Twilio, Founder Collective's and IA Ventures' Trade Desk and DigitalOcean stakes, First Round's Square stake and Y Combinator's estimates were re-checked; the low-confidence fund histories of Sutter Hill, Altos, Celesta, Y Combinator, Contour and Pelion were re-checked; and four takeout values were corrected ([§10.4](#104-valuation-and-the-end-date)).
- **Version 7:**
  - Each new position records its source document, method and arithmetic in the book's provenance note, and each pair the sweeps found records its outcome in the register.
  - Every research file from the cut-off runs was checked for truncated or missing output before integration; all 1,280 name-probe searches completed (14 of them through single-word fallback queries).
  - The ranking was rebuilt from the book and fund files, and the report's figures were checked against the data files by an independent review.
- **Version 8:**
  - Each fund-level split records its source filing (accession number) and arithmetic in the research files; splits that rest on estimates are flagged and carried into the fund ranges.
  - Fund totals reconcile to the firm totals: the difference is the value held in single-company vehicles and other vehicles outside any fund generation ([report §4](report/value_per_dollar_report_v8.md#4-the-20-funds-with-the-most-value-per-dollar)).
  - The firm and fund rankings were rebuilt from book v17 and fund files v17, and the report's figures were checked against the data files by an independent review.

### 10.12 Fund-level measure

- **Unit:** a fund generation, as defined in [report §4](report/value_per_dollar_report_v8.md#4-the-20-funds-with-the-most-value-per-dollar). Partners' side funds and top-up funds that take a fixed share of the generation's deals belong to it. A single-company vehicle forms its own unit and is not ranked.
- **Value:** `V_fund = Σ (company value at 2 October 2026 × firm's stake × fund's share of the firm's shares × primary fraction of the fund's shares)`.
  - Shares a filing identifies as bought from other holders score zero.
  - Where the book counts more of a firm's stake as bought from holders than the filings identify, the rest is taken first from the funds whose shares' origin is not identified, then pro rata.
- **Capital at risk:** `K_fund = Σ (commitment × w(vintage, strategy))` over the generation's in-scope vehicles, with the weights of [§10.7](#107-capital-at-risk).
- **Headline:** the consistency-adjusted value per dollar of [§10.1](#101-the-measure), computed on the fund's companies.
- **Positions without per-fund filings** go to the generation named in the holder's name where it identifies one (a fund number or year). Otherwise they go to the generation whose investment period (vintage to vintage + 6 years) covers the firm's entry year: where several overlap, the largest; for entries at Series C or later, the growth generation active then; for companies outside the US, the firm's funds for that country, or its US or global funds if it has none. With no known entry year, the listing year less six is used.
- **Look-through:** shares moved to continuation or roll-over vehicles are credited to the generation that bought them (DFJ Fund IX and DFJ Growth 2006 continuation funds, Altos Ventures IV Liquidity Fund, Sequoia Grove). Sequoia Grove's shares are credited pro rata to the Sequoia funds holding the same company.
- **Scope:** the funds of ranked firms. Evergreen and annual-deployment pools, cross-generation co-investment schemes and single-company vehicles are not ranked; their figures are given in [report §4](report/value_per_dollar_report_v8.md#4-the-20-funds-with-the-most-value-per-dollar) where notable.
