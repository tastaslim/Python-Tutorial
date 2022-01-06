# import unittest
#
# from src import main
#
#
# class TestMain(unittest.TestCase):
#     def test_main_success(self):
#         self.assertEqual(main.do_stuff(2), 6)
#         self.assertNotEqual(main.do_stuff(8), 9)
#         self.assertEqual(main.do_stuff(9.5), 13.5)
#         self.assertRaises(TypeError, main.do_stuff, 'a')
#
#     # def test_main_failure(self):
#     #     num1 = 10
#     #     num2 = int('a')
#     #     result = main.do_stuff(num1, num2)
#     #     self.assertTrue(isinstance(result, ValueError))
#
#
# if __name__ == '__main__':
#     unittest.main()
# Given that num2>=num1
def count_elements(arr, num1, num2):
    count = 0
    for element in arr:
        if num1 <= element <= num2:
            count += 1
    return count


# Alternate Consecutive sum:  Basically question is to  find all even elements less than or equal to x
def count_happy_numbers(x):
    if x == 0:
        return 1
    ans = 0
    for i in range(0, x + 1):
        if i % 2 == 0:
            ans += 1
    return ans


# print(count_happy_numbers(4))


def rearrange_digits(num):
    arr = []
    while num != 0:
        rem = num % 10
        arr.append(rem)
        num //= 10
    arr.reverse()
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                return False
    return True


print(rearrange_digits(431))
