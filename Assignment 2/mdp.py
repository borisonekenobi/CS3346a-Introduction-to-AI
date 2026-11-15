"""Provided environment and reporting helpers. Python 3.10+. No packages needed."""
from dataclasses import dataclass
from collections import defaultdict

ACTIONS=('Up','Down','Left','Right')
DELTAS={'Up':(-1,0),'Down':(1,0),'Left':(0,-1),'Right':(0,1)}
SIDE={'Up':('Left','Right'),'Down':('Right','Left'),
      'Left':('Down','Up'),'Right':('Up','Down')}

@dataclass(frozen=True)
class GridMDP:
    gamma: float=.85
    living: float=-.1
    rows: int=3
    cols: int=3
    wall: tuple=(2,2)
    goal: tuple=(1,3)
    pit: tuple=(3,2)
    start: tuple=(3,1)

    @property
    def states(self):
        return tuple((r,c) for r in range(1,self.rows+1)
                     for c in range(1,self.cols+1) if (r,c)!=self.wall)

    def actions(self,s):
        return () if s in (self.goal,self.pit) else ACTIONS

    def move(self,s,a):
        dr,dc=DELTAS[a]; n=(s[0]+dr,s[1]+dc)
        return n if n in self.states else s

    def transitions(self,s,a):
        if a not in self.actions(s): raise ValueError('Unavailable action')
        probs=defaultdict(float)
        for prob,d in zip((.7,.15,.15),(a,*SIDE[a])): probs[self.move(s,d)]+=prob
        return tuple((prob,n,3. if n==self.goal else -2. if n==self.pit else self.living)
                     for n,prob in sorted(probs.items()))

class TableMDP:
    def __init__(self,states,kernel,gamma):
        self.states=tuple(states);self.kernel=kernel;self.gamma=gamma
    def actions(self,s): return tuple(self.kernel.get(s,{}))
    def transitions(self,s,a): return tuple(self.kernel[s][a])

def q_value(mdp,values,s,a):
    return sum(p*(r+mdp.gamma*values[n]) for p,n,r in mdp.transitions(s,a))

def greedy_policy(mdp,values):
    """Stable order: differences below 1e-12 count as ties."""
    policy={}
    for s in mdp.states:
        if not mdp.actions(s): continue
        qs={a:q_value(mdp,values,s,a) for a in mdp.actions(s)}
        best=max(qs.values())
        policy[s]=next(a for a in mdp.actions(s) if qs[a]>=best-1e-12)
    return policy

def solve(mdp,sweep,tol=1e-6,max_sweeps=10000):
    values={s:0. for s in mdp.states}
    history=[values.copy()]
    for k in range(1,max_sweeps+1):
        new=sweep(mdp,values)
        delta=max(abs(new[s]-values[s]) for s in mdp.states)
        history.append(new.copy());values=new
        if delta<tol:
            residual=max(abs(sweep(mdp,values)[s]-values[s]) for s in mdp.states)
            return values,greedy_policy(mdp,values),history,delta,residual
    raise RuntimeError('Did not converge within max_sweeps')

def display_rows(mdp,values,policy=None):
    return [[('Wall' if (r,c)==mdp.wall else
              'G value 0' if (r,c)==mdp.goal else
              'P value 0' if (r,c)==mdp.pit else
              f'{values[(r,c)]:.6f}'+(f' {policy[(r,c)]}' if policy else ''))
             for c in range(1,mdp.cols+1)] for r in range(1,mdp.rows+1)]
