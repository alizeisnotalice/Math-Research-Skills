# Pandigital package bounded replay

Source: `EXT-0372`, author manuscript dated 20 Nov 2026, physical pp. 7--10 and 16--17 (51 pages total), SHA-256 `416859ccbf2b60a054144b4747b4f01e74d070d81684cf1e8336888310a5c55f`.

The source identifies the public `Bendjex/pandigital-certified` v3.0 package and Zenodo record `10.5281/zenodo.24356239`.  A source archive was acquired separately for review.  Its `c5/t_hc_smoke.py` was replayed with Python 3.12.13, python-flint 0.9.0, NumPy 2.5.4, mpmath 1.3.0 and SymPy 1.14.0; the macOS build used the package C source with directed-rounding flags but no unavailable OpenMP flag.  It built tables through five digits (158,855 classes), checked 828 values, and ended `fail 0`.

This gives a concrete bounded replay route for an exact/interval checker.  It does **not** replay the manuscript's full grammar, cells, coverage logs, unbounded-intermediate branch, or Theorems 1--2 optimum claims.  Treat any listed optimum as unverified until the complete versioned certificate package and coverage table are reproduced.
