# Releasing a version

This is the maintainers' procedure for publishing the dataset on GitHub and archiving each release on Zenodo with a DOI. Zenodo is free for public deposits.

## One-time set-up

1. **The repository** is https://github.com/dan-g-odin/vc-value (public). Its address is already filled in across the metadata files. If it moves, for example to an Odin organisation account, run `python scripts/set_release_metadata.py --repo-url <new address>` and commit the result.
2. **Upload the files.** In the browser: open the repository, choose *Add file → Upload files* (or the *uploading an existing file* link on an empty repository), and drag in everything inside the release folder. The browser uploader refuses files whose names start with a dot ("This file is hidden"), so create those one at a time with *Add file → Create new file* from the repository's front page, typing the full name (typing `/` makes a folder) and pasting the contents: `.zenodo.json` (needed before the first release) and the six files under `.github/` (the `validate` workflow, the four issue-template files and the pull-request template). `.gitattributes` and `.gitignore` matter only to people using git. With git instead, everything is included in one go:
   ```bash
   git init -b main
   git add .
   git commit -m "Dataset release 1.0.0"
   git remote add origin https://github.com/dan-g-odin/vc-value.git
   git push -u origin main
   ```
3. **Repository settings:** add a description and topics (`venture-capital`, `open-data`, `private-equity`, `ipo`, `dataset`); enable Issues and Discussions. Once there is more than one maintainer, protect `main` and require a passing `validate` check and one review before merging (with a single maintainer, a required review would block their own changes).
4. **Link Zenodo:** sign in to [zenodo.org](https://zenodo.org) with GitHub, open *Account → GitHub*, press *Sync now* and switch the repository on. Do this before publishing the first release: Zenodo archives only releases published after the switch is on, and reads their metadata from `.zenodo.json`.

## Each release

1. Update `CHANGELOG.md` (move "Unreleased" entries under the new version) and set the version and date:
   ```bash
   python scripts/set_release_metadata.py --version X.Y.Z --date YYYY-MM-DD
   python scripts/make_data_dictionary.py
   python scripts/build_sqlite.py
   python scripts/validate.py
   ```
2. Commit, then create a tag and a GitHub release named `vX.Y.Z` with the changelog entry as notes. Zenodo creates the new version and its DOI within minutes.
3. After the first release, copy the **concept DOI** (all versions) and the **version DOI** from the Zenodo record, then:
   ```bash
   python scripts/set_release_metadata.py --doi 10.5281/zenodo.<version-id> --concept-doi 10.5281/zenodo.<concept-id>
   ```
   This adds the DOI badge and citation link to the README, the `doi` to `CITATION.cff` and the `id` to `datapackage.json`. Commit the change (it will be archived with the next release).
4. Check the Zenodo record: title, creators, licence, keywords, version and the link back to GitHub.

## Release checklist

- [ ] `python scripts/validate.py` passes (warnings documented in `docs/limitations.md`).
- [ ] `frictionless validate datapackage.json` passes.
- [ ] `docs/data_dictionary.md` regenerated; `database/venture_value_per_dollar.sqlite` rebuilt.
- [ ] `CHANGELOG.md`, `CITATION.cff`, `.zenodo.json` and `datapackage.json` show the new version and date.
- [ ] No placeholder (`OWNER`) left: the validator warns if one is.
- [ ] Sources and known limitations documented; no confidential or personal material added.

## Changing the licence

Version 1.0.0 is released under CC-BY-4.0. To release under another open licence (for example CC0 1.0 or ODC-By 1.0), change it before the first public release in all five places: `LICENSE` (full text), the licence section of `README.md`, `license` in `CITATION.cff` (SPDX identifier), `license` in `.zenodo.json` (Zenodo identifier, for example `cc0-1.0`) and `licenses` in `datapackage.json`. A licence cannot be withdrawn from copies already published, so decide before the first release.

## Size limits

The CSV files total under 5 MB and the SQLite database about 6 MB, well inside GitHub's file limits and Zenodo's per-record limit (50 GB). No Git LFS is needed.
