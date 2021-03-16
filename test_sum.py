import unittest
import random
import string


class TestSum(unittest.TestCase):
    sumValue = 0

    def setUp(self):
        print("Printing setup method")
        self.sumValue = random.randint(2, 10)

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be six")
        res = ''.join(random.choices(string.ascii_uppercase +
                                     string.digits, k=7))
        print(res)

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 3)), 6, "Should be six")
        print(self.sumValue)


if __name__ == "__main__":
    unittest.main()
