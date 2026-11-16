"""Complete only these two functions. Keep their signatures unchanged."""
def synchronous_sweep(mdp, old_values):
    """Return a NEW dict for every state, using only old_values in all backups.
    mdp.states lists states. mdp.actions(s) lists valid actions, empty at a terminal.
    mdp.transitions(s,a) yields (probability, next_state, reward) outcomes.
    mdp.gamma is the discount. Terminal values must be 0. Do not change old_values.
    """
    new_values = {}
    for state in mdp.states:
        actions = mdp.actions(state)

        if not actions:
            new_values[state] = 0.0
            continue

        max_value = float('-inf')
        for action in actions:
            expected_value = 0.0
            for prob, next_state, reward in mdp.transitions(state, action):
                expected_value += prob * (reward + mdp.gamma * old_values[next_state])
            max_value = max(max_value, expected_value)

        new_values[state] = max_value

    return new_values

def q_learning_update(q, state, action, reward, next_state, terminated,
                      next_actions, alpha, gamma):
    """Update only q[(state,action)] IN PLACE and return its new value.
    Missing pairs have value 0. If terminated, bootstrap is 0 even if q has
    entries for next_state. Otherwise maximize over next_actions; an empty
    nonterminal action list is an error. Use the pre-update Q values for the target.
    """
    old_value = q.get((state, action), 0.0)

    if terminated:
        next_value = 0.0
    else:
        if not next_actions:
            raise ValueError("Nonterminal state must have at least one action")

        next_value = max(
            q.get((next_state, a), 0.0)
            for a in next_actions
        )

    new_value = old_value + alpha * (
            reward + gamma * next_value - old_value
    )

    q[(state, action)] = new_value
    return new_value
