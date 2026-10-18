# Value created per dollar at risk: venture firms ranked on US listings, 2014–2026 (excluding life sciences)

*Odin research, analysis report version 8, 18 October 2026. It accompanies dataset release 1.0.0, which leaves out the holder lines of natural persons. Data: holdings book v17 (2,313 holder lines across 418 listings) and fund histories for 180 firms (3,422 vehicles).*

> **Performance end date: the close on Friday 2 October 2026.** Every figure in this report is measured at that close: company values, the value of each stake, value per dollar, the annual returns and the QQQ benchmark they are compared with. Price moves, listings, takeovers and filings after that date are not reflected. The end date is fixed and later versions keep it unless Odin decides to roll it forward (§13).

*New in version 8:*
- *Two new rankings: the 20 companies that created the most long-term value (§3) and the 20 individual funds with the highest value per dollar (§4).*
- *For the fund ranking, each firm's large stakes were traced to the funds that held them, from the per-fund holdings in directors' Forms 3 and 4, Schedule 13G filings, prospectuses and investors' rights agreements. The same filings showed where the book had counted shares bought from other holders as bought from the company, and where fund sizes were wrong. Those corrections are applied to the firm ranking too (§8).*
- *The top two are no longer shown as joint first. Firms are ranked on their central figures even where their ranges overlap (Odin, 18 October 2026), so Sutter Hill (11.6x) ranks first and Founders Fund (11.2x) second.*
- *Lowercase Capital's RT fund is in scope and its sidecar is counted as the Slack cheque it was, on a commercial database record of the Slack investment (Odin, 18 October 2026). Lowercase rises from sixth to fifth (8.8x).*
- *DFJ's SpaceX stake is still an estimate: no DFJ filing lists SpaceX shares (checked 18 October 2026), and the first 13F that could do so covers the quarter ending 31 December 2026.*
- *Amicus Capital and IT-Farm are no longer pursued (Odin, 18 October 2026).*

*Carried over from versions 6 and 7:*
- *The headline is consistency-adjusted value per dollar, with one-third of the weight on value beyond the largest company.*
- *Firms are ranked only if they are independent venture managers investing pooled outside capital, mainly in private technology companies. Other investors are listed separately with their figures (§6).*
- *Version 7's coverage check (§8) stands. Appendix D lists every change since version 5.*

---

## Summary

- **What is measured.** The universe is 424 US venture-backed listings from January 2014 to June 2026, excluding life sciences. For each firm we take the stock its funds bought from these companies (primary capital), value it at the 2 October 2026 close as if never sold, and divide by the capital the firm had at risk of producing these listings.
- **A fixed end date.** All values are taken at the close on 2 October 2026 and held there. A firm whose companies have risen since then is not credited, and one whose companies have fallen is not marked down.
- **The headline rewards consistency as well as size, without punishing one great company too hard.**
  - Plain value per dollar lets one company carry a firm: Gigafund makes 30.9x on SpaceX alone and Pelion 22.9x on Cloudflare alone.
  - The headline is the **consistency-adjusted value per dollar**: a weighted geometric mean of the firm's value per dollar and its value per dollar *excluding its single largest company*, with 1 added to each so that a one-company firm still scores.
  - Value per dollar carries two-thirds of the weight and value beyond the largest company one-third. A firm that owes everything to one company scores (1 + value per dollar)^(2/3) − 1, so 25x becomes 7.8x.
  - Plain value per dollar and the "beyond the largest company" figure are shown alongside.
- **Sutter Hill first (11.6x), Founders Fund second (11.2x).**
  - Sutter Hill created value per dollar at 14.4x from Snowflake, Astera Labs and Pure Storage, and still 7.4x without Snowflake. Its capital at risk is estimated, because it invests mainly from one evergreen fund, so its range is wide (7.8x–16.6x).
  - Founders Fund makes more on the plain measure, 15.5x on SpaceX and Palantir, but 5.7x without SpaceX. The consistency adjustment is what puts Sutter Hill ahead.
  - The two ranges overlap, so the order of the top two is not firm (§7).
- **IA Ventures is third (10.0x).** Its seed stakes in DigitalOcean, Datadog and The Trade Desk make 12.4x on $0.34bn at risk, and 6.4x beyond its largest company, second only to Sutter Hill.
- **Then three single-company records: Gigafund (9.1x, SpaceX), Lowercase Capital (8.8x, Uber) and Pelion (7.3x, Cloudflare).**
  - Lowercase rises from sixth to fifth (7.7x to 8.8x). Its RT fund, which a commercial database record lists as the Slack investor, now counts as a fund, and the sidecar beside it counts at the size of its Slack cheque instead of a $40m placeholder.
  - Pelion, fifth in version 7 at 7.9x, is sixth at 7.3x: Lowercase's change lifts it above Pelion, and 10.5% of Pelion's Cloudflare shares were bought from other holders (common stock, and preferred held by funds formed after the rounds that issued it).
- **Then Union Square Ventures (6.3x), Benchmark (6.0x), Bessemer (5.1x) and DFJ (4.4x).** Greylock (3.7x) and Sequoia (3.7x) follow at 11th and 12th.
- **DFJ is tenth on SpaceX.** DFJ's venture and growth funds have held SpaceX since 2009. No filing gives a share count, so the stake (about 1.54%, range 1.15%–1.85%) is sized from a Forbes estimate and checked against the rounds DFJ is known to have joined. Its range is 2.8x–5.4x; without SpaceX it would make 0.91x, around 77th.
- **The companies (§3).** SpaceX's $2.1trn at 2 October 2026 is 37% of the universe's $5.7trn, and the 20 most valuable listings make up 74%. Palantir ($326bn), Alibaba, CrowdStrike and Arista Networks follow. Shopify has multiplied 89 times since listing, Arista 77 times and CrowdStrike 32 times. Venture funds held half of Cloudflare and 45% of Datadog at listing, and none of Alibaba, Arista or CoreWeave.
- **The funds (§4).** Founders Fund II, a $220m fund of 2007, made $37.4bn, mostly from SpaceX and Palantir: 269x plain and 183x adjusted, more than three times any other fund.
  - Next come Bullet Time Ventures I (David Cohen's $4.85m seed fund: Uber and Twilio, 53x), Founders Fund III (52x), Index Ventures VI (40x), Lowercase Ventures Fund I ($8.5m, Uber, 38x), FirstMark Capital I (37x) and Sequoia Capital XII (35x).
  - Every top-20 fund is of vintage 2005–2012. Half owe 80% or more of their value to one company, and eight have commitments of less than $100m.
- **Corrections from the fund-level filings (§8).**
  - Shares bought from other holders, now removed: Pelion's Cloudflare (10.5%), Index's Datadog (7.5%), Andreessen Horowitz's Coinbase (18.6%), Lightspeed's Rubrik (10.2%), Accel's Etsy (34.6%) and UiPath (10.3%), and Benchmark's Uber (8.8%: Seed shares issued before Benchmark's first round).
  - JVP's CyberArk stake is now counted as mostly bought from the company: JVP rises from 61st to 42nd and RPM Ventures leaves the top 50.
  - Fund sizes corrected include FirstMark I ($300m to about $220m), Khosla Ventures Seed B ($300m to $397m), Altos Ventures IV ($64.9m to $86m) and Sequoia Capital XII.
  - Benchmark falls from 6.2x to 6.0x and stays eighth. The top-50 line stays at 1.38x. Below the top ten, Index and FirstMark, and Amplify and Andreessen Horowitz, swap places, and Accel falls from 23rd to 25th.
- **Odin's classification is unchanged.** The thirteen firms Odin identified are listed separately (§6), as are ten more that fail the same test.
- **Breadth still pays.** Compared with plain value per dollar, Sequoia (33 companies) rises from 27th to 12th, Greylock from 23rd to 11th, Index from 24th to 14th and Andreessen Horowitz from 44th to 28th. Firms that rest almost entirely on one company move down: Venrock (Cloudflare) from 11th to 18th, Contour (Datadog) from 13th to 21st, Harbor Pacific (Zoom) from 15th to 29th and March Capital (CrowdStrike) from 17th to 31st.
- **How firm the order is.** Under the 19 alternative specifications in §7, the rankings correlate at 0.947 or more with the main one. Excluding SpaceX, a different question, is shown separately.
  - Sutter Hill and Founders Fund are the top two under 13 of the 19 checks. Sutter Hill leads under 12 of them and Founders Fund under four; Founders Fund is never below third and Sutter Hill never below fourth.
  - The form of the adjustment decides who leads. With a fifth of the weight on depth instead of a third, Gigafund (15.0x) and Lowercase (13.1x) would lead, just ahead of Founders Fund (12.8x) and Sutter Hill (12.6x).
  - The adjusted ranking correlates 0.98 with plain value per dollar and 0.98 with the annualised version against the QQQ (§2).
- **What could still move it:**
  - Sutter Hill's capital estimate.
  - The SpaceX attributions (Founders Fund, Gigafund and DFJ).
  - The classification review (§13): restored one at a time, OpenView would rank 9th and Hydrazine 10th.
  - The form of the consistency adjustment (§7).

---

## 1. The ranking: consistency-adjusted value per dollar of capital at risk

**How to read it:**
- **Value per $ at risk** is the value at 2 October 2026 of the firm's primary stakes in 2014–2026 listings, divided by its capital at risk.
- **Beyond largest company** is the same ratio with the firm's largest company left out. It measures how much value the rest of the record created.
- **Consistency-adjusted value per $** (the headline) combines the two:

  `adjusted = (1 + value per $)^(2/3) × (1 + value per $ beyond the largest company)^(1/3) − 1`

  - A firm whose value is spread across many companies scores close to its plain value per dollar.
  - A firm that owes everything to one company scores (1 + value per $)^(2/3) − 1. For example, 25x becomes 7.8x and 8x becomes 3.3x.
- **Capital at risk** is each fund's committed capital multiplied by the share of its eventual listings expected to fall inside the window (§10.7). For example, a 2011 early-stage fund counts 92%, a 2000 fund 25% (the floor) and a 2022 early-stage fund 9%.
- **Range from estimated inputs** recomputes the figure with:
  - estimated stakes at their low and high values;
  - uncertain primary shares at their low and high cases;
  - low-confidence fund sizes halved and doubled, or the documented capital range where one exists (§10.9).
  - A dash means the range is narrower than 5% of the figure.
- **Rank range (all checks)** is the best and worst rank across that range and the 19 alternative specifications in §7. It excludes the ex-SpaceX view, which answers a different question.
- **◊** marks firms whose figure would fall by more than 30% at the low end of their range.
- **Order.** Firms are ranked on their central figures. Where neighbouring ranges overlap, as they do for Sutter Hill and Founders Fund and for most neighbouring pairs, the order between them is not firm; the rank range shows how far each firm could move.
- **What is not counted:** acquisitions, private holdings, omitted listings below $2bn and listings outside the US. Every firm's figure therefore understates its total return; the comparison between firms is the point.

| Rank | Firm | Consistency-adjusted value per $ | Range from estimated inputs | Rank range (all checks) | Value per $ at risk | Beyond largest company | Value ($bn) | Capital at risk ($bn) | Largest company (share of value; companies) | Rank vs QQQ (§2) |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 1 | Sutter Hill ◊ | 11.6x | 7.8x–16.6x | 1–5 | 14.4x | 7.4x | 19.1 | 1.33 | Snowflake (49% of 5) | 3 |
| 2 | Founders Fund | 11.2x | 10.6x–11.6x | 1–3 | 15.5x | 5.7x | 95.2 | 6.16 | SpaceX (63% of 12) | 2 |
| 3 | IA Ventures | 10.0x | 9.1x–10.0x | 1–6 | 12.4x | 6.4x | 4.3 | 0.34 | DigitalOcean (49% of 3) | 4 |
| 4 | Gigafund | 9.1x | 6.7x–10.4x | 1–9 | 30.9x | 0 | 11.0 | 0.36 | SpaceX (100% of 1) | 1 |
| 5 | Lowercase Capital | 8.8x | 6.5x–12.2x | 1–6 | 23.4x | 0.58x | 2.3 | 0.10 | Uber (98% of 2) | 5 |
| 6 | Pelion | 7.3x | 6.9x–7.5x | 5–9 | 22.9x | 0 | 15.1 | 0.66 | Cloudflare (100% of 1) | 6 |
| 7 | Union Square Ventures | 6.3x | 5.4x–7.3x | 4–8 | 7.0x | 5.0x | 10.2 | 1.46 | Twilio (28% of 7) | 7 |
| 8 | Benchmark | 6.0x | 5.9x–6.3x | 5–9 | 7.6x | 3.7x | 18.0 | 2.37 | Uber (52% of 16) | 10 |
| 9 | Bessemer | 5.1x | 4.8x–5.3x | 7–10 | 7.0x | 2.6x | 48.4 | 6.92 | Shopify (63% of 16) | 9 |
| 10 | DFJ / Draper Fisher Jurvetson ◊ | 4.4x | 2.8x–5.4x | 9–21 | 7.7x | 1.0x | 29.8 | 3.85 | SpaceX (87% of 11) | 12 |
| 11 | Greylock | 3.7x | 3.4x–4.0x | 11–18 | 4.1x | 3.1x | 14.6 | 3.55 | Airbnb (25% of 11) | 16 |
| 12 | Sequoia Capital | 3.7x | 3.1x–4.1x | 10–22 | 4.0x | 3.2x | 82.6 | 20.77 | SpaceX (18% of 33) | 11 |
| 13 | FirstMark | 3.5x | 3.4x–3.6x | 11–17 | 6.7x | 0.60x | 13.2 | 1.98 | Shopify (91% of 3) | 13 |
| 14 | Index Ventures | 3.4x | – | 11–19 | 4.1x | 2.3x | 30.5 | 7.44 | Datadog (45% of 22) | 14 |
| 15 | Founder Collective | 3.3x | – | 10–29 | 4.6x | 1.6x | 0.9 | 0.18 | The Trade Desk (66% of 2) | 20 |
| 16 | First Round Capital | 3.3x | 3.1x–3.4x | 11–24 | 4.3x | 1.7x | 4.4 | 1.00 | Uber (61% of 7) | 17 |
| 17 | Granite Ventures ◊ | 3.0x | 2.0x–3.1x | 11–40 | 4.7x | 1.0x | 1.0 | 0.22 | Anaplan (78% of 2) | 28 |
| 18 | Venrock | 3.0x | 2.7x–3.2x | 11–25 | 6.9x | 0.03x | 14.7 | 2.13 | Cloudflare (100% of 2) | 26 |
| 19 | Redpoint | 2.9x | 2.5x–3.2x | 16–34 | 3.9x | 1.5x | 12.4 | 3.22 | Snowflake (60% of 12) | 24 |
| 20 | Ribbit Capital | 2.9x | 2.6x–3.2x | 10–26 | 3.9x | 1.4x | 11.5 | 2.92 | Robinhood (63% of 7) | 8 |
| 21 | Contour Venture Partners | 2.8x | 2.5x–2.9x | 13–27 | 6.5x | 0 | 1.6 | 0.24 | Datadog (100% of 1) | 22 |
| 22 | Romulus Capital | 2.7x | 2.2x–3.2x | 15–32 | 6.3x | 0 | 1.0 | 0.16 | EquipmentShare (100% of 1) | 21 |
| 23 | Khosla Ventures | 2.6x | 2.4x–2.7x | 20–33 | 3.2x | 1.8x | 19.2 | 6.08 | Rocket Lab (44% of 11) | 27 |
| 24 | Gemini Israel | 2.6x | 2.5x–2.7x | 17–42 | 4.8x | 0.39x | 1.3 | 0.28 | JFrog (92% of 2) | 32 |
| 25 | Accel | 2.6x | 2.4x–2.8x | 17–28 | 3.7x | 1.1x | 56.0 | 15.21 | CrowdStrike (70% of 24) | 25 |
| 26 | Glynn Capital ◊ | 2.5x | 1.5x–3.9x | 11–70 | 3.3x | 1.3x | 2.1 | 0.65 | Palantir (62% of 6) | 29 |
| 27 | Amplify Partners ◊ | 2.3x | 1.3x–3.6x | 13–55 | 4.2x | 0.39x | 2.3 | 0.56 | Datadog (91% of 2) | 15 |
| 28 | Andreessen Horowitz | 2.3x | 2.2x–2.7x | 20–35 | 2.4x | 2.1x | 30.8 | 12.66 | SpaceX (15% of 21) | 23 |
| 29 | Harbor Pacific Capital ◊ | 2.3x | 1.2x–4.7x | 10–57 | 5.0x | 0 | 0.1 | 0.03 | Zoom (100% of 1) | 41 |
| 30 | Highway 12 Ventures | 2.3x | 2.0x–2.3x | 20–49 | 4.9x | 0 | 0.2 | 0.05 | SendGrid (100% of 1) | 40 |
| 31 | March Capital | 2.2x | 2.0x–2.7x | 21–68 | 4.8x | 0 | 5.7 | 1.19 | CrowdStrike (100% of 1) | 19 |
| 32 | SV Angel ◊ | 2.2x | 0.85x–4.6x | 10–83 | 2.4x | 1.9x | 0.9 | 0.39 | Airbnb (21% of 32) | 30 |
| 33 | Red Swan ◊ | 2.0x | 0.71x–3.8x | 11–91 | 4.1x | 0.08x | 0.1 | 0.02 | Coinbase (98% of 2) | 33 |
| 34 | Banyan Partners | 2.0x | 2.0x–3.0x | 19–56 | 3.5x | 0.29x | 4.8 | 1.36 | Pinduoduo (92% of 2) | 31 |
| 35 | Granite Hill Capital Partners ◊ | 2.0x | 1.0x–3.0x | 18–70 | 4.1x | 0 | 0.1 | 0.03 | SentinelOne (100% of 1) | 44 |
| 36 | Emergence Capital | 1.9x | – | 31–42 | 2.8x | 0.78x | 3.3 | 1.19 | Zoom (72% of 4) | 37 |
| 37 | Section 32 | 1.9x | 1.4x–2.7x | 17–49 | 2.7x | 0.74x | 1.5 | 0.53 | Dave (73% of 3) | 18 |
| 38 | Flybridge | 1.8x | – | 32–51 | 3.7x | 0.02x | 1.7 | 0.46 | MongoDB (99% of 2) | 48 |
| 39 | Hummer Winblad | 1.8x | 1.5x–2.1x | 24–50 | 2.6x | 0.72x | 1.1 | 0.42 | MuleSoft (73% of 2) | 38 |
| 40 | Y Combinator ◊ | 1.8x | 0.97x–3.0x | 17–72 | 2.1x | 1.3x | 3.8 | 1.80 | DoorDash (37% of 11) | 34 |
| 41 | Altos Ventures | 1.7x | 1.7x–1.8x | 32–58 | 3.5x | 0 | 2.9 | 0.83 | Roblox (100% of 1) | 36 |
| 42 | JVP | 1.7x | 1.2x–2.1x | 30–56 | 3.5x | 0 | 3.8 | 1.09 | CyberArk (100% of 1) | 39 |
| 43 | NEA | 1.7x | 1.6x–1.7x | 33–46 | 2.1x | 0.94x | 33.0 | 15.54 | Cloudflare (56% of 15) | 46 |
| 44 | Celesta Capital | 1.6x | 1.5x–1.7x | 37–67 | 3.2x | 0 | 1.8 | 0.57 | Credo (100% of 1) | 45 |
| 45 | 8VC | 1.6x | 1.5x–2.0x | 34–99 | 2.9x | 0.11x | 5.2 | 1.77 | Palantir (96% of 4) | 42 |
| 46 | Madrona | 1.5x | – | 39–50 | 1.9x | 0.98x | 2.9 | 1.56 | Smartsheet (48% of 7) | 49 |
| 47 | Cathay Innovation | 1.5x | 1.3x–1.7x | 31–65 | 2.1x | 0.56x | 1.6 | 0.74 | Pinduoduo (74% of 2) | 47 |
| 48 | Revel Partners ◊ | 1.5x | 1.00x–2.0x | 33–71 | 2.9x | 0 | 0.1 | 0.03 | The Trade Desk (100% of 1) | 57 |
| 49 | Felicis ◊ | 1.4x | 0.64x–2.4x | 27–95 | 2.4x | 0.23x | 2.2 | 0.92 | Shopify (90% of 7) | 50 |
| 50 | Mobius Venture Capital | 1.4x | 0.97x–1.7x | 11–92 | 2.1x | 0.42x | 1.1 | 0.54 | Bloom Energy (80% of 2) | 35 |

Ranks 51 to 147 are in Appendix A.

**What stands out:**
- **The two leaders.**
  - Sutter Hill spread its value across Snowflake (49%), Astera Labs (31%) and Pure Storage (19%), and makes 7.4x beyond its largest company, more than any other firm.
  - Founders Fund made 15.5x on $6.2bn at risk, from SpaceX (63% of its value) and Palantir (28%), and is first on total primary value.
  - Palantir carries Founders Fund's depth: it is three-quarters of Founders Fund's value beyond SpaceX. Without it, Founders Fund would score 6.2x and rank seventh, just behind Union Square Ventures.
- **IA Ventures, third.** DigitalOcean (49% of its value), Datadog (33%) and The Trade Desk (18%), all seed investments made in 2010–13, on $0.34bn of capital at risk. Only Sutter Hill makes more beyond its largest company.
- **Single-company records.** Gigafund, Lowercase and Pelion owe all or nearly all their value to one company. The adjustment takes them from 30.9x, 23.4x and 22.9x to 9.1x, 8.8x and 7.3x: fourth to sixth.
- **Breadth at the top.** Nine of the top 25 make more than 2x beyond their largest company: Sutter Hill, IA Ventures, Founders Fund, Union Square Ventures (Twilio 28%, Coinbase 25%, Cloudflare 17%), Benchmark, Sequoia (SpaceX 18% of 33 companies), Greylock (Airbnb 25%), Bessemer and Index.
- **Concentration remains common.** Eighteen of the top 25 owe more than half their value to one company. Ten owe 70% or more (Accel's CrowdStrike share, 69.95%, shows as 70% in the table but is just below):
  - Gigafund, Pelion, Contour (Datadog) and Romulus (EquipmentShare) owe all of it to one company, and Venrock (Cloudflare) and Lowercase (Uber) almost all.
  - DFJ (SpaceX 87%), FirstMark (Shopify), Granite (Anaplan) and Gemini Israel (JFrog) owe 70% or more.
- **Small firms still compete.** Thirteen of the top 25 have capital at risk below $2bn. IA Ventures ($0.34bn), Founder Collective ($0.18bn) and Granite ($0.22bn) rank 3rd, 15th and 17th. Among the firms ranked since version 7, Harbor Pacific ($0.03bn at risk), Red Swan ($0.02bn), Granite Hill ($0.03bn) and Revel ($0.03bn) each rest on one early stake (Zoom, Coinbase, SentinelOne and The Trade Desk).
- **The platforms.** Sequoia makes 3.7x on $20.8bn (12th), Index 3.4x on $7.4bn (14th), Accel 2.6x on $15.2bn (25th), Andreessen Horowitz 2.3x on $12.7bn (28th) and NEA 1.7x on $15.5bn (43rd). Kleiner Perkins (1.2x) is 56th, Lightspeed (0.94x) 75th and IVP (0.88x) 82nd. HongShan (0.38x) is 115th even with Pinduoduo, because its large Hong Kong and mainland China listings are outside this universe.
- **Accelerators and seed platforms.** SV Angel (2.2x, 32nd) and Y Combinator (1.8x, 40th) rest on estimated stakes below the 5% disclosure threshold, so their ranges are wide. Techstars Ventures is 91st (0.72x) and 500 Global 129th (0.20x).
- **Lux Ventures is last.** Its only scored position is a small estimated Planet stake.

---

## 2. Annualised ranking against the QQQ

Value per dollar ignores time: a dollar committed in 2008 has had longer to grow than one committed in 2020. This ranking expresses the same consistency-adjusted value as an annual return and compares it with what the same money would have earned in the Nasdaq-100 price index, tracked by the QQQ, up to the same end date.

**How it works:**
- Each firm's capital at risk is drawn year by year as its funds deploy it. Its consistency-adjusted value (the headline figure × capital at risk) is taken at the 2 October 2026 close, and the QQQ is measured to the same close.
- **Annual return vs QQQ** is the Direct Alpha (Gredil, Griffiths and Stucke, 2014): the firm's annual return over and above the QQQ's, on the same cash flows.
- Only listings inside the window count, so most firms' absolute figures are negative; the median ranked firm's is −15.9% a year. The first column therefore shows each firm's annual return relative to the median firm, in percentage points.
- **Value vs QQQ-grown capital** (the Kaplan–Schoar public market equivalent) divides the adjusted value by what the same capital would be worth had it been invested in the QQQ.
- **Unadjusted annual return vs QQQ** uses the plain value, for comparison (median −12.1%).

| Rank | Firm | Annual return vs median firm (points) | Annual return vs QQQ | Value vs QQQ-grown capital | Unadjusted annual return vs QQQ | Rank (§1) |
|---:|---|---:|---:|---:|---:|---:|
| 1 | Gigafund | +34.6 | +18.8% | 3.09x | +40.8% | 4 |
| 2 | Founders Fund | +24.2 | +8.3% | 2.39x | +11.2% | 2 |
| 3 | Sutter Hill ◊ | +18.4 | +2.5% | 1.49x | +3.8% | 1 |
| 4 | IA Ventures | +18.3 | +2.5% | 1.35x | +4.3% | 3 |
| 5 | Lowercase Capital | +16.0 | +0.1% | 1.01x | +8.0% | 5 |
| 6 | Pelion | +15.3 | −0.6% | 0.92x | +7.3% | 6 |
| 7 | Union Square Ventures | +15.0 | −0.8% | 0.90x | +0.0% | 7 |
| 8 | Ribbit Capital | +14.6 | −1.3% | 0.92x | +3.1% | 20 |
| 9 | Bessemer | +13.0 | −2.9% | 0.66x | −0.7% | 9 |
| 10 | Benchmark | +12.1 | −3.7% | 0.52x | −2.4% | 8 |
| 11 | Sequoia Capital | +11.9 | −4.0% | 0.62x | −3.4% | 12 |
| 12 | DFJ / Draper Fisher Jurvetson ◊ | +11.5 | −4.4% | 0.51x | −0.6% | 10 |
| 13 | FirstMark | +11.3 | −4.6% | 0.59x | +1.0% | 13 |
| 14 | Index Ventures | +10.5 | −5.4% | 0.50x | −3.9% | 14 |
| 15 | Amplify Partners ◊ | +10.2 | −5.6% | 0.64x | +1.8% | 27 |
| 16 | Greylock | +9.7 | −6.2% | 0.38x | −5.6% | 11 |
| 17 | First Round Capital | +9.2 | −6.6% | 0.42x | −4.4% | 16 |
| 18 | Section 32 | +9.1 | −6.7% | 0.67x | −0.6% | 37 |
| 19 | March Capital | +9.0 | −6.8% | 0.57x | +2.6% | 31 |
| 20 | Founder Collective | +8.9 | −6.9% | 0.40x | −4.4% | 15 |
| 21 | Romulus Capital | +8.9 | −7.0% | 0.48x | +0.9% | 22 |
| 22 | Contour Venture Partners | +8.8 | −7.1% | 0.42x | −0.3% | 21 |
| 23 | Andreessen Horowitz | +8.6 | −7.2% | 0.50x | −6.7% | 28 |
| 24 | Redpoint | +8.6 | −7.3% | 0.34x | −5.3% | 19 |
| 25 | Accel | +8.5 | −7.4% | 0.40x | −4.4% | 25 |
| 26 | Venrock | +8.3 | −7.6% | 0.30x | −2.3% | 18 |
| 27 | Khosla Ventures | +7.4 | −8.5% | 0.32x | −7.1% | 23 |
| 28 | Granite Ventures ◊ | +7.2 | −8.7% | 0.17x | −6.6% | 17 |
| 29 | Glynn Capital ◊ | +7.0 | −8.9% | 0.32x | −6.6% | 26 |
| 30 | SV Angel ◊ | +6.9 | −8.9% | 0.36x | −8.2% | 32 |
| 31 | Banyan Partners | +6.9 | −9.0% | 0.45x | −2.6% | 34 |
| 32 | Gemini Israel | +6.5 | −9.4% | 0.15x | −6.4% | 24 |
| 33 | Red Swan ◊ | +5.9 | −10.0% | 0.32x | −3.9% | 33 |
| 34 | Y Combinator ◊ | +5.7 | −10.1% | 0.40x | −8.6% | 40 |
| 35 | Mobius Venture Capital | +5.7 | −10.1% | 0.07x | −8.6% | 50 |
| 36 | Altos Ventures | +5.7 | −10.2% | 0.32x | −3.5% | 41 |
| 37 | Emergence Capital | +5.6 | −10.2% | 0.28x | −7.2% | 36 |
| 38 | Hummer Winblad | +5.6 | −10.3% | 0.12x | −8.5% | 39 |
| 39 | JVP | +5.4 | −10.5% | 0.23x | −5.1% | 42 |
| 40 | Highway 12 Ventures | +5.2 | −10.7% | 0.13x | −6.8% | 30 |
| 41 | Harbor Pacific Capital ◊ | +5.1 | −10.7% | 0.20x | −5.7% | 29 |
| 42 | 8VC | +5.1 | −10.8% | 0.44x | −2.6% | 45 |
| 43 | Galileo Partners | +4.8 | −11.0% | 0.06x | −8.7% | 65 |
| 44 | Granite Hill Capital Partners ◊ | +4.6 | −11.3% | 0.20x | −6.1% | 35 |
| 45 | Celesta Capital | +4.4 | −11.5% | 0.34x | −4.2% | 44 |
| 46 | NEA | +4.4 | −11.5% | 0.20x | −9.6% | 43 |
| 47 | Cathay Innovation | +4.1 | −11.8% | 0.41x | −7.0% | 47 |
| 48 | Flybridge | +4.1 | −11.8% | 0.14x | −7.6% | 38 |
| 49 | Madrona | +3.8 | −12.1% | 0.20x | −10.4% | 46 |
| 50 | Felicis ◊ | +3.6 | −12.2% | 0.33x | −6.3% | 49 |

Ranks 51 to 147 are in Appendix B.

**What changes from §1:**
- **The two rankings agree closely** (rank correlation 0.98).
- **Recent capital moves up.** Gigafund's money went in during 2017–24 and SpaceX listed in 2026, so it ranks first here (fourth in §1). Ribbit (average capital year 2020) rises from 20th to 8th, Amplify (2020) from 27th to 15th, Section 32 (2021) from 37th to 18th and March Capital (2019) from 31st to 19th.
- **Older capital moves down.** Benchmark's capital centres on 2010–13 (average year 2012), so it moves from eighth to tenth. Granite's 2005 fund takes it from 17th to 28th, and Gemini Israel's 2004–07 funds from 24th to 32nd. Harbor Pacific (average year 2012) falls from 29th to 41st.
- **Near 1x the effect reverses.** A poor result spread over more years costs less a year, so firms with old capital and modest figures rise: Galileo from 65th to 43rd, Bay Partners from 77th to 55th, El Dorado from 68th to 51st and Mobius from 50th to 35th. Firms with recent capital and modest figures fall: Armory Square from 58th to 68th, Quiet Capital from 60th to 69th and Pear VC from 78th to 88th.

---

## 3. The 20 companies that created the most value

**How to read it:**
- **Long-term value created** is the value at the 2 October 2026 close of all the shares outstanding at listing, held as if never sold and restated for splits. It is the same company value from which every firm's stake is valued in this report.
- **Value at listing** is the same share count at the offer price (the reference price for direct listings).
- **Venture funds' stake at listing** adds up the stakes held going into the listing by the venture firms in the book, whether ranked, listed separately or without fund histories. Money of individuals and families is left out: family offices, angel groups, members' deal platforms and vehicles investing their principals' own money, such as RTP Ventures, Leonid Boguslavsky's vehicle, which held 7.5% of Datadog. **Primary value created by venture funds** is the part of their stakes bought from the company, valued at the end date.
- Values are those of the listing-day shares only. Shares issued later, dividends and buybacks are not counted.

| Rank | Company | Listed | Value at listing ($bn) | Value at 2 Oct 2026 ($bn) | Multiple since listing | Venture funds' stake at listing | Primary value created by venture funds ($bn) | Largest venture holders (stake at listing) |
|---:|---|---|---:|---:|---:|---:|---:|---|
| 1 | SpaceX | Jun 2026 | 1,779.5 | 2,095.4 | 1.2x | 10.9% | 136.2 | Founders Fund 3.1%; Vy Capital 2.1%; DFJ 1.6% |
| 2 | Palantir | Sep 2020 | 16.4 | 325.9 | 19.9x | 10.9% | 34.3 | Founders Fund 8.1%; 8VC 1.6%; Mithril Capital 0.8% |
| 3 | Alibaba | Sep 2014 | 167.6 | 260.9 | 1.6x | – | – | none (largest holders: SoftBank, Yahoo) |
| 4 | CrowdStrike | Jun 2019 | 6.7 | 212.5 | 31.8x | 22.8% | 47.9 | Accel 18.7%; March Capital 2.7%; IVP 1.3% |
| 5 | Arista Networks | Jun 2014 | 2.7 | 210.9 | 77.2x | – | – | none (largest holders: founders) |
| 6 | Uber | May 2019 | 76.3 | 115.5 | 1.5x | 19.2% | 20.0 | Benchmark 8.8%; GV 3.9%; Lowercase Capital 2.6% |
| 7 | Shopify | May 2015 | 1.3 | 112.7 | 89.1x | 45.0% | 47.6 | Bessemer 27.1%; FirstMark 10.6%; OMERS Ventures 5.4% |
| 8 | Cloudflare | Sep 2019 | 4.4 | 102.4 | 23.3x | 50.4% | 49.9 | NEA 17.9%; Pelion 16.5%; Venrock 14.2% |
| 9 | Airbnb | Dec 2020 | 40.6 | 97.0 | 2.4x | 27.7% | 26.3 | Sequoia Capital 13.7%; Founders Fund 4.4%; Greylock 3.8% |
| 10 | Robinhood | Jul 2021 | 32.0 | 95.0 | 3.0x | 32.5% | 29.5 | Index Ventures 10.1%; NEA 8.9%; Ribbit Capital 7.6% |
| 11 | Snowflake | Sep 2020 | 33.2 | 94.4 | 2.8x | 26.7% | 25.2 | Sutter Hill 9.9%; Redpoint 7.9%; Sequoia Capital 7.5% |
| 12 | Spotify | Apr 2018 | 26.5 | 84.2 | 3.2x | 2.6% | 2.2 | Accel 2.0%; Kleiner Perkins 0.6% |
| 13 | Pinduoduo (PDD) | Jul 2018 | 29.6 | 83.5 | 2.8x | 20.5% | 12.7 | Banyan Partners 9.3%; HongShan 4.1%; Sequoia Capital 2.7% |
| 14 | Datadog | Sep 2019 | 7.8 | 80.3 | 10.3x | 44.7% | 32.0 | Index Ventures 18.5%; OpenView 14.6%; Meritech 3.6% |
| 15 | Nu Holdings (Nubank) | Dec 2021 | 41.5 | 61.9 | 1.5x | 30.3% | 18.7 | Sequoia Capital 16.2%; Founders Fund 4.1%; Kaszek 3.9% |
| 16 | DoorDash | Dec 2020 | 32.4 | 60.1 | 1.9x | 27.1% | 16.3 | Sequoia Capital 16.3%; Khosla Ventures 2.5%; CRV 2.5% |
| 17 | Astera Labs | Mar 2024 | 5.6 | 54.5 | 9.7x | 10.8% | 5.9 | Sutter Hill 10.8% |
| 18 | CoreWeave | Mar 2025 | 18.6 | 41.6 | 2.2x | – | – | none (largest holders: Magnetar, the founders, Fidelity) |
| 19 | Atlassian | Dec 2015 | 4.4 | 39.2 | 8.9x | 6.9% | 0.3 | Accel 6.9% |
| 20 | Coinbase | Apr 2021 | 52.2 | 38.2 | 0.7x | 42.0% | 14.5 | Andreessen Horowitz 14.1%; Union Square Ventures 6.7%; Ribbit Capital 5.7% |

**What stands out:**
- **Concentration.** The 20 most valuable listings are worth $4.3trn, 74% of the universe's $5.7trn, and the top ten alone 63%. SpaceX, listed in June 2026, is worth $2.1trn, more than the next nine together.
- **Compounding after listing.** Shopify is worth 89 times its value at listing, Arista Networks 77 times, CrowdStrike 32 times, Cloudflare 23 times and Palantir 20 times. Ten of the 20 listed in 2020 or later, so much of their value was created before listing; Coinbase is worth less than at its 2021 direct listing (0.7x).
- **Venture ownership varies widely.** Venture funds held half of Cloudflare at listing and 45% of Datadog and Shopify, but 2.6% of Spotify and 11% of SpaceX and Palantir. Alibaba (SoftBank and Yahoo), Arista Networks (its founders) and CoreWeave (Magnetar, the founders and Fidelity) had no venture-fund holder at listing.
- **What venture funds created.** Venture funds' primary stakes in these 20 companies are worth $519bn, 63% of all venture primary value in the universe. Founders Fund (SpaceX, Palantir, Airbnb, Nubank), Sequoia (seven of the 20) and Accel (CrowdStrike, Spotify, Atlassian) hold the most of it.
- **Atlassian** has one venture holder, Accel: 6.9% on its Schedule 13G three weeks after the listing (press reports gave 11.2%, kept as the high case). Accel bought most of its shares from insiders (CNBC: $60m of shares in 2010), so its primary value is small ($0.3bn).

---

## 4. The 20 funds with the most value per dollar

**What a fund is here.** One generation of a firm's funds: the main fund with the parallel, principals', entrepreneurs' and annex vehicles that invest beside it. Founders Fund II includes its principals' and entrepreneurs' funds; Bessemer Venture Partners VII includes its 2009 Special Opportunity Fund, which took 53–54% of each Fund VII deal checked.

**How each firm's stakes are split across its funds.**
- **From filings.** For each position worth $0.3bn or more held by a firm that could have a top-20 fund, the shares held at the listing were split by fund, where the filings allow, from:
  - directors' and 10% holders' Forms 3 and 4, which list each fund's shares;
  - Schedule 13G cover pages, where each fund is a reporting person;
  - 13F information tables by manager, prospectus footnotes and investors' rights agreements.
- **Coverage.** 36 firms and 234 positions were split this way, 72% of the ranked firms' primary value: 69% from per-fund share counts and 3%, mainly DFJ's SpaceX stake, from Form ADV asset values or press.
- **The rest** goes to the fund named in the holder's name where it identifies one (9%), otherwise to the fund whose investment period covers the firm's entry (19%). Late-stage entries go to growth funds, and a firm's funds for the company's country are used where it has them. Some large positions had no per-fund filing and follow this rule, among them Redpoint's Snowflake, Andreessen Horowitz's SpaceX and Kaszek's Nubank.
- **Look-through.** Shares later moved into continuation or roll-over vehicles are credited to the fund that bought them: DFJ's two continuation funds, Altos Ventures IV's 2019 liquidity fund and Sequoia's Grove vehicles.
- **Not credited to any fund.** $28.0bn of the ranked firms' value sits in single-company vehicles and other vehicles outside any fund generation. The largest are Gigafund's SpaceX vehicles ($8.1bn), Founders Fund's Lembas II ($7.7bn, SpaceX), DFJ Growth's single-company vehicles ($3.2bn, mainly SpaceX), Founders Fund's general partner holding company ($3.0bn, SpaceX), Lightspeed's Rubrik vehicles ($1.6bn) and the Sequoia Capital Fund ($1.2bn, SpaceX).

**How funds are measured.** As firms are: primary shares only, valued at the 2 October 2026 close; capital at risk = commitment × the timing weight for the fund's vintage and strategy (§10.7); the same consistency-adjusted headline.
- Shares a fund bought from other holders score zero, as at firm level.
- Because a fund holds fewer listed companies than its firm, the adjustment bites harder. UV Partners IV makes 152x on Cloudflare alone and scores 27.7x.

**Ranked:** the funds of the 147 ranked firms. **Not ranked:**
- single-company vehicles;
- evergreen or annual-deployment pools with no fixed size or vintage: Sutter Hill's evergreen fund and Y Combinator's standard deals before 2018;
- co-investment schemes that span fund generations (Index's Yucca);
- the funds of firms listed separately (§6).

**The range** recomputes each fund's figure with estimated stakes and primary shares at their low and high cases, low-confidence fund sizes halved and doubled or their documented range, and estimated splits between funds at their low and high cases.

| Rank | Fund | Firm | Vintage | Committed ($m) | Capital at risk ($m) | Value created ($bn) | Value per $ at risk | Consistency-adjusted value per $ | Range | Largest company (share of value) | How the holding is known |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | Founders Fund II | Founders Fund | 2007 | 220 | 139 | 37.4 | 269.3x | 183.5x | 152.9x–189.8x | SpaceX (68% of 4) | Schedule 13G |
| 2 | Bullet Time Ventures (Fund I) | Techstars Ventures | 2009 | 4.85 | 4.40 | 0.44 | 99.9x | 53.3x | 36.3x–66.5x | Uber (85% of 2) | press for Uber (no filing names the holder); investors' rights agreement for Twilio |
| 3 | Founders Fund III | Founders Fund | 2010 | 250 | 220 | 16.1 | 73.4x | 52.2x | 48.7x–54.2x | Palantir (64% of 3) | Form 3 |
| 4 | Index Ventures VI | Index Ventures | 2012 | 459 | 419 | 21.2 | 50.6x | 39.7x | – | Datadog (52% of 6) | Form 3 |
| 5 | Lowercase Ventures Fund I | Lowercase Capital | 2010 | 8.50 | 8.03 | 2.0 | 243.1x | 38.1x | 32.4x–45.7x | Uber (100% of 1) | prospectus total; split by vehicle reconstructed |
| 6 | FirstMark Capital I | FirstMark | 2006 | 220 | 129 | 12.6 | 97.8x | 37.2x | 34.9x–40.7x | Shopify (95% of 2) | Schedule 13G |
| 7 | Sequoia Capital XII | Sequoia Capital | 2006 | 481 | 282 | 15.4 | 54.6x | 35.4x | 31.4x–37.9x | Airbnb (73% of 4) | Form 3 |
| 8 | IA Venture Strategies Fund I | IA Ventures | 2010 | 50.0 | 47.2 | 2.2 | 46.5x | 33.2x | 30.2x–33.2x | Datadog (64% of 2) | investors' rights agreement |
| 9 | First Round Capital II | First Round Capital | 2008 | 125 | 105 | 4.2 | 40.3x | 29.0x | – | Uber (63% of 3) | prospectus (FRC II as nominee for its generation) |
| 10 | UV Partners IV (Pelion) | Pelion | 2007 | 120 | 88.4 | 13.5 | 152.5x | 27.7x | – | Cloudflare (100% of 1) | Form 3 |
| 11 | Bessemer Venture Partners VII (incl. Special Opportunity Fund) | Bessemer | 2007 | 1,350 | 807 | 37.8 | 46.8x | 27.3x | – | Shopify (81% of 3) | Schedule 13G |
| 12 | DFJ Growth Fund 2006 | DFJ | 2006 | 290 | 61.7 | 5.9 | 95.5x | 24.5x | 13.4x–34.6x | SpaceX (99% of 2) | estimate: DFJ's SpaceX stake split by the funds' Form ADV asset values |
| 13 | Union Square Ventures 2008 | Union Square Ventures | 2008 | 156 | 123 | 4.3 | 35.0x | 24.3x | – | Twilio (67% of 2) | Form 3 |
| 14 | Founders Fund IV | Founders Fund | 2011 | 625 | 570 | 17.9 | 31.4x | 23.1x | 21.7x–24.0x | SpaceX (61% of 8) | Schedule 13G |
| 15 | Amplify Partners (Fund I) | Amplify Partners | 2012 | 57.1 | 52.4 | 2.3 | 44.6x | 21.0x | 10.7x–32.8x | Datadog (91% of 2) | investors' rights agreement; stake estimated from rounds |
| 16 | The Founders Fund (Fund I) | Founders Fund | 2005 | 50.0 | 20.9 | 1.6 | 78.0x | 17.4x | – | Palantir (100% of 1) | Form 3 |
| 17 | Contour Venture Partners (Fund I) | Contour Venture Partners | 2006 | 23.5 | 14.5 | 1.1 | 75.2x | 17.0x | 15.1x–17.0x | Datadog (100% of 1) | Form 3 |
| 18 | Felicis Ventures II | Felicis | 2010 | 40.0 | 37.8 | 1.4 | 37.7x | 16.9x | 6.3x–36.6x | Shopify (93% of 4) | investors' rights agreement; split with a Felicis vehicle estimated |
| 19 | Founder Collective (Fund I) | Founder Collective | 2009 | 40.0 | 36.3 | 0.85 | 23.4x | 16.5x | – | The Trade Desk (66% of 2) | Form 3 |
| 20 | Sequoia Capital U.S. Venture Fund XIV | Sequoia Capital | 2012 | 653 | 596 | 12.9 | 21.6x | 16.2x | 14.5x–16.8x | Nubank (58% of 3) | Schedule 13G |

**What stands out:**
- **Founders Fund II is in a class of its own.** A $220m fund of 2007, it was Founders Fund's investing fund when the firm made SpaceX's first institutional investment in 2008, and it holds 43% of Founders Fund's SpaceX shares and 38% of its Palantir shares. With its Airbnb and Twilio stakes it is worth $37.4bn: 269x plain and 183x adjusted, more than three times any other fund. Four Founders Fund generations are in the top 20 (II, III, IV and Fund I).
- **Small seed funds with one great company.**
  - Bullet Time Ventures I, David Cohen's $4.85m fund of 2009 (now Techstars Ventures), turned a $50,000 cheque in Uber's 2010 seed, and a stake in Twilio's 2009 seed, into $0.44bn: 100x plain, 53x adjusted.
  - Lowercase Ventures Fund I ($8.5m, 2010) holds about two-thirds of Lowercase's Uber shares, all bought from the company: 243x plain, 38x adjusted.
  - On the adjusted measure, IA Venture Strategies Fund I ($50m) scores 33x on Datadog and The Trade Desk, Contour Venture Partners I ($23.5m) 17x on Datadog and Founder Collective I ($40m) 16.5x on The Trade Desk and Uber.
- **Larger funds with broad records.** Index Ventures VI ($459m; Datadog, Robinhood, Figma) scores 39.7x and Sequoia Capital XII ($481m; Airbnb's seed, Dropbox, Unity) 35.4x. Bessemer Venture Partners VII ($1.35bn with its Special Opportunity Fund; Shopify, Twilio, Pinterest) is the largest fund in the top 20, at 27.3x.
- **The same companies recur.** Datadog is the largest company in four top-20 funds (Index VI, IA I, Amplify I, Contour I), Uber in three (Bullet Time I, Lowercase I, First Round II) and Shopify in three (FirstMark I, Bessemer VII, Felicis II). SpaceX leads three (Founders Fund II and IV, DFJ Growth 2006).
- **Vintages.** All 20 are of vintage 2005–2012. Later funds' best companies are mostly still private or listed recently, and their timing weights already allow for that.
- **Just outside:** Gigafund 0 (15.9x), Andreessen Horowitz Fund I (15.8x), Accel Growth Fund II (15.5x), K9 Ventures I (13.3x) and Accel Leaders Fund (12.6x). Their ranges overlap those of ranks 15–20.
- **Not ranked, but high:**
  - NYC Seed's fund (Datadog) would score 45.4x; NYC Seed is a public economic-development fund (§6).
  - Y Combinator's standard deals before 2018 would score 34.6x as one pool.
  - Capricorn's Technology Impact Growth Fund I (SpaceX) would score 26.0x; Capricorn is listed separately.
  - OpenView Venture Partners IV (Datadog) would score 13.9x; OpenView is listed separately at Odin's request, pending review (§6).
  - Sutter Hill's evergreen fund would score 12.5x as one pool.
  - Single-company vehicles are not ranked. The highest would be Felicis's Clover Fund (21.8x, Shopify) and Benchmark's 2026 Cerebras vehicles (42.4x, because a 2026 vintage counts less than 1% of its capital).
- **Where the evidence is weaker** (the widest ranges):
  - DFJ Growth Fund 2006: no filing gives SpaceX shares by fund, so DFJ's stake is split by the asset values its adviser reports for each vehicle.
  - Felicis Ventures II: Shopify's coattail agreement names Felicis II and Clover Fund, a Felicis vehicle that raised $7m in October 2013, but gives no counts, so about 35% of Felicis's Shopify shares is assumed to sit in Clover (range 0%–50%).
  - Lowercase Ventures Fund I: the Uber prospectus gives one total for three Lowercase vehicles; the split is reconstructed from the shares each offered in the IPO's over-allotment option and from round prices (§7). A 2010 single-investor Lowercase vehicle ($11.07m) that bought Twitter shares from holders is treated as a secondary vehicle, as at firm level; counted in Fund I's capital, it would roughly halve the fund's figure.
  - Amplify Partners I: Amplify's Datadog stake is a round estimate.
  - Bullet Time Ventures I: no filing names the Uber holder; the evidence is David Cohen's own account of the fund.

---

## 5. What drives the top 25

For each firm: the listings that contribute most primary value at 2 October 2026, with the round and year of the firm's first investment, and the two funds that carry most of its capital at risk.
- For every SpaceX holder, the value shown is the part counted as primary.
- Fund sizes shown are the in-scope amounts.
- Sutter Hill's capital is shown as estimated capital deployed per year.

| Rank | Firm | Largest contributors (primary value, $bn; first round) | Capital at risk mostly from |
|---:|---|---|---|
| 1 | Sutter Hill | Snowflake 9.3 (Series Seed 2012); Astera Labs 5.9 (Series A 2018); Pure Storage 3.6 (Series A 2009) | Sutter Hill capital deployed 2021 (2021, $400m); 1962 Opportunity Fund I (2024, $750m) |
| 2 | Founders Fund | SpaceX 59.9 (Series D 2008); Palantir 26.2 (Series B 2006); Airbnb 4.3 (Series C 2012) | Founders Fund Growth II (2022, $3431m); Founders Fund Growth (2020, $1500m) |
| 3 | IA Ventures | DigitalOcean 2.1 (Seed 2013); Datadog 1.4 (Seed 2010); The Trade Desk 0.8 (Seed 2010) | IA Venture Strategies Fund III (2015, $160m); IA Venture Strategies Fund II (2011, $105m) |
| 4 | Gigafund | SpaceX 11.0 (Series H 2017) | Gigafund 0.6 (2020, $72m); Gigafund 0.2 (2018, $46m) |
| 5 | Lowercase Capital | Uber 2.2 (Seed 2010); Slack 0.1 (Series E 2015) | Lowercase Frontier (2014, $46m); Lowercase Spur (2012, $34m) |
| 6 | Pelion | Cloudflare 15.1 (Series A 2009) | Pelion Ventures VI (2015, $206m); Pelion Ventures VII (2019, $365m) |
| 7 | Union Square Ventures | Twilio 2.9 (Series A 2009); Coinbase 2.5 (Series A 2013); Cloudflare 1.8 (Series C 2012) | USV Opportunity 2019 (2018, $238m); USV Opportunity 2014 (2014, $166m) |
| 8 | Benchmark | Uber 9.3 (Series A 2011); Cerebras 3.0 (Series A 2016); Confluent 1.1 (Series A 2014) | Benchmark Capital Partners VII (2010, $425m); Benchmark Capital Partners VIII (2013, $425m) |
| 9 | Bessemer | Shopify 30.6 (Series A 2010); Twilio 6.1 (Series B 2010); Rocket Lab 6.0 (Series B 2015) | Bessemer Venture Partners X L.P. (2018, $1850m); Bessemer Venture Partners VIII… (2010, $885m) |
| 10 | DFJ / Draper Fisher Jurvetson | SpaceX 25.8 (Series E 2009); Coinbase 1.3 (Series C 2015); Box 0.7 (Series A 2006) | DFJ Growth IV (2020, $810m); DFJ Growth 2016 (2016, $535m) |
| 11 | Greylock | Airbnb 3.7 (Series A 2010); Pure Storage 3.6 (Series B 2010); Okta 2.8 (Series A 2010) | Greylock XIV Limited Partnership (2013, $963m); Greylock XIII Limited Partnership (2009, $920m) |
| 12 | Sequoia Capital | SpaceX 15.1 (Series L 2019); Airbnb 13.2 (Seed 2009); Nu 10.1 (Seed 2013) | Sequoia Capital Global Growth Fund III -… (2018, $8004m); Sequoia Capital Global Growth Fund II (2015, $2000m) |
| 13 | FirstMark | Shopify 12.0 (Series A 2010); Pinterest 0.9 (Series 1 2009); Airbnb 0.3 (Series E 2015) | FirstMark Capital OF IV (2022, $550m); Firstmark V (2011, $225m) |
| 14 | Index Ventures | Datadog 13.7 (Series A 2012); Robinhood 8.9 (Seed 2013); Figma 1.3 (Seed 2013) | Index Ventures Growth VI (2021, $2000m); Index Ventures Growth IV (2018, $1000m) |
| 15 | Founder Collective | The Trade Desk 0.6 (Seed 2010); Uber 0.3 (Seed 2010) | Founder Collective II (2012, $70m); Founder Collective III (2016, $75m) |
| 16 | First Round Capital | Uber 2.7 (Seed 2010); Roblox 1.5 (Seed 2009); Upstart 0.1 (Seed 2012) | First Round Capital V (2014, $175m); First Round Capital IV (2012, $149m) |
| 17 | Granite Ventures | Anaplan 0.8 (Series B 2011); Marqeta 0.2 (Series A 2011) | Granite Ventures II (2005, $350m); Granite Ventures (2000, $150m) |
| 18 | Venrock | Cloudflare 14.6 (Series A 2009); Quantenna 0.1 (Series A) | Venrock Associates V (2007, $600m); Venrock Opportunities Fund (2021, $675m) |
| 19 | Redpoint | Snowflake 7.5 (Series B 2014); Pure Storage 1.3 (Series C 2011); Nu 1.1 (Series D 2016) | Redpoint Omega IV (2021, $725m); Redpoint Ventures IV (2010, $400m) |
| 20 | Ribbit Capital | Robinhood 7.3 (Series A 2014); Coinbase 2.2 (Series A 2013); Nu 1.2 (Series E 2018) | Ribbit Bullfrog II (2021, $1150m); Bullfrog Capital (2020, $500m) |
| 21 | Contour Venture Partners | Datadog 1.6 (Seed 2011) | Contour Opportunity Fund III (2021, $75m); Contour Venture Partners II (2009, $40m) |
| 22 | Romulus Capital | EquipmentShare 1.0 (Series A 2016) | Romulus Capital III (2015, $83m); Romulus Capital II (2012, $42m) |
| 23 | Khosla Ventures | Rocket Lab 8.5 (Series A 2013); Block (Square) 3.8 (Series A 2009); DoorDash 1.5 (Seed 2013) | Khosla Ventures IV (2011, $1050m); Khosla Ventures V (2014, $1000m) |
| 24 | Gemini Israel | JFrog 1.2 (Series A 2012); WalkMe 0.1 (Series B 2012) | Gemini Israel V L.P. (2007, $150m); Gemini Israel IV L.P. (2004, $200m) |
| 25 | Accel | CrowdStrike 39.1 (Series B 2013); Slack 5.3 (Series A 2010); Spotify 1.7 | Accel Leaders 4 L.P. (2022, $4000m); Accel Leaders 3 L.P. (2020, $2255m) |

---

## 6. Firms not ranked

The main table ranks independent venture managers: firms that invest pooled capital from outside investors through limited-partnership funds, mainly in private technology companies. The firms below are measured the same way and listed separately.

**Firms Odin identified as outside the standard definition (October 2026):**

| Firm | Why not ranked | Consistency-adjusted value per $ | Value per $ at risk | Beyond largest company | Value ($bn) | Capital at risk ($bn) | Largest company |
|---|---|---:|---:|---:|---:|---:|---|
| LCP Quantum Partners | Invests through single-company vehicles (Infleqtion) | 5.4x | 15.3x | 0 | 0.39 | 0.03 | Infleqtion |
| OpenView | Moved out at Odin's request; fund records show conventional venture funds (under review) | 5.2x | 12.7x | 0.26x | 12.00 | 0.94 | Datadog |
| Hydrazine Capital ◊ | Sam Altman's fund; its investors include Peter Thiel and the University of Michigan (under review) | 5.1x | 10.4x | 0.75x | 1.57 | 0.15 | Reddit |
| Capricorn ◊ | Jeff Skoll's investment firm; SpaceX through single-purpose vehicles | 4.8x | 9.6x | 0.75x | 10.73 | 1.12 | SpaceX |
| Global Frontier ◊ | Mostly single-company: an Infleqtion vehicle, a small 2021 fund and a frontier-markets hedge fund | 4.6x | 12.2x | 0 | 0.34 | 0.03 | Infleqtion |
| BOKA Group ◊ | One single-company vehicle (Infleqtion) | 4.4x | 11.5x | 0 | 0.16 | 0.01 | Infleqtion |
| RTP Ventures | Leonid Boguslavsky's own capital; he is the dominant investor even in RTP Global's funds | 4.0x | 10.0x | 0 | 6.07 | 0.60 | Datadog |
| Mosaic Venture Partners | Moved out at Odin's request; fund records show conventional venture funds (under review) | 4.0x | 10.0x | 0 | 0.23 | 0.02 | Five9 |
| Vy Capital ◊ | Growth-stage investor; its SpaceX stake came through single-purpose vehicles and merger stock | 3.8x | 6.8x | 0.80x | 9.06 | 1.33 | SpaceX |
| Frazier Technology Ventures | Moved out at Odin's request; fund records show conventional venture funds (under review) | 3.6x | 8.7x | 0 | 0.68 | 0.08 | DocuSign |
| Commonwealth Capital | Moved out at Odin's request; fund records show conventional venture funds (under review) | 1.5x | 3.1x | 0 | 0.70 | 0.23 | Acacia |
| Evergreen Venture Partners | Moved out at Odin's request; fund records show conventional venture funds (under review) | 1.5x | 2.9x | 0 | 0.63 | 0.21 | Varonis |
| Morgan Creek Digital | Digital-asset fund manager | 1.4x | 2.6x | 0 | 0.22 | 0.08 | Figure |

- **Fund records show five of these to be conventional closed-end venture partnerships:** OpenView, Frazier Technology Ventures, Mosaic, Commonwealth Capital Ventures and Evergreen.
  - **OpenView:** seven funds with 2006–2022 vintages.
  - **Frazier Technology Ventures:** two funds, in 2000 and 2004.
  - **Mosaic:** two Toronto funds, in 1997 and 2000.
  - **Commonwealth Capital Ventures:** four Boston funds, 1995–2006. Its investors included U.S. Trust.
  - **Evergreen:** Israeli funds whose investors included HarbourVest and Illinois TRS.
  - All five invested in private technology companies. Restored one at a time, OpenView would rank 9th, Mosaic 11th, Frazier 13th, and Commonwealth and Evergreen 46th and 47th; restored together, 9th, 12th, 15th, 49th and 51st. They are listed here as Odin asked, pending review (§13).
- **Hydrazine Capital** is Sam Altman's fund. Its records also show outside institutional money: Peter Thiel provided most of Fund I, and the University of Michigan committed up to $100m to Fund II and $75m to Fund IV. Restored, it would rank 10th (5.1x, just behind Bessemer). It is listed here as Odin asked, pending review.
- **Single-company syndicates.** LCP Quantum Partners, Global Frontier and BOKA Group bought Infleqtion's 2020–25 rounds through vehicles whose only known holding is Infleqtion (mostly so for Global Frontier, which also has a small 2021 fund).
- **Proprietary capital.** RTP Ventures' Datadog stake was funded from Leonid Boguslavsky's own balance sheet, and he is the dominant investor even in RTP Global's funds.
- **Capricorn and Vy Capital.**
  - Capricorn is Jeff Skoll's investment firm (family office and impact funds).
  - Vy Capital is a growth-stage investor. Most of its capital is in pooled funds, but its SpaceX stake came through single-purpose vehicles and merger stock.
  - Both are measured on their SpaceX stakes as traced in version 4.
- **Morgan Creek Digital** is a digital-asset manager.

**The same test applied to the rest of the table:**

| Firm | Why not ranked | Consistency-adjusted value per $ | Value per $ at risk | Beyond largest company | Value ($bn) | Capital at risk ($bn) | Largest company |
|---|---|---:|---:|---:|---:|---:|---|
| OMERS Ventures | Venture arm of the OMERS pension plan | 1.8x | 3.8x | 0 | 3.03 | 0.80 | Shopify |
| SWaN & Legend | Consumer brands and restaurants, funded mainly by wealthy individuals (CAVA) | 1.5x | 2.9x | 0 | 0.61 | 0.21 | CAVA |
| GV ◊ | Invests Alphabet's own capital | 1.1x | 1.5x | 0.56x | 7.26 | 4.90 | Uber |
| Bluestem Capital ◊ | Generalist syndicate funds and single-company vehicles for regional investors | 0.59x | 1.0x | 0 | 0.11 | 0.11 | Workiva |
| Yorktown Partners | Energy-focused private equity (Solaris Oilfield) | 0.14x | 0.22x | 0 | 1.13 | 5.05 | Solaris Oilfield |

- **GV and OMERS Ventures** invest a corporation's or a pension plan's own capital. They were ranked with a label in version 4.
- **Yorktown** is an energy private-equity firm.
- **Bluestem** raises generalist syndicate funds and single-company vehicles from regional investors.
- **SWaN & Legend** backs consumer brands and restaurants with money mainly from wealthy individuals, and its book position is CAVA.
- **Kept in the main table:**
  - **Sutter Hill:** one evergreen fund (plus a 2024 opportunity fund). It is a venture firm investing in private technology, and its capital comes from its partners and a few endowments and foundations.
  - **Gigafund:** invests through a series of concentrated vehicles, most of them SpaceX, with about a third of its capital at risk in vehicles without SpaceX. On the single-company test applied to the Infleqtion syndicates it could be listed separately; it is kept pending review (§13).
  - **Norwest and Sapphire:** each has (or had) a single corporate investor, Wells Fargo and SAP respectively. Both are kept as separately branded managers, unlike GV, which invests Alphabet's capital directly; both are flagged in §13.
  - **Zeev Ventures:** has raised outside funds since 2014.

**Newly measured holders listed separately (version 7):**

| Firm | Why not ranked | Consistency-adjusted value per $ | Value per $ at risk | Beyond largest company | Value ($bn) | Capital at risk ($bn) | Largest company |
|---|---|---:|---:|---:|---:|---:|---|
| NYC Seed ◊ | Seed fund of New York City and State economic-development bodies, a university and a nonprofit (Datadog) | 45.4x | 315.6x | 0 | 0.50 | 0.00 | Datadog |
| K5 Global | Raises outside money mainly through single-company vehicles (SpaceX) | 1.8x | 3.6x | 0 | 1.55 | 0.43 | SpaceX |
| Protoscale Capital ◊ | Single-company vehicles (Rubrik) | 1.7x | 3.4x | 0 | 0.08 | 0.02 | Rubrik |
| VaynerRSE ◊ | Funded by Stephen Ross's RSE Ventures (Coinbase) | 0.89x | 1.6x | 0 | 0.03 | 0.02 | Coinbase |
| Avid Park ◊ | Venture vehicle with essentially one outside investor, run by a former hedge-fund manager | 0.52x | 0.88x | 0 | 0.08 | 0.09 | Rubrik |

- **NYC Seed** is a seed fund set up by New York City and New York State economic-development bodies with a university and a nonprofit. Its Datadog stake (0.62%) is large against its very small capital, hence the extreme figure; it is listed separately as a public economic-development fund.
- **K5 Global** raises outside money mainly through single-company vehicles, like the Infleqtion syndicates. Only its four SpaceX-named vehicles, whose first sales coincide with SpaceX's own primary offerings, are counted (0.074% of SpaceX). Vehicles matched to SpaceX rounds by date alone, and shares from later tender offers or the xAI merger, score zero.
- **Protoscale Capital** (Rubrik) invests through single-company vehicles; **Avid Park** (Rubrik) is a venture vehicle with essentially one outside investor; **VaynerRSE** (Coinbase) was funded by Stephen Ross's RSE Ventures.

**Family offices and individuals:**

| Firm | Why not ranked | Consistency-adjusted value per $ | Value per $ at risk | Beyond largest company | Value ($bn) | Capital at risk ($bn) | Largest company |
|---|---|---:|---:|---:|---:|---:|---|
| Cabaret Security | Invests one person's or one family's own money | not measurable | – | – | 0.76 | n/a | CyberArk |
| IGSB ◊ | Invests one person's or one family's own money | 3.7x | 9.0x | 0 | 1.80 | 0.20 | AppFolio |
| Rose Park Advisors ◊ | Invests one person's or one family's own money | 3.4x | 8.1x | 0 | 1.19 | 0.15 | Coupang |
| Breyer Capital ◊ | Invests one person's or one family's own money | 2.1x | 4.3x | 0 | 1.36 | 0.31 | Circle |
| Apollo Projects | Invests one person's or one family's own money | 1.4x | 2.8x | 0 | 0.20 | 0.07 | Reddit |
| David B. Blundin ◊ | Invests one person's or one family's own money | 0.81x | 1.4x | 0 | 0.22 | 0.15 | EverQuote |
| AME Cloud Ventures ◊ | Invests one person's or one family's own money | 0.72x | 1.2x | 0.08x | 0.52 | 0.44 | Zoom |
| Trilogy Equity Partners ◊ | Invests one person's or one family's own money | 0.65x | 1.1x | 0 | 0.21 | 0.19 | Remitly |
| Horizons Ventures (Li Ka Shing) ◊ | Invests one person's or one family's own money | 0.52x | 0.87x | 0 | 1.32 | 1.51 | Zoom |
| BRM Group ◊ | Invests one person's or one family's own money | 0.34x | 0.54x | 0 | 0.15 | 0.28 | eToro |

**Firms not measured:**
- **Cabaret Security** (Amnon Shoshani's holding company, a CyberArk seed investor) has no record of the amounts it deployed.
- **Family-office holders with no deployment records:** K1W1 (Sir Stephen Tindall, Rocket Lab), the Kraft family (Dave), Tao Capital (IonQ; also 10.6m SpaceX shares of unresearched origin), Morningside (the Chan family) and Emerson Collective. Artal / Invus and Act III Holdings (Ron Shaich), both in CAVA, and Global Oryx (Joby) are in the same position. The version 7 screen of prospectus holders found four more, outside the book: KOPACC (the Jamison family; about 4% of CoreWeave), Gemini Investments (a trust vehicle in Yuri Milner's DST group; 4.1% of Figure), Greenover Group (a Williams family vehicle; nLIGHT) and Green Bay Advisors (Dropbox; provisional).
- **Centillion Venture Capital** (A10 Networks, $0.11bn) cannot be sized without Taiwanese registry data. On assumed fund sizes it would land between 0.5x and 3.5x on the headline measure (0.9x–8.5x plain). A10's other Taiwanese holders (Enspire Capital, Harbinger III and H&A Venture Capital) are unmeasured for the same reason.
- **Renminbi-only managers** have no capital at risk in the main specification: Yuanzhan (Hesai), Rothsfortune (Chagee) and Dehui (Atour), and Webull's lead investors Bojiang and Hongdao, whose stakes are held mainly by renminbi partnerships. Dehui is a private-equity and advisory boutique.
- **Holders added in version 7 without fund histories.** These are in the book with their stakes but are not scored:

| Holder | Stakes (share of company) | Primary value ($m) | Why not scored |
|---|---|---:|---|
| Youniversity Ventures | Airbnb 0.52% | 504 | principals' own money (Jawed Karim, Keith Rabois, Kevin Hartz) |
| FundersClub | Coinbase 0.56% | 214 | invests mainly through single-deal vehicles for its members |
| TEEC Angel Fund | Zoom 0.78% | 186 | angel-club fund ($3.5m of assets and 21 owners on its Form ADV) |
| Three Kingdoms Capital | Zoom 0.70% | 167 | Matt Ocko's personal vehicle |
| IT-Farm | Zoom 0.65% | 155 | Tokyo venture manager with institutional investors; fund sizes not found; set aside by Odin (October 2026) |
| Pioneer Venture Partners | Avalara 2.42% | 147 | angel-group LLC investing its members' money; no Form D |
| Egan-Managed Capital | Acacia 3.29% | 135 | Egan family capital |
| Seed Capital Partners | CyberArk 1.00% | 121 | SoftBank-affiliated fund (corporate capital) |
| GlobalLink1 Capital | Astera Labs 0.17% | 92 | a personal charitable trust |
| A-Grade Investments | Airbnb 0.08% | 74 | principals' own money (Ashton Kutcher, Guy Oseary, Ron Burkle) |
| Amicus Capital | GrubHub 1.54% | 73 | no Form D, fund size or outside investor found; set aside by Odin (October 2026): appears largely inactive |
| Tim Draper (personal vehicles) | Box 1.28%, Twilio 0.05% | 63 | Tim Draper's own money (Draper Associates L.P., Riskmasters III) |
| Delta-V Capital | Zayo 0.60% | 50 | pooled funds; screened out (its 2011 fund alone is too large for the stake to reach the line) |
| QueensBridge | Coinbase 0.12%, Dropbox 0.00% | 46 | mainly the principals' own money (Nas and Anthony Saleh); no Form D |
| Liquid 2 Ventures | GitLab 0.39% | 28 | stake held in vehicles that predate its funds; screened out on fund sizes |
| Inspiration Ventures | UserTesting 4.64% | 25 | pooled funds; screened out on central assumptions (§8) |
| SciFi VC | Coinbase 0.06% | 22 | Max and Nellie Levchin's family vehicle |
| eValue | The Trade Desk 0.17% | 8 | corporate balance-sheet money (eValue AG) |
| Amidzad | Dropbox 0.05% | 6 | principals' own money (Pejman Nozad and the Amidi family) |

- **In all, 127 firms with value lack fund histories,** including those above. They hold 2.9% of core venture value. Of those that invest pooled outside capital, none could reach the top 50 on its known fund sizes, except possibly Centillion, whose fund sizes are unknown, and the renminbi-only managers (§10.8). Amicus Capital and IT-Farm, whose fund sizes are also unknown, were set aside by Odin in October 2026 (§8).

---

## 7. How firm is the order?

**Data ranges.** Most of the top 30 have narrow ranges, because their stakes come from prospectuses, Form 3 and 13G filings and their fund sizes from Form D filings and announced closes. The widest belong to:
- **Sutter Hill (7.8x–16.6x):** capital estimated year by year, using the documented range of its deployment path.
- **Lowercase (6.5x–12.2x):** the share of its Uber stake bought from other holders (5%–37%) and the size of the sidecar's Slack cheque ($2.5m–$15m, with the stake).
- **DFJ (2.8x–5.4x):** the size of its SpaceX stake (1.15%–1.85%) and the share bought from SpaceX (60%–90%).
- **Gigafund (6.7x–10.4x):** the three readings of its SpaceX vehicles.
- **Newly ranked firms resting on estimated stakes:** Glynn (1.5x–3.9x; Palantir), Amplify (1.3x–3.6x; Datadog), Harbor Pacific (1.2x–4.7x; Zoom), Red Swan (0.71x–3.8x; Coinbase) and Granite Hill (1.0x–3.0x; SentinelOne).
- **Other estimated stakes, outside the top 30:** SV Angel (32nd; 0.85x–4.6x) and Y Combinator (40th; 0.97x–3.0x).
- **Granite (2.0x–3.1x):** sizes of its pre-2001 vehicles and whether funds it managed for Adobe and Texas Instruments count.

Across the 147 ranked firms, 73% of capital at risk rests on high-confidence fund sizes, 20% on medium and 8% on low.

**Nineteen alternative specifications.**
- **Three test the consistency adjustment itself:** a fifth of the weight on depth (one company: 25x becomes 12.6x), half the weight (version 5's headline), and depth measured beyond the two largest companies.
  - With a fifth of the weight, the single-company records gain: Gigafund 15.0x and Lowercase 13.1x lead, then Founders Fund 12.8x, Sutter Hill 12.6x, Pelion 11.7x and IA Ventures 10.9x.
  - With half the weight, Sutter Hill (10.3x), Founders Fund (9.5x) and IA Ventures (9.0x) lead, then Union Square Ventures and Benchmark; Lowercase, Gigafund and Pelion fall to sixth, seventh and ninth.
  - Measured beyond the two largest companies, depth favours the concentrated records: Gigafund 9.1x leads, then Sutter Hill 8.8x, Founders Fund 7.8x, Lowercase 7.4x and IA Ventures 7.4x.
- **The other sixteen test capital at risk and the numerator.** IA Ventures reaches the top two under three of them: weighting by entry stage (first), shorter lags and larger low-confidence fund sizes (second in both).
- Sutter Hill and Founders Fund are the top two under 13 of the 19 checks. Sutter Hill leads under 12 of them, Founders Fund under four (pooled lags, longer lags, slower deployment and larger low-confidence fund sizes), Gigafund under two and IA Ventures under one. Founders Fund never falls below third and Sutter Hill never below fourth.
- Firms that cannot be computed under a check are held at their main figure, so their absence does not lift the others.

| Check | Rank correlation | Largest moves among the top 50 |
|---|---:|---|
| Half weight on depth (version 5's headline) | 0.992 | Y Combinator 40th → 29th; Revel 48th → 58th; NEA 43rd → 34th |
| One-fifth weight on depth (one company: 25x becomes 12.6x) | 0.996 | Contour 21st → 13th; a16z 28th → 35th; SV Angel 32nd → 39th |
| Depth measured beyond the two largest companies | 0.994 | Founder Collective 15th → 29th; Granite 17th → 27th; First Round 16th → 24th |
| Weight value by entry stage, as the stage-weighted ranking does | 0.947 | 8VC 45th → 99th; Glynn 26th → 70th; Mobius 50th → 92nd |
| Lags two years longer | 0.973 | Granite 17th → 40th; Section 32 37th → 17th; Highway 12 30th → 49th |
| Box weights (vintages 2004-2020 count in full, others not at all) | 0.980 | Celesta 44th → 67th; Banyan 34th → 56th; Cathay Innovation 47th → 65th (Mobius, with no 2004-2020 funds, held at its main figure) |
| No weight floor | 0.989 | Mobius 50th → 11th; Hummer Winblad 39th → 24th; Felicis 49th → 55th |
| One pooled lag distribution for all stages | 0.993 | Felicis 49th → 60th; Cathay Innovation 47th → 57th; First Round 16th → 24th |
| Lags one year shorter | 0.994 | Cathay Innovation 47th → 57th; Felicis 49th → 58th; Highway 12 30th → 21st |
| Include sensitivity-only funds (renminbi, crypto, secondary vehicles, unclear purpose) | 0.997 | Altos 41st → 58th; Granite 17th → 32nd; Banyan 34th → 44th |
| Deduct the life-sciences share of generalist funds | 0.997 | Section 32 37th → 17th; NEA 43rd → 33rd; Venrock 18th → 11th |
| Slower deployment | 0.997 | Granite 17th → 25th; Gemini Israel 24th → 30th; Highway 12 30th → 36th |
| Low-confidence fund sizes x0.7 | 0.998 | Revel 48th → 43rd; Altos 41st → 36th; Hummer Winblad 39th → 35th |
| Low-confidence fund sizes x1.3 | 0.999 | Mobius 50th → 55th; Revel 48th → 53rd; Altos 41st → 45th |
| US and global funds only (funds dedicated to Europe, Israel, China, India or South-East Asia removed) | 0.997 | Granite Hill 35th → 18th; Accel 25th → 17th (firms with no US or global funds held at their main figure) |
| IPO-market timing (weights follow hot and cold listing years) | 1.000 | none more than 3 places |
| Faster deployment | 1.000 | none more than 2 places |
| Sequoia Global Growth funds at 50% | 1.000 | none more than 2 places |
| Keep the Sequoia Global Equities and Heritage positions | 1.000 | none more than 1 place |

**Excluding SpaceX** answers a different question (rank correlation 0.952).
- Sutter Hill leads alone; IA Ventures, Lowercase, Pelion and Union Square Ventures follow.
- Founders Fund falls to eighth (3.8x on Palantir, Airbnb and its other listings), Sequoia to 15th (3.0x) and DFJ to 77th (0.91x).
- Gigafund has no other listing.

**Judgments behind the figures:**
- **Sutter Hill's capital.**
  - Sutter Hill invests mainly from one evergreen fund, so its capital at risk is estimated as capital deployed each year (plus its 2024 opportunity fund).
  - **Revision.** Version 4 calibrated the path to statements such as "big buyer" in rounds. Version 5 prices what the fund itself paid in its three largest listed companies: Pure Storage $62.5m, Snowflake $101m and Astera Labs $42m, from its Form 3 holdings by share class at each class's issue price. These are far smaller than the old anchors.
  - **Result.** With a lower deal pace (5–10 financings a year, about 8 assumed), deployment over 2009–24 falls from $2.35bn to $1.86bn (range $1.12bn–$3.01bn). Capital at risk falls 17%, to $1.33bn.
  - At version 4's capital Sutter Hill would make 9.6x, third behind Founders Fund and IA Ventures.
- **DFJ's SpaceX stake.**
  - **No filing gives a count.** DFJ's funds file no 13F or 13G for SpaceX. Steve Jurvetson's Form 3 as a SpaceX director reports no holdings, and Randy Glein's (DFJ Growth) only 277,800 personal shares, so neither covers the funds.
  - **Press figure.** Forbes (June 2026) reports that DFJ's growth fund invested over $800m in SpaceX from 2009 and expects a stake worth about $33bn at the listing. Converted at the share prices implied by Forbes's figures for Founders Fund and Valor, that is 202m–234m shares (1.53%–1.78%); at the $135 offer price it is 1.85%.
  - **Cross-check.** DFJ's $10m in the 2009 Series E alone is 111m shares after splits (0.84%). The 2010 Series F, the 2018–22 single-purpose vehicles (about 0.27%) and fund-level buying in later rounds take the total to 200m–250m shares, consistent with Forbes.
  - **Counted:** 1.54% (low 1.15%, high 1.85%), net of a separate xAI-derived slice that scores zero. 80% is counted as bought from SpaceX (60%–90%): the 2009–10 rounds and the vehicles dated to primary rounds, but not purchases made in tender offers.
  - **No count yet (checked 18 October 2026).** No DFJ, DFJ Growth or Threshold entity has filed a 13F, 13G or Form 3/4 listing SpaceX shares. A manager becomes subject to 13F reporting for the December quarter of the first year in which its listed holdings pass $100m, so DFJ's first 13F that could show SpaceX covers 31 December 2026 and is due by mid-February 2027.
  - **A cross-check from the fund research (§4).** The asset values DFJ's advisers report in Form ADV for the vehicles holding SpaceX at the end of 2025, converted at the December 2025 tender price, imply about 1.9% or more of SpaceX after the xAI merger, above the 1.85% high case. The marks are the advisers' own and the vehicles may hold other assets, so the estimate is kept, but DFJ's stake may be understated (§13).
  - **Effect:** DFJ makes 4.4x (10th; range 2.8x–5.4x). Without SpaceX it would make 0.91x.
- **Lowercase Capital.**
  - **The Uber stake by vehicle.** The Uber prospectus names three Lowercase vehicles holding 43.7m shares in all: Lowercase Ventures Fund I (about 28.7m shares: Sacca's $300K 2010 seed cheque and a $400K Series A cheque), Lowercase Spur (about 4.1m, a Series B pro rata) and Lowercase Industry Fund II-A (about 10.9m).
  - **The secondary vehicle.** Industry Fund II-A raised $3.5m from two investors in July 2011, when no primary round was open, and Forbes reported Travis Kalanick's anger at Sacca's attempts to buy shares from early investors. Its shares are treated as bought from holders: 25% of the stake (range 5%–37%). Its capital, and that of the 2010 Industry Fund (a Twitter vehicle), leave capital at risk.
  - **Twilio.** Twilio's 2015 investors' rights agreement lists no Lowercase entity, and Forbes calls Twilio a Sacca "individual investment", so no Twilio stake is counted.
  - **The RT fund and the sidecar (settled in version 8).** A commercial database record reviewed by Odin lists Lowercase RT Fund (Form D September 2010, about $20m from one investor) as the investor in Slack's April 2015 Series E and shows it as a multi-company fund. RT is therefore in scope; its Twitter purchases predate the window, and no Twilio stake is counted. Slack's 2019 investors' rights agreement lists Lowercase RT GP, LLC and Lowercase Sidecar, LP. The sidecar filed no Form D and co-invested in that one deal, so its capital is its Slack cheque: $7.5m central, $2.5m–$15m with the stake (0.23%, range 0.07%–0.46%). Version 7 had carried it as a $40m placeholder.
  - **Result.** 23.4x plain and 8.8x adjusted (fifth; range 6.5x–12.2x).
- **SpaceX holdings.** Version 4's vehicle-by-vehicle tracing stands for the other holders. What counts:
  - Founders Fund 92% (80%–99%); Sequoia 78%; Gigafund 40% (25%–62%); Andreessen Horowitz 40%; DFJ 80% (60%–90%).
  - Counting only blocks matched exactly to a primary round (the low cases) leaves Founders Fund at 10.6x (still second), Gigafund 8.3x and Sequoia 3.5x.
- **IA Ventures' Datadog stake (new in version 7).** IA Venture Partners' first 13F after the listing (December 2019) shows 4,076,698 shares. Grossed up for the 20% of locked-up shares released early, the holding at the listing is 5,095,872 shares, 1.76% (low case 1.41%, the 13F count alone). It came from the 2010 NYC SeedStart programme and the April 2011 seed round.
- **Estimates from rounds and share residuals (new in version 7).**
  - **Datadog:** Amplify's 2.64% (1.05%–4.77%) is a round estimate: assumed cheques in a 2012 seed extension and in Series A–D at each series' price. It was checked against the seed and Series A shares not held by Contour, Index, RTP or ICONIQ (about 7.7% of the company, shared by IA Ventures, Amplify, RRE, NYC Seed and about ten angels).
  - **Cloudflare:** Union Square Ventures' 1.71% (1.28%–2.57%) is the Series C left after the directors' Form 3 holdings.
  - **Zoom and SentinelOne:** Harbor Pacific's 0.62% is a residual by share series; Granite Hill's 1.95% is round arithmetic at each series' issue price.
- **Glynn Capital (new in version 7).** Glynn's 13F filings included locked-up venture shares until late 2017, which gives near-exact counts for Okta, Etsy and Pure Storage. Only its venture funds (Glynn Partners) count. Its Emerging Opportunity funds hold public as well as private stocks and are excluded from both capital and value, as Sequoia's Global Equities fund is. Its Palantir stake (0.41%) is a round estimate, hence the wide range.
- **March Capital (new in version 7).** Its CrowdStrike stake (2.70%) combines the 2017 Series D block (2.23%), pinned exactly by the 4,392,492-share threshold in CrowdStrike's amended stockholders' agreement, with an estimate for the 2018 Series E (0.46%, range 0.15%–1.24%). Its KnowBe4 shares, absent from KnowBe4's last-round investor agreement, are treated as bought from holders and excluded.
- **Pinduoduo.** Banyan Partners' 178.8m Series A-2 block was transferred from Colin Huang's holding vehicle, so 43% of Banyan's stake is treated as bought from the founder. If that vehicle held the shares as Banyan's nominee, Banyan would make 3.0x.
  - HongShan's Series C-1 shares were issued against cancelled founder shares, so 31% is treated the same way.
- **Granite Ventures.** Its Anaplan and Marqeta stakes came mainly from Granite Ventures II ($350m, 2005). Granite descends from Hambrecht & Quist's venture group: its pre-2001 vehicles are included (estimated), and funds it ran for Adobe and Texas Instruments count only in the low case.
- **Stakes revised in earlier verification.** First Round's Square stake is 0.3% (not the estimated 1.8%), because any holder above 0.51% of Square's 31.7m Class A shares had to file a Schedule 13G and First Round filed none. Y Combinator's Airbnb stake is 0.9%.
- **Positions not assessed.** 175 small positions ($3.2bn at 2 October 2026 prices, under 0.5% of core value) were never assessed for primary purchase and score zero.

**Size.** Value rises 1.05% for each 1% of extra capital at risk (Poisson pseudo-maximum likelihood across the 147 ranked firms, standard error 0.09). The measure neither rewards nor punishes size mechanically.

---

## 8. Coverage and attribution checks (versions 7 and 8)

*Version 7 searched for stakes the prospectus holder tables miss. Version 8 traced the large stakes to individual funds and corrected what the fund-level filings showed (end of this section).*

**Why it was needed.**
- Version 6 built holdings mainly from prospectus principal-holder tables, which list only holders of 5% or more and those tied to directors.
- Smaller stakes came from Forms 3 and 4, 13F filings, investor agreements and press. That favours firms that are large, sit on boards or are covered by the press.
- The likeliest casualties were small seed funds with stakes below 5% in very large companies: exactly the firms that can score highly per dollar.

**What was done.**
1. **Investor-agreement sweep.** For the 147 listings worth $3bn or more at 2 October 2026 (97% of the universe's value), the pre-listing investors' rights, registration rights or shareholders' agreement was read where one was filed: 1,985 holder entries across 138 listings. The fetch tool stops at about 120,000–140,000 characters, so long agreements lost their investor schedules; others were filed with blank schedules, and for seven companies (Uber, Robinhood and Wayfair among them) no agreement was found. Snap and Spotify were covered only by the 13F sweep and the name probe.
2. **13F reverse sweep.** For the same listings, EDGAR full-text search listed every 13F filer holding the company at the first quarter-end after listing, and the venture filers' share counts were read: 971 rows across 142 listings. 13F shows only listed share classes, so stakes held as unlisted Class B shares or as ordinary shares behind ADSs do not appear.
3. **Full-text name probe.** For the 72 listings whose investor lists were cut off, left blank or never filed, 128 firm names (160 search phrases) were searched across every registration statement and exhibit each company filed: 1,280 searches.
   - They returned 250 (firm, listing) matches, 111 of them not already in the book.
   - 46 became sized positions and 39 were settled during sizing as not holdings, mostly biographies or other managers' "Founders' Fund" vehicles.
   - 26 were false matches on common words ("streamlined", "battery", "valor") or product names (Palantir's "Contour").
4. **Sizing.** Two rounds of research (12–18 October) sized each new position as a share of the company's post-offering shares, with a central estimate and a low–high range. Each was graded as bought from the company or from holders, and fund histories were built for firms that could reach the top 50.
   - **Evidence, in order of preference:** directors' Form 3s at the listing, 13F counts inside the lock-up, investor-agreement schedules, share residuals by series, and round arithmetic.
5. **Closing screens (18 October).** Six pairs no one had yet examined, and nine prospectus holders that had never reached the book, were classified and screened against the top-50 line.

**Every missing pair has an outcome.** The sweeps found 328 (firm, listing) pairs missing from the book. The register (`vc_gap_register_v16_final.csv`) records the outcome of each:

| Outcome | Pairs |
|---|---:|
| Added to the book: ranked firm | 118 |
| Added with zero primary value (bought from holders, or origin not established) | 11 |
| Added: firm listed separately (§6) | 5 |
| Added: holder without a fund history (§6) | 22 |
| Checked and not added (duplicate, false match, personal money, immaterial) | 31 |
| Checked: holding not established | 2 |
| Screened: cannot reach the top-50 line | 20 |
| Immaterial 13F lot (possibly an IPO allotment) | 11 |
| Outside the per-dollar ranking by type: growth, crossover, hedge or mutual funds 42; funds of funds and secondaries managers 24; corporate, holding-company or sponsor capital 12; family offices and individuals 13; government-funded 8; crypto funds 4; venture lenders 4; SPV platform 1 | 108 |
| **Total** | **328** |

**What was added.** 181 holder lines for 99 firms, 162 of them with primary value: $69.9bn at 2 October 2026 in all, or $44.1bn excluding DFJ's SpaceX stake.
- $65.5bn goes to 73 ranked firms (75 received new lines), $2.2bn to firms listed separately and $2.1bn to 19 holders without fund histories.
- The largest additions to ranked firms:

| Firm | Value added ($bn) | Main stakes added | Rank in version 6 → 8 |
|---|---:|---|---|
| DFJ / Draper Fisher Jurvetson | 27.8 | SpaceX 1.54%, Coinbase 3.47%, Unity 3.22% | 82 → 10 |
| March Capital | 5.7 | CrowdStrike 2.70% | new → 31 |
| IVP | 3.2 | Coinbase 3.33%, Robinhood 0.69%, Pure Storage 1.86% | 88 → 82 |
| Kaszek | 2.4 | Nubank 3.80% | new → 62 |
| Amplify Partners | 2.1 | Datadog 2.64% | new → 27 |
| Glynn Capital | 2.1 | Palantir 0.41%, Okta 2.03%, Etsy 2.87% | new → 26 |
| Mithril Capital | 1.9 | Palantir 0.54%, Reddit 0.30%, Figure 0.40% | new → 64 |
| Union Square Ventures | 1.8 | Cloudflare 1.71% | 9 → 7 |
| Index Ventures | 1.7 | Pure Storage 3.69%, Slack 1.24%, Dropbox 1.56% | 13 → 14 |
| IA Ventures | 1.4 | Datadog 1.76% | 7 → 3 |
| QED Investors | 1.4 | Nubank 2.20% | new → 83 |
| Walden International | 1.0 | Credo 3.24% | new → 84 |

- **Corrections to existing lines:**
  - **DFJ's Box stake** falls from 18.5% to 17.2%. 1.49m of its shares belonged to Draper Associates L.P., Tim Draper's own vehicle (DFJ's Form 3 at the listing).
  - **Redpoint's Twilio stake** is restated from the 13G threshold (3.47%) to the director's Form 3 count (4.08%), of which 5% was bought from an early holder.
  - **Kleiner Perkins' DoorDash stake** is restated from 1.91% to 1.97% (Form 3 at the listing).

**Firm-map decisions.**
- **Renamed firms are merged with their predecessors:** Bullet Time Ventures into Techstars Ventures, Sherpa Capital into ACME Capital, and Pacven Walden into Walden International.
- **DFJ** includes DFJ Growth and the Threshold funds (DFJ Venture's later name), with their single-purpose SpaceX vehicles; DFJ's continuation funds are sensitivity-only. Tim Draper's personal vehicles are kept apart from both DFJ and Draper Associates, the fund manager.
- **Separate franchises:** Lightspeed China Partners and Lightspeed Faction (a crypto fund) are outside Lightspeed's measure. Matrix Partners China is the book's Matrix China, separate from Matrix Partners.
- **Excluded vehicles:** Glynn's Emerging Opportunity funds (public/private hybrids) are excluded, like Sequoia's Global Equities fund. Stakes held through renminbi vehicles are excluded, just as renminbi funds are excluded from capital at risk (Matrix China's and Source Code's Li Auto stakes).

**Newly ranked firms.** 46 firms gained fund histories and entered the ranking:

- **Top 50:** Glynn Capital 26 (2.5x); Amplify Partners 27 (2.3x); Harbor Pacific Capital 29 (2.3x); March Capital 31 (2.2x); Red Swan 33 (2.0x); Granite Hill Capital Partners 35 (2.0x); Revel Partners 48 (1.5x); Mobius Venture Capital 50 (1.4x).
- **51st–100th:** K9 Ventures 53 (1.3x); Kaszek 62 (1.1x); Mithril Capital 64 (1.1x); CrunchFund 73 (0.96x); Aspect Ventures 76 (0.94x); Pear VC 78 (0.91x); QED Investors 83 (0.87x); Walden International 84 (0.84x); Techstars Ventures 91 (0.72x); Streamlined Ventures 92 (0.70x); RRE Ventures 94 (0.67x).
- **Below 100th:** Floodgate 101 (0.54x); SineWave Ventures 105 (0.50x); Draper Associates 106 (0.49x); ACME Capital 109 (0.44x); Boost VC 110 (0.44x); Matrix China 119 (0.29x); Westly Group 121 (0.27x); Forerunner Ventures 123 (0.25x); Tenaya Capital 124 (0.25x); Valor Capital Group 125 (0.23x); Sozo Ventures 126 (0.23x); Haystack 127 (0.21x); DAG Ventures 128 (0.21x); 500 Global 129 (0.20x); NextEquity Partners 130 (0.19x); Version One 131 (0.17x); Ten Eleven Ventures 132 (0.16x); Almaz Capital 133 (0.15x); Tusk Ventures 134 (0.14x); Source Code Capital 136 (0.12x); Base10 Partners 138 (0.11x); Acrew Capital 140 (0.09x); China Broadband Capital 142 (0.09x); Slow Ventures 143 (0.07x); A Capital 144 (0.05x); Global Founders Capital 145 (0.03x); Lerer Hippeau 146 (0.02x).

**Holders the check could not settle.**
- **Amicus Capital** (GrubHub; exact 1.54%, worth $73m at the takeout price) and **IT-Farm** (Zoom; 0.65%, $155m) have no public fund records. Odin decided not to pursue them (18 October 2026): Amicus appears to be largely inactive today, and IT-Farm is set aside for now. Both stay in the book with their stakes, without fund histories, so neither is scored.
- **Inspiration Ventures** (UserTesting; 4.6%, $50m, of which $25m is counted as primary at the central 50%) is a pooled-fund manager, but only part of its stake is known to have been bought in the 2012 seed round. With its secondary fund left out of capital, as secondary vehicles are, it falls below the line on central assumptions (about 0.8x); only if all its shares were bought from the company would it reach about 1.5x.

**Limits of the version 7 check.**
- Listings below $3bn were not swept. They hold about 3% of the universe's value, and their small holders were covered only by the earlier census of holder tables and the closing screens.
- Long agreements were read only up to the fetch limit, and the name probe covered 128 firms, not every possible holder.
- Most new stakes are estimates with ranges, and positions whose origin could not be established score zero.
- DFJ's SpaceX stake, the largest addition, rests on a press figure.

**Fund-level attribution (version 8).** To rank individual funds (§4), seven research batches traced each large stake to the funds that held it at the listing, from the per-fund counts in Forms 3 and 4, Schedule 13G cover pages, 13F tables by manager, prospectus footnotes and investors' rights agreements, and checked the sizes of these firms' largest funds (a few could not be confirmed, among them Contour Venture Partners I and some of Sequoia's U.S. growth funds). The same filings corrected the book and the fund files:
- **Shares bought from other holders, now removed.** In each case the filings show common stock, or preferred issued before the fund holding it existed:
  - **Pelion's Cloudflare:** 5.07m of 48.4m shares (10.5%), held by Pelion Opportunity Fund I (formed in 2018), Pelion VI and Pelion V. Pelion falls from 7.9x to 7.3x.
  - **Index's Datadog:** 4.03m of 53.5m shares (7.5%), held by Index Growth III, whose first sale came after those shares were issued, and by the Yucca co-investment scheme.
  - **Andreessen Horowitz's Coinbase:** 5.49m of 29.5m shares (18.6%), common stock held by LSV Fund I, formed after Coinbase's last private round, and by a16z's crypto fund.
  - **Lightspeed's Rubrik:** 4.0m of 39.0m shares (10.2%).
  - **Accel's Etsy:** 9.17m of 26.5m shares (34.6%). Accel's first round was the 2008 Series D, but its funds also held common stock and earlier series.
  - **Benchmark's Uber:** 13.2m of 150.1m shares (8.8%), Seed shares issued before Benchmark's 2011 Series A (probably bought from holders; high case none). Benchmark falls from 6.2x to 6.0x and stays eighth.
  - **Accel's UiPath:** 10.9m of 106.3m shares (10.3%), junior preferred series issued at the same price as the senior ones, the usual form for common bought from holders (high case none).
  - **Smaller lots:** Union Square Ventures' Etsy (5.1%), Index's Figma (5.5%), Sequoia's Airbnb (1.0%), Instacart and Figma, Andreessen Horowitz's Navan, and plain common in Accel's CrowdStrike, Tenable, ForgeRock, Couchbase and Varonis stakes.
- **JVP's CyberArk.** The 13G shows JVP IV, which invested in 2002, holding 66% of JVP's shares, and JVP Opportunity VI, which bought in the December 2011 deal with Goldman Sachs, holding 34%. That deal was part new shares and part purchases from holders. The primary share rises from 50% to 83% (range 66%–100%), and JVP from 1.1x (61st) to 1.7x (42nd), entering the top 50; RPM Ventures falls to 51st.
- **Accel's Atlassian stake** is 6.9%, from its Schedule 13G three weeks after the listing, not the 11.2% press figure (kept as the high case).
- **Holdings that belong to others, removed:**
  - Stanford's shares within Emergence's Zoom block, held under a proxy to Emergence;
  - Draper Associates' shares within DFJ's Redfin and PubMatic stakes;
  - Peter Thiel's personal shares within Founders Fund's Affirm stake;
  - Sequoia's SentinelOne stake, held by its Global Equities fund, which is outside capital at risk.
- **Fund sizes:**
  - **FirstMark Capital I:** about $220m, not $300m (PE Hub reported $183m raised toward a $200m target in 2006; FirstMark's statements of assets under management agree).
  - **Khosla Ventures Seed B:** $397m (PitchBook; range $300m–$600m), not $300m.
  - **Altos Ventures IV:** $86m (its co-founder), not $64.9m. Its 2019 reserve fund ($22.9m, Form D) now counts as part of it.
  - **Sequoia Capital XII:** $420m (PitchBook), plus its principals' and technology partners' funds, about $61m together, estimated from their holdings.
  - **DFJ Growth Fund 2006:** $290m including its parallel vehicles (VentureBeat reported $290m raised in 2007; its managing partner recalls $270m), not the $250m target. DFJ Growth 2013: $470m.
  - **Others:** Pelion Ventures V $194m, Kaszek Ventures I $95m, Lightspeed Venture Partners VII $475m, Andreessen Horowitz's Annex Fund $202.2m.
  - **Partners' side funds** sized from the fixed share of every deal they take: Accel's growth and Leaders funds, Index VI and Growth I, Greylock XIV, Redpoint IV and Omega II, JVP Opportunity VI, and Sequoia's Global Growth and U.S. Growth VII principals' funds.
  - **Added:** Benchmark's two Cerebras vehicles ($225m, 2026) and Felicis's Clover Fund ($7m, 2013), whose stakes were already in the book.
- **Effect.** The ranked firms' primary value falls by $5.7bn (0.8%) and their capital at risk rises by $0.4bn. In the top ten only Pelion's and Benchmark's figures change, to 7.3x and 6.0x, and neither changes place: Benchmark stays eighth, and Pelion is sixth, where Lowercase's RT fund decision (§7) had already put it. Below them, Index and FirstMark, and Amplify and Andreessen Horowitz, swap places; Accel falls from 23rd to 25th; JVP enters the top 50 and RPM Ventures leaves it.

---

## 9. Total value created, weighted by entry stage (kept separately)

The total-value ranking, with each position weighted by the stage of the firm's first round, is kept as a companion ranking in `vc_conviction_weighted_ranking_v17.csv`, with its Layer 2 and ex-SpaceX versions. It answers a different question: how much value each firm's early conviction helped create in total, whatever the capital used.

The ten largest on that measure ($bn at 2 October 2026) are:
- Founders Fund 69.4
- Sequoia 52.5
- Bessemer 38.9
- Accel 37.8
- Index 25.9
- NEA 22.1
- Andreessen Horowitz 20.6
- DFJ 18.2
- Sutter Hill 17.1
- Khosla 15.8

DFJ is in the ten on SpaceX: its 2009 entry counts at 0.62, because SpaceX's round letters count financings rather than maturity and are read at half speed. The new positions added in version 7 are weighted the same way as the rest of the book.

---

## 10. Methodology

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
4. **Capital at risk.** The commitments of the firm's in-scope funds, each weighted by the share of its eventual listings expected to fall in the window (§10.7).
5. **The consistency adjustment.**
   - The headline is a weighted geometric mean of (1 + value per dollar) and (1 + value per dollar beyond the largest company), minus 1, with weights of two-thirds and one-third. It counts mainly how much value the firm created per dollar, and partly how much it created beyond its single biggest success.
   - Version 5 weighted the two equally. Odin judged that too harsh, because in venture one outstanding company often carries a firm, while still wanting the measure to recognise firms that rest on one company. A one-company firm keeps (1 + value per dollar)^(2/3) − 1 instead of √(1 + value per dollar) − 1: 25x becomes 7.8x rather than 4.1x.
   - Adding 1 keeps a one-company record above zero, so a concentrated bet that works is still rewarded.
   - The adjustment is measured on companies rather than funds, because a firm's funds often hold the same company. Lowercase's second fund, for example, also held Uber.
   - The weight on depth and the definition of depth are tested in §7.
   - The same measure ranks individual funds in §4 (§10.12).

No entry-stage weight is applied; weighting by stage is one of the robustness checks (§7).

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
- **Version 7 additions (§8),** in order of preference:
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

- **Performance end date.** Every value is measured at the close on Friday 2 October 2026 and held there. The end date is the same for every firm, listing and benchmark, and later versions keep it unless Odin decides otherwise (§13).
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
  - Lowercase: 25% of its Uber stake (Industry Fund II-A, see §7).
  - Pinduoduo: Banyan 43% and HongShan 31% (shares transferred from or issued against the founder's holding).
  - Version 5 listings: Meritech 56% and NEA 28% of MuleSoft (NEA's Series A shares were bought from Morgenthaler); Foundry 10.5%, Bessemer 11.8% and Bain Capital Ventures 7.3% of SendGrid; Battery 6% of Coupa and 5% of Avalara. Greenspring's MuleSoft stake and Coatue's Anaplan block were mostly or wholly bought from holders.
  - **Version 7:** DFJ 20% of SpaceX (60%–90% primary); Index 12.8% of ServiceTitan (common and Series A-1 bought from holders); Redpoint 5% of Twilio; Inspiration Ventures 50% of UserTesting (33%–100% primary). General Catalyst's GitLab block (bought in the 2020–21 employee tender), K5 Global's SpaceX shares outside its four named vehicles, Battery's Airbnb and Confluent lots, IVP's Uber lot, Kaszek's later Nubank block and Glynn's later Dropbox and Tenable purchases score zero, and March Capital's KnowBe4 shares are excluded.
  - **Version 8** (from the fund-level filings, §8): Pelion 10.5% of Cloudflare; Index 7.5% of Datadog and 5.5% of Figma; Andreessen Horowitz 18.6% of Coinbase and 6.8% of Navan (5.0% before); Lightspeed 10.2% of Rubrik; Benchmark 8.8% of Uber; Accel 34.6% of Etsy, 10.3% of UiPath and 0.9%–10.5% of its CrowdStrike, Tenable, ForgeRock, Couchbase and Varonis stakes; Union Square Ventures 5.1% of Etsy; Sequoia 1.0% of Airbnb, 8.0% of Instacart and 33% of Figma (6.7% and 30% before). JVP's CyberArk primary share is raised from 50% to 83% (66%–100%).
- **SpaceX.** Each holder's June 2026 13F or 13G stake was split into blocks by vehicle and matched to SpaceX's primary rounds, tender offers and the xAI merger. Each block counts by its probability of having been bought from SpaceX; merger stock counts zero (version 4). DFJ's stake, for which no filing exists, is treated as in §7.
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
- **Listed separately (§6):**
  - family offices and individuals;
  - corporate and pension venture arms;
  - the thirteen firms Odin identified;
  - firms that fail the same test, whether energy private equity, regional generalist syndicates, consumer investors, public economic-development funds, single-company syndicates or sponsor-funded vehicles.
- **Not scored:** holders with no fund history, either because they invest their principals' or members' own money (angel groups, family vehicles, personal trusts) or because their fund sizes could not be found (§6, §10.8).
- **Not measured per dollar:** growth, crossover and hedge funds. They appear in the companion stage-weighted file (Layer 2).

### 10.7 Capital at risk

- **Fund histories.** 3,422 vehicles for 180 firms, of which 3,041 are in scope.
  - **Sources:** EDGAR Form D filings, Form ADV private-fund data, firm and press announcements of final closes, public pension reports, SEC filings that name funds, and database profiles checked against press.
  - **Fields:** each vehicle records vintage, committed capital, strategy, mandate, geography, scope, estimated life-sciences share, source and confidence.
  - **New in version 7:** fund histories for 51 firms, and RPM's BGW Ventures IV ($40m).
  - **New in version 8:** Lowercase's RT fund in scope and its sidecar counted at its Slack cheque ($7.5m, low confidence); the corrected fund sizes and added vehicles listed in §8.
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
  - **Firms concerned:** Sutter Hill (revised in version 5, §7), RTP's proprietary capital, SAP Ventures before it became Sapphire, Y Combinator's standard deals, EPIC Ventures, Zeev Ventures' early years, SV Angel's partner-money vehicles and the family offices in §6.
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
- **Version 7** searched for stakes the holder tables miss (§8) and wrote fund histories for the 51 firms whose new stakes could matter to the ranking. Smaller pooled-fund holders were screened instead (below).
- **Firms without fund histories.** 127 firms with value remain without them. They hold 2.9% of core value ($25.0bn).
  - **Screened against the top-50 line (1.38x in versions 7 and 8).** A firm whose value comes from one company reaches the line only if its value is at least 2.66 times its capital at risk. None of the pooled-fund managers without histories passes on its known fund sizes: the closest remain Origin Ventures (GrubHub; 1.0x on its documented funds) and Morgenthaler (about 0.8x), and three firms cleared in version 6 on announced fund sizes (83North, Shunwei and Northzone) stay below.
  - **Holders and candidates screened out on fund sizes:** Delta-V Capital (its 2011 fund alone puts about $32m at risk, more than the $19m that would let its Zayo stake reach the line), Liquid 2 Ventures (whose GitLab stake also sits in vehicles that predate its funds), Inspiration Ventures (central case), C&B Capital, TeleSoft Partners, Torch Capital, Four Rivers Group, Tru Arrow Partners and L1 Capital.
  - **Not scored by type:** principals', members' or family money (A-Grade, Youniversity, Amidzad, QueensBridge, SciFi, Three Kingdoms, Egan-Managed Capital, GlobalLink1, Pioneer Venture Partners, TEEC Angel Fund, Tim Draper's personal vehicles), a single-deal platform (FundersClub) and corporate capital (Seed Capital Partners, eValue). Two of these would score highly if counted: Pioneer's Avalara stake cost about $4m and TEEC's angel-club fund held $3.5m.
  - **Open:** Centillion, whose fund sizes are unknown, and the renminbi-only managers (§6). Amicus Capital and IT-Farm were set aside by Odin (§8).
  - Two firms have no fund records at all: Luminari Capital (fuboTV, $30m of value; first fund 2015) and Stratim Capital (EverQuote, $41m).

### 10.9 Ranges

- **Range from estimated inputs:**
  - estimated stakes at their low and high values;
  - uncertain primary shares at their low and high cases;
  - low-confidence fund sizes doubled (low end) and halved (high end).
- **Where better ranges exist,** they replace that rule: Sutter Hill's deployment path, Contour, Altos, Celesta and Y Combinator (verification), and the screened firms' documented capital ranges. The adjusted figure is recomputed in each case, including which company is largest.
- **Gigafund:** the three readings of its SpaceX vehicles, each with matching capital at risk.
- **DFJ:** its SpaceX stake at 1.15% and 1.85%, with 60% and 90% bought from SpaceX.
- **Fund ranges (§4)** add the estimated splits of a firm's stake between its funds, at their low and high cases.
- **Rank range:** the best and worst of two things:
  - the firm's rank when its own figure is moved to the ends of its range and the others stay central;
  - its ranks under the 19 specifications in §7 (the ex-SpaceX view is excluded).

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
- **Version 5:** fourteen large stakes held by leading firms were re-checked against Forms 3 and 13G (all matched at the share level); Lowercase's Uber and Twilio, Founder Collective's and IA Ventures' Trade Desk and DigitalOcean stakes, First Round's Square stake and Y Combinator's estimates were re-checked; the low-confidence fund histories of Sutter Hill, Altos, Celesta, Y Combinator, Contour and Pelion were re-checked; and four takeout values were corrected (§10.4).
- **Version 7:**
  - Each new position records its source document, method and arithmetic in the book's provenance note, and each pair the sweeps found records its outcome in the register.
  - Every research file from the cut-off runs was checked for truncated or missing output before integration; all 1,280 name-probe searches completed (14 of them through single-word fallback queries).
  - The ranking was rebuilt from the book and fund files, and the report's figures were checked against the data files by an independent review.
- **Version 8:**
  - Each fund-level split records its source filing (accession number) and arithmetic in the research files; splits that rest on estimates are flagged and carried into the fund ranges.
  - Fund totals reconcile to the firm totals: the difference is the value held in single-company vehicles and other vehicles outside any fund generation (§4).
  - The firm and fund rankings were rebuilt from book v17 and fund files v17, and the report's figures were checked against the data files by an independent review.

### 10.12 Fund-level measure

- **Unit:** a fund generation, as defined in §4. Partners' side funds and top-up funds that take a fixed share of the generation's deals belong to it. A single-company vehicle forms its own unit and is not ranked.
- **Value:** `V_fund = Σ (company value at 2 October 2026 × firm's stake × fund's share of the firm's shares × primary fraction of the fund's shares)`.
  - Shares a filing identifies as bought from other holders score zero.
  - Where the book counts more of a firm's stake as bought from holders than the filings identify, the rest is taken first from the funds whose shares' origin is not identified, then pro rata.
- **Capital at risk:** `K_fund = Σ (commitment × w(vintage, strategy))` over the generation's in-scope vehicles, with the weights of §10.7.
- **Headline:** the consistency-adjusted value per dollar of §10.1, computed on the fund's companies.
- **Positions without per-fund filings** go to the generation named in the holder's name where it identifies one (a fund number or year). Otherwise they go to the generation whose investment period (vintage to vintage + 6 years) covers the firm's entry year: where several overlap, the largest; for entries at Series C or later, the growth generation active then; for companies outside the US, the firm's funds for that country, or its US or global funds if it has none. With no known entry year, the listing year less six is used.
- **Look-through:** shares moved to continuation or roll-over vehicles are credited to the generation that bought them (DFJ Fund IX and DFJ Growth 2006 continuation funds, Altos Ventures IV Liquidity Fund, Sequoia Grove). Sequoia Grove's shares are credited pro rata to the Sequoia funds holding the same company.
- **Scope:** the funds of ranked firms. Evergreen and annual-deployment pools, cross-generation co-investment schemes and single-company vehicles are not ranked; their figures are given in §4 where notable.

---

## 11. Sources

- **SEC EDGAR:**
  - final prospectuses (424B4, 424B1, 424B3) and registration statements (S-1, F-1, S-4, F-4) with their exhibits, including investors' rights, registration rights and shareholders' agreements;
  - closing 8-Ks and 20-Fs;
  - Forms 3, 4 and D;
  - Schedules 13G and 13D;
  - Form 13F-HR;
  - EDGAR full-text search (the version 7 name probe and 13F reverse sweep).
- **Odin's IPO inputs dataset:** listing dates, sectors, post-offering share counts and offer prices.
- **Prices:** exchange and over-the-counter closes on 2 October 2026, the performance end date (stockanalysis.com and Yahoo Finance); takeout terms from merger filings and acquirers' reports.
- **Fund histories:**
  - Form D and D/A filings, and Form ADV private-fund data (including privatefunddata.com);
  - firm and press announcements of fund closes (including Buyouts Insider, Private Equity International, AVCJ, Globes, TechCrunch, Fortune, Axios and VentureBeat);
  - public pension and endowment reports;
  - PitchBook, CB Insights, Preqin and KANDO public profiles.
- **DFJ's SpaceX stake:** Forbes (12 June 2026) for the stake's estimated value and DFJ's investment since 2009; Inc. and Forge for DFJ's 2009 Series E cheque; SpaceX's Form D filings for the round ladder; the SpaceX directors' Forms 3; DFJ's Form ADV private-fund data (via aum13f.com) for the fund split.
- **Fund-level attribution (version 8):** directors' and 10% holders' Forms 3 and 4, Schedule 13G cover pages and 13F information tables by manager at each listing; prospectus footnotes and investors' rights agreements; for fund sizes, Form D filings, press reports of final closes, PitchBook profiles (Khosla Ventures Seed B, Sequoia Capital XII), FirstMark's statements of assets under management, an interview with Altos Ventures' co-founder (Acquired podcast), and a commercial database record on Lowercase RT Fund reviewed by Odin.
- **Benchmark:** Nasdaq-100 year-end closes and QQQ monthly closes, to the 2 October 2026 close.
- **Round chronology and leads:** company and firm releases, TechCrunch, Reuters, Bloomberg, Forbes, the Financial Times, AVCJ, PEdaily and 36Kr.

---

## 12. Limitations

1. **Single outcomes still matter.** Even after the adjustment, 18 of the top 25 owe more than half their value to one company, and half of the top-20 funds owe 80% or more to one. A large price move in SpaceX, Snowflake, Uber, Cloudflare or Datadog would reorder the top of the table, but only if Odin rolls the end date forward.
2. **The consistency adjustment is a judgment.** The one-third weight on depth, depth measured beyond one company, and the added 1 are choices. Other reasonable choices change the order little overall (rank correlations 0.992–0.996, §7), but the form of the adjustment decides who leads: with a fifth of the weight on depth, or with depth measured beyond the two largest companies, a single-company firm would.
3. **Sutter Hill's capital is estimated.** It has no fund series, so its range is the widest in the top ten.
4. **SpaceX attributions are estimates,** inferred from vehicle dates and prices; the ranges show the effect. DFJ's stake, the largest single addition in version 7, rests on a press estimate cross-checked by round arithmetic, with no filing behind it.
5. **Listings below $2bn and outside the US are omitted.** Omitted listings below $2bn (IPOs and SPAC mergers) are not counted, and listings in Hong Kong, mainland China, Europe and Israel are outside the universe. Firms whose companies list there look weaker per dollar (HongShan, IDG, Index, Accel, JVP, Gemini Israel).
6. **IPO exits only.** Acquisitions of private companies and companies still private are outside the measure.
7. **Capital at risk is partly estimated.** 8% of the ranked firms' capital at risk rests on low-confidence sizes, including Lowercase's sidecar (counted at its Slack cheque) and partners' side funds sized from their holdings.
8. **Small stakes are partly estimated,** and positions never assessed for primary purchase score zero.
9. **Secondary purchases are removed only where the evidence reveals them.**
10. **Coverage of small holders.** The version 7 check swept every listing worth $3bn or more. Small holders of smaller listings rely on the prospectus holder tables and the closing screens. Two holders without fund records (Amicus Capital and IT-Farm) were set aside by Odin and are not scored.
11. **Classification.** Who counts as a venture firm is a judgment, and five of the firms Odin moved out have conventional fund structures (§13).
12. **Renminbi capital.** Firms that invest only through renminbi funds have no capital at risk in the main specification and cannot be ranked.
13. **A single, fixed end date.** Every figure is a snapshot at the 2 October 2026 close, with no adjustment for later price moves, dilution, distributions or dividends.
14. **This is value created, not investor returns.** It ignores fees, carried interest and actual exit prices.
15. **Fund splits are partly estimated.** About 72% of the ranked firms' value is split between funds from filings and other per-fund evidence (69% from per-fund share counts); the rest follows holder names or the fund-vintage rule. Some splits that matter at the top rest on estimates: DFJ's SpaceX stake by fund, Felicis's Shopify stake between Felicis Ventures II and its Clover Fund, Lowercase's Uber stake by vehicle and Bullet Time Ventures' Uber holding (§4). A fund's figure is also more sensitive than its firm's to an error in its size.

---

## 13. Decisions

Settled (October 2026):
- **Headline:** consistency-adjusted value per dollar of capital at risk, with two-thirds of the weight on value per dollar and one-third on value beyond the largest company (Odin, 12 October 2026). Plain value per dollar and depth are shown alongside. Secondary: the same value as an annual return against the QQQ, shown relative to the median firm.
- **Performance end date:** all values are measured at the close on 2 October 2026 and kept at that date from version 7 on (Odin, 18 October 2026). Rolling it forward would mean repricing every listing and the benchmark.
- **Order of the ranking:** firms are ranked on their central figures, even where ranges overlap (Odin, 18 October 2026). Sutter Hill therefore ranks first and Founders Fund second.
- **Lowercase Capital:** the RT fund is in scope and the sidecar counts at its Slack cheque, on a commercial database record of the Slack investment (Odin, 18 October 2026).
- **Amicus Capital and IT-Farm:** not pursued (Odin, 18 October 2026). Both stay in the book without fund histories.
- **New rankings:** the 20 companies with the most long-term value created (value at 2 October 2026 of the listing-day shares) and the 20 individual funds with the highest consistency-adjusted value per dollar (Odin, 18 October 2026). A fund is a fund generation, not a single legal vehicle; only the ranked firms' funds are ranked.
- **Who is ranked:** independent venture managers investing pooled outside capital through LP/GP funds, mainly in private technology companies. Other investors, including the holders newly measured in version 7, are listed separately with their figures.
- **SpaceX:** probability-weighted attributions, with the strict reading as the low case; DFJ's stake is a press-based estimate with a range. No DFJ filing lists SpaceX shares yet (checked 18 October 2026); the first 13F that could covers 31 December 2026.
- **Weight floor:** the 25% floor is kept.
- **Section 32:** its estimated stakes are kept, with ranges.
- **Centillion:** left unmeasured.
- **Omitted listings:** every omitted venture-backed listing worth $2bn or more is added (IPOs, ADR offerings, direct listings and SPAC mergers).
- **Coverage (version 7):** every (firm, listing) pair found by the sweeps has a recorded outcome, and every firm that could reach the top 50 on its new stakes has a fund history, except where fund sizes could not be found.
- **Unchanged from earlier versions:**
  - the stage-weighted ranking is kept as a separate file;
  - no minimum number of companies;
  - life-sciences deduction as a sensitivity only.

Still open:
1. **Classification review.** Which firms belong in the main table?
   - **Five conventional venture partnerships moved out:** OpenView, Frazier Technology Ventures, Mosaic, Commonwealth Capital Ventures and Evergreen. Each raised closed-end funds and invested in private technology; institutional investors are documented for Commonwealth and Evergreen. Restored one at a time, OpenView would rank 9th (5.2x), Mosaic 11th (4.0x), Frazier 13th (3.6x), and Commonwealth and Evergreen 46th and 47th (1.5x).
   - **Hydrazine Capital, moved out:** Sam Altman's fund, but with outside institutional investors (Peter Thiel in Fund I; the University of Michigan in Funds II and IV). Restored, it would rank 10th (5.1x).
   - **Gigafund, kept:** its vehicles are concentrated in SpaceX, like the Infleqtion syndicates and K5 Global, which are listed separately. Listed separately, Lowercase and Pelion would move up to fourth and fifth, and Greylock would enter the top ten.
   - **Norwest and Sapphire, kept:** each has or had a single corporate investor (Wells Fargo; SAP for Sapphire's early funds). Both rank below 100th, so the choice moves nothing above them.
2. **Renminbi-only managers.** Should firms whose stakes came only from renminbi funds be measured with those funds in capital at risk, rather than left unmeasured?
   - The cases found are Dehui (a private-equity boutique, not ranked anyway), Bojiang and Hongdao (Webull; fund sizes not found), Rothsfortune (0.6x on that basis) and Yuanzhan (Hesai; roughly 0.35x–1.5x on version 3's capital estimates, 0.7x central).
3. **DFJ's SpaceX stake.** Keep the press-based estimate (1.54%, range 1.15%–1.85%) until a count appears. The asset values in DFJ's Form ADV point to about 1.9% or more, so the stake may be understated. DFJ's first 13F that could include SpaceX covers 31 December 2026 and is due by mid-February 2027; a confirmation from DFJ would settle it sooner.
4. **Fund ranking (new).** Whether to seek per-fund counts for the estimated splits that matter most (DFJ Growth Fund 2006, Felicis Ventures II, Lowercase Ventures Fund I), and whether Sutter Hill's and Y Combinator's pools, the funds of firms listed separately, or single-company vehicles should be ranked alongside funds.

---

## Appendix A: consistency-adjusted value per dollar, ranks 51 to 147

| Rank | Firm | Consistency-adjusted value per $ | Range from estimated inputs | Rank range (all checks) | Value per $ at risk | Beyond largest company | Value ($bn) | Capital at risk ($bn) | Largest company (share of value; companies) | Rank vs QQQ (§2) |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 51 | RPM Ventures | 1.4x | 1.1x–1.5x | 45–85 | 1.9x | 0.60x | 0.3 | 0.16 | Figure (68% of 2) | 56 |
| 52 | DCVC | 1.4x | 1.3x–1.4x | 42–65 | 1.6x | 0.91x | 1.7 | 1.05 | Rocket Lab (44% of 7) | 58 |
| 53 | K9 Ventures ◊ | 1.3x | 0.32x–2.6x | 23–116 | 2.1x | 0.30x | 0.1 | 0.07 | Twilio (85% of 2) | 62 |
| 54 | Vertex Ventures | 1.3x | – | 49–64 | 2.3x | 0.12x | 1.2 | 0.53 | CyberArk (95% of 2) | 53 |
| 55 | Genesis Partners | 1.3x | 0.90x–1.6x | 43–80 | 1.6x | 0.63x | 0.4 | 0.24 | Riskified (62% of 2) | 52 |
| 56 | Kleiner Perkins | 1.2x | 1.2x–1.3x | 46–73 | 1.4x | 0.88x | 10.3 | 7.09 | Bloom Energy (39% of 21) | 61 |
| 57 | Matrix Partners | 1.2x | – | 51–70 | 1.5x | 0.73x | 2.8 | 1.89 | Acacia (50% of 4) | 59 |
| 58 | Armory Square Ventures | 1.2x | 1.1x–1.2x | 52–75 | 2.2x | 0 | 0.1 | 0.04 | ACV Auctions (100% of 1) | 68 |
| 59 | Globespan Capital | 1.2x | 0.97x–1.3x | 46–96 | 1.9x | 0.21x | 0.9 | 0.48 | Roku (89% of 2) | 54 |
| 60 | Quiet Capital | 1.1x | 0.96x–1.2x | 35–88 | 2.2x | 0 | 1.0 | 0.46 | Reddit (100% of 1) | 69 |
| 61 | Scale Venture Partners | 1.1x | – | 55–95 | 1.3x | 0.83x | 2.0 | 1.51 | JFrog (37% of 7) | 64 |
| 62 | Kaszek ◊ | 1.1x | 0.71x–1.4x | 43–91 | 2.1x | 0 | 2.4 | 1.11 | Nu (100% of 1) | 70 |
| 63 | CRV | 1.1x | – | 53–78 | 1.4x | 0.66x | 2.9 | 2.12 | DoorDash (52% of 6) | 67 |
| 64 | Mithril Capital | 1.1x | 1.1x–1.5x | 46–100 | 1.7x | 0.27x | 2.1 | 1.24 | Palantir (84% of 4) | 72 |
| 65 | Galileo Partners | 1.1x | – | 26–79 | 2.0x | 0 | 0.1 | 0.06 | Talend (100% of 1) | 43 |
| 66 | Capital Today | 1.1x | 0.98x–1.1x | 59–74 | 1.6x | 0.33x | 3.1 | 1.93 | JD.com (80% of 3) | 71 |
| 67 | Menlo Ventures | 1.1x | 0.93x–1.2x | 56–77 | 1.7x | 0.28x | 5.5 | 3.35 | Roku (83% of 5) | 63 |
| 68 | El Dorado Ventures | 1.1x | 0.95x–1.2x | 50–88 | 2.0x | 0 | 0.4 | 0.21 | Coupa (100% of 1) | 51 |
| 69 | Bull Capital Partners ◊ | 1.1x | 0.64x–1.6x | 45–96 | 2.0x | 0 | 0.7 | 0.35 | JD.com (100% of 1) | 73 |
| 70 | Credo Ventures | 1.1x | – | 47–85 | 2.0x | 0 | 0.2 | 0.10 | UiPath (100% of 1) | 74 |
| 71 | Novak Biddle | 1.0x | 0.88x–1.1x | 51–92 | 1.8x | 0 | 0.4 | 0.23 | Appian (100% of 1) | 60 |
| 72 | Elephant Partners | 0.99x | – | 52–86 | 1.8x | 0 | 1.1 | 0.63 | KnowBe4 (100% of 1) | 84 |
| 73 | CrunchFund ◊ | 0.96x | 0.28x–2.6x | 25–120 | 1.2x | 0.52x | 0.1 | 0.06 | GitLab (57% of 3) | 80 |
| 74 | Sigma Partners | 0.96x | 0.92x–0.98x | 64–91 | 1.5x | 0.19x | 1.4 | 0.91 | DocuSign (87% of 3) | 65 |
| 75 | Lightspeed | 0.94x | 0.90x–0.99x | 60–86 | 1.1x | 0.72x | 12.7 | 11.90 | Rubrik (33% of 14) | 82 |
| 76 | Aspect Ventures ◊ | 0.94x | 0.63x–1.1x | 64–96 | 1.7x | 0 | 0.4 | 0.23 | Chime (100% of 1) | 83 |
| 77 | Bay Partners | 0.93x | 0.80x–1.0x | 54–99 | 1.4x | 0.27x | 0.4 | 0.28 | MuleSoft (80% of 2) | 55 |
| 78 | Pear VC | 0.91x | 0.83x–0.95x | 54–89 | 1.6x | 0 | 0.5 | 0.29 | DoorDash (100% of 1) | 88 |
| 79 | Blumberg Capital | 0.91x | – | 55–91 | 1.4x | 0.25x | 0.6 | 0.46 | Nutanix (81% of 2) | 79 |
| 80 | Promus Ventures | 0.90x | 0.68x–1.1x | 53–105 | 1.6x | 0 | 0.2 | 0.10 | Rocket Lab (100% of 1) | 86 |
| 81 | Foundation Capital | 0.89x | 0.84x–0.91x | 73–84 | 1.3x | 0.23x | 3.2 | 2.37 | Cerebras (83% of 6) | 75 |
| 82 | IVP | 0.88x | 0.76x–0.97x | 66–111 | 1.0x | 0.60x | 6.6 | 6.31 | CrowdStrike (42% of 15) | 85 |
| 83 | QED Investors ◊ | 0.87x | 0.38x–1.8x | 41–115 | 1.6x | 0 | 1.4 | 0.87 | Nu (100% of 1) | 91 |
| 84 | Walden International ◊ | 0.84x | 0.47x–1.0x | 63–106 | 1.3x | 0.17x | 1.2 | 0.90 | Credo (87% of 2) | 66 |
| 85 | EPIC Ventures | 0.83x | 0.59x–1.1x | 71–99 | 1.5x | 0 | 0.2 | 0.16 | Instructure (100% of 1) | 78 |
| 86 | August Capital | 0.83x | – | 70–94 | 1.00x | 0.54x | 1.6 | 1.63 | GitLab (46% of 4) | 77 |
| 87 | Eclipse Ventures | 0.83x | – | 61–92 | 1.5x | 0 | 2.2 | 1.52 | Cerebras (100% of 1) | 95 |
| 88 | Ignition Partners | 0.83x | – | 63–102 | 1.3x | 0.11x | 1.2 | 0.89 | DocuSign (92% of 3) | 76 |
| 89 | OATV | 0.75x | 0.69x–0.88x | 67–98 | 1.2x | 0.07x | 0.2 | 0.19 | Fastly (94% of 2) | 87 |
| 90 | General Catalyst | 0.72x | 0.64x–0.77x | 74–95 | 0.81x | 0.55x | 6.0 | 7.37 | Circle (32% of 10) | 96 |
| 91 | Techstars Ventures ◊ | 0.72x | 0.32x–1.2x | 58–116 | 1.1x | 0.16x | 0.4 | 0.40 | Uber (85% of 2) | 94 |
| 92 | Streamlined Ventures ◊ | 0.70x | 0.25x–1.4x | 50–123 | 1.2x | 0 | 0.2 | 0.16 | DoorDash (100% of 1) | 102 |
| 93 | Foundry Group | 0.68x | 0.66x–0.71x | 84–97 | 0.78x | 0.50x | 1.4 | 1.74 | SendGrid (35% of 4) | 93 |
| 94 | RRE Ventures ◊ | 0.67x | 0.35x–0.96x | 73–116 | 1.0x | 0.17x | 1.1 | 1.06 | Datadog (84% of 2) | 89 |
| 95 | IDG Capital ◊ | 0.66x | 0.43x–0.78x | 89–110 | 0.79x | 0.42x | 3.8 | 4.83 | Circle (46% of 8) | 92 |
| 96 | Qumra | 0.64x | – | 86–108 | 0.95x | 0.16x | 0.5 | 0.51 | JFrog (83% of 2) | 105 |
| 97 | Mayfield | 0.61x | 0.49x–0.70x | 91–105 | 0.80x | 0.30x | 1.7 | 2.09 | HashiCorp (63% of 5) | 90 |
| 98 | Zeev Ventures ◊ | 0.61x | 0.35x–0.95x | 75–116 | 1.0x | 0 | 0.8 | 0.73 | Navan (100% of 1) | 109 |
| 99 | Meritech | 0.60x | 0.46x–0.73x | 86–121 | 0.66x | 0.49x | 2.1 | 3.10 | Roblox (26% of 10) | 98 |
| 100 | Oak Investment Partners | 0.56x | 0.52x–0.58x | 87–115 | 0.68x | 0.35x | 2.3 | 3.41 | Circle (49% of 3) | 81 |
| 101 | Floodgate ◊ | 0.54x | 0.32x–0.95x | 75–116 | 0.85x | 0.07x | 0.3 | 0.34 | Okta (91% of 3) | 99 |
| 102 | Dawn Capital | 0.52x | – | 90–108 | 0.88x | 0 | 0.5 | 0.58 | Mimecast (100% of 1) | 110 |
| 103 | Initialized Capital ◊ | 0.52x | 0.35x–0.73x | 87–116 | 0.76x | 0.13x | 0.5 | 0.61 | Coinbase (82% of 5) | 111 |
| 104 | Battery Ventures | 0.51x | 0.49x–0.55x | 99–108 | 0.54x | 0.45x | 3.2 | 5.91 | Zayo (16% of 12) | 104 |
| 105 | SineWave Ventures ◊ | 0.50x | 0.17x–1.2x | 57–131 | 0.83x | 0 | 0.1 | 0.08 | SentinelOne (100% of 1) | 113 |
| 106 | Draper Associates ◊ | 0.49x | 0.27x–0.91x | 78–120 | 0.72x | 0.11x | 0.1 | 0.16 | Coinbase (85% of 2) | 107 |
| 107 | M/C Partners | 0.46x | – | 93–114 | 0.77x | 0 | 0.9 | 1.16 | Zayo (100% of 1) | 97 |
| 108 | DCM | 0.44x | – | 97–116 | 0.51x | 0.32x | 1.3 | 2.56 | Figure (37% of 5) | 101 |
| 109 | ACME Capital ◊ | 0.44x | 0.21x–0.87x | 84–126 | 0.52x | 0.30x | 0.4 | 0.70 | Uber (41% of 3) | 108 |
| 110 | Boost VC ◊ | 0.44x | 0.11x–0.76x | 89–136 | 0.73x | 0 | 0.0 | 0.06 | Coinbase (100% of 1) | 116 |
| 111 | Trinity Ventures | 0.40x | – | 103–118 | 0.54x | 0.17x | 0.7 | 1.31 | New Relic (69% of 4) | 100 |
| 112 | Sapphire Ventures | 0.40x | 0.36x–0.43x | 92–119 | 0.46x | 0.29x | 2.2 | 4.72 | JFrog (35% of 11) | 119 |
| 113 | Spark Capital | 0.39x | – | 105–120 | 0.44x | 0.29x | 1.9 | 4.39 | Affirm (34% of 9) | 117 |
| 114 | GGV Capital | 0.39x | 0.29x–0.54x | 101–121 | 0.46x | 0.26x | 2.1 | 4.63 | HashiCorp (43% of 15) | 114 |
| 115 | Sequoia China (HongShan) | 0.38x | 0.34x–0.47x | 107–118 | 0.45x | 0.25x | 5.3 | 11.80 | Pinduoduo (45% of 20) | 123 |
| 116 | Tribeca Venture Partners | 0.36x | 0.32x–0.38x | 106–117 | 0.58x | 0 | 0.2 | 0.29 | ACV Auctions (100% of 1) | 115 |
| 117 | BV Capital | 0.30x | 0.21x–0.37x | 107–126 | 0.45x | 0.03x | 0.8 | 1.80 | AppFolio (94% of 2) | 124 |
| 118 | True Ventures | 0.29x | – | 110–123 | 0.38x | 0.14x | 0.8 | 2.08 | HashiCorp (62% of 2) | 120 |
| 119 | Matrix China | 0.29x | 0.26x–0.31x | 117–135 | 0.41x | 0.09x | 0.8 | 1.93 | Futu (78% of 4) | 121 |
| 120 | Highland Capital | 0.29x | 0.27x–0.30x | 113–130 | 0.40x | 0.09x | 0.7 | 1.80 | Xometry (78% of 3) | 103 |
| 121 | Westly Group ◊ | 0.27x | 0.09x–0.65x | 96–141 | 0.44x | 0 | 0.1 | 0.32 | SentinelOne (100% of 1) | 118 |
| 122 | Bain Capital Ventures | 0.27x | – | 118–132 | 0.29x | 0.21x | 1.2 | 4.08 | Rubrik (27% of 6) | 122 |
| 123 | Forerunner Ventures ◊ | 0.25x | 0.10x–0.45x | 108–139 | 0.41x | 0 | 0.3 | 0.62 | Chime (100% of 1) | 127 |
| 124 | Tenaya Capital | 0.25x | 0.22x–0.33x | 117–134 | 0.31x | 0.13x | 0.3 | 0.95 | New Relic (58% of 3) | 106 |
| 125 | Valor Capital Group ◊ | 0.23x | 0.07x–0.61x | 97–142 | 0.37x | 0 | 0.1 | 0.27 | Coinbase (100% of 1) | 131 |
| 126 | Sozo Ventures ◊ | 0.23x | 0.09x–0.41x | 104–141 | 0.36x | 0 | 0.2 | 0.63 | Coinbase (100% of 1) | 132 |
| 127 | Haystack ◊ | 0.21x | 0.09x–0.43x | 111–141 | 0.33x | 0 | 0.0 | 0.08 | HashiCorp (100% of 1) | 135 |
| 128 | DAG Ventures ◊ | 0.21x | 0.12x–0.29x | 118–138 | 0.25x | 0.13x | 0.3 | 1.17 | Wealthfront (47% of 4) | 112 |
| 129 | 500 Global ◊ | 0.20x | 0.07x–0.43x | 111–142 | 0.24x | 0.12x | 0.1 | 0.46 | GitLab (49% of 5) | 126 |
| 130 | NextEquity Partners ◊ | 0.19x | 0.04x–0.78x | 89–144 | 0.30x | 0 | 0.0 | 0.14 | SentinelOne (100% of 1) | 133 |
| 131 | Version One | 0.17x | 0.16x–0.19x | 128–138 | 0.27x | 0 | 0.0 | 0.10 | Coinbase (100% of 1) | 134 |
| 132 | Ten Eleven Ventures ◊ | 0.16x | 0.06x–0.26x | 123–143 | 0.26x | 0 | 0.1 | 0.25 | KnowBe4 (100% of 1) | 136 |
| 133 | Almaz Capital ◊ | 0.15x | 0.06x–0.27x | 122–143 | 0.23x | 0 | 0.1 | 0.26 | Xometry (100% of 1) | 125 |
| 134 | Tusk Ventures ◊ | 0.14x | 0.07x–0.33x | 117–142 | 0.22x | 0 | 0.0 | 0.10 | Coinbase (100% of 1) | 140 |
| 135 | Greycroft | 0.14x | – | 131–137 | 0.17x | 0.08x | 0.3 | 1.59 | Semrush (51% of 3) | 138 |
| 136 | Source Code Capital | 0.12x | 0.10x–0.14x | 126–142 | 0.19x | 0 | 0.3 | 1.38 | RLX (100% of 1) | 139 |
| 137 | Norwest | 0.11x | 0.10x–0.12x | 133–140 | 0.12x | 0.09x | 0.7 | 6.02 | Dave (28% of 6) | 137 |
| 138 | Base10 Partners ◊ | 0.11x | 0.03x–0.14x | 129–144 | 0.13x | 0.06x | 0.1 | 0.56 | Reddit (50% of 2) | 144 |
| 139 | Polaris Partners | 0.10x | – | 129–141 | 0.13x | 0.04x | 0.3 | 2.44 | Impinj (74% of 2) | 129 |
| 140 | Acrew Capital ◊ | 0.09x | 0.01x–0.20x | 130–146 | 0.14x | 0 | 0.0 | 0.34 | Chime (100% of 1) | 145 |
| 141 | Canaan Partners | 0.09x | 0.09x–0.10x | 130–142 | 0.11x | 0.05x | 0.3 | 2.77 | Instacart (52% of 2) | 128 |
| 142 | China Broadband Capital ◊ | 0.09x | 0.02x–0.27x | 122–145 | 0.13x | 0 | 0.1 | 1.05 | Airbnb (100% of 1) | 130 |
| 143 | Slow Ventures ◊ | 0.07x | 0.03x–0.15x | 134–145 | 0.10x | 0 | 0.0 | 0.41 | Slack (100% of 1) | 143 |
| 144 | A Capital ◊ | 0.05x | 0.01x–0.22x | 127–146 | 0.07x | 0 | 0.0 | 0.17 | Coinbase (100% of 1) | 141 |
| 145 | Global Founders Capital ◊ | 0.03x | 0.01x–0.08x | 143–146 | 0.04x | 0 | 0.1 | 1.81 | Slack (100% of 1) | 142 |
| 146 | Lerer Hippeau ◊ | 0.02x | 0.01x–0.04x | 140–146 | 0.03x | 0.00x | 0.0 | 0.51 | Warby Parker (98% of 2) | 146 |
| 147 | Lux Ventures ◊ | 0.00x | 0.00x–0.01x | 147 | 0.00x | 0 | 0.0 | 2.21 | Planet (100% of 1) | 147 |

## Appendix B: annualised ranking, ranks 51 to 147

| Rank | Firm | Annual return vs median firm (points) | Annual return vs QQQ | Value vs QQQ-grown capital | Unadjusted annual return vs QQQ | Rank (§1) |
|---:|---|---:|---:|---:|---:|---:|
| 51 | El Dorado Ventures | +3.3 | −12.6% | 0.06x | −9.9% | 68 |
| 52 | Genesis Partners | +3.2 | −12.7% | 0.07x | −11.4% | 55 |
| 53 | Vertex Ventures | +2.8 | −13.0% | 0.17x | −8.4% | 54 |
| 54 | Globespan Capital | +2.8 | −13.1% | 0.07x | −10.7% | 59 |
| 55 | Bay Partners | +2.6 | −13.3% | 0.05x | −11.6% | 77 |
| 56 | RPM Ventures | +2.6 | −13.3% | 0.17x | −10.7% | 51 |
| 57 | Revel Partners ◊ | +2.6 | −13.3% | 0.19x | −8.1% | 48 |
| 58 | DCVC | +2.5 | −13.4% | 0.29x | −11.4% | 52 |
| 59 | Matrix Partners | +2.1 | −13.7% | 0.09x | −12.5% | 57 |
| 60 | Novak Biddle | +2.0 | −13.9% | 0.06x | −11.1% | 71 |
| 61 | Kleiner Perkins | +1.8 | −14.1% | 0.14x | −12.9% | 56 |
| 62 | K9 Ventures ◊ | +1.7 | −14.1% | 0.16x | −10.7% | 53 |
| 63 | Menlo Ventures | +1.7 | −14.2% | 0.11x | −11.0% | 67 |
| 64 | Scale Venture Partners | +1.4 | −14.4% | 0.13x | −13.3% | 61 |
| 65 | Sigma Partners | +1.4 | −14.5% | 0.06x | −12.2% | 74 |
| 66 | Walden International ◊ | +1.1 | −14.7% | 0.05x | −12.4% | 84 |
| 67 | CRV | +1.0 | −14.8% | 0.13x | −13.1% | 63 |
| 68 | Armory Square Ventures | +1.0 | −14.9% | 0.24x | −8.4% | 58 |
| 69 | Quiet Capital | +0.9 | −15.0% | 0.38x | −5.3% | 60 |
| 70 | Kaszek ◊ | +0.8 | −15.0% | 0.31x | −6.8% | 62 |
| 71 | Capital Today | +0.3 | −15.5% | 0.16x | −12.0% | 66 |
| 72 | Mithril Capital | +0.2 | −15.6% | 0.15x | −12.1% | 64 |
| 73 | Bull Capital Partners ◊ | +0.2 | −15.7% | 0.12x | −11.2% | 69 |
| 74 | Credo Ventures | +0.0 | −15.9% | 0.18x | −10.0% | 70 |
| 75 | Foundation Capital | −0.1 | −16.0% | 0.08x | −13.1% | 81 |
| 76 | Ignition Partners | −0.2 | −16.1% | 0.06x | −13.3% | 88 |
| 77 | August Capital | −0.4 | −16.3% | 0.07x | −15.2% | 86 |
| 78 | EPIC Ventures | −0.6 | −16.5% | 0.08x | −12.5% | 85 |
| 79 | Blumberg Capital | −0.7 | −16.6% | 0.10x | −13.6% | 79 |
| 80 | CrunchFund ◊ | −0.7 | −16.6% | 0.14x | −14.7% | 73 |
| 81 | Oak Investment Partners | −0.9 | −16.8% | 0.03x | −15.9% | 100 |
| 82 | Lightspeed | −1.1 | −16.9% | 0.19x | −15.5% | 75 |
| 83 | Aspect Ventures ◊ | −1.1 | −17.0% | 0.18x | −11.4% | 76 |
| 84 | Elephant Partners | −1.1 | −17.0% | 0.29x | −8.7% | 72 |
| 85 | IVP | −1.3 | −17.2% | 0.13x | −15.7% | 82 |
| 86 | Promus Ventures | −1.6 | −17.5% | 0.20x | −11.1% | 80 |
| 87 | OATV | −1.6 | −17.5% | 0.06x | −14.4% | 89 |
| 88 | Pear VC | −2.1 | −18.0% | 0.22x | −10.8% | 78 |
| 89 | RRE Ventures ◊ | −2.4 | −18.3% | 0.07x | −15.4% | 94 |
| 90 | Mayfield | −2.6 | −18.5% | 0.06x | −16.4% | 97 |
| 91 | QED Investors ◊ | −2.9 | −18.8% | 0.24x | −10.7% | 83 |
| 92 | IDG Capital ◊ | −3.3 | −19.2% | 0.07x | −17.8% | 95 |
| 93 | Foundry Group | −3.4 | −19.3% | 0.09x | −18.2% | 93 |
| 94 | Techstars Ventures ◊ | −3.6 | −19.5% | 0.13x | −15.6% | 91 |
| 95 | Eclipse Ventures | −3.9 | −19.8% | 0.26x | −11.2% | 87 |
| 96 | General Catalyst | −4.6 | −20.4% | 0.14x | −18.9% | 90 |
| 97 | M/C Partners | −4.7 | −20.6% | 0.04x | −16.5% | 107 |
| 98 | Meritech | −4.8 | −20.7% | 0.09x | −19.6% | 99 |
| 99 | Floodgate ◊ | −5.0 | −20.9% | 0.07x | −17.4% | 101 |
| 100 | Trinity Ventures | −5.2 | −21.1% | 0.04x | −19.1% | 111 |
| 101 | DCM | −5.3 | −21.2% | 0.04x | −20.2% | 108 |
| 102 | Streamlined Ventures ◊ | −5.5 | −21.4% | 0.18x | −14.4% | 92 |
| 103 | Highland Capital | −6.1 | −22.0% | 0.02x | −19.9% | 120 |
| 104 | Battery Ventures | −6.5 | −22.3% | 0.07x | −21.8% | 104 |
| 105 | Qumra | −6.6 | −22.4% | 0.16x | −17.4% | 96 |
| 106 | Tenaya Capital | −8.0 | −23.8% | 0.02x | −22.5% | 124 |
| 107 | Draper Associates ◊ | −8.1 | −24.0% | 0.10x | −20.0% | 106 |
| 108 | ACME Capital ◊ | −8.2 | −24.1% | 0.08x | −22.6% | 109 |
| 109 | Zeev Ventures ◊ | −8.3 | −24.2% | 0.18x | −16.4% | 98 |
| 110 | Dawn Capital | −8.6 | −24.5% | 0.11x | −18.1% | 102 |
| 111 | Initialized Capital ◊ | −8.8 | −24.6% | 0.14x | −20.0% | 103 |
| 112 | DAG Ventures ◊ | −9.1 | −25.0% | 0.02x | −23.9% | 128 |
| 113 | SineWave Ventures ◊ | −9.2 | −25.1% | 0.12x | −19.1% | 105 |
| 114 | GGV Capital | −9.4 | −25.3% | 0.06x | −23.7% | 114 |
| 115 | Tribeca Venture Partners | −9.4 | −25.3% | 0.04x | −20.7% | 116 |
| 116 | Boost VC ◊ | −10.9 | −26.8% | 0.11x | −20.6% | 110 |
| 117 | Spark Capital | −11.0 | −26.9% | 0.07x | −25.4% | 113 |
| 118 | Westly Group ◊ | −11.2 | −27.0% | 0.03x | −23.0% | 121 |
| 119 | Sapphire Ventures | −11.9 | −27.7% | 0.08x | −26.0% | 112 |
| 120 | True Ventures | −12.1 | −28.0% | 0.05x | −25.6% | 118 |
| 121 | Matrix China | −12.7 | −28.6% | 0.05x | −25.1% | 119 |
| 122 | Bain Capital Ventures | −12.9 | −28.8% | 0.04x | −27.8% | 122 |
| 123 | Sequoia China (HongShan) | −13.5 | −29.4% | 0.08x | −27.1% | 115 |
| 124 | BV Capital | −14.6 | −30.4% | 0.05x | −25.1% | 117 |
| 125 | Almaz Capital ◊ | −14.7 | −30.6% | 0.02x | −27.1% | 133 |
| 126 | 500 Global ◊ | −16.6 | −32.5% | 0.04x | −30.6% | 129 |
| 127 | Forerunner Ventures ◊ | −17.8 | −33.7% | 0.06x | −27.9% | 123 |
| 128 | Canaan Partners | −19.2 | −35.1% | 0.01x | −33.3% | 141 |
| 129 | Polaris Partners | −19.3 | −35.2% | 0.01x | −32.1% | 139 |
| 130 | China Broadband Capital ◊ | −19.8 | −35.7% | 0.01x | −32.3% | 142 |
| 131 | Valor Capital Group ◊ | −20.2 | −36.1% | 0.07x | −30.1% | 125 |
| 132 | Sozo Ventures ◊ | −20.3 | −36.2% | 0.06x | −29.9% | 126 |
| 133 | NextEquity Partners ◊ | −21.1 | −36.9% | 0.05x | −31.7% | 130 |
| 134 | Version One | −21.8 | −37.7% | 0.04x | −32.2% | 131 |
| 135 | Haystack ◊ | −21.9 | −37.8% | 0.06x | −31.7% | 127 |
| 136 | Ten Eleven Ventures ◊ | −22.1 | −38.0% | 0.04x | −32.7% | 132 |
| 137 | Norwest | −22.8 | −38.6% | 0.01x | −37.5% | 137 |
| 138 | Greycroft | −22.8 | −38.7% | 0.03x | −36.3% | 135 |
| 139 | Source Code Capital | −26.3 | −42.1% | 0.03x | −37.1% | 136 |
| 140 | Tusk Ventures ◊ | −29.2 | −45.1% | 0.05x | −39.2% | 134 |
| 141 | A Capital ◊ | −30.7 | −46.5% | 0.01x | −42.7% | 144 |
| 142 | Global Founders Capital ◊ | −33.5 | −49.4% | 0.01x | −46.1% | 145 |
| 143 | Slow Ventures ◊ | −34.9 | −50.8% | 0.02x | −45.3% | 143 |
| 144 | Base10 Partners ◊ | −37.5 | −53.4% | 0.04x | −50.8% | 138 |
| 145 | Acrew Capital ◊ | −38.6 | −54.5% | 0.04x | −48.7% | 140 |
| 146 | Lerer Hippeau ◊ | −41.3 | −57.2% | 0.00x | −52.8% | 146 |
| 147 | Lux Ventures ◊ | −79.2 | −95.1% | 0.00x | −91.7% | 147 |

## Appendix C: data files

*In the open dataset these files are replaced by the tables in `data/`: see the mapping in [docs/methodology.md](../methodology.md#report-files-and-dataset-tables).*

All values in these files are at the 2 October 2026 close (column `valuation_date`).
- **`vc_value_per_dollar_ranking_v8.csv`**, one row per firm:
  - the consistency-adjusted figure with its range and rank range, the same figure at a fifth and at half the weight on depth, plain value per dollar and its range, and value beyond the largest company;
  - value, capital at risk and the annualised measures (adjusted and unadjusted);
  - type, the reason a firm is not ranked, notes (including what changed in versions 7 and 8), and ranks on primary value and on stage-weighted value.
  - Firms not ranked are listed after the ranked firms.
- **`vc_fund_ranking_v8.csv`:** every ranked firm's fund generations with vintage, committed capital, capital at risk, value, plain and adjusted value per dollar with range, largest company and how its split was established, and the vehicles in each generation.
- **`vc_fund_attribution_v8.csv`:** each position's split between the firm's funds, with the share, primary fraction, value, basis (filing type or rule) and source.
- **`vc_top20_companies_v8.csv`:** the 20 companies with the most long-term value created, with value at listing and at the end date, venture funds' stake and primary value, and the largest venture holders.
- **`vc_fund_histories_v7.csv`:** every fund vehicle for the 180 firms, with vintage, size, strategy, scope, source, confidence and its capital at risk under the main specification.
- **`vc_value_creation_book_v17.csv`:** every holder line, with:
  - the stake (and its range where estimated), valuation at the end date and provenance;
  - the primary share, with low and high cases where uncertain;
  - the stage-weighted value;
  - for version 7 additions, the research file, method and arithmetic in the provenance note; for version 8 corrections, the change and its filing (`v17_change`).
- **`vc_conviction_weighted_ranking_v17.csv`:** the stage-weighted total-value rankings (Layer 1, Layer 2, Layer 1 ex-SpaceX).
- **`vc_gap_register_v16_final.csv`:** the 328 (firm, listing) pairs version 7's coverage check found missing, with sources, 13F counts and each pair's outcome.
- **`vc-v17-changes.md`** (in the project): every change made in book v17 and fund files v17, with its filing, and the fund-level research behind §4.

## Appendix D: changes since version 5

**Version 8:**
- **New rankings:** the 20 companies with the most long-term value created (§3) and the 20 fund generations with the highest consistency-adjusted value per dollar (§4), from fund-level attribution research on 36 firms' 234 positions.
- **Book v17 (numerator):** shares bought from other holders removed from Pelion's Cloudflare, Index's Datadog and Figma, Andreessen Horowitz's Coinbase and Navan, Lightspeed's Rubrik, Benchmark's Uber, Accel's Etsy, UiPath and five smaller stakes, Union Square Ventures' Etsy, and Sequoia's Airbnb, Instacart and Figma; JVP's CyberArk primary share raised from 50% to 83%; Accel's Atlassian stake taken from its 13G (6.9%, not 11.2%); other investors' shares removed from Emergence's Zoom, DFJ's Redfin and PubMatic, and Founders Fund's Affirm blocks; Sequoia's SentinelOne stake (Global Equities fund) removed. Net −$5.7bn of ranked firms' value.
- **Fund files v17 (denominator):** sizes corrected for FirstMark Capital I, Khosla Ventures Seed B, Altos Ventures IV (with its reserve fund), Sequoia Capital XII (with its side funds), DFJ Growth 2006 and 2013, Pelion V, Kaszek I, Lightspeed VII, Bessemer VII's two vehicles and a16z's Annex Fund; partners' side funds sized for Accel, Index, Greylock, Redpoint, JVP and Sequoia; Benchmark's Cerebras vehicles and Felicis's Clover Fund added; Glynn's funds separated; Lowercase RT in scope with its sidecar at the Slack cheque.
- **Ranking order:** the top two are no longer shown as joint first; firms are ranked on their central figures (Sutter Hill first, Founders Fund second).
- **Closed items:** Amicus Capital and IT-Farm set aside; DFJ's SpaceX stake checked against EDGAR (no count yet).
- **Report:** new §3 and §4; sections 3–11 of version 7 are now 5–13, and §10.12 describes the fund-level measure.

**Version 7:**
- **Performance end date** fixed at the 2 October 2026 close for every figure (Odin, 18 October 2026).
- **Coverage check (§8):** investor-agreement sweep and 13F reverse sweep of the 147 listings worth $3bn or more, full-text name probe of 72 listings (1,280 searches), two sizing rounds and closing screens.
- **Book v16 (numerator):** 181 holder lines added for 99 firms ($69.9bn of primary value; $44.1bn excluding DFJ's SpaceX stake). Corrections to DFJ's Box, Redpoint's Twilio and Kleiner Perkins' DoorDash stakes.
- **Fund files (denominator):** fund histories for 51 more firms (180 in all), sized mainly from Form D filings; Lowercase's sidecar and RPM's BGW Ventures IV added to existing files.
- **Firm map:** Bullet Time into Techstars Ventures, Sherpa into ACME Capital, Pacven Walden into Walden International; Tim Draper's personal vehicles kept apart from DFJ; Glynn's hybrid funds and stakes held through renminbi vehicles excluded.
- **Classification:** NYC Seed, K5 Global, Protoscale Capital, Avid Park and VaynerRSE listed separately by the existing test.
- **Ranking:** 147 firms ranked (101 in version 6). The stage-weighted companion ranking is rebuilt from book v16, with the new positions weighted like the rest (vintage-adjusted, SpaceX at half speed).
- **Report:** new section on the coverage check (now §8); sections 6–10 of version 6 became 7–11.

**Version 6:**
- **Weight on depth** lowered from one-half to one-third (Odin, 12 October 2026). A one-company firm now keeps (1 + value per dollar)^(2/3) − 1.
- **Checks on the adjustment** became the one-fifth and one-half weights and depth beyond the two largest companies (§7).
- **Re-screen** of firms without fund histories at the new weight, with Origin Ventures' fund sizes documented from Form D filings and press.

**Version 5:**
- **Method:** consistency-adjusted headline (§10.1); three robustness checks on the adjustment; firm classification (13 firms moved out at Odin's request, 4 more by the same test, SWaN & Legend kept out); Sutter Hill and Founders Fund joint first.
- **Universe (§10.2):** seventeen listings added ($149bn).
- **Book v15:** Lowercase's Uber stake 25% removed as bought from holders and its Twilio stake removed; First Round's Square stake 1.8% → 0.3%; Y Combinator's Airbnb stake 1.6% → 0.9%; four takeout values corrected; holder types corrected; Gaorong merged into Banyan; DFJ Growth's Anaplan stake attributed to DFJ; mFund attributed to NetDragon.
- **Fund histories:** new files for Granite Ventures, Cathay Innovation, Romulus Capital, Highway 12 Ventures, Bay Partners, El Dorado Ventures and SWaN & Legend; Sutter Hill's capital deployed in 2009–24 revised from $2.35bn to $1.86bn; Lowercase's Industry Fund vehicles moved to sensitivity only; Altos, Celesta, Y Combinator and Pelion corrected.
