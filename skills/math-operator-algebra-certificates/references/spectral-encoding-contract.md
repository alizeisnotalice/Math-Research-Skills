# Spectral-encoding contract

Source: OpenAI, *Relative generation and the generator problem for finite factors*, version `openai/math@3344da59991ed94f9ba711217b29c1d760badfa6`, SHA-256 `c5838d4e6aba1dc13c368ca778839478d1a7a6429ee068101b01c33dc97b6e89`, PDF pp. 13--14, Lemmas 5.2 and 5.4. The paper is a preprint; only the two elementary encodings below are independently rederived here.

## A. Commuting projection code

Let `(e_m)_{m>=1}` be commuting projections in a unital von Neumann algebra and put `b = sum_{m>=1} 2*3^{-m} e_m`. The series converges in operator norm since `sum 2*3^{-m}=1`. Having recovered `e_1,...,e_{m-1}`, let `r_m=b-sum_{j<m}2*3^{-j}e_j`. Because all factors commute, on the `1-e_m` summand its scalar functional-calculus values lie in `[0,3^{-m}]`; on the `e_m` summand they lie in `[2*3^{-m},3*3^{-m}]`. The intervals have a gap at `(3/2)*3^{-m}`, so `e_m = 1_{((3/2)3^{-m},infinity)}(r_m)`.

Thus every `e_m` is in `W*(b)`. This proves the encoding and nothing about a noncommuting family, a merely strongly convergent series, or availability of a claimed projection-valued functional calculus.

## B. Four-to-two block code

Let `N=W*(a_1,a_2,a_3,a_4)` be unital and each `a_i=a_i^*`. Choose a real `C > ||a_1||+||a_2||` and set `A=diag(a_1,a_2+C1)`, `B=[[a_3,1],[1,a_4]]` in `M_2(N)`.

For any `||a_1|| < lambda < C-||a_2||`, functional calculus gives `E_11=1_{(-infinity,lambda)}(A)` and `E_22=1-E_11`. Hence `E_12=E_11 B E_22` and `E_21=E_12^*`. The four corner identities

`a_1E_11=E_11AE_11`, `a_2E_11=E_12AE_21-CE_11`, `a_3E_11=E_11BE_11`, `a_4E_11=E_12BE_21`

put `NE_11` in `W*(A,B)`. Matrix-unit multiplication then puts every `NE_ij` there, proving `W*(A,B)=M_2(N)`.

The strict gap and supplied generation identity are indispensable. In particular, this is not a proof of relative generation, single generation, or existence of a usable `C` when norm information is absent.

## Finite exact check

`scripts/check_block_encoding.py` specializes to real rational matrices. Its row-sum bounds `R_i` satisfy `||a_i|| <= R_i`; requiring `C>R_1+R_2` is a deliberately stronger, exact checkable sufficient condition. It confirms the displayed four corner identities and the generated-algebra dimensions in the concrete finite model. Such a replay validates that finite model only; the general result is the proof above plus the stated functional-calculus hypothesis.
