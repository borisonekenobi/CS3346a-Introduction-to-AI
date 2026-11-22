"""Provided experiment driver; fitting uses train.csv only."""
from pathlib import Path
import argparse
import csv
import html
import json
from a3_support import load_algorithms, choose_threshold, classify, metrics

def read_cases(path):
    with Path(path).open(newline='', encoding='utf-8') as stream:
        rows = list(csv.DictReader(stream))
    X = [[int(row[f'x{j}']) for j in (1, 2, 3)] for row in rows]
    return [row['case_id'] for row in rows], X, [int(row['label']) for row in rows]

def run(module, data_dir):
    _, X_train, y_train = read_cases(data_dir / 'train.csv')
    val_ids, X_val, y_val = read_cases(data_dir / 'validation.csv')
    model = module.fit_nb(X_train, y_train, alpha=1.0)
    p_val = [module.posterior_one(model, x) for x in X_val]
    chosen, rows = choose_threshold(y_val, p_val)
    # Freeze chosen threshold before examining the test outcomes.
    test_ids, X_test, y_test = read_cases(data_dir / 'test.csv')
    p_test = [module.posterior_one(model, x) for x in X_test]
    pred_test = [classify(p, chosen) for p in p_test]
    report = dict(
        experiment='A3 synthetic support triage',
        provenance='Fixed hand-authored teaching data; not real support messages',
        seed=None, dependencies='Python 3.10+ standard library only',
        alpha=1.0, priors=model.priors, p_one=model.p_one,
        validation=rows, selected_threshold=chosen,
        test=metrics(y_test, pred_test),
        test_routine_only_baseline=metrics(y_test, [0] * len(y_test)),
        limitation='Tiny synthetic sample; no real-world or calibration guarantee')
    predictions = {}
    for name, ids, labels, probs in [('validation', val_ids, y_val, p_val),
                                     ('test', test_ids, y_test, p_test)]:
        predictions[name] = [dict(case_id=i, label=y, probability_review=p,
                                  prediction=classify(p, chosen))
                             for i, y, p in zip(ids, labels, probs)]
    return report, predictions

def write_outputs(out, report, predictions):
    out.mkdir(parents=True, exist_ok=True)
    (out / 'report.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    for name, rows in predictions.items():
        with (out / f'predictions_{name}.csv').open('w', newline='', encoding='utf-8') as stream:
            writer = csv.DictWriter(stream, fieldnames=rows[0].keys())
            writer.writeheader(); writer.writerows(rows)
    bars = ''.join(
        '<tr><td>{:.2f}</td><td>{:.3f}</td><td>{}</td><td><div style="width:{}px;'
        'height:18px;background:#4f2d7f"></div></td></tr>'.format(
            r['threshold'], r['accuracy'], r['total_cost'], r['total_cost'] * 18)
        for r in report['validation'])
    page = ('<!doctype html><html lang="en"><meta charset="utf-8"><title>A3 report</title>'
            '<style>body{font:18px/1.6 system-ui;max-width:900px;margin:40px auto;padding:20px}'
            'th,td{padding:9px 18px;text-align:left;border-bottom:1px solid #ddd}'
            'pre{background:#f4f3f6;padding:18px;white-space:pre-wrap}</style>'
            '<h1>Synthetic support triage</h1><p>Measured on the supplied teaching data. '
            'Smaller validation cost is better. This is not a real-world benchmark.</p>'
            '<table><tr><th>Threshold</th><th>Accuracy</th><th>Cost</th><th>Cost bar</th></tr>'
            + bars + '</table><h2>Experiment record</h2><pre>'
            + html.escape(json.dumps(report, indent=2)) + '</pre></html>')
    (out / 'report.html').write_text(page, encoding='utf-8')

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--module', type=Path, help='optional path to an implementation')
    parser.add_argument('--data-dir', type=Path, default=Path(__file__).with_name('data'))
    parser.add_argument('--out', type=Path, default=Path('results'))
    args = parser.parse_args()
    report, predictions = run(load_algorithms(args.module), args.data_dir)
    write_outputs(args.out, report, predictions)
    print(json.dumps(dict(selected_threshold=report['selected_threshold'],
                          test=report['test']), indent=2))
    print(f'Wrote {args.out.resolve()}')

if __name__ == '__main__':
    main()
