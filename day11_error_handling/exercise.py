"""
Find output of the code for below test cases:
1. When divided by 0 ==> age=0
2. Value error ==> age is not number

"""


def test():
    while True:
        # noinspection PyBroadException
        try:
            age = int(input("Enter your age: "))
            print(100 / age)
        except ValueError as err:
            print(err)
            continue
        except ZeroDivisionError as err:
            print(err)
            break
        else:
            print("Completed!!!")
        finally:
            print("I will run at any cost")

        print("Please respond")


# test()

"""
In the above, code raise an error instead of printing it. Now find output of code
"""


def test1():
    while True:
        # noinspection PyBroadException
        try:
            age = int(input("Enter your age: "))
            print(100 / age)
        except ValueError as err:
            raise ValueError(err)
        except ZeroDivisionError as err:
            raise ZeroDivisionError(err)
        else:
            print("Completed!!!")
        finally:
            print("I will run at any cost")

        print("Please respond")

# test1()
