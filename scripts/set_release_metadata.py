#!/usr/bin/env python3
"""Fill in the repository URL, DOI, version and release date across the metadata files before a release.

Usage:
    python scripts/set_release_metadata.py --repo-url https://github.com/<owner>/<name>
    python scripts/set_release_metadata.py --doi 10.5281/zenodo.1234567 --concept-doi 10.5281/zenodo.1234566
    python scripts/set_release_metadata.py --version 1.1.0 --date 2027-01-15

Edits README.md, CITATION.cff, .zenodo.json and datapackage.json in place. Standard library only."""
import argparse, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLACEHOLDER = 'https://github.com/OWNER/venture-value-per-dollar'


def sub_file(path, fn):
    p = ROOT / path; t = p.read_text(encoding='utf-8'); n = fn(t)
    if n != t: p.write_text(n, encoding='utf-8'); print('updated', path)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo-url'); ap.add_argument('--doi', help='version DOI from Zenodo'); ap.add_argument('--concept-doi', help='concept DOI (all versions)')
    ap.add_argument('--version'); ap.add_argument('--date', help='release date, YYYY-MM-DD')
    a = ap.parse_args()
    if a.repo_url:
        url = a.repo_url.rstrip('/')
        current = json.loads((ROOT / 'datapackage.json').read_text(encoding='utf-8')).get('homepage', PLACEHOLDER)
        for p in sorted(ROOT.rglob('*')):
            rel = p.relative_to(ROOT)
            if p.is_file() and p.suffix in ('.md', '.cff', '.json', '.yml', '.yaml') and rel.parts[0] not in ('data', 'schema', '.git'):
                sub_file(str(rel), lambda t: t.replace(PLACEHOLDER, url).replace(current, url))
    cite_doi = a.concept_doi or a.doi
    if cite_doi:
        badge = f'[![DOI](https://zenodo.org/badge/DOI/{cite_doi}.svg)](https://doi.org/{cite_doi})'
        sub_file('README.md', lambda t: re.sub(r'<!-- DOI-BADGE -->.*?<!-- /DOI-BADGE -->', f'<!-- DOI-BADGE -->{badge}<!-- /DOI-BADGE -->', t, flags=re.S))
        sub_file('README.md', lambda t: re.sub(r'<!-- CITATION-LINK -->.*?<!-- /CITATION-LINK -->', f'<!-- CITATION-LINK -->https://doi.org/{cite_doi}<!-- /CITATION-LINK -->', t, flags=re.S))
        def cff(t):
            t = re.sub(r'^#? ?doi: .*$', f'doi: {cite_doi}', t, flags=re.M)
            return t
        sub_file('CITATION.cff', cff)
        def dpk(t):
            d = json.loads(t); d['id'] = f'https://doi.org/{cite_doi}'; return json.dumps(d, indent=2, ensure_ascii=False) + '\n'
        sub_file('datapackage.json', dpk)
    if a.version:
        sub_file('README.md', lambda t: re.sub(r'Version \d+\.\d+\.\d+', f'Version {a.version}', t))
    if a.version or a.date:
        def cff(t):
            if a.version: t = re.sub(r'^version: .*$', f'version: {a.version}', t, flags=re.M)
            if a.date: t = re.sub(r'^date-released: .*$', f'date-released: {a.date}', t, flags=re.M)
            return t
        sub_file('CITATION.cff', cff)
        def zen(t):
            d = json.loads(t)
            if a.version: d['version'] = a.version
            if a.date: d['publication_date'] = a.date
            return json.dumps(d, indent=2, ensure_ascii=False) + '\n'
        sub_file('.zenodo.json', zen)
        def dpk(t):
            d = json.loads(t)
            if a.version: d['version'] = a.version
            if a.date: d['created'] = f'{a.date}T00:00:00Z'
            return json.dumps(d, indent=2, ensure_ascii=False) + '\n'
        sub_file('datapackage.json', dpk)
    print('done. Re-run python scripts/make_data_dictionary.py if the version changed.')


if __name__ == '__main__':
    main()
