# kesten82 — Increasing events in the percolation textbook

**Reading status:** `selected_chapters_read`. The whole 432-page author-hosted book was obtained; its title page is physical PDF p. 3. Scanned Chapter 4, “Increasing Events,” was visually read page by page (printed pp. 69–80; PDF pp. 77–88). PDFKit text extraction was blank for these scans. R03 accepted the selected-chapter evidence in round 7; the current source/coverage metadata correction to physical p. 3 is included for final rebinding.

**Reference:** Harry Kesten, *Percolation Theory for Mathematicians* (Birkhäuser, 1982), DOI [10.1007/978-1-4899-2730-9](https://doi.org/10.1007/978-1-4899-2730-9). The author-hosted full copy identifies a CC BY-NC-SA 3.0 license.

## Results read in Chapter 4

- Lemma 4.1: coordinatewise increasing functions have monotone expectations under coordinatewise increases of product occupation probabilities. The displayed bound depends on the number \(m\) of coordinates on which the function depends and the relevant single-site probability ratios.
- Proposition 4.1 (FKG): for bounded increasing functions \(f,g\) of finitely many independent Bernoulli coordinates, \(\mathbb E(fg)\ge\mathbb E f\,\mathbb E g\); the event form is positive association.
- Proposition 4.2 (Russo): for an increasing event \(E\) depending on finitely many coordinates, \(\partial_{p(v)}\mathbb P(E)=\mathbb P(v\text{ is pivotal})\). Along a linear interpolation of site parameters, the derivative is the sum of parameter increments times pivotal probabilities.

The proof conditions on the state at one coordinate, uses independence of the remaining coordinates, and identifies the difference between the two conditional event probabilities with pivotality. Chapter 4 also gives connectivity/susceptibility consequences of positive association on connected graphs.

## Applicability boundary

These are product-measure and increasing-event tools. They do not by themselves prove strict monotonicity: an essential enhancement/pivotal comparison is still required. For infection-time questions, first check that the event is a finite-coordinate increasing event; infinite-volume limits require a separate limiting argument.
**Selected-unit coverage:** [reading_coverage.json](../reading_coverage.json) (`/selected_book_units/kesten82`).
