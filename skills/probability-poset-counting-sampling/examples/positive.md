# Positive example: exact finite free-square counts

For the free-boundary n×n grid, build only in-square nearest-neighbor edges and use the descending-order recurrence from [method.md](../references/method.md). On selection of v, it contributes one peak exactly when all its neighbors remain unselected.

The checked implementation is [verify_counts.py](../evidence/W09/verify_counts.py); the saved output is [verification_results.json](../evidence/W09/verification_results.json).

| n | Total labelings | Exactly 1 peak | Exactly 2 peaks | DP states |
|---:|---:|---:|---:|---:|
| 2 | 24 | 16 | 8 | 37 |
| 3 | 362,880 | 29,568 | 143,808 | 902 |
| 4 | 20,922,789,888,000 | 35,704,394,880 | 779,299,174,080 | 74,217 |

The DP agrees with an independent enumeration of all `(n²)!` labelings for n=2 and n=3. For n=3, among the 143,808 labelings with exactly two peaks, Manhattan distances 2, 3, and 4 occur 63,552, 64,512, and 15,744 times, respectively. One seeded exact branch-sampling trace is also saved; its existence demonstrates the finite sampler, not a distance limit.

These are exact finite calculations. They do not show that the normalized peak distance tends to zero as n grows.
