import argparse,json
from pathlib import Path
from mdp import GridMDP,solve,display_rows
from student_algorithms import synchronous_sweep,q_learning_update
from experience import INITIAL_Q,Q_TRACE,AVAILABLE

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',default='results.json');args=ap.parse_args()
    results={}
    for living in [-.1,.5]:
        mdp=GridMDP(living=living)
        v,policy,history,delta,residual=solve(mdp,synchronous_sweep)
        name=f'living_{living}'
        results[name]={'sweeps':len(history)-1,'delta':delta,'residual':residual,
                       'error_bound':residual/(1-mdp.gamma),
                       'values':{str(s):x for s,x in v.items()},
                       'policy':{str(s):a for s,a in policy.items()},
                       'first_two_sweeps':[display_rows(mdp,h) for h in history[1:3]]}
        print(name,'sweeps',len(history)-1,'start',round(v[mdp.start],6),'action',policy[mdp.start])
    q=INITIAL_Q.copy();trace=[]
    for s,a,r,n,done in Q_TRACE:
        trace.append(q_learning_update(q,s,a,r,n,done,AVAILABLE[n],.5,.9))
    results['q_trace']=trace
    print('Q trace:',trace)
    Path(args.out).write_text(json.dumps(results,indent=2)+'\n')
    print('Wrote',args.out)

if __name__=='__main__':main()
