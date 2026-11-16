# Assignment 2

## Problem 1 Answers

### 1A

#### States

$S = {(1,1), (1,2), (1,3), (2,1), (2,3), (3,1), (3,2), (3,3)}$

All nonterminal states have the following four available actions. The terminal states $G$ and $P$ have no available
actions. If a movement hits a boundary or wall, the agent remains in its current state. Probabilities leading to the
same resulting state are combined.

#### Available Actions

$A = {\text{up}, \text{down}, \text{left}, \text{right}}$

#### Transition Model

$T(s'|s,a) = P(s'|s,a)$

$T(s'|s, a) = \begin{cases}
0.70 & \text{if intended direction} \\
0.15 & 90^\circ \text{ left of the intended direction} \\
0.15 & 90^\circ \text{ right of the intended direction}
\end{cases}$

#### Rewards

$R(s,a,s') = \begin{cases}
+3 & \text{if } s' = G \\
-2 & \text{if } s' = P \\
-0.1 & \text{otherwise}
\end{cases}$

Terminal Handling

$V(G) = V(P) = 0$, $\gamma = 0.85$

#### Bellman Optimality Equation

$V^*(s) = \max_{a \in A(s)} \sum_{s' \in S} T(s'|s,a) [R(s,a,s') + \gamma V^*(s')]$

#### Action Up at (1,1)

| Resulting State | Probability | Reward |
|-----------------|-------------|--------|
| (1,1)           | 0.85        | -0.1   |
| (1,2)           | 0.15        | -0.1   |

$Q((1,1), up) = 0.85[-0.1 + 0.85V^*(1,1)] + 0.15 * [-0.1 + 0.85V^*(1,2)]$

$Q((1,1), up) = -0.1 + 0.7225V^*(1,1) + 0.1275V^*(1,2)$

### 1B

#### Sweep 1

| $V_1$  |        |        |
|:------:|:------:|:------:|
| $-0.1$ | $2.07$ |  $0$   |
| $-0.1$ |  Wall  | $2.07$ |
| $-0.1$ |  $0$   | $-0.1$ |

#### Sweep 1 Backups

|  Cell   | Maximizing action | Backup Calculation                    | Backup result |
|:-------:|:-----------------:|:--------------------------------------|:-------------:|
| $(1,1)$ |        up         | $0.7(-0.1) + 0.15(-0.1) + 0.15(-0.1)$ |    $-0.1$     |
| $(1,2)$ |       right       | $0.7(3) + 0.15(-0.1) + 0.15(-0.1)$    |    $2.07$     |
| $(2,1)$ |        up         | $0.7(-0.1) + 0.15(-0.1) + 0.15(-0.1)$ |    $-0.1$     |
| $(2,3)$ |        up         | $0.7(3) + 0.15(-0.1) + 0.15(-0.1)$    |    $2.07$     |
| $(3,1)$ |       left        | $0.7(-0.1) + 0.15(-0.1) + 0.15(-0.1)$ |    $-0.1$     |
| $(3,3)$ |       right       | $0.7(-0.1) + 0.15(-0.1) + 0.15(-0.1)$ |    $-0.1$     |

#### Sweep 2

|  $V_2$   |         |         |
|:--------:|:-------:|:-------:|
| $1.106$  | $2.598$ |   $0$   | 
| $-0.185$ |  Wall   | $2.598$ | 
| $-0.185$ |   $0$   | $0.834$ |

#### Sweep 2 Backups

|  Cell   | Maximizing action | Backup Calculation                                                           | Backup result |
|:-------:|:-----------------:|:-----------------------------------------------------------------------------|:-------------:|
| $(1,1)$ |       right       | $0.7(-0.1 + 0.85(2.07)) + 0.15(-0.1 + 0.85(-0.1)) + 0.15(-0.1 + 0.85(-0.1))$ |    $1.106$    |
| $(1,2)$ |       right       | $0.7(3 + 0.85(0)) + 0.15(-0.1 + 0.85(2.07)) + 0.15(-0.1 + 0.85(2.07))$       |    $2.598$    |
| $(2,1)$ |        up         | $0.7(-0.1 + 0.85(-0.1)) + 0.15(-0.1 + 0.85(-0.1)) + 0.15(-0.1 + 0.85(-0.1))$ |   $-0.185$    |
| $(2,3)$ |        up         | $0.7(3 + 0.85(0)) + 0.15(-0.1 + 0.85(2.07)) + 0.15(-0.1 + 0.85(2.07))$       |    $2.598$    |
| $(3,1)$ |       left        | $0.7(-0.1 + 0.85(-0.1)) + 0.15(-0.1 + 0.85(-0.1)) + 0.15(-0.1 + 0.85(-0.1))$ |   $-0.185$    |
| $(3,3)$ |        up         | $0.7(-0.1 + 0.85(2.07)) + 0.15(-2 + 0.85(0)) + 0.15(-0.1 + 0.85(-0.1))$      |    $0.834$    |

#### All Actions for S

|  State  |    Up     |   Down    |   Left   |   Right   |
|:-------:|:---------:|:---------:|:--------:|:---------:|
| $(3,1)$ | $-0.4572$ | $-0.4572$ | $-0.185$ | $-1.4555$ |

### 1C

#### Returned Approximate Values

$V(s) \approx \begin{bmatrix}
1.993 & 2.779 & 0 \\
1.458 & \text{Wall} & 2.779 \\
0.553 & 0 & 1.454
\end{bmatrix}$

#### Greedy Policy

| State | Best Action |
|:-----:|:-----------:|
| (1,1) |    Right    |
| (1,2) |    Right    |
| (2,1) |     Up      |
| (2,3) |     Up      |
| (3,1) |     Up      |
| (3,3) |     Up      |

#### Convergence Results

| Measurement                      |                 Result |
|:---------------------------------|-----------------------:|
| Number of Sweeps                 |                     23 |
| Last Delta                       | $7.263 \times 10^{-7}$ |
| Fresh Bellman Residual           | $3.442 \times 10^{-7}$ |
| Residual-Based Value-Error Bound | $2.295 \times 10^{-6}$ |

Value iteration stopped after the first complete sweep where the maximum absolute change was strictly below $10^{-6}$.

### 1D

#### Why the Agent Stays in the Left Column

Under the fixed policy, the agent always chooses Left. Starting at $S=(3,1)$, the intended Left movement hits the
boundary, so the agent stays in the same cell. The two possible slips move it Up or Down. The Down movement also hits
the boundary, while the Up movement moves it to $(2,1)$.

From $(2,1)$, the agent can move to either $(1,1)$ or $(3,1)$, or remain in $(2,1)$. At $(1,1)$, all possible outcomes
also remain in the left column.

Therefore, the agent can never leave the left column or reach the goal or pit. Every transition ends in a nonterminal
state and gives a reward of $-0.1$.

#### Calculating $V^\pi(S)$

Since every transition gives a reward of $-0.1$, the discounted reward sequence is:

$V^\pi(S) = -0.1 - 0.1(0.85) - 0.1(0.85)^2 - \cdots$

Using the infinite geometric series formula, we have:

$V^\pi(S) = \frac{-0.1}{1-0.85} =\frac{-0.1}{0.15} = \boxed{-\frac{2}{3}}$

#### Why Finite Value Does Not Imply Success or Optimality

The value is finite because the discount factor is less than 1, which makes the infinite sum of discounted rewards
converge. However, this does not mean the agent reaches the goal. Under this policy, the agent stays in the left column
forever and continuously receives negative rewards. Therefore, having a finite discounted value does not guarantee that
a policy achieves the goal or is optimal.

### 1E

#### One Decision Remaining

With one decision left, choosing Safe gives an immediate reward of 4 and terminates. Choosing Invest gives a reward of 0
and moves to Y, but there are no decisions remaining to collect the reward at Y.

Therefore:

$Q(X,\text{Safe}) = 4$

$Q(X,\text{Invest}) = 0$

The optimal action is Safe, with a value of:

$\boxed{V_1(X) = 4}$

#### Two Decisions Remaining

With two decisions left, choosing Invest gives an immediate reward of 0 and moves to Y. The agent can then take the only
available action at Y, which gives a reward of 7 and terminates.

Therefore:

$Q(X,\text{Safe}) = 4$

$Q(X,\text{Invest}) = 0 + 0.85(7) = 5.95$

The optimal action is Invest, with a value of:

$\boxed{V_2(X) = 5.95}$

#### State Information Needed for a Finite Horizon

The number of decisions remaining must be included in the state information because the optimal action depends on the
remaining horizon. For example, Safe is optimal with one decision remaining, while Invest is optimal with two decisions
remaining. The state can be represented as $(s, h)$, where $s$ is the current MDP state and $h$ is the number of
decisions remaining.
