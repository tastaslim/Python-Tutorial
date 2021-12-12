from time import time


def performance(your_function):
    def some_function(*args, **kwargs):
        start = time()
        your_function(*args, **kwargs)
        end = time()
        print(f"It took {end - start} seconds to execute")

    return some_function


@performance
def func() -> None:
    for i in range(10000000):
        print(2)


# func()  # takes nearly 14 seconds to complete its execution
# print(args["string"])  # error because tuple indices must be int (args it tuple, kwargs is dictionary)

"""
Create an @authenticated decorator that only allows the function to run if user has 'valid' set to True:
"""


def authentication(your_function):
    def some_function(user):
        your_function(user) if user["valid"] else print(f"Invalid username {user['name']}.")

    return some_function


@authentication
def my_func(user) -> None:
    print(f"User information : {user}")


user1 = {
    'name': 'Sorna',
    'valid': True  # changing this will either run or not run the message_friends function.
}
my_func(user1)
