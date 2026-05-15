# Prof. Tal Raviv — personal homepage

Static Jekyll site for `talraviv.github.io` (or wherever you decide to host it),
migrated from the old Wix site. Designed to look and feel like the *al-folio*
academic theme while being deliberately lightweight: no jekyll-scholar, no
image-processing plugins — just plain Jekyll, fully GitHub-Pages compatible
out of the box.

## What's in here

```
.
├── _config.yml              # site settings, author info, navigation
├── _data/
│   ├── publications.yml     # journal papers, chapters, working papers
│   └── students.yml         # MSc and PhD students
├── _layouts/                # HTML templates (default, page)
├── _pages/                  # publications, students, events
├── index.md                 # home page (bio + selected publications)
├── assets/
│   ├── css/main.scss        # styling
│   ├── img/profile.jpg      # ← populated by mirror_assets.py
│   └── pdf/                 # ← populated by mirror_assets.py
├── scripts/
│   └── mirror_assets.py     # one-shot: pull PDFs + photo from old Wix site
├── Gemfile
└── README.md
```

Editing is intentionally simple: the publication list and student list live in
plain YAML files. Add a new paper by appending to `_data/publications.yml`.

## First-time setup

### 1. Mirror the assets from your old Wix site

This pulls every PDF, dataset, and your profile photo from the old Wix CDN,
drops them under `assets/`, and rewrites `_data/publications.yml` so the
links point at the local copies. **Run this once, before publishing — once
the Wix site is gone, those URLs disappear.**

```bash
python3 scripts/mirror_assets.py
```

It writes a `.bak` backup of `publications.yml` alongside the file, and
skips anything it's already downloaded.

### 2. Install Ruby + Jekyll, then build locally

```bash
# Ruby (macOS, via Homebrew) — skip if you already have a recent Ruby
brew install ruby

# in this repo:
bundle install
bundle exec jekyll serve
```

Open <http://localhost:4000>. Edits to `_data/*.yml`, markdown pages, or
SCSS are picked up live.

### 3. Push to GitHub Pages

```bash
git init
git add .
git commit -m "initial commit — migrate from Wix"
git branch -M main
git remote add origin git@github.com:<your-username>/<repo>.git
git push -u origin main
```

Then on GitHub:

- **Settings → Pages → Build and deployment**: set source to *"Deploy from a
  branch"*, branch *main*, folder */ (root)*.
- Wait ~30 seconds; GitHub builds the site and publishes it at
  `https://<your-username>.github.io/<repo>/` (or the apex `*.github.io`
  domain if you name the repo `<your-username>.github.io`).

Update `url:` and `baseurl:` in `_config.yml` to match.

### 4. (Optional) Point your TAU subdomain at GitHub Pages

`talraviv.sites.tau.ac.il` is a TAU-managed host. To redirect it to GitHub
Pages you'll need TAU IT to add a CNAME or HTTP redirect. The alternative
is to leave the TAU page as a stub that links to your new site, or to use
a domain you own (configure under *Settings → Pages → Custom domain*).

## Day-to-day edits

| Want to…                  | Edit                                                   |
|---------------------------|--------------------------------------------------------|
| Update bio                | `index.md`                                             |
| Add a paper               | append an entry to `journal:` in `_data/publications.yml` |
| Promote to "Selected"     | add `featured: true` to the entry                      |
| Add a student             | top of `_data/students.yml`                            |
| Tweak the colors / layout | `assets/css/main.scss`                                 |
| Add a new page            | drop a `.md` file in `_pages/` and list it in `_config.yml` `nav:` |

## Notes on the migration

- The old Wix site mixed several link sources: Wix CDN PDFs, publisher DOIs,
  Dropbox links, and old `~talraviv/` paths on the TAU engineering server.
  Where possible, the YAML now prefers DOI links — they're stable. Wix
  CDN PDFs will be replaced with `/assets/pdf/...` links by the mirror script.
- A handful of student thesis PDFs were on `eng.tau.ac.il/~talraviv/`. Those
  are kept as-is; if they're dead, drop the local copies in `assets/pdf/`
  and update the URLs in `_data/students.yml`.
- The "Events" page from Wix was empty ("Not yet"), so the new page is too.
  Delete it from `nav:` in `_config.yml` if you want it gone entirely.
