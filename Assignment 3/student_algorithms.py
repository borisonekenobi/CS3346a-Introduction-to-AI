"""CS3346A Fall 2026 A3. Implement only these two functions.

Use Python's standard library. Keep these names and signatures.
Do not replace the algorithms with a prebuilt classifier or hardcoded results.
"""
import math
from a3_support import (NBModel, validate_training, validate_query,
                        probability_one_from_log_scores)

def fit_nb(X, y, alpha=1.0):
    """Return NBModel using empirical priors and Bernoulli Laplace smoothing.

    X: list of n binary rows, each with d >= 1 features.
    y: n binary class labels, containing both classes.
    priors[c] = N_c / n; p_one[c][j] = (N_cj+alpha)/(N_c+2*alpha).
    Support any positive feature count and positive alpha; do not mutate inputs.
    """
    n, d = validate_training(X, y, alpha)
    # TODO: count examples and feature-one occurrences within each class.
    # TODO: form the priors and class-conditional feature probabilities.
    raise NotImplementedError('Implement fit_nb')

def posterior_one(model, x):
    """Return P(class=1 | x) under the fitted Bernoulli naive Bayes model.

    Include BOTH present and absent feature likelihoods. Compute two log scores
    with math.log, then use probability_one_from_log_scores(log0, log1).
    """
    validate_query(model, x)
    # TODO: compute a log score for each class, including its prior.
    raise NotImplementedError('Implement posterior_one')
