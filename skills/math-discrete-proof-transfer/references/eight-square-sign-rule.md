# Exact three-bit eight-square sign rule

The exact identity below is Equation (12) and the sign cancellation used on
physical pp. 16–17 of *A \(2^{o(n)}\) Time Algorithm for 3-SAT*.
The fixed source is the `Eight.Signs` declaration in
`eth/proof/statements/EightSquareStatement.lean` at the paper's public
formal revision \(16a5ce41304fcdaea4e0be7c132e1c361dc26da5\).

For \(p,q\in\{0,1\}^3\), set \(\sigma(p,q)=(-1)^{\phi(p,q)}\), with the
nine-term polynomial \(\phi\) implemented term by term in the script.
For \(p,q,r,s\in\{0,1\}^3\) the verified sign identity is
\[
\mathbf 1_{p\oplus q=r\oplus s}
  [\sigma(p,q)\sigma(r,s)+\sigma(p,s)\sigma(r,q)]
   =2\mathbf 1_{p=r,\ q=s}.
\]
All \(8^4=4096\) cases were checked in base MATLAB. Exactly 512 satisfy the
XOR condition, with 64 diagonal cases and 448 cancellations.

~~~sh
matlab -batch "run('scripts/check_eight_square_signs.m')"
~~~

The paper and repository PDFs match byte-for-byte for source SHA-256
`7af518b09342c967ea371c74b8989806684c5d02aabe5763ca08554aff5025a0`.
For the separate local Hexagon copy
`85034e06e1d058aa4ed7d895c226ae755ebd3a5c6614b07ba14981915c4f7360`,
one exact stamp removal and whitespace normalization give matching
extracted text. Its physical display agrees for this sign rule. The case
enumeration supports the displayed identity. The general factorization,
recursive algorithm, model translation and ETH claim carry separate
dependencies. [Fixed formal source](https://github.com/anthropics/formal-math/tree/16a5ce41304fcdaea4e0be7c132e1c361dc26da5/eth)
