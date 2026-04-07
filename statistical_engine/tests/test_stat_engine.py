import unittest
from src.stat_engine import StatEngine


class TestStatEngine(unittest.TestCase):

    def test_mean_even(self):
        engine = StatEngine([2, 4, 6, 8])
        self.assertEqual(engine.get_mean(), 5)

    def test_median_odd(self):
        engine = StatEngine([3, 1, 2])
        self.assertEqual(engine.get_median(), 2)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            StatEngine([])

    def test_std_known(self):
        engine = StatEngine([2, 4, 4, 4, 5, 5, 7, 9])
        self.assertAlmostEqual(engine.get_variance(is_sample=False), 4, places=5)


if __name__ == "__main__":
    unittest.main()