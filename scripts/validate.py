#!/usr/bin/env python3
"""Validate the dataset against its schemas and recompute the headline figures from the core tables.

Usage:
    python scripts/validate.py            # full validation
    python scripts/validate.py --quick    # schema checks only (types, constraints, keys)

Exit code 0 if no errors (warnings are allowed), 1 otherwise. Needs only pandas."""
import argparse, json, math, re, sys
from collections import defaultdict
from datetime import date
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
errors, warnings = [], []


def err(msg): errors.append(msg)
def warn(msg): warnings.append(msg)


def load_package():
    dp = json.loads((ROOT / 'datapackage.json').read_text(encoding='utf-8'))
    res = {}
    for r in dp['resources']:
        schema = r['schema']
        if isinstance(schema, str):
            schema = json.loads((ROOT / schema).read_text(encoding='utf-8'))
        res[r['name']] = dict(path=ROOT / r['path'], schema=schema)
    return dp, res


def read_raw(path):
    return pd.read_csv(path, dtype=str, keep_default_na=False, na_values=[], encoding='utf-8')


def is_date(s):
    try:
        y, m, d = map(int, s.split('-')); date(y, m, d); return bool(re.fullmatch(r'\d{4}-\d{2}-\d{2}', s))
    except Exception:
        return False


def typed(raw, schema):
    """Check types and constraints on the raw strings and return a typed DataFrame."""
    out = {}
    name_ = raw.attrs.get('name')
    expected = [f['name'] for f in schema['fields']]
    if list(raw.columns) != expected:
        err(f'{name_}: header {list(raw.columns)} does not match schema {expected}')
        return None
    for f in schema['fields']:
        c, t, cons = f['name'], f['type'], f.get('constraints', {})
        s = raw[c]
        missing = s == ''
        if cons.get('required') and missing.any():
            err(f'{name_}.{c}: {int(missing.sum())} missing values in a required field (first row {int(missing.idxmax()) + 2})')
        v = s[~missing]
        if t == 'integer':
            bad = v[~v.str.fullmatch(r'-?\d+')]
            if len(bad): err(f'{name_}.{c}: {len(bad)} values are not integers (e.g. {bad.iloc[0]!r})')
            col = pd.to_numeric(s.where(~missing), errors='coerce').astype('Int64')
        elif t == 'number':
            col = pd.to_numeric(s.where(~missing), errors='coerce')
            bad = v[col[~missing].isna()]
            if len(bad): err(f'{name_}.{c}: {len(bad)} values are not numbers (e.g. {bad.iloc[0]!r})')
        elif t == 'boolean':
            bad = v[~v.isin(['true', 'false'])]
            if len(bad): err(f'{name_}.{c}: {len(bad)} values are not true/false (e.g. {bad.iloc[0]!r})')
            col = s.map({'true': True, 'false': False})
        elif t == 'date':
            bad = v[~v.map(is_date)]
            if len(bad): err(f'{name_}.{c}: {len(bad)} values are not ISO dates (e.g. {bad.iloc[0]!r})')
            col = s.where(~missing)
        else:
            col = s.where(~missing)
        if 'enum' in cons:
            bad = v[~v.isin([str(x) for x in cons['enum']])]
            if len(bad): err(f'{name_}.{c}: {len(bad)} values outside the allowed set (e.g. {bad.iloc[0]!r})')
        if 'pattern' in cons:
            bad = v[~v.str.fullmatch(cons['pattern'])]
            if len(bad): err(f'{name_}.{c}: {len(bad)} values do not match {cons["pattern"]} (e.g. {bad.iloc[0]!r})')
        if t in ('integer', 'number'):
            num = pd.to_numeric(col, errors='coerce')
            if 'minimum' in cons and (num < cons['minimum']).any():
                err(f'{name_}.{c}: {int((num < cons["minimum"]).sum())} values below the minimum {cons["minimum"]}')
            if 'maximum' in cons and (num > cons['maximum']).any():
                err(f'{name_}.{c}: {int((num > cons["maximum"]).sum())} values above the maximum {cons["maximum"]}')
        if cons.get('unique'):
            dup = v[v.duplicated()]
            if len(dup): err(f'{name_}.{c}: {len(dup)} duplicate values (e.g. {dup.iloc[0]!r})')
        out[c] = col
    df = pd.DataFrame(out)
    pk = schema.get('primaryKey', [])
    if pk:
        if raw[pk].eq('').any(axis=None):
            err(f'{name_}: missing values in the primary key {pk}')
        d = raw.duplicated(subset=pk)
        if d.any():
            err(f'{name_}: {int(d.sum())} duplicate primary keys {pk} (e.g. {raw.loc[d, pk].iloc[0].tolist()})')
    return df


def close(a, b, rel=1e-3, abs_=1e-6):
    return abs(a - b) <= abs_ + rel * max(abs(a), abs(b))


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--quick', action='store_true'); args = ap.parse_args()
    dp, res = load_package()
    T, RAW = {}, {}
    for name, r in res.items():
        if not r['path'].exists():
            err(f'{name}: file {r["path"].relative_to(ROOT)} not found'); continue
        raw = read_raw(r['path']); raw.attrs['name'] = name; RAW[name] = raw
        T[name] = typed(raw, r['schema'])
    # foreign keys
    for name, r in res.items():
        if T.get(name) is None: continue
        for fk in r['schema'].get('foreignKeys', []):
            ref = fk['reference']; target = ref['resource'] or name
            if T.get(target) is None: err(f'{name}: foreign-key target {target} missing'); continue
            src = RAW[name][fk['fields']]; keep = ~src.eq('').any(axis=1)
            have = set(map(tuple, RAW[target][ref['fields']].values.tolist()))
            bad = [tuple(x) for x in src[keep].values.tolist() if tuple(x) not in have]
            if bad: err(f'{name}: {len(bad)} values of {fk["fields"]} not found in {target}.{ref["fields"]} (e.g. {bad[0]})')
    if any(v is None for v in T.values()) or args.quick:
        return report(dp, quick=True)
    recompute(T)
    return report(dp)


def recompute(T):
    L, Fi, G, V, H, A = T['listings'], T['firms'], T['fund_generations'], T['fund_vehicles'], T['holdings'], T['fund_allocations']
    FM, FU, S, TW = T['firm_metrics'], T['fund_metrics'], T['listing_venture_summary'], T['timing_weights']
    n0 = len(errors)
    # listings: company values
    ads = L.ads_ratio.fillna(1.0)
    for r, a in zip(L.itertuples(), ads):
        if pd.notna(r.value_end_usd_bn) and not close(r.value_end_usd_bn, r.shares_post_offering_m * r.split_factor * r.price_end_usd / a / 1000):
            err(f'listings {r.listing_id}: value_end_usd_bn does not equal shares x split factor x price / ADS ratio')
        if pd.notna(r.value_at_listing_usd_bn) and pd.notna(r.offer_price_usd) and not close(r.value_at_listing_usd_bn, r.shares_post_offering_m * r.offer_price_usd / a / 1000):
            err(f'listings {r.listing_id}: value_at_listing_usd_bn does not equal shares x offer price / ADS ratio')
    cnt = H.groupby('listing_id').size()
    bad = L[L.n_holding_lines != L.listing_id.map(cnt).fillna(0).astype(int)]
    if len(bad): err(f'listings: n_holding_lines wrong for {len(bad)} listings (e.g. {bad.listing_id.iloc[0]})')
    # holdings: values
    lv = L.set_index('listing_id')
    for r in H.itertuples():
        if pd.notna(r.stake_pct):
            if not close(r.value_end_usd_bn, r.stake_pct / 100 * lv.value_end_usd_bn[r.listing_id], abs_=1e-7):
                err(f'holdings {r.holding_id}: value_end_usd_bn does not equal stake_pct x company value')
        if not close(r.primary_value_usd_bn, r.value_end_usd_bn * r.primary_share, abs_=1e-7):
            err(f'holdings {r.holding_id}: primary_value_usd_bn does not equal value_end_usd_bn x primary_share')
        if not close(r.primary_value_counted_usd_bn, r.primary_value_usd_bn * r.inside_capital_at_risk_share, abs_=1e-7):
            err(f'holdings {r.holding_id}: primary_value_counted_usd_bn does not equal primary value x inside share')
        for lo, mid, hi in [('stake_pct_low', 'stake_pct', 'stake_pct_high'), ('primary_share_low', 'primary_share', 'primary_share_high')]:
            a, b, c = getattr(r, lo), getattr(r, mid), getattr(r, hi)
            if pd.notna(a) and pd.notna(b) and a > b + 1e-6: err(f'holdings {r.holding_id}: {lo} above {mid}')
            if pd.notna(c) and pd.notna(b) and c < b - 1e-6: err(f'holdings {r.holding_id}: {hi} below {mid}')
    # fund vehicles: timing weights and capital at risk
    tw = TW.set_index(['vintage', 'strategy'])
    for r in V.itertuples():
        w = tw.loc[(r.vintage, r.strategy), 'deployed_year_weight' if r.is_capital_deployed_row else 'timing_weight']
        if not close(r.timing_weight, w, abs_=2e-6): err(f'fund_vehicles {r.vehicle_id}: timing_weight differs from timing_weights.csv')
        k = r.committed_usd_m * r.timing_weight if (r.in_scope == 'Y' and pd.notna(r.committed_usd_m) and r.committed_usd_m > 0) else 0.0
        if not close(r.capital_at_risk_usd_m, k, abs_=2e-3): err(f'fund_vehicles {r.vehicle_id}: capital_at_risk_usd_m does not equal committed x timing_weight')
    gk = V[V.in_scope == 'Y'].groupby('generation_id').capital_at_risk_usd_m.sum()
    for r in G.itertuples():
        if not close(r.capital_at_risk_usd_m, gk.get(r.generation_id, 0.0), abs_=0.01): err(f'fund_generations {r.generation_id}: capital at risk differs from its vehicles')
    # allocations against holdings
    core = H[H.holder_type == 'core_venture'].copy(); core['vin'] = core.value_end_usd_bn * core.inside_capital_at_risk_share
    hv = core.groupby(['firm_id', 'listing_id']).agg(vin=('vin', 'sum'), vc=('primary_value_counted_usd_bn', 'sum'))
    ag = A.groupby(['firm_id', 'listing_id']).agg(sh=('share_of_firm_stake', 'sum'), vt=('value_end_usd_bn', 'sum'), vp=('primary_value_usd_bn', 'sum'))
    for k, r in ag.iterrows():
        if abs(r.sh - 1) > 1e-5: err(f'fund_allocations {k}: shares sum to {r.sh:.6f}, not 1')
        if k not in hv.index: err(f'fund_allocations {k}: no core venture holding for this firm and listing'); continue
        h = hv.loc[k]
        if not close(r.vt, h.vin, abs_=1e-4): err(f'fund_allocations {k}: value differs from holdings ({r.vt:.6f} vs {h.vin:.6f})')
        if not close(r.vp, h.vc, abs_=1e-4):
            (warn if r.vp < h.vc else err)(f'fund_allocations {k}: primary value {r.vp:.6f} vs holdings {h.vc:.6f}'
                                           + (' (per-fund filings identify more shares bought from holders than the firm-level line; documented)' if r.vp < h.vc else ''))
    # firm metrics
    vk = V[V.in_scope == 'Y'].groupby('firm_id').capital_at_risk_usd_m.sum() / 1000
    byco = core.groupby(['firm_id', 'listing_id']).primary_value_counted_usd_bn.sum()
    for r in FM.itertuples():
        if r.firm_id not in byco.index.get_level_values(0):
            continue
        c = byco.loc[r.firm_id]; Vv = c.sum(); K = vk.get(r.firm_id, 0.0)
        if not close(r.value_primary_usd_bn, Vv): err(f'firm_metrics {r.firm_id}: V {r.value_primary_usd_bn} differs from holdings ({Vv:.6f})')
        if not close(r.capital_at_risk_usd_bn, K): err(f'firm_metrics {r.firm_id}: K {r.capital_at_risk_usd_bn} differs from fund vehicles ({K:.6f})')
        if K > 0 and pd.notna(r.consistency_adjusted_value_per_dollar):
            eff = Vv / K; dep = (Vv - c.max()) / K; cons = (1 + eff) ** (2 / 3) * (1 + dep) ** (1 / 3) - 1
            for nm, a, b in [('value_per_dollar', r.value_per_dollar, eff), ('value_per_dollar_beyond_largest', r.value_per_dollar_beyond_largest, dep),
                             ('consistency_adjusted_value_per_dollar', r.consistency_adjusted_value_per_dollar, cons)]:
                if not close(a, b, abs_=1e-5): err(f'firm_metrics {r.firm_id}: {nm} {a} differs from recomputation {b:.6f}')
            if int((c > 0).sum()) != r.companies: err(f'firm_metrics {r.firm_id}: companies {r.companies} differs from {int((c > 0).sum())}')
            if c.max() > 0 and c.idxmax() != r.largest_company_listing_id and not close(c.max(), c.get(r.largest_company_listing_id, 0)):
                err(f'firm_metrics {r.firm_id}: largest company {r.largest_company_listing_id} differs from {c.idxmax()}')
    rk = FM[FM.measurement_status == 'ranked'].sort_values('rank')
    if list(rk['rank']) != list(range(1, len(rk) + 1)): err('firm_metrics: ranks are not 1..n')
    viol = [(a.firm_id, b.firm_id) for a, b in zip(rk.iloc[:-1].itertuples(), rk.iloc[1:].itertuples())
            if b.consistency_adjusted_value_per_dollar > a.consistency_adjusted_value_per_dollar + 1e-9]
    if viol: err(f'firm_metrics: ranks are not in descending order of the headline (e.g. {viol[0]})')
    # fund metrics
    gV = A[A.generation_id.notna()].groupby(['generation_id', 'listing_id']).primary_value_usd_bn.sum()
    gK = G.set_index('generation_id').capital_at_risk_usd_m
    for r in FU.itertuples():
        c = gV.loc[r.generation_id] if r.generation_id in gV.index.get_level_values(0) else pd.Series(dtype=float)
        if not close(r.value_primary_usd_bn, c.sum(), abs_=1e-5): err(f'fund_metrics {r.generation_id}: value differs from allocations')
        if not close(r.capital_at_risk_usd_m, gK[r.generation_id], abs_=0.01): err(f'fund_metrics {r.generation_id}: capital at risk differs from fund_generations')
        K = r.capital_at_risk_usd_m / 1000
        if K > 0 and len(c):
            eff = c.sum() / K; cons = (1 + eff) ** (2 / 3) * (1 + (c.sum() - c.max()) / K) ** (1 / 3) - 1
            if not close(r.consistency_adjusted_value_per_dollar, cons, abs_=1e-4): err(f'fund_metrics {r.generation_id}: headline differs from recomputation ({cons:.4f})')
    rr = FU[FU['rank'].notna()].sort_values('rank')
    if list(rr['rank']) != list(range(1, len(rr) + 1)): err('fund_metrics: ranks are not 1..n')
    # listing venture summary
    ven = core[core.firm_id.map(Fi.set_index('firm_id').counts_as_venture_fund)]
    pe = (ven.stake_pct * ven.inside_capital_at_risk_share).groupby(ven.listing_id).sum()
    vp = ven.groupby('listing_id').primary_value_counted_usd_bn.sum()
    for r in S.itertuples():
        if not close(r.venture_funds_stake_pct, pe.get(r.listing_id, 0.0), abs_=1e-5): err(f'listing_venture_summary {r.listing_id}: venture stake differs from holdings')
        if not close(r.venture_primary_value_usd_bn, vp.get(r.listing_id, 0.0), abs_=1e-6): err(f'listing_venture_summary {r.listing_id}: venture primary value differs from holdings')
    # placeholders left from the template
    for f in ['README.md', 'CITATION.cff', '.zenodo.json', 'datapackage.json']:
        if (ROOT / f).exists() and 'github.com/OWNER/' in (ROOT / f).read_text(encoding='utf-8'):
            warn(f'{f}: repository URL placeholder (github.com/OWNER/...) not yet replaced; run scripts/set_release_metadata.py before release')
    print(f'recomputation checks: {len(errors) - n0} errors')


def report(dp, quick=False):
    name = dp.get('name'); ver = dp.get('version')
    print(f'{name} {ver}: {len(dp["resources"])} resources checked' + (' (schema checks only)' if quick else ''))
    for w in warnings[:50]: print('WARNING', w)
    if len(warnings) > 50: print(f'... {len(warnings) - 50} more warnings')
    for e in errors[:100]: print('ERROR', e)
    if len(errors) > 100: print(f'... {len(errors) - 100} more errors')
    print('OK' if not errors else f'FAILED with {len(errors)} errors', f'({len(warnings)} warnings)')
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
