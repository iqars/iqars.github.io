# QARS website maintenance

## Project organization

This is a static GitHub Pages site using Jekyll and the Cayman remote theme
(`pages-themes/cayman@v0.2.0`). Keep that setup and avoid new dependencies unless
needed and approved.

- `index.md`: current semester, always published at `/`.
- `2026-winter-spring/index.md`: preserved program at `/2026-winter-spring/`.
- `archive/index.md`: previous semester directory, published at `/archive/`.
- `_config.yml`: site metadata, remote theme, default layout, and build exclusions.
- `_layouts/seminar.html`: wraps content with navigation and inherits Cayman's
  `default` layout. Do not copy or replace the upstream Cayman layout.
- `_includes/navigation.html`: shared Current semester / Archive navigation.
- `assets/css/style.scss`: small additions to the Cayman stylesheet.
- `materials/papers.md`: shared paper collection at `/materials/papers.html`.
- `materials/slides/`: historical files; preserve their exact names and paths.
  Its `README.md` generates `/materials/slides/index.html` and lists PDFs.
- `materials/2026-fall/`: Fall 2026 materials and their landing page.
- `scripts/check_links.py`: Python standard library check of built local links.
- `docs/research-paper-inventory-before.json`: the original bibliography audit
  inventory, including duplicate entries; retain it for comparison.
- `docs/research-paper-collection-review.md`: reorganization, source checks,
  citation corrections, and validation report. `docs/` is excluded from the site.

## Update the current semester

Edit `index.md`. Keep its `/` permalink, semester heading, location, committee,
topics, schedule, and contact sections. Use only confirmed information. Mark
unknown details as "To be announced"; do not carry forward a room, committee,
meeting time, speaker, or topic without confirmation. Keep the shared paper
collection available. A schedule need not contain invented placeholder meetings.

For a confirmed schedule, follow the archived HTML table structure, including
`scope="col"` headers and a `.schedule-scroll` wrapper with `role="region"`, an
accessible label, `tabindex="0"`, and a referenced scrolling hint. Keep all six
columns readable through horizontal scrolling on mobile.

## Archive a completed semester

1. Before replacing the homepage, copy its entire program into
   `YYYY-semester/index.md` (for example, `2026-fall/index.md`).
2. Set an explicit permalink `/YYYY-semester/` and `archived: true` in front
   matter. Keep the seminar title in the Cayman header and identify the archived
   semester in the content.
3. Preserve all topics, dates, time notes, presenters, titles, moderators,
   contact details, and resource links. Compare against the previous homepage.
4. Change relative material links to site-root paths through `relative_url` so
   nesting the program cannot break them. Do not move the linked files.
5. Add the semester to `archive/index.md`, newest first.
6. Replace the homepage with the next semester and create its materials folder.
   Keep past semester URLs stable and all archives listed.

This uses ordinary Jekyll pages, with no semester-specific layout changes.

## Add slides and papers

- Put new Fall slides and supporting files in `materials/2026-fall/`; future
  semesters should get their own `materials/YYYY-semester/` directory.
- Add descriptive links to the semester program and its materials landing
  page. New filenames should be descriptive and use simple hyphenated names.
- Do not rename or remove historical files, including those with spaces,
  parentheses, or accents. Existing links may be bookmarked externally.
- Add shared references to `materials/papers.md` using its established topic
  headings and citation format. Do not duplicate the collection per semester.
- The collection has seven main categories: Quantum Algorithms & Optimization;
  Quantum Simulation & Many-Body Physics; Dissipative Quantum Algorithms & Open
  Systems; Quantum Learning, Tomography & Machine Learning; Quantum Complexity &
  Computational Advantage; Classical Simulability, Entanglement & Randomness;
  and Quantum Computing Architectures & Fault Tolerance. Give each paper one
  primary entry, identified by arXiv ID or DOI. Use internal links for any useful
  cross-references instead of repeating bibliography entries.
- Suggested entry format (maintainer guidance, not public page content):

  ```markdown
  - <span id="paper-identifier"></span>**[Paper Title](URL)** <span class="paper-meta">— Author(s) (Venue, Year)</span><br>
    <span class="paper-description">Optional concise contribution and limitations.</span>
  ```

  Use full author names for up to three authors, or the first full name plus
  `et al.` for four or more. Prefer verified publication metadata and publication
  year; cite `(arXiv, Year)` when only the preprint record is confirmed. Sort
  approximately newest first within each subtopic. Preserve useful notes such as
  `discussed YYYY-MM-DD`, but add discussion dates only with explicit evidence.
  Verify new metadata against arXiv, official proceedings, publishers, or DOI
  registration records; report unresolved fields rather than inventing them.
  Preserve paper anchors and the legacy section-anchor aliases when reorganizing.
- Use Liquid URLs in Markdown and HTML, for example
  `[Slides]({{ '/materials/2026-fall/example.pdf' | relative_url }})`.
  Preserve existing external paper URLs and presentation titles.

## Build, preview, and validate

Use the existing Gemfile. Local development currently uses Ruby 3.3.6 (recorded
in the local `.ruby-version`; it is not tracked). Python 3.9+ runs the link checker.

```sh
bundle check
# Only if dependencies are missing:
bundle install
bundle exec jekyll build --trace
python3 scripts/check_links.py _site
bundle exec jekyll serve --host 127.0.0.1 --port 4000
```

Open `http://127.0.0.1:4000/`, `/archive/`, `/2026-winter-spring/`, and the
materials pages. Check a narrow mobile viewport and a desktop viewport. Ensure
the page itself does not scroll sideways, all six schedule columns are available
within the scroll area, and keyboard focus and navigation are visible.

The remote theme build needs access to GitHub to fetch the pinned theme.
Report network or build limitations rather than changing the deployment setup.

The link checker verifies local HTML/resource paths and HTML fragments, including
URL-encoded filenames. It skips external URLs; it does not verify paper contents
or remote availability. If testing a nonempty baseurl, pass the same prefix with
`--baseurl`. Compare historical program text, row structure, and resource targets
against the pre-change homepage, and confirm original materials are unchanged.
Run `git diff --check` before review. Do not add `_site/`, local Bundler state,
credentials, caches, or backup files to Git.

## Link preservation and change control

Preserve `/materials/papers.html`, `/materials/slides/`, all existing presentation
URLs, and published archive permalinks. Keep Current Semester / Research Papers /
Archive navigation on every rendered
content page. Do not delete existing seminar information or materials. Work on
a separate branch. Do not commit, push, merge, or deploy without user approval.
