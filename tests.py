import unittest
from src.slidingAlgorithm import slidingAlgorithm


class AlgoUnitTests(unittest.TestCase):
    def test_algo(self):
        """
        Use a list of values to make it clear that:
        Sliding avg of last 3 values should result in 0
        Full avg of all values would be <0
        Note: the code to use n, observed_value_list and the code
        to obtain observed_avg will depend on your implementation
        """
        n = 3
        observed_value_list = [-3, -2, -1, 0, 1]
        observed_avg = slidingAlgorithm(observed_value_list, n)

        # add code to obtain observed_avg
        self.assertAlmostEqual(0, observed_avg)

        # Example from the Spec
        n = 5
        observed_value_list = [39.4, 30.0, 66.2, 78.1, 55.9, 35.1]
        observed_avg = slidingAlgorithm(observed_value_list, n)

        # add code to obtain observed_avg
        self.assertAlmostEqual(53.06, observed_avg)

        # Example from the Spec and EDGE CASE
        n = 5
        observed_value_list = [31.0, 30.0]
        observed_avg = slidingAlgorithm(observed_value_list, n)

        # add code to obtain observed_avg
        self.assertAlmostEqual(30.5, observed_avg)


if __name__ == "__main__":
    unittest.main()
