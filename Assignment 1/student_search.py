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
    if node.kind == 'MAX':
        best_val = -inf
        for child in children:
            child_val = alpha_beta(child, alpha, beta, reverse, visited)
            best_val = max(best_val, child_val)
            alpha = max(alpha, best_val)
            if alpha >= beta:
                break
        return best_val
    else:
        best_val = inf
        for child in children:
            child_val = alpha_beta(child, alpha, beta, reverse, visited)
            best_val = min(best_val, child_val)
            beta = min(beta, best_val)
            if alpha >= beta:
                break
        return best_val


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

    if node.kind == 'MAX':
        children = []
        for child in node.children: children.append(expectimax(child, visited))
        return max(children)
    elif node.kind == 'CHANCE':
        expected_value = 0.0
        for child, p in zip(node.children, node.probabilities):
            child_val = expectimax(child, visited)
            expected_value += p * child_val
        return expected_value
    else:
        raise ValueError('expectimax accepts only MAX/CHANCE/LEAF trees')
