#!/usr/bin/env python3
"""Build one SQLite database holding every table, with primary keys, foreign keys and convenience views.

Usage:
    python scripts/build_sqlite.py                       # writes database/venture_value_per_dollar.sqlite
    python scripts/build_sqlite.py --output /tmp/x.sqlite

Uses only the Python standard library."""
import argparse, csv, json, sqlite3, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SQL_TYPE = {'string': 'TEXT', 'integer': 'INTEGER', 'number': 'REAL', 'boolean': 'INTEGER', 'date': 'TEXT'}

VIEWS = {
    'v_firm_ranking': """
        SELECT fm.rank, f.firm_name, fm.consistency_adjusted_value_per_dollar, fm.adjusted_low, fm.adjusted_high,
               fm.rank_range_best, fm.rank_range_worst, fm.value_per_dollar, fm.value_per_dollar_beyond_largest,
               fm.value_primary_usd_bn, fm.capital_at_risk_usd_bn, l.company AS largest_company, fm.largest_company_share, fm.companies,
               fm.rank_vs_qqq, fm.direct_alpha_vs_qqq_adjusted
        FROM firm_metrics fm JOIN firms f USING (firm_id) LEFT JOIN listings l ON l.listing_id = fm.largest_company_listing_id
        WHERE fm.measurement_status = 'ranked' ORDER BY fm.rank""",
    'v_fund_ranking': """
        SELECT fu.rank, fu.fund_display_name, f.firm_name, fu.vintage, fu.committed_usd_m, fu.capital_at_risk_usd_m, fu.value_primary_usd_bn,
               fu.value_per_dollar, fu.consistency_adjusted_value_per_dollar, fu.adjusted_low, fu.adjusted_high,
               l.company AS largest_company, fu.largest_company_share, fu.largest_company_split_basis
        FROM fund_metrics fu JOIN firms f USING (firm_id) LEFT JOIN listings l ON l.listing_id = fu.largest_company_listing_id
        WHERE fu.rank IS NOT NULL ORDER BY fu.rank""",
    'v_top_companies': """
        SELECT s.rank_by_value_end, l.company, l.listing_date, s.value_at_listing_usd_bn, s.value_end_usd_bn, s.multiple_since_listing,
               s.venture_funds_stake_pct, s.venture_primary_value_usd_bn, s.largest_venture_holders
        FROM listing_venture_summary s JOIN listings l USING (listing_id) ORDER BY s.rank_by_value_end""",
    'v_holdings': """
        SELECT h.holding_id, l.company, h.listing_id, l.listing_date, f.firm_name, h.firm_id, h.holder_type, h.holder_as_filed, h.stake_pct,
               h.value_end_usd_bn, h.primary_share, h.primary_value_counted_usd_bn, h.first_round, h.entry_year, h.stake_confidence
        FROM holdings h JOIN listings l USING (listing_id) JOIN firms f USING (firm_id)""",
}


def load(dp):
    out = {}
    for r in dp['resources']:
        schema = r['schema']
        if isinstance(schema, str):
            schema = json.loads((ROOT / schema).read_text(encoding='utf-8'))
        out[r['name']] = (r, schema)
    return out


def order(res):
    """Create referenced tables before the tables that reference them."""
    done, seq = set(), []
    def visit(n, stack=()):
        if n in done: return
        for fk in res[n][1].get('foreignKeys', []):
            t = fk['reference']['resource'] or n
            if t != n and t not in stack: visit(t, stack + (n,))
        done.add(n); seq.append(n)
    for n in res: visit(n)
    return seq


def convert(v, t):
    if v == '': return None
    if t == 'integer': return int(v)
    if t == 'number': return float(v)
    if t == 'boolean': return 1 if v == 'true' else 0
    return v


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--output', default=str(ROOT / 'database' / 'venture_value_per_dollar.sqlite')); args = ap.parse_args()
    dp = json.loads((ROOT / 'datapackage.json').read_text(encoding='utf-8'))
    res = load(dp); out = Path(args.output); out.parent.mkdir(parents=True, exist_ok=True)
    if out.exists(): out.unlink()
    con = sqlite3.connect(out); con.execute('PRAGMA foreign_keys = ON')
    for name in order(res):
        r, s = res[name]
        cols = [f'"{f["name"]}" {SQL_TYPE[f["type"]]}' + (' NOT NULL' if f.get('constraints', {}).get('required') else '') for f in s['fields']]
        cons = [f'PRIMARY KEY ({", ".join(chr(34) + c + chr(34) for c in s["primaryKey"])})']
        for fk in s.get('foreignKeys', []):
            ref = fk['reference']
            cons.append(f'FOREIGN KEY ({", ".join(fk["fields"])}) REFERENCES {ref["resource"] or name} ({", ".join(ref["fields"])})')
        con.execute(f'CREATE TABLE {name} (\n  ' + ',\n  '.join(cols + cons) + '\n)')
        types = [f['type'] for f in s['fields']]
        with open(ROOT / r['path'], newline='', encoding='utf-8') as fh:
            rd = csv.reader(fh); header = next(rd)
            assert header == [f['name'] for f in s['fields']], f'{name}: header does not match schema'
            rows = [[convert(v, t) for v, t in zip(row, types)] for row in rd]
        con.executemany(f'INSERT INTO {name} VALUES ({", ".join("?" * len(types))})', rows)
        for fk in s.get('foreignKeys', []):
            con.execute(f'CREATE INDEX IF NOT EXISTS idx_{name}_{"_".join(fk["fields"])} ON {name} ({", ".join(fk["fields"])})')
        print(f'{name:26s} {len(rows):6d} rows')
    for v, q in VIEWS.items():
        con.execute(f'CREATE VIEW {v} AS {q}')
    con.execute('CREATE TABLE _metadata (key TEXT PRIMARY KEY, value TEXT)')
    meta = {'name': dp.get('name'), 'title': dp.get('title'), 'version': dp.get('version'), 'performance_end_date': '2026-10-02',
            'license': dp['licenses'][0]['name'], 'homepage': dp.get('homepage', '')}
    con.executemany('INSERT INTO _metadata VALUES (?, ?)', list(meta.items()))
    con.commit()
    bad = con.execute('PRAGMA foreign_key_check').fetchall()
    if bad:
        print('foreign-key violations:', bad[:10]); sys.exit(1)
    con.execute('VACUUM'); con.close()
    print(f'wrote {out} ({out.stat().st_size / 1e6:.1f} MB); foreign keys checked')


if __name__ == '__main__':
    main()
