def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


a = rev_str("hello")
print(next(a))  # Output: o
print(next(a))  # Output: l
print(next(a))  # Output: l
print(next(a))  # Output: e
print(next(a))  # Output: h
next(a)  # This will raise error (StopIteration) as no items are left.

for char in a:
    print(char)

# square each term using list comprehension
my_list = [1, 3, 6, 10]
list_ = [x ** 2 for x in my_list]

# same thing can be done using a generator expression
# generator expressions are surrounded by parenthesis ()
generator = (x ** 2 for x in my_list)


def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x + y
        yield x


def square(nums):
    for num in nums:
        yield num ** 2


print(sum(square(fibonacci_numbers(10))))
