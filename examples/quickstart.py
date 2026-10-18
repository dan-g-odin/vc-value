#!/usr/bin/env python3
"""Quick start: load the tables with pandas, look at the rankings and drill into one firm.

Run from the repository root:  python examples/quickstart.py"""
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]


def read(table, group='core'):
    return pd.read_csv(ROOT / 'data' / group / f'{table}.csv', keep_default_na=False, na_values=[''])


listings, firms, holdings = read('listings'), read('firms'), read('holdings')
vehicles, allocations, generations = read('fund_vehicles'), read('fund_allocations'), read('fund_generations')
firm_metrics, fund_metrics, companies = read('firm_metrics', 'derived'), read('fund_metrics', 'derived'), read('listing_venture_summary', 'derived')
names = firms.set_index('firm_id').firm_name
firm_metrics['rank'] = firm_metrics['rank'].astype('Int64'); fund_metrics['rank'] = fund_metrics['rank'].astype('Int64')

pd.set_option('display.width', 160); pd.set_option('display.max_colwidth', 60)

print('Top 10 firms by consistency-adjusted value per dollar of capital at risk (end date 2 October 2026)')
top = firm_metrics[firm_metrics.measurement_status == 'ranked'].sort_values('rank').head(10)
print(top.assign(firm=top.firm_id.map(names))[['rank', 'firm', 'consistency_adjusted_value_per_dollar', 'adjusted_low', 'adjusted_high',
                                               'value_per_dollar', 'value_primary_usd_bn', 'capital_at_risk_usd_bn', 'largest_company_listing_id']]
      .round(2).to_string(index=False))

print('\nTop 10 fund generations')
tf = fund_metrics[fund_metrics['rank'].notna()].sort_values('rank').head(10)
print(tf[['rank', 'fund_display_name', 'vintage', 'committed_usd_m', 'value_primary_usd_bn', 'value_per_dollar', 'consistency_adjusted_value_per_dollar']]
      .round(2).to_string(index=False))

print('\nTop 10 companies by long-term value created')
tc = companies.merge(listings[['listing_id', 'company', 'listing_date']], on='listing_id').head(10)
print(tc[['rank_by_value_end', 'company', 'listing_date', 'value_end_usd_bn', 'multiple_since_listing', 'venture_funds_stake_pct', 'largest_venture_holders']]
      .round(1).to_string(index=False))

# Drill-down: one firm's holdings, how its value splits between funds, and its capital at risk
firm = 'founders-fund'
h = holdings[(holdings.firm_id == firm) & (holdings.holder_type == 'core_venture')].merge(listings[['listing_id', 'company']], on='listing_id')
print(f'\n{names[firm]}: primary value counted by listing ($bn)')
print(h.groupby('company').primary_value_counted_usd_bn.sum().sort_values(ascending=False).round(2).to_string())
a = allocations[allocations.firm_id == firm].merge(generations[['generation_id', 'generation_label']], on='generation_id', how='left')
a['credited_to'] = a.generation_label.fillna(a.vehicle_outside_fund_files)
print(f'\n{names[firm]}: primary value by fund generation or outside vehicle ($bn)')
print(a.groupby('credited_to').primary_value_usd_bn.sum().sort_values(ascending=False).round(2).to_string())
k = vehicles[(vehicles.firm_id == firm) & (vehicles.in_scope == 'Y')]
print(f'\n{names[firm]}: capital at risk ${k.capital_at_risk_usd_m.sum() / 1000:.2f}bn from {len(k)} in-scope vehicles')
