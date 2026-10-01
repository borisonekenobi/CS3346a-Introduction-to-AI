"""Public practice tests. These are examples, not the entire marking suite."""
import unittest
from game_tree import Node, leaf
from student_search import alpha_beta, expectimax

class PracticeTests(unittest.TestCase):
    def test_terminal(self):
        seen=[]
        self.assertEqual(alpha_beta(leaf('x',-3),visited=seen),-3)
        self.assertEqual(seen,['x'])

    def test_max_min(self):
        tree=Node('root','MAX',(
            Node('left','MIN',(leaf('a',3),leaf('b',5))),
            Node('right','MIN',(leaf('c',2),leaf('d',9)))))
        seen=[]
        self.assertEqual(alpha_beta(tree,visited=seen),3)
        self.assertEqual(seen,['a','b','c'])

    def test_reverse(self):
        tree=Node('root','MAX',(
            Node('left','MIN',(leaf('a',3),leaf('b',5))),
            Node('right','MIN',(leaf('c',2),leaf('d',9)))))
        seen=[]
        self.assertEqual(alpha_beta(tree,reverse=True,visited=seen),3)
        self.assertEqual(seen,['d','c','b','a'])

    def test_weighted_chance(self):
        tree=Node('root','CHANCE',(leaf('a',-2),leaf('b',10)),
                  probabilities=(0.75,0.25))
        seen=[]
        self.assertAlmostEqual(expectimax(tree,seen),1)
        self.assertEqual(seen,['a','b'])

    def test_zero_probability_is_still_visited(self):
        tree=Node('root','CHANCE',(leaf('a',100),leaf('b',4)),
                  probabilities=(0,1))
        seen=[]
        self.assertEqual(expectimax(tree,seen),4)
        self.assertEqual(seen,['a','b'])

if __name__=='__main__':
    unittest.main()
