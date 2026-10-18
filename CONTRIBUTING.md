# Contributing

Thank you for helping improve this dataset. Corrections, additions and questions about the method are all welcome.

## Ground rules

- **Every value needs a public source.** Link the filing or document and say where the figure appears (page, footnote, table). SEC EDGAR filings are preferred. Values from paywalled or licensed sources cannot be added unless the fact is also public.
- **The end date is fixed.** Values are measured at the close on 2 October 2026. A price move after that date is not a correction; rolling the end date forward is a maintainer decision made for a whole version.
- **No personal holdings.** The dataset covers institutional holders. Holdings of natural persons are not added.
- **Keep the method separate from the data.** Proposals to change how a measure is defined go in a methodology issue first.

## How to propose a change

1. **Open an issue** using the [data correction](.github/ISSUE_TEMPLATE/data_correction.yml), [missing entity](.github/ISSUE_TEMPLATE/missing_entity.yml) or [methodology question](.github/ISSUE_TEMPLATE/methodology_question.yml) template. Small, well-sourced corrections can go straight to a pull request.
2. **Edit the core tables** (`data/core/*.csv`) in a branch. Keep identifiers stable: never renumber or rename existing `firm_id`, `generation_id`, `vehicle_id`, `holding_id` or `listing_id` values. New holder lines take the next free `holding_id`; new vehicles take `firm_id--slug-of-fund-name`.
3. **Record the evidence** in the row's source and note fields (`provenance_source_url`, `provenance_note`, `source_url`, `note`).
4. **Run the checks:**
   ```bash
   pip install -r requirements.txt
   python scripts/validate.py
   ```
   The validator checks types, allowed values, primary and foreign keys, and recomputes stake values, capital at risk and the headline figures. If you changed a core value, the derived tables will no longer reconcile: say so in the pull request and the maintainers will regenerate them.
5. **Schema changes** (new columns or tables) need an issue first. Update `schema/` and `datapackage.json`, then run `python scripts/make_data_dictionary.py`.
6. **Add a line to `CHANGELOG.md`** under "Unreleased".

## Review

A maintainer checks the source, the arithmetic and the effect on the rankings, usually within a few weeks. Changes that move a ranked firm's figure are batched into the next release, which gets a new version number and a new Zenodo DOI.

## Versioning

Releases follow semantic versioning adapted to data:
- **Major** (2.0.0): a change of method, end date or schema that breaks comparability or existing code.
- **Minor** (1.1.0): corrections or additions that change values or rankings.
- **Patch** (1.0.1): documentation and metadata fixes that change no value.
