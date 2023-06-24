# print(x)  # NameError: name 'x' is not defined

def divide(x: int) -> float:
    try:
        return 20 / x
    except ValueError as e:  # just except would also work, but it is good practice to use except Exception or
        # except some_specific_exception_type
        print(f"{x} is not allowed | Error occurred ({e})")  # handles x=0 case


# divide(0)  # it will give ZeroDivisionError for 0 without error handling but works for rest values


# hence, we must handle these errors.

# ------- Another case ----------------

def take_input():
    while True:
        # noinspection PyBroadException
        try:
            age = input("Enter your age: ")
            print(f"You are {int(age)} years old")
            break
        except Exception:
            print(f"Try again. Please make sure you are entering correct age.")


# take_input()

# Although we can perform extra operations once try is completing doing main functionality for correct input but
# Just wanted to show that there is another way too by using else. Else block will only run if except block is not
# running. Meaning try runs successfully.
def error_ins():
    while True:
        # noinspection PyBroadException
        try:
            x = int(input("Enter number: "))
            print(20 / x)
        except Exception:  # Here we can replace Exception with any specific type of error too like ValueError etc
            print("Try again. Please enter valid number")
        else:  # Enters this block if try runs successfully
            print("Thank you")
            break


# error_ins()


# ------ Some other cases --------------

def error_ins2():
    while True:
        # noinspection PyBroadException
        try:
            x = int(input("Enter number: "))
            print(20 / x)
        except ValueError:  # Now except block will only run when there is error af ValueError type. For other cases it
            # will ignore which can lead to termination of code.
            print("Try again. Please enter valid number")
        else:  # Enters this block if try runs successfully
            print("Thank you")
            break


# error_ins2()

# ----- We can also handle multiple error types in code using multiple exception blocks -----------

def function():
    while True:
        # noinspection PyBroadException
        item = ''
        try:
            item = int(input("Enter a number"))
            print((1 + item) / item)
        except ZeroDivisionError:
            print(f"Divided by {item} error. Please enter correct number")
        except ValueError:
            print("ValueError exception")
        else:
            print("Thank you")
            break


# function()

def demo():
    while True:
        # noinspection PyBroadException
        try:
            a = float(input("Enter weight: "))
            b = float(input("Enter height: "))
            print(a / b)
        except ZeroDivisionError as err:
            print(err)
        except ValueError as err:
            print(f"value error {err}")
        else:
            print("Complete")
            break
        finally:
            print("I will run irrespective of try, except or else")


# demo()


def testing(item):
    try:
        ans = 20 / item
        print(ans)
    except ZeroDivisionError as err:
        raise ZeroDivisionError(f"Please enter a number other than 0. {err} error")


testing(0)
