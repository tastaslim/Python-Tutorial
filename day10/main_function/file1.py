# Wrong  way
# def test(a: int, b: int) -> int:
#     return a + b
#
#
# print(test(1, 2))
# print(
#     f'filename is {__name__}')  # filename == __main__ if executed within this file but will be file1 when this file is
# # imported in another files and used there


# right way
def test(a: int, b: int) -> int:
    return a + b


if __name__ == '__main__':
    print(test(1, 2))
    print(__name__)
