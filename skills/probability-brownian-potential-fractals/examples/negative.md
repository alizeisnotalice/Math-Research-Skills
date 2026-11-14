# Negative example: invalidly identify three different dimensions

**Bad argument.** “The planar Brownian frontier has dimension 4/3, so the smallest Jordan arc in the Brownian trace has dimension 4/3. The labyrinth result also proves the minimum is 2.”

**Why it fails.** The frontier is one distinguished boundary set; B061 minimizes over every Jordan arc contained in the trace. The labyrinth dimension is a supremum, not an infimum. Neither theorem identifies the minimum. The full trace dimension is 2, but a subset can have smaller dimension.

**Repair.** State the admissible family and optimize over that family. Use frontier results only for frontier claims, labyrinth results only for a supremum, and loop-erasure/SLE results only after proving that the resulting simple arc lies inside the prescribed trace segment and transferring the dimension through the correct radial/chordal interface.
