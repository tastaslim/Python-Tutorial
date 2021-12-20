import unittest

from src import main


class TestMain(unittest.TestCase):
    def test_main_success(self):
        self.assertEqual(main.do_stuff(2), 6)
        self.assertEqual(main.do_stuff(int('a')), 9)
        self.assertEqual(main.do_stuff(9.5), 13.5)

    # def test_main_failure(self):
    #     num1 = 10
    #     num2 = int('a')
    #     result = main.do_stuff(num1, num2)
    #     self.assertTrue(isinstance(result, ValueError))


if __name__ == '__main__':
    unittest.main()
