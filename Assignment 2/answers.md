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

## Problem 2 Answers

### 2A

#### Observed State-Action Outcomes

Combining all three episodes gives the following observed transition counts:

| State-Action Pair | Next State | Count | Total Observations |
|:-----------------:|:----------:|:-----:|:------------------:|
|     (A, try)      |    $A$     |  $1$  |        $6$         |
|     (A, try)      |    $B$     |  $5$  |        $6$         |
|     (B, send)     |    $C$     |  $2$  |        $5$         |
|     (B, send)     |    $T$     |  $3$  |        $5$         |
|    (C, reset)     |    $A$     |  $2$  |        $2$         |

#### Empirical Transition Model and Rewards

The empirical transition probability is calculated by dividing each outcome's count by the total observations for that
state-action pair. The conditional reward is the average reward observed for that outcome.

| State-Action Pair | Next State | Probability | Conditional Reward |
|:-----------------:|:----------:|:-----------:|:------------------:|
|     (A, try)      |    $A$     |    $1/6$    |        $-1$        |
|     (A, try)      |    $B$     |    $5/6$    |        $-1$        |
|     (B, send)     |    $C$     |    $2/5$    |        $-2$        |
|     (B, send)     |    $T$     |    $3/5$    |        $6$         |
|    (C, reset)     |    $A$     |     $1$     |        $-1$        |

#### One Synchronous Fixed-Policy Evaluation Sweep

Starting with zero values for all states, including the terminal state:

$V_0(A) = V_0(B) = V_0(C) = V_0(T) = 0$

Using $\gamma = 0.9$, the fixed-policy evaluation update is:

$V_1(A) = \sum_{s'}\hat P(s'|s, \pi(s)) [R(s, \pi(s), s') + \gamma V_0(s')]$

#### State A:

$V_1(A) = \frac{1}{6}[-1 + 0.9(0)] + \frac{5}{6}[-1 + 0.9(0)] = \boxed{-1}$

#### State B:

$V_1(B) = \frac{2}{5}[-2 + 0.9(0)] + \frac{3}{5}[6 + 0.9(0)] = -0.8 + 3.6 = \boxed{2.8}$

#### State C:

$V_1(C) = 1[-1 + 0.9(0)] = \boxed{-1}$

#### Terminal State T:

$V_1(T) = 0$

The resulting values after one sweep are:

| State | Value |
|:-----:|:-----:|
|  $A$  | $-1$  |
|  $B$  | $2.8$ |
|  $C$  | $-1$  |
|  $T$  |  $0$  |

#### Can the Model of Wait at A Be Determined?

No. The behaviour policy always chooses Try at A, and none of the recorded episodes contains an observation of Wait.
Therefore, there is no transition or reward information available to estimate the model of Wait. Its transition
probabilities and rewards cannot be determined from the given data, so no unobserved outcomes should be assumed.

### 2B

The discounted return from a state is calculated from its first visit until the end of the episode:

$G_t = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \cdots$

I only use the first visit to each state within an episode. The rewards from all subsequent steps are still included in
that first-visit return.

#### Episode 1

The sequence is:

$(A, -1) \rightarrow (B, 6) \rightarrow T$

- A: $G_0 = -1 + 0.9(6) = \boxed{4.4}$
- B: $G_1 = \boxed{6}$
- C: Not visited.

#### Episode 2

The sequence is:

$A(-1) \rightarrow A(-1) \rightarrow B(-2) \rightarrow C(-1) \rightarrow A(-1) \rightarrow B(6) \rightarrow T$

- A: First visited at the
  beginning: $G(A) = -1 + 0.9(-1) + 0.9^2(-2) + 0.9^3(-1) + 0.9^4(-1) + 0.9^5(6) = \boxed{-1.36216}$
- B: First visited after the second A: $G(B) = -2 + 0.9(-1) + 0.9^2(-1) + 0.9^3(6) = \boxed{0.664}$
- C: First visited after B: $G(C) = -1 + 0.9(-1) + 0.9^2(6) = \boxed{2.96}$

#### Episode 3

The sequence is:

$A(-1) \rightarrow B(-2) \rightarrow C(-1) \rightarrow A(-1) \rightarrow B(6) \rightarrow T$

- A: First visited at the beginning: $G(A) = -1 + 0.9(-2) + 0.9^2(-1) + 0.9^3(-1) + 0.9^4(6) = \boxed{-0.4024}$
- B: First visited after A: $G(B) = -2 + 0.9(-1) + 0.9^2(-1) + 0.9^3(6) = \boxed{0.664}$
- C: First visited after B: $G(C) = -1 + 0.9(-1) + 0.9^2(6) = \boxed{2.96}$

#### Final Estimates

| State |  Episode 1  | Episode 2  | Episode 3 | Estimated Value |
|:-----:|:-----------:|:----------:|:---------:|:---------------:|
|  $A$  |    $4.4$    | $-1.36216$ | $-0.4024$ |    $0.87848$    |
|  $B$  |     $6$     |  $0.664$   |  $0.664$  |    $2.44267$    |
|  $C$  | Not visited |   $2.96$   |  $2.96$   |     $2.96$      |
|  $T$  |     $0$     |    $0$     |    $0$    |       $0$       |

Therefore, the first-visit Monte Carlo estimates of the state values are:

$\boxed{V(A) \approx 0.87848}$, $\boxed{V(B) \approx 2.44267}$, $\boxed{V(C) = 2.96}$. $\boxed{V(T) = 0}$

### 2C

I use Episode 2 only, with $\alpha=0.5$, $\gamma=0.9$, and initialize all state values to zero:

$V(A) = V(B) = V(C) = V(T) = 0$

For each transition, I calculate the TD target and update the current state's value using:

$V(s) \leftarrow V(s) + 0.5[\text{Target} - V(s)]$

The transitions are processed in their listed order, using the latest values after each update.

| Step | Transition    | TD target              | Updated value  |
|------|---------------|------------------------|----------------|
| 1    | A → A, $r=-1$ | $-1+0.9(0)=-1$         | $V(A)=-0.5$    |
| 2    | A → B, $r=-1$ | $-1+0.9(0)=-1$         | $V(A)=-0.75$   |
| 3    | B → C, $r=-2$ | $-2+0.9(0)=-2$         | $V(B)=-1$      |
| 4    | C → A, $r=-1$ | $-1+0.9(-0.75)=-1.675$ | $V(C)=-0.8375$ |
| 5    | A → B, $r=-1$ | $-1+0.9(-1)=-1.9$      | $V(A)=-1.325$  |
| 6    | B → T, $r=6$  | $6$                    | $V(B)=2.5$     |

For the final transition, T is terminal, so its target is just the immediate reward of $6$, with no continuation term.

The final state values after processing all six transitions are:

| State | Final value |
|-------|------------:|
| $A$   |    $-1.325$ |
| $B$   |       $2.5$ |
| $C$   |   $-0.8375$ |
| $T$   |         $0$ |

Therefore, the final value vector is:

$\boxed{V = [-1.325, 2.5, -0.8375, 0]}$

The values are updated in place, meaning that later transitions use the most recently updated state values rather than
the initial values.

### 2D

#### Q-learning updates

I reset the Q table to the values provided in the question and use $\alpha=0.5$ and $\gamma=0.9$.

The Q-learning update rule is:

$Q(s,a) \leftarrow Q(s,a) + \alpha[\text{Target} - Q(s,a)]$

For nonterminal next states, the target is:

$\text{Target} = r + \gamma\max_{a'}Q(s',a')$

For terminal next states, the target is just the immediate reward.

**Observation 1: (B, send, -2, C, False)**

At C, the maximum Q-value is:

$\max(Q(C,reset), Q(C,send)) = \max(-0.5,0) = 0$

Target:

$-2 + 0.9(0) = -2$

Update:

$Q(B,send) = 2 + 0.5(-2-2) = \boxed{0}$

**Observation 2: (A, try, -1, B, False)**

Using the updated Q table, the maximum Q-value at B is:

$\max(Q(B,send), Q(B,retry)) = \max(0, 0) = 0$

Target:

$-1 + 0.9(0) = -1$

Update:

$Q(A, try) = 1 + 0.5(-1 - 1) = \boxed{0}$

**Observation 3: (B, send, 6, T, True)**

Since T is terminal, there is no continuation term.

Target:

$6$

Update:

$Q(B,send) = 0 + 0.5(6-0) = \boxed{3}$

#### Final Q table

After processing all three observations, the Q table is:

| State | First action | Q-value | Second action | Q-value |
|-------|--------------|--------:|---------------|--------:|
| $A$   | try          |     $0$ | wait          |   $0.5$ |
| $B$   | send         |     $3$ | retry         |     $0$ |
| $C$   | reset        |  $-0.5$ | send          |     $0$ |

#### ε-greedy policy at A

At $A$, the Q-values are:

$Q(A, try) = 0,$

$Q(A, wait) = 0.5$

Therefore, **wait is the exploitation action** because it has the highest Q-value.

With $\varepsilon = 0.2$, the agent exploits with probability $0.8$ and explores with probability $0.2$. During
exploration, it selects uniformly from both available actions, including the greedy action.

The exploration probability for each action is:

$\frac{0.2}{2} = 0.1$

Therefore, the final action probabilities are:

| Action | Exploitation | Exploration |         Total |
|--------|-------------:|------------:|--------------:|
| try    |            0 |         0.1 | **0.1 (10%)** |
| wait   |          0.8 |         0.1 | **0.9 (90%)** |

#### Why Q-learning is off-policy

Q-learning is an off-policy algorithm because it uses the maximum Q-value of the next state when calculating its target,
rather than the value of the action actually selected by the behaviour policy. This means the agent can explore
different actions while still learning the values of the optimal policy. As a result, the behaviour policy used to
collect experience can differ from the greedy policy being learned.

### 2E

Given:

$w = (0.5, -1),$

$f = (2,-1),$

$\alpha = 0.25,$

$\gamma = 0.9,$

$r = -2$

The maximum next-state Q-value is 3.

### 1. Calculate the current Q-value

Using the linear approximation:

$Q(s, a) = w_1f_1 + w_2f_2$

$Q(s, a) = (0.5)(2) + (-1)(-1)$

$\boxed{Q(s, a) = 2}$

### 2. Calculate the TD error

$\delta = r + \gamma\max_{a'}Q(s', a') - Q(s, a)$

$\delta = -2 + 0.9(3) - 2$

$\boxed{\delta = -1.3}$

### 3. Update the weights

Using the weight update rule:

$w_i \leftarrow w_i + \alpha\delta f_i$

Both weights use the same original TD error of $-1.3$.

For $w_1$:

$w_1 = 0.5 + 0.25(-1.3)(2)$

$\boxed{w_1 = -0.15}$

For $w_2$:

$w_2 = -1 + 0.25(-1.3)(-1)$

$\boxed{w_2 = -0.675}$

The updated weight vector is:

$\boxed{w' = (-0.15, -0.675)}$

### 4. Calculate the new prediction

Using the updated weights and the same feature vector:

$Q_{\text{new}}(s, a) = (-0.15)(2) + (-0.675)(-1)$

$Q_{\text{new}}(s, a) = -0.3 + 0.675$

$\boxed{Q_{\text{new}}(s, a) = 0.375}$

### Final results

| Quantity        |   Result |
|-----------------|---------:|
| Current Q-value |      $2$ |
| TD error        |   $-1.3$ |
| Updated $w_1$   |  $-0.15$ |
| Updated $w_2$   | $-0.675$ |
| New prediction  |  $0.375$ |
