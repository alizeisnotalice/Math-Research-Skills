# W09-X007 active-citation adjudication

The active-source audit identified a possible mismatch between W09-X007 and the continuous-relocation interface. A primary-source recheck resolves it in favor of the existing mathematical interface.

The local source is Talvitie, Kangas, Niinimäki and Koivisto, *A Scalable Scheme for Counting Linear Extensions*, IJCAI 2018, pp. 5119–5125, SHA-256 `ee5511cfb50b480392839b13ea406347e1db037a844d42cc07f38156b26eb435`. The publisher's paper is [0710.pdf](https://www.ijcai.org/proceedings/2018/0710.pdf). The historical `0079.pdf` URL is a different IJCAI paper and cannot serve as the bibliographic source.

On published p. 5122, Section 4 defines

\[
\Omega=\{x\in[0,1]^n:x_i-x_j\le s_{ij}\text{ for }i<j\},\qquad s_{ij}\ge0.
\]

Section 4.1 defines the coordinate-proposal-and-rejection continuous relocation chain. Theorem 2 gives stationarity of the uniform law on \(\Omega\). On pp. 5122–5123, Lemma 1 supplies coordinatewise monotonicity and bottom/top states. Theorem 3 states that monotone coupling from the past outputs an exactly uniform sample in finite expected time.

The source admits this interface only for its displayed ordered family of constraints and shared update randomness. It gives no general polynomial expected-time bound. Its relaxation Tootsie Pop result is an approximate count guarantee, so it cannot certify an exact linear-extension counter or a sampler for arbitrary peak-conditioned graph labelings.

The interface is source-supported. The malformed archival URL and the audit's mismatch conclusion based on it are superseded by this page-level recheck.

Theorem 3's finite-mean argument uses independence of the disjoint blocks of iid update pairs. The printed “mutually exclusive” should be read as “independent”: a successful block has fixed positive probability, and multiple such blocks can occur. For exactness, at deterministic lookback (T) couple the extrema to a chain started at stationarity. On coalescence their outputs agree. As (T) increases the coalescence probability tends to one, giving the uniform law for the CFTP output.
