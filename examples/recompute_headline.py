#!/usr/bin/env python3
"""Recompute every firm's headline figure from the core tables and compare it with firm_metrics.csv.

headline = (1 + V/K)^(2/3) x (1 + (V - V_top)/K)^(1/3) - 1
  V      = sum of holdings.primary_value_counted_usd_bn over the firm's core venture lines
  V_top  = the same sum for the firm's largest listing
  K      = sum of fund_vehicles.capital_at_risk_usd_m over in-scope vehicles, in billions

Also re-derives the order of the ranking: firms are ranked on the central headline figure, even where neighbouring ranges overlap.
Run from the repository root: python examples/recompute_headline.py"""
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
read = lambda p: pd.read_csv(ROOT / p, keep_default_na=False, na_values=[''])
H, V, FM = read('data/core/holdings.csv'), read('data/core/fund_vehicles.csv'), read('data/derived/firm_metrics.csv')

core = H[H.holder_type == 'core_venture']
by_listing = core.groupby(['firm_id', 'listing_id']).primary_value_counted_usd_bn.sum()
K = V[V.in_scope == 'Y'].groupby('firm_id').capital_at_risk_usd_m.sum() / 1000

rows = []
for firm in FM.firm_id:
    if firm not in by_listing.index.get_level_values(0) or K.get(firm, 0) <= 0:
        continue
    v = by_listing.loc[firm]; k = K[firm]
    eff = v.sum() / k; depth = (v.sum() - v.max()) / k
    rows.append(dict(firm_id=firm, V=v.sum(), K=k, eff=eff, depth=depth, headline=(1 + eff) ** (2 / 3) * (1 + depth) ** (1 / 3) - 1))
R = pd.DataFrame(rows).merge(FM[['firm_id', 'measurement_status', 'rank', 'consistency_adjusted_value_per_dollar', 'adjusted_low', 'adjusted_high']], on='firm_id')
R['diff'] = (R.headline - R.consistency_adjusted_value_per_dollar).abs()
R['ok'] = R['diff'] <= 1e-5 + 1e-4 * R.consistency_adjusted_value_per_dollar.abs()   # tolerance for rounding in the CSV files
print(f'{len(R)} firms recomputed; {int((~R.ok).sum())} differ from firm_metrics beyond rounding; largest difference {R["diff"].max():.1e}')

ranked = R[R.measurement_status == 'ranked'].sort_values('headline', ascending=False).reset_index(drop=True)
ranked['recomputed_rank'] = range(1, len(ranked) + 1)
mism = ranked[ranked.recomputed_rank != ranked['rank']]
print('Top five:', ', '.join(f'{r.recomputed_rank}. {r.firm_id} {r.headline:.1f}x' for r in ranked.head(5).itertuples()))
print('rank mismatches:', len(mism))
sys.exit(0 if R.ok.all() and mism.empty else 1)
