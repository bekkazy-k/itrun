from main import sum_func
import unittest


class TestSumFunc(unittest.TestCase):

    def test_correct(self):
        self.assertEqual(sum_func(5, 6), 11)

    def test_str_a(self):
        self.assertEqual(sum_func('5', 6), 11)

    def test_str_all(self):
        self.assertEqual(sum_func('5', '6'), 11)

    def test_bool_true(self):
        self.assertEqual(sum_func(5, True), False)

    def test_bool_false(self):
        self.assertEqual(sum_func(5, False), False)

    def test_list(self):
        self.assertEqual(sum_func(5, []), False)

    def test_dict(self):
        self.assertEqual(sum_func(5, {}), False)


if __name__ == '__main__':
    unittest.main()
