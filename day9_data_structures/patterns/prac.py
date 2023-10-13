"""
*****
*****
*****
*****
*****
"""


def print_square(n: int) -> None:
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print('*', end="")
        print()


"""
*
**
***
****
*****
"""


def print_triangle(n: int) -> None:
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("*", end="")
        print()


"""
    *
   **
  ***
 ****
*****
"""


def print_triangle_back(n: int) -> None:
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j >= n + 1 - i:
                print("*", end="")
            else:
                print(end=" ")
        print()


"""
*****
****
***
**
*
"""


def print_triangle_inverted(n: int) -> None:
    for i in range(1, n + 1):
        for j in range(n + 1, i, -1):
            print("*", end="")
        print()


""""
*****
 ****
  ***
   **
    *
"""


def print_triangle_inverted_back(n: int) -> None:
    for i in range(1, n + 1):
        for j in range(n + 1, i, -1):
            print("*", end="")
        print()


def print_num(n: int) -> None:
    for i in range(1, n + 1):
        k = 1
        for j in range(1, 2 * n):
            if (n - i + 1) <= j <= (n + i - 1):
                print(k, end="")
                if j < n:
                    k = k + 1
                else:
                    k = k - 1
            else:
                print("", end=" ")
        print()


if __name__ == "__main__":
    # print_square(5)
    # print_triangle(5)
    # print_triangle_back(5)
    # print_triangle_inverted(5)
    print_num(4)
