# Limitations and known issues

## Limitations

1. **Single outcomes still matter.** Even after the adjustment, 18 of the top 25 owe more than half their value to one company, and half of the top-20 funds owe 80% or more to one. A large price move in SpaceX, Snowflake, Uber, Cloudflare or Datadog would reorder the top of the table, but only if Odin rolls the end date forward.
2. **The consistency adjustment is a judgment.** The one-third weight on depth, depth measured beyond one company, and the added 1 are choices. Other reasonable choices change the order little overall (rank correlations 0.992–0.996, [report §7](report/value_per_dollar_report_v8.md#7-how-firm-is-the-order)), but the form of the adjustment decides who leads: with a fifth of the weight on depth, or with depth measured beyond the two largest companies, a single-company firm would.
3. **Sutter Hill's capital is estimated.** It has no fund series, so its range is the widest in the top ten.
4. **SpaceX attributions are estimates,** inferred from vehicle dates and prices; the ranges show the effect. DFJ's stake, the largest single addition in version 7, rests on a press estimate cross-checked by round arithmetic, with no filing behind it.
5. **Listings below $2bn and outside the US are omitted.** Omitted listings below $2bn (IPOs and SPAC mergers) are not counted, and listings in Hong Kong, mainland China, Europe and Israel are outside the universe. Firms whose companies list there look weaker per dollar (HongShan, IDG, Index, Accel, JVP, Gemini Israel).
6. **IPO exits only.** Acquisitions of private companies and companies still private are outside the measure.
7. **Capital at risk is partly estimated.** 8% of the ranked firms' capital at risk rests on low-confidence sizes, including Lowercase's sidecar (counted at its Slack cheque) and partners' side funds sized from their holdings.
8. **Small stakes are partly estimated,** and positions never assessed for primary purchase score zero.
9. **Secondary purchases are removed only where the evidence reveals them.**
10. **Coverage of small holders.** The version 7 check swept every listing worth $3bn or more. Small holders of smaller listings rely on the prospectus holder tables and the closing screens. Two holders without fund records (Amicus Capital and IT-Farm) were set aside by Odin and are not scored.
11. **Classification.** Who counts as a venture firm is a judgment, and five of the firms Odin moved out have conventional fund structures ([report §13](report/value_per_dollar_report_v8.md#13-decisions)).
12. **Renminbi capital.** Firms that invest only through renminbi funds have no capital at risk in the main specification and cannot be ranked.
13. **A single, fixed end date.** Every figure is a snapshot at the 2 October 2026 close, with no adjustment for later price moves, dilution, distributions or dividends.
14. **This is value created, not investor returns.** It ignores fees, carried interest and actual exit prices.
15. **Fund splits are partly estimated.** About 72% of the ranked firms' value is split between funds from filings and other per-fund evidence (69% from per-fund share counts); the rest follows holder names or the fund-vintage rule. Some splits that matter at the top rest on estimates: DFJ's SpaceX stake by fund, Felicis's Shopify stake between Felicis Ventures II and its Clover Fund, Lowercase's Uber stake by vehicle and Bullet Time Ventures' Uber holding ([report §4](report/value_per_dollar_report_v8.md#4-the-20-funds-with-the-most-value-per-dollar)). A fund's figure is also more sensitive than its firm's to an error in its size.

## Known data issues in version 1.0.0

1. **Two life-sciences listings remain in the universe.** Mersana Therapeutics (`MRSN`) and Kala Pharmaceuticals (`KALA`) have no sector in the source IPO dataset and were not filtered out. Together they are worth about $36m at the end date; the only primary value in a ranked firm is NEA's $8.3m in Mersana (0.03% of NEA's value), so no rank changes. They are flagged for removal in the next minor version.
2. **Three holder lines are known but not sized** (Fidelity, Foxhaven Asset Management and Winslow Capital in Cargurus Inc; `stake_confidence` = `KNOWN_UNSIZED`): `stake_pct` is blank and their value is zero.
3. **Five company values are not tied to a recorded price** (Yodlee (`YDLE`), Fitbit (`FIT`), Osprey Tech Acq Corp (`SFTW.`), Bluecity Hldg Ltd (`BLCT`), Ozon Holdings PLC (`OZON`)): the holdings book records the company value only, so `price_end_usd` is the implied per-share value (`price_end_note`).
4. **Fund-level and firm-level primary value differ slightly for two positions.** For Accel's Freshworks and Sequoia's Unity stakes, the per-fund filings identify slightly more shares bought from other holders than the firm-level line (primary shares of 81.8% and 65.6%, against 82% and 66%). The fund allocations use the filings, so fund totals fall short of the firm figures by $1.9m and $11.0m. `scripts/validate.py` reports these two as warnings.
5. **Values outside any fund generation.** About $28bn of the ranked firms' value sits in single-company vehicles and other vehicles outside the fund files (`fund_allocations.vehicle_outside_fund_files`); it counts at firm level but in no fund's figure.
6. **Sector** is blank for the two listings in item 1; `entry_year` and `first_round` are missing for some holder lines.
7. **Some free-text fields keep internal version codes** (for example "v14 G1", "v15 U2") that mark the book version in which a value was changed.
