import unittest
from yandex_testing_lesson import reverse


class TestReverse(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverse(''), '')

    def test_list_type(self):
        with self.assertRaises(TypeError):
            reverse(["hi"])

    def test_int_type(self):
        with self.assertRaises(TypeError):
            reverse(1)

    def test_palindrome(self):
        self.assertEqual(reverse("hih"), "hih")

    def test_default(self):
        self.assertEqual(reverse("hello, friend"),
                         "dneirf ,olleh")


if __name__ == "__main__":
    unittest.main()
