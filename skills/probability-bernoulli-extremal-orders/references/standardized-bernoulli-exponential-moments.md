# Exponential moments after Bernoulli standardization

Let \(S\) be a sum of independent Bernoulli variables, with mean \(\mu\) and variance \(\sigma^2\ge1\). Set \(W=(S-\mu)/\sigma\). For every \(t\ge0\),
\[
 \mathbb E e^{t|W|} \le 2\exp(e^t-1-t).
\]
To obtain the bound, write \(W=\sum_i X_i\) with centered independent \(X_i\), \(|X_i|\le1\) and \(\sum_i\mathbb E X_i^2=1\). Termwise comparison in the exponential series gives
\(e^{\pm tx}\le 1\pm tx+(e^t-1-t)x^2\) for \(|x|\le1\). Take expectations, multiply the factors and use \(1+y\le e^y\). The bound follows from \(e^{t|W|}\le e^{tW}+e^{-tW}\).

The corresponding square-exponential claim fails. Take \(S_n\sim\mathrm{Bin}(n,2/n)\) for \(n\ge4\), so \(\mu=2\) and \(\sigma^2=2(1-2/n)\). The event \(S_n=n\) alone contributes
\[
 (2/n)^n \exp\{n(n-2)/2\}
\]
to \(\mathbb E e^{W_n^2}\). Its logarithm tends to infinity. For \(n=16\) this one contribution already exceeds \(2^{64}\), since \(e>2\).

Auld and Neammanee, *Journal of Inequalities and Applications* 2024:10, physical pp. 7–8, Lemmas 3.3–3.4, use a uniform square-exponential bound in their subsequent local-normal argument. The binomial family refutes that auxiliary bound. To use the target local-limit statement, cite an independently established result or provide substitute estimates for every dependent step. The linear-exponential estimate above applies where only a fixed linear exponential is required. [Published source](https://doi.org/10.1186/s13660-024-03087-4)
