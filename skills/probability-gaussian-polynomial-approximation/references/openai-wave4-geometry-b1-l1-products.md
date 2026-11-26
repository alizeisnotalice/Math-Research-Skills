# Independent Gaussian-square products

Source: *Independent products in real L1: asymptotic midpoint convexity without AUC renormings*, OpenAI 2026-09-27, SHA-256 `40d5f05445bd8d39f9bcbc21fc8cc082ea246498e77bcc7e72a5560adc68018c`, physical pp. 7--10.

Pinned original: <https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Independent-products-in-real-L1-asymptotic-midpoint-convexity-without-AUC-renormings-September-27-2026/manuscript.pdf>.

For independent standard Gaussian pairs, put `A_i=(G_i+G'_i)/sqrt(2)` and `C_i=(G_i-G'_i)/sqrt(2)`. For fixed coefficients `a_i`, the source has `H-H'` distributed as `2 sum a_i A_i C_i`. Conditional on the `A_i`, its variance is `4V`, with `V=sum a_i^2A_i^2`, `E V=s^2`, and `E V^2=s^4+2 sum a_i^4<=3s^4`. Thus `P(V>=s^2/2)>=1/12` for `s>0`, and `P(|H-H'|>=2Ks)>=P(|G|>=sqrt(2)K)/12`.

The manuscript additionally needs its independent-product and even-convexity hypotheses for midpoint moduli; this reference transfers only the conditional Gaussian moment/tail component.

```sh
python3 scripts/gaussian_product_moment_wave4_geometry_b1.py --self-test
python3 scripts/gaussian_product_moment_wave4_geometry_b1.py --a 1/2 1/3
```
