# Research Paper Collection review

Local bibliography review: October 16, 2026, on
`codex/fall-2026-semester-archive`. The results below record the bibliography
reorganization before subsequent presenter edits and the final local commit.
No push, PR, merge, deployment, or Pages configuration change was performed for
this task.

## Collection statistics

| Measure | Count |
| --- | ---: |
| Original entries | 82 |
| Original unique papers | 81 |
| Unique papers after reorganization | 94 |
| Duplicate entries removed | 1 |
| Newly added papers | 13 |
| Required recommended papers represented exactly once | 23 |

The duplicate was arXiv:2504.14841, `(Sub)Exponential Quantum Speedup for
Optimization`, previously listed under both Optimization and Quantum Advantage.
It now has one primary location under Quantum Algorithms & Optimization.
The immutable [original inventory](research-paper-inventory-before.json) records
all 82 original entries, their identifiers, metadata, categories, and line numbers.

## Taxonomy and primary locations

### Quantum Algorithms & Optimization (14)

- Fundamental Algorithmic Primitives: 5
- Quantum Optimization: 6
- Quantum Algorithms for Linear and Nonlinear Problems: 3

### Quantum Simulation & Many-Body Physics (13)

- Hamiltonian Simulation: 5
- Quantum Chemistry and Molecular Simulation: 2
- Analog and Digital-Analog Quantum Simulation: 4
- Many-Body Dynamics and Simulation Algorithms: 2

### Dissipative Quantum Algorithms & Open Systems (11)

- Quantum Gibbs Sampling: 2
- Ground-State and Thermal-State Preparation: 7
- Learning and Characterizing Open Quantum Systems: 2

### Quantum Learning, Tomography & Machine Learning (16)

- Classical Shadows and Shadow Tomography: 4
- Quantum State Learning and Certification: 4
- Quantum Learning Theory and Complexity: 3
- Quantum Machine Learning and Generative Models: 2
- Classical Machine-Learning Foundations: 3

### Quantum Complexity & Computational Advantage (11)

- Quantum Complexity Classes and Circuit Complexity: 3
- Quantum Advantage and Computational Separations: 6
- Interactive Proofs and Nonlocal Games: 2

### Classical Simulability, Entanglement & Randomness (15)

- Classical Simulation and Tensor Networks: 5
- Entanglement and Simulation Complexity: 2
- Pseudorandomness and Unitary Designs: 5
- Pseudoentanglement: 3

### Quantum Computing Architectures & Fault Tolerance (14)

- Fault Tolerance, Error Correction, and Compilation: 3
- Hardware Platforms and Quantum Memory: 3
- Distributed Quantum Computing: 4
- Hybrid and Alternative Computing Models: 4

Important moves:

- Tensor-network surveys, DMRG, and circuit learning now sit under Classical
  Simulability, Entanglement & Randomness instead of Hamiltonian Simulation.
- Gibbs sampling, dissipative state preparation, imaginary-time state preparation,
  and open-system learning share the dedicated open-systems category.
- Nonlinear differential equations and fluid-dynamics algorithms are grouped under
  Quantum Algorithms for Linear and Nonlinear Problems.
- `Strengths and Weaknesses of Quantum Computing` is treated as a foundational
  complexity reference rather than a fault-tolerance paper.
- The sample-based Krylov-diagonalization algorithm is under many-body simulation;
  coherent atom-array hardware is under architectures.
- Classical backpropagation references remain together as machine-learning
  foundations. No descriptions were generated for every older paper.

## Newly added papers

| Paper | Primary category |
| --- | --- |
| [Verifiable Quantum Advantage via Optimized DQI Circuits](https://arxiv.org/abs/2510.10967) | Quantum Algorithms & Optimization |
| [Provable Speedups in Convex Optimization via Quantum Dynamics](https://doi.org/10.4230/LIPIcs.TQC.2026.4) | Quantum Algorithms & Optimization |
| [Quantum Simulation with Sum-of-Squares Spectral Amplification](https://arxiv.org/abs/2505.01528) | Quantum Simulation & Many-Body Physics |
| [Information-Computation Gaps in Quantum Learning via Low-Degree Likelihood](https://arxiv.org/abs/2505.22743) | Quantum Learning, Tomography & Machine Learning |
| [Fundamentals of quantum Boltzmann machine learning with visible and hidden units](https://arxiv.org/abs/2512.19819) | Quantum Learning, Tomography & Machine Learning |
| [QMA has perfect completeness](https://arxiv.org/abs/2609.13032) | Quantum Complexity & Computational Advantage |
| [Quantum precomputation: parallelizing cascade circuits and the Moore-Nilsson conjecture is false](https://arxiv.org/abs/2510.04411) | Quantum Complexity & Computational Advantage |
| [Efficiently simulable quantum circuits with large entanglement, magic, and non-Gaussianity via code-compiled tensor networks](https://arxiv.org/abs/2607.08396) | Classical Simulability, Entanglement & Randomness |
| [Strong random unitaries and fast scrambling](https://arxiv.org/abs/2509.26310) | Classical Simulability, Entanglement & Randomness |
| [Spectral Small-Incremental-Entangling: Breaking Quasi-Polynomial Complexity Barriers in Long-Range Interacting Systems](https://arxiv.org/abs/2509.12014) | Classical Simulability, Entanglement & Randomness |
| [A Constant Rate Quantum Computer on a Line](https://arxiv.org/abs/2502.16132) | Quantum Computing Architectures & Fault Tolerance |
| [Learning Arbitrary Lindbladians with Quantum Error Correction](https://arxiv.org/abs/2606.18188) | Dissipative Quantum Algorithms & Open Systems |
| [Exponential quantum advantage in processing massive classical data](https://arxiv.org/abs/2604.07639) | Quantum Complexity & Computational Advantage |

## Bibliographic verification and corrections

The bibliography uses full names for up to three authors and the first full name
plus `et al.` for four or more. Metadata was read from arXiv citation tags and
journal references, DOI/Crossref registration records, official publishers, and
conference proceedings. A confirmed publication year is used with a venue;
`(arXiv, Year)` identifies a verified preprint record without claiming that no
later publication exists. Publication metadata lookup was not exhaustive across
all possible later versions.

### Verified title updates

Case, punctuation, typographic apostrophes, and journal-name expansion are not
counted as substantive title corrections below.

| Previous title | Verified title | Source |
| --- | --- | --- |
| End-to-End Efficient Quantum Thermal and Ground State Preparation Made Simple | Simple and efficient end-to-end quantum thermal and ground state preparation | [Verified record](https://arxiv.org/abs/2508.05703) |
| Quantum Singular Value Transformation without Block Encodings | Quantum singular value transformation without block encodings: Near-optimal complexity with minimal ancilla | [Verified record](https://arxiv.org/abs/2504.02385) |
| A Grand Unification of Quantum Algorithms | Grand Unification of Quantum Algorithms | [Verified record](https://api.crossref.org/works/10.1103%2FPRXQuantum.2.040203) |
| Is there evidence for exponential quantum advantage in quantum chemistry? | Evaluating the evidence for exponential quantum advantage in ground-state quantum chemistry | [Verified record](https://api.crossref.org/works/10.1038%2Fs41467-023-37587-6) |

### Verified publication-year corrections and completed dates

| Paper | Previous year | Verified citation year / venue | Source |
| --- | --- | --- | --- |
| [Exponential Separations Between Learning With and Without Quantum Memory](https://arxiv.org/abs/2111.05881) | 2021 | 2022, FOCS | [Verified record](https://api.crossref.org/works?query.title=Exponential+separations+between+learning+with+and+without+quantum+memory&rows=3) |
| [Determining eigenstates and thermal states on a quantum computer using quantum imaginary time evolution](https://arxiv.org/abs/1901.07653) | 2019 | 2020, Nature Physics | [Verified record](https://arxiv.org/abs/1901.07653) |
| [Simple and efficient end-to-end quantum thermal and ground state preparation](https://arxiv.org/abs/2508.05703) | 2025 | 2026, Nature Physics | [Verified record](https://arxiv.org/abs/2508.05703) |
| [Lower bounding the MaxCut of high girth 3-regular graphs using the QAOA](https://arxiv.org/abs/2503.12789) | Missing | 2025, arXiv | [Verified record](https://arxiv.org/abs/2503.12789) |
| [Distributed Quantum Simulation](https://arxiv.org/abs/2411.02881) | 2024 | 2026, Physical Review Letters | [Verified record](https://arxiv.org/abs/2411.02881) |
| [How the backpropagation algorithm works](http://neuralnetworksanddeeplearning.com/chap2.html) | Missing | 2015, Neural Networks and Deep Learning, Ch. 2 | [Verified record](http://neuralnetworksanddeeplearning.com/chap2.html) |

For `Exponential Separations Between Learning With and Without Quantum Memory`,
the conference is FOCS 2021, but the publisher's proceedings publication date is
February 2022; the citation uses 2022 as its publication year. Its 2021 preprint
link is retained. `Quantum Simulation with Sum-of-Squares Spectral Amplification`
was recommended as a 2025 preprint; the verified PRL publication is from 2026.

### Author and venue cleanup

- Corrected the first author of `Digital-analog quantum computing of fermion-boson
  models in superconducting circuits` from Yamamoto to **Shubham Kumar**, as listed
  by [arXiv](https://arxiv.org/abs/2308.12040). The paper URL is unchanged.
- Replaced the collective short credit “Google Quantum AI et al.” with the named
  first author **Dmitry A. Abanin et al.**, matching the
  [arXiv author list](https://arxiv.org/abs/2506.10191).
- Expanded and standardized other author abbreviations against the citation
  records; this is formatting normalization, not a claim that all original
  abbreviated credits were incorrect.
- Populated the following ten original entries that lacked authors:

| Paper | Verified author display |
| --- | --- |
| [Learning the structure of open quantum systems](https://arxiv.org/abs/2606.30358) | Laura Lewis, Ewin Tang, John Wright |
| [A comprehensive framework to simulate real-time chemical dynamics on a fault-tolerant quantum computer](https://arxiv.org/abs/2504.06348) | Felipe H. da Jornada et al. |
| [Optimal Lower Bounds for Hamiltonian Simulation](https://arxiv.org/abs/2607.19852) | Alexander Zlokapa, Richard R. Allen, Aram W. Harrow |
| [Rapid Mixing of Quantum Gibbs Samplers for Weakly-Interacting Quantum Systems](https://arxiv.org/abs/2510.04954) | Štěpán Šmíd et al. |
| [End-to-End Quantum Algorithm for Nonlinear Fluid Dynamics with Bounded Quantum Advantage](https://doi.org/10.1103/xysy-q3fp) | David Jennings et al. |
| [Lower bounding the MaxCut of high girth 3-regular graphs using the QAOA](https://arxiv.org/abs/2503.12789) | Edward Farhi et al. |
| [Quantum singular value transformation without block encodings: Near-optimal complexity with minimal ancilla](https://arxiv.org/abs/2504.02385) | Shantanav Chakraborty et al. |
| [Distributed Quantum Simulation](https://arxiv.org/abs/2411.02881) | Tianfeng Feng et al. |
| [Multi-qubit Toffoli with exponentially fewer T gates](https://arxiv.org/abs/2510.07223) | David Gosset, Robin Kothari, Chenyi Zhang |
| [Trading modes against energy](https://arxiv.org/abs/2509.18854) | Lukas Brenner, Beatriz Dias, Robert Koenig |

- Added verified publication venues where available, including the APL
  Computational Physics review, PRL publication of Distributed Quantum Simulation,
  and the TQC 2026 convex-optimization proceedings paper; retained arXiv citations
  where only that record was confirmed.
- All original paper URLs are retained. DOI/arXiv identifiers were used for
  deduplication; no two final entries share a verified publication DOI.
- Preserved the introductory DMRG note. Added “Discussed 2026-05-19” only to
  `Exponential quantum advantage in processing massive classical data`, based on
  the dated row in `2026-winter-spring/index.md` (the archive was not edited).

### Access limits and unresolved verification

- **One main collection URL could not be content-verified:**
  [IEEE's backpropagation paper](https://ieeexplore.ieee.org/document/118638/)
  returned HTTP 202 with an empty page. The title, author, IJCNN venue, and 1989
  date were independently verified from
  [Crossref's DOI record](https://api.crossref.org/works/10.1109%2FIJCNN.1989.118638).
  Its original URL is preserved; this response does not establish that the URL
  is permanently broken.
- The secondary publisher DOI for `Tensor Network Techniques for Quantum
  Computation`, [10.22323/9788898587049](https://doi.org/10.22323/9788898587049),
  returned HTTP 403. The main arXiv link works; the citation therefore uses the
  verified 2025 arXiv record rather than an unverified publication venue.
- Several Crossref requests were rate-limited (HTTP 429). No unavailable Crossref
  response was used to invent fields; arXiv journal references, publisher pages,
  and targeted successful follow-ups supplied the retained metadata instead.
- The one-sentence recommended-paper descriptions summarize the cited sources;
  this is a bibliography audit, not an independent verification of their proofs.
  Candidate advantages, restricted measurement models, approximation error,
  resource estimates, and empirical evidence are distinguished where relevant.

## Website and maintenance changes

- Added a compact seven-category “Browse by Topic” index with explicit anchors.
- Preserved all **32 previous section anchors**, including aliases to the nearest
  corresponding new category/subtopic. No repository links to old paper-section
  fragments were found, but aliases also protect external bookmarks.
- Added stable identifier-based anchors for all 94 canonical paper entries.
- Shared navigation now reads Current Semester / Research Papers / Archive and
  marks the active page. The archived source is unchanged; its shared navigation
  updates through the common include as requested.
- Renamed only the homepage paper button to “Research Paper Collection”; its URL
  and the Fall materials button are unchanged. The Fall schedule, committee,
  location, selected topics, AI section, and contact match the pre-task local page.
- Added scoped bibliography typography and a responsive topic index; no frontend
  framework, database, JavaScript, or dependency was added. Existing local CSS
  changes remain intact.
- Moved public entry-format instructions into `AGENTS.md`, together with the
  taxonomy, author, sorting, identifier, and source-verification conventions.
- Excluded `docs/` from Jekyll so review reports and the old inventory are not
  public-facing pages.

## Validation

- Jekyll build with the pinned remote Cayman theme: **passed**.
- `python3 scripts/check_links.py _site`: **105 internal links across seven HTML
  pages; zero failures** after the initial reorganization build.
- External collection URLs: **93 HTTP 200 responses out of 94 unique URLs**;
  the remaining IEEE URL returned empty HTTP 202, as noted above.
- All 13 newly added primary paper URLs returned HTTP 200.
- Preservation checks passed: all 81 original unique references are present; all
  23 recommended URLs appear once; all 94 identifier-based entry anchors and all
  32 previous heading anchors exist, with no duplicate IDs.
- The seven category counts are 14 / 13 / 11 / 16 / 11 / 15 / 14, totaling 94.
- All 23 recommended entries have descriptions. The archive confirms the single
  added discussion date, May 19, 2026.
- The homepage is byte-for-byte unchanged except for the approved button label.
  Archived sources, historical presentation files, and unrelated files match the
  pre-task hashes. Existing local stylesheet content is a verbatim prefix.
- Desktop (1280px) and mobile (375px) checks passed with no page-wide overflow;
  the topic index uses two columns on desktop and one on mobile. Keyboard
  activation of a topic link successfully updates the fragment URL.
- `git diff --check` passed. The full diff was inspected for unrelated changes.
- Final preview restart with the updated config passed: Jekyll built in 1.307
  seconds and is serving `http://127.0.0.1:4000/` with auto-regeneration enabled.
- Final internal link check again passed: 105 links across seven HTML pages,
  zero failures. All 38 unique local page/resource URLs returned HTTP 200.
- The excluded inventory URL returns HTTP 404; `_site/docs/` is absent.
- The renamed homepage button and shared Current Semester / Research Papers
  navigation were tested in the browser. The collection is left open for review.
- All 94 rendered title/author/venue/year displays match the verified citation
  records, and the original inventory contains all 82 entries.

## Diff and local preview

This task changes `materials/papers.md`, `_includes/navigation.html`, `index.md`
(button label only), `assets/css/style.scss` (scoped additions), `_config.yml`
(`docs/` exclusion), and `AGENTS.md`; it adds this report and the original inventory.
Pre-existing local homepage, bibliography, and stylesheet changes were preserved.
No presentation files, archive source, Gemfile, lockfile, or Pages settings were
changed. The local preview is `http://127.0.0.1:4000/materials/papers.html`.

### Git diff receipt

The working tree has six modified tracked files and two new audit documents.
The tracked diff includes the earlier local Fall homepage and CSS edits; those
were not reset. Within this task the homepage change is only the button label,
and bibliography CSS is appended after the pre-existing local stylesheet.
The complete collection rewrite is expected from taxonomy and citation cleanup.
No commit or remote Git operation was performed during the bibliography review.

## Final pre-commit review

The subsequent Fall homepage edits name Philippe Karan and Mouheymen Khamadja
for October 30 and display `Simon Ducharme (?):` for November 13. The schedule
introduction now specifies that unconfirmed presenters are marked TBD.

The final Jekyll build passed. The internal link checker again checked 105 links
across seven HTML pages with zero failures, and `git diff --check` passed.
The archived program, archive index, and all 25 tracked files in the historical
slides directory (24 PDFs and its README) remain byte-for-byte unchanged against
the branch's previous commit. All 81 original unique paper URLs are preserved;
the collection contains 94 unique paper entries in seven categories, with no
duplicate rendered IDs. Audit documents remain excluded from the built site.
The latest presenter names and schedule introduction appear in the built HTML.
