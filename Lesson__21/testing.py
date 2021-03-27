# from main import sum_func
from main import num_is_palindrome
import unittest

#
# class TestSumFunc(unittest.TestCase):
#
#     def test_correct(self):
#         self.assertEqual(sum_func(5, 6), 11)
#
#     def test_str_a(self):
#         self.assertEqual(sum_func('5', 6), 11)
#
#     def test_str_all(self):
#         self.assertEqual(sum_func('5', '6'), 11)
#
#     def test_bool_true(self):
#         self.assertEqual(sum_func(5, True), False)
#
#     def test_bool_false(self):
#         self.assertEqual(sum_func(5, False), False)
#
#     def test_list(self):
#         self.assertEqual(sum_func(5, []), False)
#
#     def test_dict(self):
#         self.assertEqual(sum_func(5, {}), False)
#
#     def test_incorrect_str(self):
#         self.assertEqual(sum_func(5, 'khjasdfg'), False)


class TestNumIsPalindrome(unittest.TestCase):

    def test_1(self):
        self.assertEqual(num_is_palindrome(535), True)

    def test_2(self):
        self.assertEqual(num_is_palindrome(53), False)

    def test_3(self):
        self.assertEqual(num_is_palindrome(5), True)

    def test_4(self):
        self.assertEqual(num_is_palindrome(), True)

    def test_5(self):
        self.assertEqual(num_is_palindrome(5.5), True)

    def test_6(self):
        self.assertEqual(num_is_palindrome(5.53), False)

    def test_7(self):
        self.assertEqual(num_is_palindrome(12345678987654321), True)



if __name__ == '__main__':
    unittest.main()
