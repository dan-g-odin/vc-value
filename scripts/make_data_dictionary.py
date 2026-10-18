#!/usr/bin/env python3
"""Generate docs/data_dictionary.md from datapackage.json and schema/*.json.

Usage:
    python scripts/make_data_dictionary.py           # (re)write docs/data_dictionary.md
    python scripts/make_data_dictionary.py --check   # exit 1 if the file is out of date (used in CI)"""
import argparse, csv, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs' / 'data_dictionary.md'
GROUPS = [('data/core/', 'Core tables', 'Observations taken from filings and other sources: listings, holders, fund histories, holdings, fund splits and benchmark prices.'),
          ('data/derived/', 'Derived tables', 'Figures computed from the core tables: firm and fund metrics, robustness checks, company summaries and the companion stage-weighted ranking.'),
          ('data/reference/', 'Reference tables', 'Parameters and records behind the method: timing weights, lag distributions, strategy parameters, specifications and the coverage register.')]


def esc(s):
    return str(s).replace('|', '\\|').replace('\n', ' ')


def constraints(f):
    c = f.get('constraints', {}); out = []
    if c.get('unique'): out.append('unique')
    if 'enum' in c: out.append('one of: ' + ', '.join(f'`{x}`' for x in c['enum']))
    if 'minimum' in c: out.append(f'min {c["minimum"]}')
    if 'maximum' in c: out.append(f'max {c["maximum"]}')
    if 'pattern' in c: out.append(f'pattern `{c["pattern"]}`')
    return '; '.join(out)


def build():
    dp = json.loads((ROOT / 'datapackage.json').read_text(encoding='utf-8'))
    L = ['# Data dictionary', '',
         f'*{dp["title"]}, version {dp["version"]}. Generated from `datapackage.json` and `schema/*.json` by `scripts/make_data_dictionary.py`; do not edit by hand.*', '',
         'All values are measured at the performance end date, the close on **2 October 2026**. Money is in US dollars (`_usd_m` millions, `_usd_bn` billions). '
         'Shares of a total are fractions from 0 to 1 unless the column ends in `_pct` (percent). Blank cells are missing values. Booleans are `true`/`false`. Dates are ISO 8601.', '']
    for prefix, title, blurb in GROUPS:
        rs = [r for r in dp['resources'] if r['path'].startswith(prefix)]
        L += [f'- **{title}:** ' + ', '.join(f'[`{r["name"]}`](#{r["name"]})' for r in rs)]
    L.append('')
    for prefix, title, blurb in GROUPS:
        L += [f'## {title}', '', blurb, '']
        for r in [r for r in dp['resources'] if r['path'].startswith(prefix)]:
            s = json.loads((ROOT / r['schema']).read_text(encoding='utf-8')) if isinstance(r['schema'], str) else r['schema']
            with open(ROOT / r['path'], newline='', encoding='utf-8') as fh:
                n = sum(1 for _ in csv.reader(fh)) - 1
            L += [f'### {r["name"]}', '', f'**{r["title"]}.** {r["description"]}', '',
                  f'- File: [`{r["path"]}`](../{r["path"]}) ({n:,} rows)', f'- Primary key: `{", ".join(s["primaryKey"])}`']
            for fk in s.get('foreignKeys', []):
                L.append(f'- Foreign key: `{", ".join(fk["fields"])}` → `{fk["reference"]["resource"]}.{", ".join(fk["reference"]["fields"])}`')
            L += ['', '| Field | Type | Required | Description | Constraints |', '|---|---|---|---|---|']
            for f in s['fields']:
                L.append(f'| `{f["name"]}` | {f["type"]} | {"yes" if f.get("constraints", {}).get("required") else ""} | {esc(f.get("description", ""))} | {esc(constraints(f))} |')
            L.append('')
    return '\n'.join(L).rstrip() + '\n'


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--check', action='store_true'); a = ap.parse_args()
    text = build()
    if a.check:
        if not OUT.exists() or OUT.read_text(encoding='utf-8') != text:
            print('docs/data_dictionary.md is out of date: run python scripts/make_data_dictionary.py'); sys.exit(1)
        print('docs/data_dictionary.md is up to date'); return
    OUT.parent.mkdir(exist_ok=True); OUT.write_text(text, encoding='utf-8'); print(f'wrote {OUT.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
