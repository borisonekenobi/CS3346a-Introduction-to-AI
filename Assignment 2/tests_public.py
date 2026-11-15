import unittest
from mdp import TableMDP
from student_algorithms import synchronous_sweep,q_learning_update

class PublicChecks(unittest.TestCase):
    def test_snapshot(self):
        mdp=TableMDP(('x','y','T'),{'x':{'go':[(1.,'y',0.)]},'y':{'exit':[(1.,'T',2.)]}},.5)
        old={'x':0.,'y':0.,'T':0.};new=synchronous_sweep(mdp,old)
        self.assertEqual(old,{'x':0.,'y':0.,'T':0.})
        self.assertEqual(new,{'x':0.,'y':2.,'T':0.})
    def test_terminal_target(self):
        q={('x','go'):2.,('T','bad'):100.}
        result=q_learning_update(q,'x','go',4.,'T',True,('bad',),.5,.9)
        self.assertAlmostEqual(result,3.)

if __name__=='__main__':unittest.main()
