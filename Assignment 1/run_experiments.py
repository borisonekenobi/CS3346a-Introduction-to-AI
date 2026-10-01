"""Run the supplied trees and save results.json plus an SVG comparison."""
import argparse, importlib, json
from html import escape
from pathlib import Path
from game_tree import assessment_tree

def save_chart(records, path):
    # Counts are measurements of evaluated terminal leaves, not total nodes.
    body=['<svg xmlns="http://www.w3.org/2000/svg" width="760" height="330" viewBox="0 0 760 330">',
          '<rect width="760" height="330" fill="white"/>',
          '<text x="28" y="36" font-family="sans-serif" font-size="21">Evaluated terminal leaves</text>']
    for i,r in enumerate(records):
        y=85+i*75; n=r['evaluated_leaves']; width=n*30
        body.extend([f'<text x="28" y="{y+22}" font-family="sans-serif" font-size="16">{escape(r["name"])}</text>',
                     f'<rect x="255" y="{y}" width="{width}" height="34" fill="#4F2683"/>',
                     f'<text x="{265+width}" y="{y+23}" font-family="sans-serif" font-size="17">{n}</text>'])
    body.append('</svg>');path.write_text('\n'.join(body),encoding='utf-8')

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--module',default='student_search')
    parser.add_argument('--out',default='results')
    args=parser.parse_args();module=importlib.import_module(args.module)
    records=[]
    try:
        for name,reverse in [('Alpha-beta LTR',False),('Alpha-beta RTL',True)]:
            seen=[];v=module.alpha_beta(assessment_tree(),reverse=reverse,visited=seen)
            records.append(dict(name=name,root_value=v,evaluated_leaves=len(seen),leaf_order=seen))
        seen=[];v=module.expectimax(assessment_tree(chance=True),visited=seen)
        records.append(dict(name='Expectimax',root_value=v,evaluated_leaves=len(seen),leaf_order=seen))
    except NotImplementedError as exc:
        parser.exit(2,str(exc)+'\n')
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    (out/'results.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8')
    save_chart(records,out/'comparison.svg')
    print(json.dumps(records,indent=2))
    print('Saved',out/'results.json','and',out/'comparison.svg')

if __name__=='__main__':main()
