# Safe Hilbert--Schmidt power bound for a nonnormal sweep

For any finite complex matrix `T` and integers `r>=s>=1`, set `Q=T* T`.
The source's finite-dimensional bound is

`||T^r||_HS^2 <= ||Q||_op^(r-s) Tr(Q^s)`.

Use `T* T`, not `T T*`, in the certificate.  The inequality is a power/norm
bound only; it does not establish a spectral gap or a sweep mixing theorem.

Source: *Compatibility entropy and the spectrum of a Thorp sweep*,
SHA-256 `dae8f5ca5b99fbecbbafd5644faea7f6d147b1b16493b31383ebd4c1e2e8fec1`,
physical p. 8, Lemma 2.4; [pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Compatibility-entropy-and-the-spectrum-of-a-Thorp-sweep-September-26-2026/paper.pdf).
