"""Provided data model and assessment trees. Do not edit for your submission."""
from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class Node:
    name: str
    kind: str
    children: tuple = ()
    utility: Optional[float] = None
    probabilities: tuple = ()

def leaf(name, utility):
    return Node(name, 'LEAF', utility=float(utility))

def record_leaf(node, visited):
    if visited is not None:
        visited.append(node.name)
    return node.utility

def assessment_tree(chance=False):
    rows = [('L1',(4,7)), ('L2',(3,15)), ('M1',(2,6)),
            ('M2',(9,5)), ('R1',(1,10)), ('R2',(8,9))]
    lower = {name: Node(name, 'MAX', tuple(
        leaf(name+suffix, value) for suffix,value in zip(('a','b'),values)))
        for name,values in rows}
    probs = {'L':(0.4,0.6), 'M':(0.25,0.75), 'R':(0.8,0.2)}
    upper = tuple(Node(name, 'CHANCE' if chance else 'MIN',
                       (lower[name+'1'],lower[name+'2']),
                       probabilities=probs[name] if chance else ())
                  for name in ('L','M','R'))
    return Node('ROOT','MAX',upper)
