from main import sum_func
import unittest


class TestSumFunc(unittest.TestCase):

    def test_correct(self):
        self.assertEqual(sum_func(5, 6), 11)

    def test_str_a(self):
        self.assertEqual(sum_func('5', 6), 11)

    def test_str_all(self):
        self.assertEqual(sum_func('5', '6'), 11)


if __name__ == '__main__':
    unittest.main()
