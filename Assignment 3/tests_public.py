"""Visible checks on a toy fixture, not the assignment's answer key."""
import unittest
from a3_support import load_algorithms, NBModel, classify, choose_threshold

class PublicTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.alg = load_algorithms()

    def test_fit_toy(self):
        model = self.alg.fit_nb([[0], [1], [1]], [0, 1, 1])
        self.assertIsInstance(model, NBModel)
        self.assertAlmostEqual(model.priors[0], 1/3)
        self.assertAlmostEqual(model.priors[1], 2/3)
        self.assertAlmostEqual(model.p_one[0][0], 1/3)
        self.assertAlmostEqual(model.p_one[1][0], 3/4)

    def test_posterior_toy_present_and_absent(self):
        model = NBModel((1/3, 2/3), ((1/3,), (3/4,)))
        self.assertAlmostEqual(self.alg.posterior_one(model, [1]), 9/11)
        self.assertAlmostEqual(self.alg.posterior_one(model, [0]), 3/7)

    def test_provided_threshold_boundary_and_tie(self):
        self.assertEqual(classify(0.5, 0.5), 1)
        chosen, _ = choose_threshold([0, 1], [0.1, 0.9], [0.25, 0.75])
        self.assertEqual(chosen, 0.75)

if __name__ == '__main__':
    unittest.main()
