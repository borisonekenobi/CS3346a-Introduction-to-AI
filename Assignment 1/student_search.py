"""Complete ONLY the two TODO regions. Python 3.10+; standard library only."""
from math import inf
from game_tree import record_leaf

def alpha_beta(node, alpha=-inf, beta=inf, reverse=False, visited=None):
    """Return a fail-soft value, pruning when alpha >= beta.

    reverse=True reverses children at EVERY internal node.
    Only evaluated terminal names go into the caller's visited list.
    With a full (-inf, inf) root window the returned root value is exact.
    With a narrow window a cut-off result may be a bound.
    """
    if node.kind == 'LEAF':
        return record_leaf(node, visited)
    if node.kind not in ('MAX', 'MIN'):
        raise ValueError('alpha_beta accepts only MAX/MIN/LEAF trees')
    children = node.children[::-1] if reverse else node.children
    # TODO 1: MAX/MIN recursion; pass the current window and visited list.
    # Update alpha or beta, stop on alpha >= beta, and return the best value
    # observed (fail-soft). Do not call expectimax or inspect unvisited leaves.
    raise NotImplementedError('Complete alpha_beta in student_search.py')

def expectimax(node, visited=None):
    """Return exact expected utility in a finite MAX/CHANCE/LEAF tree.

    Probabilities are valid, supplied in child order, and sum to one.
    Every child must be evaluated, including a zero-probability child;
    this convention fixes the trace expected by the marking tests.
    """
    if node.kind == 'LEAF':
        return record_leaf(node, visited)
    if node.kind not in ('MAX', 'CHANCE'):
        raise ValueError('expectimax accepts only MAX/CHANCE/LEAF trees')
    # TODO 2: MAX recursion or the probability-weighted sum at CHANCE.
    # Preserve supplied order and record leaves through recursive calls.
    raise NotImplementedError('Complete expectimax in student_search.py')
