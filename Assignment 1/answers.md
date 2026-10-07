# Assignment 1

## Part A: Search problem data

### A1

|                      |             BFS              |          DFS          |                UCS                |
|:---------------------|:----------------------------:|:---------------------:|:---------------------------------:|
| Removal Order        | `S`, `A`, `B`, `C`, `D`, `G` |  `S`, `A`, `C`, `G`   |   `S`, `B`, `A`, `C`, `D`, `G`    |
| Returned S-to-G Path |    `S` → `A` → `C` → `G`     | `S` → `A` → `C` → `G` | `S` → `B` → `A` → `C` → `D` → `G` |
| Total Cost           |       $4 + 1 + 5 = 10$       |   $4 + 1 + 5 = 10$    |      $1 + 1 + 1 + 1 + 2 = 6$      |

Frontier Tracking:

| State Removed | Active Frontier |
|:-------------:|:----------------|
|       S       | `[B:1, A:4]`    |
|       B       | `[A:2, C:6]`    |
|       A       | `[C:3, D:6]`    |
|       C       | `[D:4, G:8]`    |
|       D       | `[G:6]`         |
|       G       | **STOP**        |

### A2

#### True Cheapest Cost $h^*$

- $h^*(G) = 0$
- $h^*(D) = 2$
- $h^*(C) = 3$
- $h^*(A) = 4$
- $h^*(B) = 5$
- $h^*(S) = 6$

#### Is the heuristic admissible?

| State | $h$ | $h^*$ | Admissible? |
|:-----:|:---:|:-----:|:-----------:|
|   S   |  6  |   6   |     Yes     |
|   A   |  0  |   4   |     Yes     |
|   B   |  5  |   5   |     Yes     |
|   C   |  0  |   3   |     Yes     |
|   D   |  2  |   2   |     Yes     |
|   G   |  0  |   0   |     Yes     |

Yes, the heuristic is admissible because for every state, the heuristic value $h$ is less than or equal to the true
cheapest cost $h^*$.

#### Is the heuristic consistent?

| State | Successor | $h(State)$ | $h(Successor)$ | $cost(State, Successor)$ | Consistent? |
|:-----:|:---------:|:----------:|:--------------:|:------------------------:|:-----------:|
|   S   |     A     |     6      |       0        |            4             |     No      |
|   S   |     B     |     6      |       5        |            1             |     Yes     |
|   A   |     C     |     0      |       0        |            1             |     Yes     |
|   A   |     D     |     0      |       2        |            4             |     Yes     |
|   B   |     A     |     5      |       0        |            1             |     No      |
|   B   |     C     |     5      |       0        |            5             |     Yes     |
|   C   |     D     |     0      |       2        |            1             |     Yes     |
|   C   |     G     |     0      |       0        |            5             |     Yes     |
|   D   |     G     |     2      |       0        |            2             |     Yes     |

No, the heuristic is not consistent because there are cases where $h (State) > cost (State, Successor) + h (Successor)$,
such as for the transitions from `S` to `A` and from `B` to `A`.

### A3

| State Removed | $g$ | $h$ | $f$ | Active Frontier           |
|:-------------:|:---:|:---:|:---:|:--------------------------|
|     **S**     |  0  |  6  |  6  | `[A:4/4, B:1/6]`          |
|     **A**     |  4  |  0  |  4  | `[C:5/5, B:1/6, D:8/10]`  |
|     **C**     |  5  |  0  |  5  | `[B:1/6, D:6/8, G:10/10]` |
|     **B**     |  1  |  5  |  6  | `[A:2/2, D:6/8, G:10/10]` |
|    **A***     |  2  |  0  |  2  | `[C:3/3, D:6/8, G:10/10]` |
|    **C***     |  3  |  0  |  3  | `[D:4/6, G:8/8]`          |
|     **D**     |  4  |  2  |  6  | `[G:6/6]`                 |
|     **G**     |  6  |  0  |  6  | **STOP**                  |

**Final Returned S-to-G Path:** `S` → `B` → `A` → `C` → `D` → `G`

**Total Cost:** $1 + 1 + 1 + 1 + 2 = 6$

**Reopened States:** `A`, `C`

### A4

| State Removed | $g$ | $h$ | $f$ | Active Frontier           |
|:-------------:|:---:|:---:|:---:|:--------------------------|
|     **S**     |  0  |  6  |  6  | `[A:4/4, B:1/6]`          |
|     **A**     |  4  |  0  |  4  | `[C:5/5, B:1/6, D:8/10]`  |
|     **C**     |  5  |  0  |  5  | `[B:1/6, D:6/8, G:10/10]` |
|     **B**     |  1  |  5  |  6  | `[D:6/8, G:10/10]`        |
|     **D**     |  6  |  2  |  8  | `[G:8/8]`                 |
|     **G**     |  8  |  0  |  8  | **STOP**                  |

**Final Returned S-to-G Path:** `S` → `A` → `C` → `D` → `G`

**Total Cost:** $4 + 1 + 1 + 2 = 8$

Admissibility guarantees optimal paths in tree searches, but graph searches require consistency to ensure the first path
found to any state is the cheapest. When a heuristic is inconsistent, the algorithm can prematurely close a state via a
suboptimal path. Without reopening capabilities, these suboptimal path assignments become permanent. Reopening rescues
the search by allowing the algorithm to dynamically correct these early errors. It intercepts cheaper pathways to closed
states, restores them to the frontier, and forces the true optimal path to emerge.
