from day12_debugging.testing.child_test import ChildTest


def guess_number(x):
    no_of_attempts = int(input("Enter maximum guess limit: "))
    a = int(input())
    while no_of_attempts != 0:
        if a > x:
            print("Too high")
        elif a < x:
            print("Too low")
        else:
            print(f"Congratulations, you guessed number {a}:{x} correctly")
        a = int(input())
        no_of_attempts -= 1


def main():
    print("Inside main")
    num = int(input("Enter number"))
    guess_number(num)


# main()

test = ChildTest("John", 28)
test.print_test()
