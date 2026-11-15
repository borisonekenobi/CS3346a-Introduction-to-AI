"""Complete only these two functions. Keep their signatures unchanged."""
def synchronous_sweep(mdp, old_values):
    """Return a NEW dict for every state, using only old_values in all backups.
    mdp.states lists states. mdp.actions(s) lists valid actions, empty at a terminal.
    mdp.transitions(s,a) yields (probability, next_state, reward) outcomes.
    mdp.gamma is the discount. Terminal values must be 0. Do not change old_values.
    """
    raise NotImplementedError('Complete the synchronous Bellman sweep')

def q_learning_update(q, state, action, reward, next_state, terminated,
                      next_actions, alpha, gamma):
    """Update only q[(state,action)] IN PLACE and return its new value.
    Missing pairs have value 0. If terminated, bootstrap is 0 even if q has
    entries for next_state. Otherwise maximize over next_actions; an empty
    nonterminal action list is an error. Use the pre-update Q values for the target.
    """
    raise NotImplementedError('Complete one Q-learning update')
