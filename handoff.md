# Project Handoff: Tal Raviv Personal Homepage

Last verified: September 23, 2026

This document contains the information needed to continue maintaining the
website from another computer. The recommended transfer method is to clone the
GitHub repository on the office computer. Do not copy an active `.git`
directory through Dropbox, because simultaneous Dropbox and Git updates can
create difficult repository conflicts.

## Project summary

- Live website: <https://tal69.github.io/>
- GitHub repository: <https://github.com/tal69/tal69.github.io>
- Default branch: `main`
- Deployment: GitHub Actions and GitHub Pages
- Site generator: Jekyll 4.4
- GitHub Actions Ruby version: Ruby 3.3
- Locked Bundler version: Bundler 4.0.11
- Baseline website-content commit before this handoff: `f0b8fa3`

The website is a small static Jekyll site. Most content changes require editing
Markdown or YAML files, building locally, and pushing to `main`. A successful
push automatically starts the deployment workflow.

## Recommended transfer to the office computer

### 1. Install the basic tools

Install Git, a Ruby 3.3.x environment, and Bundler 4.0.11. Ruby 3.3 is
recommended because it matches the GitHub Actions workflow. A Ruby version
manager such as `rbenv` or `mise` is preferable to the macOS system Ruby.

Verify the tools:

```bash
git --version
ruby --version
gem install bundler -v 4.0.11
bundle _4.0.11_ --version
```

GitHub authentication is required for pushing changes. One convenient option
is the GitHub CLI:

```bash
brew install gh
gh auth login
gh auth setup-git
```

Cloning this public repository does not require authentication. Authentication
is needed only before the first push from the office computer.

### 2. Clone a fresh working copy

Use a local development folder that is not synchronized by Dropbox:

```bash
mkdir -p ~/Projects
cd ~/Projects
git clone https://github.com/tal69/tal69.github.io.git
cd tal69.github.io
```

If the repository already exists on the office computer, update it safely:

```bash
cd /path/to/tal69.github.io
git status
git switch main
git pull --ff-only origin main
```

Do not pull over uncommitted work. Review or commit local changes first.

### 3. Install dependencies and test the site

```bash
bundle _4.0.11_ install
bundle _4.0.11_ exec jekyll build
bundle _4.0.11_ exec jekyll serve
```

Open <http://127.0.0.1:4000/> in a browser. Stop the local server with
`Ctrl-C`.

The generated `_site/` directory, `.jekyll-cache/`, `.bundle/`, and `vendor/`
are local build or dependency artifacts. They should not be committed.

## Normal editing and publishing workflow

Before editing:

```bash
git switch main
git pull --ff-only origin main
git status
```

After editing:

```bash
bundle _4.0.11_ exec jekyll build
git status
git diff
git add path/to/each-intended-file
git commit -m "Describe the website update"
git push origin main
```

Add specific files rather than using `git add .` or `git add -A`. This reduces
the risk of committing temporary files or unrelated local changes.

After pushing, monitor the workflow named **Build and deploy Jekyll site to
Pages** in the repository's Actions tab. When it succeeds, verify the relevant
page on the live website. GitHub Pages must be configured with **GitHub
Actions** as its source. The older branch-deployment instructions in
`README.md` are no longer authoritative.

## Important files

| File or directory | Purpose |
| --- | --- |
| `index.md` | Main page, short biography, and selected recent papers |
| `_data/publications.yml` | Journal papers, book chapters, and working papers |
| `_pages/publications.md` | Publications page template and ordering logic |
| `_data/students.yml` | Student records |
| `_pages/students.md` | Students page |
| `_pages/events.md` | Events page |
| `_config.yml` | Site metadata, navigation, plugins, and build exclusions |
| `assets/css/main.scss` | Site styles |
| `_layouts/` | Shared HTML page layouts |
| `_includes/` | Reusable page fragments |
| `assets/img/` | Profile image and other images |
| `assets/pdf/` | Locally hosted papers, data files, and related assets |
| `.github/workflows/jekyll.yml` | Automated build and GitHub Pages deployment |
| `scripts/mirror_assets.py` | One-time Wix migration helper |

Do not rerun `scripts/mirror_assets.py` casually. It was written for the Wix
migration, creates backup files, downloads assets, and rewrites URLs.

The repository also contains a tracked Python cache file and an old
`email_to_tau_it.md` note. They are not needed for normal site maintenance.
The email note and migration script are currently copied into local Jekyll
builds as static files. Treat their eventual cleanup as a separate task rather
than mixing it into a publication update.

## Publication editing rules

The journal list in `_data/publications.yml` uses explicit `cv_number` values.
These numbers must match the CV exactly and remain unique. The publications
page sorts journal articles by `cv_number`, so the YAML file's physical order
does not control the full publications page.

When adding a journal article:

1. Confirm its number against the latest CV.
2. Add one journal record with a unique `cv_number`.
3. Prefer the publisher DOI for `url`.
4. Use the final journal year, volume, issue, pages, or article number when
   available.
5. Set `featured: true` only if it should appear under **Selected recent
   publications** on the main page.
6. Keep featured journal records in newest-to-oldest order in the YAML file,
   because the main page preserves the source order.
7. Build locally and inspect both the main page and `/publications/`.

Working papers are stored under `working:`. The publications template displays
that array in reverse source order. A paper accepted or published by a journal
should appear in the journal section rather than the working-paper section.

## Current publication and content state

At the time of this handoff:

- Journal publications are numbered consecutively from 1 through 46 to match
  the CV.
- Publication 46 is **The lecture-hall quadratic assignment problem**,
  *Computers & Operations Research* (2026), volume 196, article 107659, linked
  to <https://doi.org/10.1016/j.cor.2026.107659>.
- The selected recent publications are numbers 46, 45, 42, and 40, in that
  newest-to-oldest order.
- **Escort-Flow Approach for Simultaneous Multi-Load Retrieval in Puzzle-Based
  Storage** is a working paper dated July 2026.
- **Admission and Assortment Optimization for Multi-size Automated Parcel
  Lockers** is a working paper dated July 2026.
- The lecture-hall paper is not in the working-paper section.
- The Events page includes the October 26, 2026 Data Science, Operations and
  Analytics conference and its Mind-IL registration link.
- The main-page biography says "more than 45 papers" and uses the formal name
  "Leon Recanati Graduate School of Business Administration."

## Deployment details

The workflow file is `.github/workflows/jekyll.yml`. It runs after every push
to `main` and can also be started manually. Its main steps are:

1. Check out the repository.
2. Set up Ruby 3.3 and restore or install the Bundler dependencies.
3. Configure GitHub Pages.
4. Run the production Jekyll build.
5. Upload the generated site artifact.
6. Deploy the artifact to GitHub Pages.

If a deployment fails, open the failed Actions run and inspect the first failed
step. Reproduce the build locally with the locked Bundler version before
changing dependencies:

```bash
bundle _4.0.11_ install
JEKYLL_ENV=production bundle _4.0.11_ exec jekyll build
```

If `Gemfile.lock` changes during setup on a new computer, inspect the diff
before committing it. Platform or Bundler differences can cause lockfile-only
changes that are unrelated to the website content.

## Local-only state on the original computer

When this file was prepared, the original working copy contained these changes
outside the published `main` branch:

- `Gemfile.lock` was modified locally by removing one Bundler checksum line.
  Review that diff before deciding whether it should be kept.
- `AGENTS.MD` was untracked.
- `sitemap.xml` was untracked.

These items will not appear in a fresh office-computer clone unless they are
reviewed and committed separately or copied manually. They were intentionally
left out of this handoff commit to avoid mixing unrelated local state with the
transfer documentation.

## Safety checklist before switching computers

- Confirm `git status` on the original computer.
- Confirm that all intended website changes are committed and pushed.
- Record or manually copy any untracked files that are still needed.
- On the office computer, confirm that `git log -1` shows the expected commit.
- Run a local Jekyll build before editing.
- Pull before each work session and avoid editing the same repository on two
  computers at the same time.
- Push at the end of each work session and confirm the Pages workflow succeeds.
