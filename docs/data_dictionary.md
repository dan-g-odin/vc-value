# Data dictionary

*Venture value created per dollar at risk: US venture-backed listings, 2014-2026, version 1.0.0. Generated from `datapackage.json` and `schema/*.json` by `scripts/make_data_dictionary.py`; do not edit by hand.*

All values are measured at the performance end date, the close on **2 October 2026**. Money is in US dollars (`_usd_m` millions, `_usd_bn` billions). Shares of a total are fractions from 0 to 1 unless the column ends in `_pct` (percent). Blank cells are missing values. Booleans are `true`/`false`. Dates are ISO 8601.

- **Core tables:** [`listings`](#listings), [`firms`](#firms), [`fund_generations`](#fund_generations), [`fund_vehicles`](#fund_vehicles), [`holdings`](#holdings), [`fund_allocations`](#fund_allocations), [`benchmark_prices`](#benchmark_prices)
- **Derived tables:** [`firm_metrics`](#firm_metrics), [`firm_robustness`](#firm_robustness), [`fund_metrics`](#fund_metrics), [`listing_venture_summary`](#listing_venture_summary), [`holding_stage_weights`](#holding_stage_weights), [`stage_weighted_rankings`](#stage_weighted_rankings)
- **Reference tables:** [`timing_weights`](#timing_weights), [`lag_distributions`](#lag_distributions), [`strategy_parameters`](#strategy_parameters), [`specifications`](#specifications), [`coverage_register`](#coverage_register)

## Core tables

Observations taken from filings and other sources: listings, holders, fund histories, holdings, fund splits and benchmark prices.

### listings

**Listings (the universe).** One row per US venture-backed, non-life-sciences listing from 24 January 2014 to 12 June 2026 (IPOs, ADR offerings, direct listings and SPAC mergers). Company values are for the shares outstanding at listing, held to the 2 October 2026 close.

- File: [`data/core/listings.csv`](../data/core/listings.csv) (424 rows)
- Primary key: `listing_id`

| Field | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `listing_id` | string | yes | Ticker at listing, used as the listing key throughout the dataset. | unique; pattern `^[A-Z0-9.]+$` |
| `company` | string | yes | Company name. |  |
| `listing_date` | date | yes | First trading day (IPO, ADR offering or direct listing) or SPAC merger closing date. |  |
| `listing_year` | integer | yes | Calendar year of listing_date. | min 2014; max 2026 |
| `sector` | string |  | Sector classification of the source IPO dataset (blank for two listings: see docs/limitations.md). | one of: `Software/SaaS`, `Internet/Consumer`, `Fintech`, `Transport/Mobility`, `Media/Entertainment`, `Hardware/Electronics`, `Consumer Goods`, `Energy/Climate`, `Semiconductors`, `Industrials`, `Real Estate`, `Other` |
| `offer_price_usd` | number |  | Offer price per share, or per ADS for ADS issuers; the reference price for direct listings and SPAC mergers. Unit: USD. | min 0 |
| `ads_ratio` | number |  | Ordinary shares per ADS for issuers listed through ADSs; blank otherwise. | min 0 |
| `shares_post_offering_m` | number |  | Shares outstanding after the offering, all economic classes (after closing for SPAC mergers, excluding unvested earnout and sponsor shares), reconciled to the prospectus. Unit: million shares. | min 0 |
| `split_factor` | number |  | Cumulative split factor from listing to the 2 October 2026 close (shares held at the end date per share held at listing). | min 0 |
| `price_end_usd` | number |  | Close on 2 October 2026 per share (per ADS for ADS issuers); for acquired companies, the consideration per share at completion; for companies delisted to over-the-counter markets, the OTC close. Unit: USD. | min 0 |
| `price_end_note` | string |  | How price_end_usd was set where it is not a close on the end date or a recorded takeout price (implied by the recorded company value). |  |
| `value_at_listing_usd_bn` | number |  | shares_post_offering_m x offer_price_usd / ads_ratio, in billions. Unit: USD bn. | min 0 |
| `value_end_usd_bn` | number |  | Long-term value created: shares_post_offering_m x split_factor x price_end_usd / ads_ratio, in billions, at the 2 October 2026 close. Unit: USD bn. | min 0 |
| `n_holding_lines` | integer | yes | Number of holder lines for the listing in holdings.csv. | min 0 |
| `valuation_date` | date | yes | Performance end date for every value in the row (2026-10-02). |  |

### firms

**Firms and other holders.** One row per investment firm or other institutional holder that appears in holdings.csv. Natural persons are not included. measurement_status says whether the firm is ranked on value per dollar, measured but listed separately, or not measured.

- File: [`data/core/firms.csv`](../data/core/firms.csv) (792 rows)
- Primary key: `firm_id`

| Field | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `firm_id` | string | yes | Stable identifier (lower-case slug of firm_name). | unique; pattern `^[a-z0-9-]+$` |
| `firm_name` | string | yes | Name used in the analysis. Renamed firms are merged with their predecessors (for example Bullet Time Ventures into Techstars Ventures). | unique |
| `holder_type` | string | yes | Holder category. Only core_venture firms can be ranked; for the two holders with lines of more than one type, the predominant type. | one of: `core_venture`, `growth_crossover`, `corporate_strategic`, `mutual_fund`, `hedge_fund`, `sovereign`, `family_office`, `other` |
| `measurement_status` | string | yes | ranked: in the main value-per-dollar ranking; listed_separately: measured the same way but outside the definition of an independent venture manager; not_scored_no_fund_history: core venture holder without a fund history; not_measured_holder_type: growth, crossover, hedge, mutual-fund, corporate, sovereign and other holders. | one of: `ranked`, `listed_separately`, `not_scored_no_fund_history`, `not_measured_holder_type` |
| `separate_listing_group` | string |  | For listed_separately firms, the group they are reported in: identified_by_odin (firms Odin identified as outside the standard definition), same_test (firms failing the same test), newly_measured_v7 (holders measured in report version 7), family_office_or_individual. | one of: `identified_by_odin`, `same_test`, `newly_measured_v7`, `family_office_or_individual` |
| `reason_not_ranked` | string |  | Why a measured firm is not ranked, or why a core venture holder is not scored. |  |
| `has_fund_history` | boolean | yes | True if fund_vehicles.csv holds the firm's fund history. |  |
| `counts_as_venture_fund` | boolean | yes | True if the firm's holdings count as venture funds in listing_venture_summary.csv: core venture holders less money of individuals and families (family offices, angel groups, members' deal platforms and principals' own vehicles). |  |
| `n_listings` | integer | yes | Number of listings in which the firm has a holder line. | min 1 |
| `note` | string |  | What changed for this firm across versions and key judgments behind its figures (measured firms only). |  |

### fund_generations

**Fund generations.** One row per fund generation: a main fund with the parallel, principals', entrepreneurs', annex and partners' side vehicles that invest beside it. Single-company vehicles form their own generation. This is the unit of the fund ranking.

- File: [`data/core/fund_generations.csv`](../data/core/fund_generations.csv) (1,789 rows)
- Primary key: `generation_id`
- Foreign key: `firm_id` → `firms.firm_id`

| Field | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `generation_id` | string | yes | Stable identifier: firm_id, two hyphens, and a slug of generation_label. | unique; pattern `^[a-z0-9-]+$` |
| `firm_id` | string | yes | Firm managing the generation. |  |
| `generation_label` | string | yes | Short label of the generation (for example "FF II", "Index VI"). |  |
| `vintage` | integer |  | Vintage year of the generation's main vehicle. | min 1960; max 2026 |
| `committed_usd_m` | number |  | Committed capital of the generation's in-scope vehicles. Unit: USD m. | min 0 |
| `capital_at_risk_usd_m` | number |  | Sum of capital_at_risk_usd_m over the generation's in-scope vehicles. Unit: USD m. | min 0 |
| `vehicle_roles` | string |  | Roles of the vehicles in the generation, separated by "\|". |  |
| `is_growth_generation` | boolean |  | True if the generation's largest vehicle follows a growth strategy. |  |
| `is_single_company_vehicle` | boolean |  | True for single-company vehicles (SPVs), which are not ranked. |  |
| `fund_geography` | string |  | Geographic focus used by the attribution rule (US/Global or a country). |  |
| `has_low_confidence_size` | boolean |  | True if any in-scope vehicle has a low-confidence size. |  |
| `size_confidence` | string |  | Confidence in the size of the main vehicle. | one of: `HIGH`, `MED`, `LOW` |
| `n_vehicles` | integer |  | Number of vehicles in the generation. | min 0 |
| `rankable` | boolean | yes | True if the generation can enter the fund ranking. |  |
| `not_ranked_reason` | string |  | Why a generation cannot be ranked (single-company vehicle, evergreen or annual pool, cross-generation scheme, firm listed separately, no capital at risk). |  |

### fund_vehicles

**Fund vehicles (fund histories).** One row per fund vehicle in the fund histories of 180 firms: vintage, committed capital, strategy, scope and capital at risk, with source and confidence. Capital deployed per year by firms without a fund series is recorded as one row per year.

- File: [`data/core/fund_vehicles.csv`](../data/core/fund_vehicles.csv) (3,422 rows)
- Primary key: `vehicle_id`
- Foreign key: `firm_id` → `firms.firm_id`
- Foreign key: `generation_id` → `fund_generations.generation_id`

| Field | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `vehicle_id` | string | yes | Stable identifier: firm_id, two hyphens, and a slug of fund_name. | unique; pattern `^[a-z0-9-]+$` |
| `firm_id` | string | yes | Firm managing the vehicle. |  |
| `generation_id` | string | yes | Fund generation the vehicle belongs to. |  |
| `fund_name` | string | yes | Legal or reported name of the vehicle. |  |
| `role` | string | yes | Role of the vehicle within its generation. | one of: `main`, `parallel`, `principals`, `entrepreneurs`, `annex`, `side`, `opportunity`, `spv`, `feeder`, `other` |
| `vintage` | integer | yes | Vintage year (first close or first sale). | min 1960; max 2026 |
| `is_capital_deployed_row` | boolean | yes | True for rows recording capital deployed in one calendar year (firms without a fund series); their timing weight is deployed_year_weight. |  |
| `committed_usd_m` | number |  | Committed capital (for "capital deployed" rows, capital deployed in that year). Unit: USD m. | min 0 |
| `size_basis` | string |  | How the size was established (for example formd_sold, press_final_close, implied from holdings, estimate). |  |
| `strategy` | string | yes | Investment strategy, which sets the deployment pace and stage mix used for capital at risk. | one of: `seed`, `early`, `multi`, `growth` |
| `mandate` | string |  | Mandate as researched (for example flagship, opportunity, seed, sector fund). |  |
| `geography` | string |  | Geographic mandate. |  |
| `in_scope` | string | yes | Scope in the main specification: Y in capital at risk; N excluded (life-sciences, public-equity, credit, fund-of-funds and similar vehicles); S sensitivity only (renminbi, crypto, secondary or unclear vehicles). | one of: `Y`, `N`, `S` |
| `in_scope_as_researched` | string |  | Scope as originally researched, before review. |  |
| `life_sciences_share` | number |  | Estimated share of a generalist fund invested in life sciences (used only in a sensitivity check). | min 0; max 1 |
| `size_confidence` | string |  | Confidence in committed_usd_m. Low-confidence sizes are halved and doubled in the ranges. | one of: `HIGH`, `MED`, `LOW` |
| `capital_at_risk_usd_m` | number | yes | committed_usd_m x timing_weight for in-scope vehicles; 0 otherwise. Unit: USD m. | min 0 |
| `timing_weight` | number |  | Share of the vehicle's eventual listings expected to fall inside the 2014-2026 window (see timing_weights.csv). | min 0; max 1 |
| `source_url` | string |  | Main source (EDGAR Form D, press release, filing). |  |
| `note` | string |  | Evidence and reasoning behind the size, vintage and scope. |  |

### holdings

**Holdings (holder lines).** One row per holder line: the stake an institutional holder held going into a listing, as a share of post-offering shares, with its value at the end date, the share bought from the company (primary) and provenance. Holdings of natural persons are not included.

- File: [`data/core/holdings.csv`](../data/core/holdings.csv) (1,956 rows)
- Primary key: `holding_id`
- Foreign key: `listing_id` → `listings.listing_id`
- Foreign key: `firm_id` → `firms.firm_id`

| Field | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `holding_id` | string | yes | Stable identifier of the holder line. | unique; pattern `^H[0-9]{4}$` |
| `listing_id` | string | yes | Listing. |  |
| `firm_id` | string | yes | Firm the line is attributed to (all vehicles a firm controls are combined). |  |
| `holder_as_filed` | string |  | Holder as named in the source filing. |  |
| `holder_type` | string | yes | Holder category of this line. | one of: `core_venture`, `growth_crossover`, `corporate_strategic`, `mutual_fund`, `hedge_fund`, `sovereign`, `family_office`, `other` |
| `stake_pct` | number |  | Shares held going into the listing, as-converted, as a percentage of post-offering shares (after closing for SPAC mergers); blank where the holding is known but not sized (stake_confidence KNOWN_UNSIZED). Unit: %. | min 0; max 100 |
| `stake_pct_low` | number |  | Low estimate of stake_pct where the stake is estimated. Unit: %. | min 0; max 100 |
| `stake_pct_high` | number |  | High estimate of stake_pct where the stake is estimated. Unit: %. | min 0; max 100 |
| `stake_confidence` | string |  | Confidence in stake_pct (KNOWN_UNSIZED: holding known but not sized). | one of: `HIGH`, `MED`, `LOW`, `KNOWN_UNSIZED` |
| `stake_source` | string |  | Filing or method behind stake_pct (for example a 424B4 footnote, Form 3, 13F count, round arithmetic). |  |
| `primary_evidence` | string |  | Evidence grade for whether the shares were bought from the company. | one of: `primary_confirmed`, `primary_likely`, `position_only`, `secondary_major`, `mostly_secondary`, `secondary_only`, `not_established`, `not_assessed` |
| `secondary_fraction` | number |  | Quantified share of the stake bought from other holders, where one is known. | min 0; max 1 |
| `primary_share` | number | yes | Share of the stake counted as bought from the company (primary). | min 0; max 1 |
| `primary_share_low` | number |  | Low case of primary_share where it is uncertain. | min 0; max 1 |
| `primary_share_high` | number |  | High case of primary_share where it is uncertain. | min 0; max 1 |
| `first_round` | string |  | Round of the firm's first investment in the company. |  |
| `entry_year` | integer |  | Year of the firm's first investment. | min 1980; max 2026 |
| `led_round` | string |  | Whether the firm led a round. | one of: `yes`, `no`, `co-led`, `likely`, `unknown` |
| `led_round_detail` | string |  | Detail behind led_round where recorded. |  |
| `board_seat_at_listing` | string |  | Whether the firm held a board seat at listing. | one of: `yes`, `no`, `likely`, `right_only`, `unknown` |
| `board_seat_detail` | string |  | Detail behind board_seat_at_listing where recorded. |  |
| `secondary_noted` | string |  | Whether a sale or purchase of existing shares was noted. | one of: `yes`, `no` |
| `value_at_listing_usd_bn` | number |  | stake_pct / 100 x listings.value_at_listing_usd_bn. Unit: USD bn. | min 0 |
| `value_end_usd_bn` | number | yes | stake_pct / 100 x listings.value_end_usd_bn (2 October 2026 close). Unit: USD bn. | min 0 |
| `primary_value_usd_bn` | number | yes | value_end_usd_bn x primary_share. Unit: USD bn. | min 0 |
| `inside_capital_at_risk_share` | number | yes | Share of the line held by vehicles inside the firm's capital at risk (below 1 where part is held by vehicles outside it, such as Sequoia's Global Equities fund). | min 0; max 1 |
| `primary_value_counted_usd_bn` | number | yes | primary_value_usd_bn x inside_capital_at_risk_share: the value counted in firm_metrics. Unit: USD bn. | min 0 |
| `provenance_confidence` | string |  | Confidence in the primary-share assessment (blank for lines added in the version 7 coverage check, graded in stake_confidence). | one of: `HIGH`, `MED`, `LOW` |
| `provenance_source_url` | string |  | Source URLs, separated by ";". |  |
| `provenance_note` | string |  | Evidence, method and arithmetic behind the stake and primary share. |  |
| `change_note_v17` | string |  | Correction made in book v17 (report version 8), with its filing. |  |

### fund_allocations

**Fund allocations.** How each ranked or measured firm's stake in a listing is split between its fund generations, with the primary fraction of each part and the evidence. Value held by vehicles outside any fund generation carries vehicle_outside_fund_files instead of generation_id.

- File: [`data/core/fund_allocations.csv`](../data/core/fund_allocations.csv) (1,145 rows)
- Primary key: `allocation_id`
- Foreign key: `firm_id` → `firms.firm_id`
- Foreign key: `listing_id` → `listings.listing_id`
- Foreign key: `generation_id` → `fund_generations.generation_id`

| Field | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `allocation_id` | string | yes | Stable identifier. | unique; pattern `^A[0-9]{5}$` |
| `firm_id` | string | yes | Firm. |  |
| `listing_id` | string | yes | Listing. |  |
| `generation_id` | string |  | Fund generation credited (blank when the shares sit outside any generation). |  |
| `vehicle_outside_fund_files` | string |  | Vehicle outside the fund files that holds the shares (single-company vehicles, general-partner entities, roll-over vehicles), or UNKNOWN. |  |
| `share_of_firm_stake` | number | yes | Share of the firm's shares in the listing held by this generation or vehicle. | min 0; max 1 |
| `primary_fraction` | number | yes | Share of these shares counted as bought from the company. | min 0; max 1 |
| `primary_value_usd_bn` | number | yes | Primary value credited to this generation or vehicle. Unit: USD bn. | min 0 |
| `value_end_usd_bn` | number | yes | Value of these shares at the 2 October 2026 close, primary or not. Unit: USD bn. | min 0 |
| `basis` | string |  | Evidence for the split: form3, form4, 13g, prospectus, ira (investors' rights agreement), 13f+ledger, press, name (holder name), rule (fund-vintage rule) and variants. |  |
| `basis_group` | string | yes | Grouping of basis used in the report. | one of: `per_fund_share_counts`, `adviser_values_or_press`, `holder_name`, `vintage_rule`, `other` |
| `confidence` | string |  | Confidence in the split. | one of: `HIGH`, `MED`, `LOW` |
| `split_source` | string | yes | filing_research: per-fund filing research on large positions; manual: reconciled by hand from filings; rule: holder-name or vintage rule. | one of: `filing_research`, `manual`, `rule` |

### benchmark_prices

**Public-market benchmark prices.** Nasdaq-100 year-end closes (before 2017) and QQQ monthly closes (from November 2016) used for the annualised comparison, and the QQQ close on the 2 October 2026 end date.

- File: [`data/core/benchmark_prices.csv`](../data/core/benchmark_prices.csv) (162 rows)
- Primary key: `series_id, date`

| Field | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `series_id` | string | yes | NDX_YEAR_END: Nasdaq-100 index year-end close; QQQ_MONTHLY: QQQ month-end close (dated at the first trading day of the month); QQQ_END_DATE: QQQ close on the end date. | one of: `NDX_YEAR_END`, `QQQ_MONTHLY`, `QQQ_END_DATE` |
| `date` | date | yes | Observation date (31 December for year-end closes; the month's first trading day for monthly bars). |  |
| `close` | number | yes | Closing level (index points or USD per QQQ share, unadjusted). | min 0 |
| `source` | string | yes | Source of the series. |  |
| `note` | string |  | Notes. |  |

## Derived tables

Figures computed from the core tables: firm and fund metrics, robustness checks, company summaries and the companion stage-weighted ranking.

### firm_metrics

**Firm metrics (value per dollar ranking).** One row per measured firm: the ranked firms and the firms listed separately. All values at the 2 October 2026 close. Headline: consistency-adjusted value per dollar = (1 + V/K)^(2/3) x (1 + (V - V_top)/K)^(1/3) - 1.

- File: [`data/derived/firm_metrics.csv`](../data/derived/firm_metrics.csv) (180 rows)
- Primary key: `firm_id`
- Foreign key: `firm_id` → `firms.firm_id`
- Foreign key: `largest_company_listing_id` → `listings.listing_id`

| Field | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `firm_id` | string | yes | Firm. | unique |
| `measurement_status` | string | yes | ranked or listed_separately. | one of: `ranked`, `listed_separately` |
| `rank` | integer |  | Rank on the central headline figure (ranked firms). Neighbouring firms' ranges often overlap; see rank_range_best and rank_range_worst. | min 1 |
| `consistency_adjusted_value_per_dollar` | number |  | Headline figure (x). | min 0 |
| `adjusted_low` | number |  | Headline at the low end of the range from estimated inputs. | min 0 |
| `adjusted_high` | number |  | Headline at the high end of the range from estimated inputs. | min 0 |
| `rank_range_best` | integer |  | Best rank across the input range and the 19 alternative specifications. | min 1 |
| `rank_range_worst` | integer |  | Worst rank across the input range and the 19 alternative specifications. | min 1 |
| `value_per_dollar` | number |  | V / K: primary value at the end date divided by capital at risk (x). | min 0 |
| `value_per_dollar_low` | number |  | value_per_dollar at the low end of the range. | min 0 |
| `value_per_dollar_high` | number |  | value_per_dollar at the high end of the range. | min 0 |
| `rank_value_per_dollar` | integer |  | Rank on plain value per dollar among ranked firms. | min 1 |
| `value_per_dollar_beyond_largest` | number |  | (V - V_top) / K, where V_top is the primary value of the largest company (x). | min 0 |
| `beyond_largest_low` | number |  | value_per_dollar_beyond_largest at the low end of the range. | min 0 |
| `beyond_largest_high` | number |  | value_per_dollar_beyond_largest at the high end of the range. | min 0 |
| `adjusted_one_fifth_weight` | number |  | Headline with a fifth of the weight on depth. | min 0 |
| `adjusted_half_weight` | number |  | Headline with half the weight on depth (version 5 headline). | min 0 |
| `adjusted_beyond_two_largest` | number |  | Headline with depth measured beyond the two largest companies. | min 0 |
| `value_primary_usd_bn` | number |  | V: sum of holdings.primary_value_counted_usd_bn over the firm's core venture lines. Unit: USD bn. | min 0 |
| `capital_at_risk_usd_bn` | number |  | K: sum of fund_vehicles.capital_at_risk_usd_m over the firm's in-scope vehicles, in billions. Unit: USD bn. | min 0 |
| `companies` | integer |  | Number of listings with primary value. | min 0 |
| `largest_company_listing_id` | string |  | Listing with the largest primary value. |  |
| `largest_company_share` | number |  | Share of V from the largest company. | min 0; max 1 |
| `could_fall_over_30pct` | boolean |  | True if the headline would fall by more than 30% at the low end of the range (marked with a diamond in the report). |  |
| `capital_low_confidence_share` | number |  | Share of K resting on low-confidence fund sizes. | min 0; max 1 |
| `value_estimated_share` | number |  | Share of V resting on estimated stakes. | min 0; max 1 |
| `mean_year_capital_at_risk` | number |  | Capital-weighted mean year in which capital at risk was drawn. |  |
| `rank_vs_qqq` | integer |  | Rank on the annualised measure against the QQQ. | min 1 |
| `direct_alpha_vs_median_firm` | number |  | Adjusted Direct Alpha minus the median ranked firm's (fraction per year). |  |
| `direct_alpha_vs_qqq_adjusted` | number |  | Direct Alpha against the Nasdaq-100 (QQQ) on the adjusted value (fraction per year). |  |
| `pme_vs_qqq_adjusted` | number |  | Kaplan-Schoar public market equivalent on the adjusted value (x). |  |
| `irr_adjusted` | number |  | Internal rate of return on the adjusted value (fraction per year). |  |
| `direct_alpha_vs_qqq_unadjusted` | number |  | Direct Alpha on the plain value (fraction per year). |  |
| `pme_vs_qqq_unadjusted` | number |  | Kaplan-Schoar PME on the plain value (x). |  |
| `irr_unadjusted` | number |  | Internal rate of return on the plain value (fraction per year). |  |
| `rank_total_value_all_core` | integer |  | Rank on primary value among all core venture holders. | min 1 |
| `rank_stage_weighted_all_core` | integer |  | Rank on stage-weighted value among all core venture holders. | min 1 |
| `rank_ex_spacex` | integer |  | Rank with SpaceX excluded (a different question, shown separately). | min 1 |
| `reason_not_ranked` | string |  | Why a firm listed separately is not ranked. |  |
| `note` | string |  | Changes and judgments behind the firm's figures. |  |

### firm_robustness

**Firm ranks under alternative specifications.** Rank and headline of each ranked firm under the main specification, the 19 alternative specifications and the ex-SpaceX view (see specifications.csv).

- File: [`data/derived/firm_robustness.csv`](../data/derived/firm_robustness.csv) (3,087 rows)
- Primary key: `firm_id, specification_id`
- Foreign key: `firm_id` → `firms.firm_id`
- Foreign key: `specification_id` → `specifications.specification_id`

| Field | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `firm_id` | string | yes | Firm. |  |
| `specification_id` | string | yes | Specification. |  |
| `rank` | integer |  | Rank among ranked firms under the specification, by the headline figure. | min 1 |
| `consistency_adjusted_value_per_dollar` | number |  | Headline figure under the specification (x). | min 0 |
| `value_per_dollar` | number |  | Plain value per dollar under the specification (x), where computed. | min 0 |

### fund_metrics

**Fund metrics (fund ranking).** One row per fund generation with value: value per dollar and the consistency-adjusted headline at the 2 October 2026 close, with ranges. Ranked: rankable generations of ranked firms.

- File: [`data/derived/fund_metrics.csv`](../data/derived/fund_metrics.csv) (453 rows)
- Primary key: `generation_id`
- Foreign key: `generation_id` → `fund_generations.generation_id`
- Foreign key: `firm_id` → `firms.firm_id`
- Foreign key: `largest_company_listing_id` → `listings.listing_id`

| Field | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `generation_id` | string | yes | Fund generation. | unique |
| `firm_id` | string | yes | Firm. |  |
| `rank` | integer |  | Rank on the headline among rankable generations of ranked firms. | min 1 |
| `fund_display_name` | string | yes | Name used in the report. |  |
| `vintage` | integer |  | Vintage year. | min 1960; max 2026 |
| `committed_usd_m` | number |  | Committed capital of in-scope vehicles. Unit: USD m. | min 0 |
| `capital_at_risk_usd_m` | number |  | Capital at risk. Unit: USD m. | min 0 |
| `value_primary_usd_bn` | number |  | Sum of fund_allocations.primary_value_usd_bn credited to the generation. Unit: USD bn. | min 0 |
| `value_per_dollar` | number |  | Primary value divided by capital at risk (x). | min 0 |
| `consistency_adjusted_value_per_dollar` | number |  | Headline on the generation's companies (x). | min 0 |
| `adjusted_low` | number |  | Low end of the range (rankable generations). | min 0 |
| `adjusted_high` | number |  | High end of the range (rankable generations). | min 0 |
| `companies` | integer |  | Number of listings with primary value. | min 0 |
| `largest_company_listing_id` | string |  | Listing with the largest primary value. |  |
| `largest_company_share` | number |  | Share of the generation's value from its largest company. | min 0; max 1 |
| `largest_company_split_basis` | string |  | Evidence for the split of the largest company's shares. |  |
| `share_of_value_split_from_filings` | number |  | Share of the generation's value split between funds from per-fund filings. | min 0; max 1 |
| `size_confidence` | string |  | Confidence in the generation's size. | one of: `HIGH`, `MED`, `LOW` |
| `rankable` | boolean | yes | True if the generation can be ranked. |  |
| `not_ranked_reason` | string |  | Why the generation is not ranked. |  |

### listing_venture_summary

**Venture ownership and value by listing.** One row per listing with a holder line: long-term value created, and the stake and primary value of venture funds (firms with counts_as_venture_fund = true). The report's top 20 companies are rank_by_value_end 1 to 20.

- File: [`data/derived/listing_venture_summary.csv`](../data/derived/listing_venture_summary.csv) (418 rows)
- Primary key: `listing_id`
- Foreign key: `listing_id` → `listings.listing_id`

| Field | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `listing_id` | string | yes | Listing. | unique |
| `rank_by_value_end` | integer | yes | Rank by value_end_usd_bn. | min 1 |
| `value_at_listing_usd_bn` | number |  | Value at listing. Unit: USD bn. | min 0 |
| `value_end_usd_bn` | number |  | Value at the 2 October 2026 close. Unit: USD bn. | min 0 |
| `multiple_since_listing` | number |  | value_end_usd_bn / value_at_listing_usd_bn. | min 0 |
| `venture_funds_stake_pct` | number |  | Sum of stake_pct x inside_capital_at_risk_share over venture-fund lines. Unit: %. | min 0; max 100 |
| `venture_primary_value_usd_bn` | number |  | Sum of primary_value_counted_usd_bn over venture-fund lines. Unit: USD bn. | min 0 |
| `n_venture_fund_holders` | integer |  | Number of venture firms with a stake. | min 0 |
| `largest_venture_holders` | string |  | Up to three largest venture holders with their stakes. |  |

### holding_stage_weights

**Stage weights by holding (companion ranking).** Entry-stage weights and stage-weighted values of each holder line, used only by the companion stage-weighted ranking.

- File: [`data/derived/holding_stage_weights.csv`](../data/derived/holding_stage_weights.csv) (1,956 rows)
- Primary key: `holding_id`
- Foreign key: `holding_id` → `holdings.holding_id`

| Field | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `holding_id` | string | yes | Holder line. | unique |
| `stage_bucket` | string |  | Stage bucket of the firm's first round. |  |
| `letter_index` | number |  | Round-letter index of the first round. |  |
| `effective_index_after_vintage` | number |  | Round index after the vintage adjustment. |  |
| `stage_weight` | number |  | Stage weight applied (vintage-adjusted). | min 0; max 1 |
| `stage_weight_unadjusted` | number |  | Stage weight before the vintage adjustment. | min 0; max 1 |
| `stage_weight_basis` | string |  | Basis of the stage weight. |  |
| `value_stage_weighted_usd_bn` | number |  | primary value x stage weight. Unit: USD bn. | min 0 |
| `value_flat_scale_usd_bn` | number |  | Value under the unadjusted (flat) stage scale. Unit: USD bn. | min 0 |
| `entry_multiple` | number |  | Multiple from the firm's entry price to the end-date value, where known. |  |
| `company_multiple` | number |  | Multiple from the first institutional round to the end-date value, where known. |  |
| `outcome_conviction_share` | number |  | Outcome-based conviction share. | min 0; max 1 |
| `outcome_basis` | string |  | Basis of outcome_conviction_share. |  |
| `value_outcome_usd_bn` | number |  | Value under the outcome-based weighting. Unit: USD bn. | min 0 |

### stage_weighted_rankings

**Stage-weighted total-value rankings (companion).** Companion ranking of total value created, weighted by the stage of each firm's first round, in three layers.

- File: [`data/derived/stage_weighted_rankings.csv`](../data/derived/stage_weighted_rankings.csv) (1,327 rows)
- Primary key: `layer, firm_id`
- Foreign key: `firm_id` → `firms.firm_id`

| Field | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `layer` | string | yes | core_venture; core_plus_growth (adds growth, crossover and hedge funds); core_venture_ex_spacex. | one of: `core_venture`, `core_plus_growth`, `core_venture_ex_spacex` |
| `firm_id` | string | yes | Firm. |  |
| `rank_stage_weighted` | integer |  | Rank on stage-weighted value within the layer. | min 1 |
| `rank_primary` | integer |  | Rank on primary value. | min 1 |
| `rank_flat` | integer |  | Rank on flat-scale value. | min 1 |
| `rank_outcome` | integer |  | Rank on outcome-weighted value. | min 1 |
| `value_stage_weighted_usd_bn` | number |  | Stage-weighted value. Unit: USD bn. | min 0 |
| `value_primary_usd_bn` | number |  | Primary value. Unit: USD bn. | min 0 |
| `value_flat_scale_usd_bn` | number |  | Flat-scale value. Unit: USD bn. | min 0 |
| `value_outcome_usd_bn` | number |  | Outcome-weighted value. Unit: USD bn. | min 0 |
| `value_as_owned_usd_bn` | number |  | Value of all shares held, primary or not. Unit: USD bn. | min 0 |
| `stage_ratio` | number |  | value_stage_weighted / value_primary. | min 0 |
| `companies` | integer |  | Listings with primary value. | min 0 |

## Reference tables

Parameters and records behind the method: timing weights, lag distributions, strategy parameters, specifications and the coverage register.

### timing_weights

**Timing weights for capital at risk.** Share of a fund's eventual listings expected to fall inside the 2014-2026 window, by vintage and strategy (main specification), and the weight for capital deployed in a given calendar year.

- File: [`data/reference/timing_weights.csv`](../data/reference/timing_weights.csv) (268 rows)
- Primary key: `vintage, strategy`

| Field | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `vintage` | integer | yes | Fund vintage, or calendar year of deployment for deployed_year_weight. | min 1960; max 2026 |
| `strategy` | string | yes | Strategy. | one of: `seed`, `early`, `multi`, `growth` |
| `timing_weight` | number | yes | Weight for a fund of this vintage and strategy, with the 25% floor for capital invested up to 2004 by funds of vintage 1995 or later. | min 0; max 1 |
| `timing_weight_no_floor` | number | yes | Same weight without the floor. | min 0; max 1 |
| `deployed_year_weight` | number | yes | Weight for capital deployed in calendar year = vintage (rows recorded as capital deployed per year), with the floor. | min 0; max 1 |
| `deployed_year_weight_no_floor` | number | yes | Same weight without the floor. | min 0; max 1 |

### lag_distributions

**Entry-to-listing lag distributions.** Probability that a listing occurs a given number of years after the firm's entry, by entry-stage group, estimated from 554 entry-to-listing pairs corrected for double truncation (Efron-Petrosian) and smoothed.

- File: [`data/reference/lag_distributions.csv`](../data/reference/lag_distributions.csv) (104 rows)
- Primary key: `stage_group, lag_years`

| Field | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `stage_group` | string | yes | early (seed and Series A), mid (Series B and C), late (Series D and later), pooled. | one of: `early`, `mid`, `late`, `pooled` |
| `lag_years` | integer | yes | Years from entry to listing. | min 0 |
| `probability` | number | yes | Probability mass. | min 0; max 1 |

### strategy_parameters

**Deployment and stage-mix parameters.** Deployment schedule (share of commitments invested in each year from vintage) and entry-stage mix by fund strategy, used to compute timing weights.

- File: [`data/reference/strategy_parameters.csv`](../data/reference/strategy_parameters.csv) (31 rows)
- Primary key: `strategy, parameter, key`

| Field | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `strategy` | string | yes | Strategy. | one of: `seed`, `early`, `multi`, `growth` |
| `parameter` | string | yes | deployment_share (key = years after vintage) or stage_mix (key = stage group). | one of: `deployment_share`, `stage_mix` |
| `key` | string | yes | Year offset or stage group. |  |
| `value` | number | yes | Share. | min 0; max 1 |

### specifications

**Robustness specifications.** The main specification, the 19 alternative specifications and the ex-SpaceX view used in firm_robustness.csv.

- File: [`data/reference/specifications.csv`](../data/reference/specifications.csv) (21 rows)
- Primary key: `specification_id`

| Field | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `specification_id` | string | yes | Identifier. | unique |
| `title` | string | yes | Short description. |  |
| `group` | string | yes | main; adjustment (form of the consistency adjustment); capital_at_risk; numerator; different_question. | one of: `main`, `adjustment`, `capital_at_risk`, `numerator`, `different_question` |
| `rank_correlation_with_main` | number |  | Spearman rank correlation of the headline with the main specification across ranked firms. | min -1; max 1 |

### coverage_register

**Coverage-check register.** Every (firm, listing) pair the version 7 coverage check found missing from the holder tables, with sources, 13F counts and the outcome.

- File: [`data/reference/coverage_register.csv`](../data/reference/coverage_register.csv) (328 rows)
- Primary key: `register_id`
- Foreign key: `listing_id` → `listings.listing_id`
- Foreign key: `firm_id` → `firms.firm_id`

| Field | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `register_id` | string | yes | Stable identifier. | unique; pattern `^G[0-9]{3}$` |
| `firm_name_as_found` | string | yes | Firm as found by the sweeps. |  |
| `firm_id` | string |  | Firm the pair was attributed to in holdings.csv, where it was added. |  |
| `listing_id` | string | yes | Listing. |  |
| `company_value_usd_bn` | number |  | Company value at the end date. Unit: USD bn. | min 0 |
| `sources` | string |  | Sweeps that found the pair (investor agreement, 13F, name probe). |  |
| `entity` | string |  | Entities named in the source. |  |
| `shares_13f` | number |  | Shares in the first 13F after listing, where found. | min 0 |
| `pct_13f` | number |  | shares_13f as a percentage of post-offering shares. Unit: %. | min 0 |
| `firm_in_book_before_check` | string |  | Whether and how the firm was in the holder tables before the check. |  |
| `outcome` | string | yes | Outcome of the pair. |  |
| `outcome_group` | string | yes | Grouping of outcome used in the report. | one of: `added_ranked`, `added_zero_primary`, `added_listed_separately`, `added_no_fund_history`, `checked_not_added`, `checked_not_established`, `screened_out`, `immaterial_13f_lot`, `outside_ranking_by_type` |
| `outcome_note` | string |  | Sizing and reasoning. |  |
| `stake_pct_added` | number |  | Stake added to holdings.csv (% of post-offering shares). Unit: %. | min 0 |
| `stake_pct_added_x_primary` | number |  | stake_pct_added x primary share. Unit: %. | min 0 |
