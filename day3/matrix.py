matrix = [
    [0, 1, 2, 3, 4],
    [5, 6, 7, 8, 9],
    [10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19]
]


def print_matrix_test(two_dimensional_arr) -> None:
    row = len(two_dimensional_arr)
    for i in range(row):
        col = len(two_dimensional_arr[i])
        for j in range(col):
            print(two_dimensional_arr[i][j], end=" ")
        print()


#
#
def print_matrix_1(two_dimension_arr):
    for arr in two_dimension_arr:
        for element in arr:
            print(element, end=" ") if element == 1 else print(end=" ")
        print()


#
#
def print_matrix(two_dimension_arr):
    for value in two_dimension_arr:
        print(value)


#
#
# # print_matrix(matrix)
#
#
def spiral_print(two_dimensional_arr):
    start_row, end_row = 0, len(two_dimensional_arr) - 1
    start_col, end_col = 0, len(two_dimensional_arr[0]) - 1
    while start_row <= end_row and start_col <= end_col:
        for i in range(start_col, end_col + 1):
            print(two_dimensional_arr[start_row][i], end=" ")
        start_row += 1
        for i in range(start_row, end_row + 1):
            print(two_dimensional_arr[i][end_col], end=" ")
        end_col -= 1
        if start_row <= end_row:
            for i in range(end_col, start_col - 1, -1):
                print(two_dimensional_arr[end_row][i], end=" ")
            end_row -= 1
        if start_col <= end_col:
            for i in range(end_row, start_row - 1, -1):
                print(two_dimensional_arr[i][start_col], end=" ")
            start_col += 1


if __name__ == "__main__":
    # spiral_print(matrix)
    # print_matrix_1(matrix)
    print_matrix_test(matrix)
#
# # 80C --> PPF 150k
# # Open PPF account
# # Mutual Funds
# # 80U --> Handicap
# # PF --> Employer contribution + Employee contribution
# # HRA --> CTC
# # 80E --> Education loan
# # NPS Account --> Pension Scheme
