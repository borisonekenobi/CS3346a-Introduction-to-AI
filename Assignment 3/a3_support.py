"""Provided infrastructure for CS3346A Fall 2026 Assignment 3. Do not edit."""
from dataclasses import dataclass
from pathlib import Path
import importlib.util
import math
import os
import sys

@dataclass(frozen=True)
class NBModel:
    # priors[c] = P(class=c); p_one[c][j] = P(feature j=1 | class=c).
    priors: tuple[float, float]
    p_one: tuple[tuple[float, ...], tuple[float, ...]]

def validate_training(X, y, alpha):
    """Return (number of rows, number of features), or raise ValueError."""
    if not isinstance(alpha, (int, float)) or not math.isfinite(alpha) or alpha <= 0:
        raise ValueError('alpha must be finite and positive')
    if not X or len(X) != len(y) or not X[0]:
        raise ValueError('nonempty aligned X and y are required')
    d = len(X[0])
    if any(len(row) != d or any(v not in (0, 1) for v in row) for row in X):
        raise ValueError('X must be rectangular and binary')
    if set(y) != {0, 1}:
        raise ValueError('both binary classes must occur')
    return len(X), d

def validate_query(model, x):
    if len(x) != len(model.p_one[0]) or any(v not in (0, 1) for v in x):
        raise ValueError('query must be binary and match the model dimension')

def probability_one_from_log_scores(log0, log1):
    """Stable two-class normalization; students need not implement this."""
    if not (math.isfinite(log0) and math.isfinite(log1)):
        raise ValueError('finite log scores required')
    offset = max(log0, log1)
    w0, w1 = math.exp(log0 - offset), math.exp(log1 - offset)
    return w1 / (w0 + w1)

def classify(probability_one, threshold):
    return int(probability_one >= threshold)

def metrics(labels, predictions):
    if not labels or len(labels) != len(predictions):
        raise ValueError('nonempty aligned labels and predictions required')
    if any(v not in (0, 1) for v in (*labels, *predictions)):
        raise ValueError('labels and predictions must be binary')
    tp = sum(y == 1 and p == 1 for y, p in zip(labels, predictions))
    fp = sum(y == 0 and p == 1 for y, p in zip(labels, predictions))
    tn = sum(y == 0 and p == 0 for y, p in zip(labels, predictions))
    fn = sum(y == 1 and p == 0 for y, p in zip(labels, predictions))
    n = len(labels)
    return dict(TP=tp, FP=fp, TN=tn, FN=fn, n=n,
                accuracy=(tp + tn) / n,
                precision=tp / (tp + fp) if tp + fp else 0.0,
                recall=tp / (tp + fn) if tp + fn else 0.0,
                total_cost=4 * fn + fp, mean_cost=(4 * fn + fp) / n)

def choose_threshold(labels, probabilities, thresholds=(0.15, 0.50, 0.75)):
    """Validation only: minimize 4*FN+FP; exact ties choose largest threshold."""
    rows = []
    for threshold in thresholds:
        if not 0 <= threshold <= 1:
            raise ValueError('threshold outside [0,1]')
        row = dict(threshold=threshold, **metrics(
            labels, [classify(p, threshold) for p in probabilities]))
        rows.append(row)
    if not rows:
        raise ValueError('at least one threshold required')
    return min(rows, key=lambda r: (r['total_cost'], -r['threshold']))['threshold'], rows

def load_algorithms(path=None):
    """Load a local student/reference module without changing its file name."""
    path = Path(path or os.environ.get('A3_SUBMISSION') or
                Path(__file__).with_name('student_algorithms.py')).resolve()
    spec = importlib.util.spec_from_file_location('a3_loaded_algorithms', path)
    if spec is None or spec.loader is None:
        raise ValueError(f'cannot load {path}')
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module
