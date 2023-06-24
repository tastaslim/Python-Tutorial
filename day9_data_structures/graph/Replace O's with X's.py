"""
Given a matrix mat of size N x M where every element is either O or X.
Replace all O with X that are surrounded by X.
A O (or a set of O) is considered to be surrounded by X if there are X at locations just below, just above, just left
and just right of it.

Example 1:

Input: n = 5, m = 4
mat = {{'X', 'X', 'X', 'X'},
       {'X', 'O', 'X', 'X'},
       {'X', 'O', 'O', 'X'},
       {'X', 'O', 'X', 'X'},
       {'X', 'X', 'O', 'O'}}
Output: ans = {{'X', 'X', 'X', 'X'},
               {'X', 'X', 'X', 'X'},
               {'X', 'X', 'X', 'X'},
               {'X', 'X', 'X', 'X'},
               {'X', 'X', 'O', 'O'}}
Explanation: Following the rule the above
matrix is the resultant matrix.
Your Task:
You do not need to read input or print anything. Your task is to complete the function fill() which takes n, m and mat
as input parameters ad returns a 2D array representing the resultant matrix.

Expected Time Complexity: O(n*m)
Expected Auxiliary Space: O(n*m)

Constraints:
1 ≤ n, m ≤ 500
"""


class Solution:
    def __dfs__(self, visited, final_ans, root, row, col, rows, columns):
        visited[row][col] = True
        nodes_to_visit = [(row - 1, col), (row + 1, col), (row, col + 1), (row, col - 1)]
        for (temp_row, temp_col) in nodes_to_visit:
            if 0 <= temp_row < rows and 0 <= temp_col < columns and not visited[temp_row][temp_col] and \
                    final_ans[temp_row][temp_col] == 'o':
                self.__dfs__(visited, final_ans, root, temp_row, temp_col, rows, columns)

    def convert_o_with_x(self, grid: list):
        final_ans = [row[:] for row in grid]
        rows = len(grid)
        columns = len(grid[0])
        visited_arr = [[False for _ in range(columns)] for _ in range(rows)]
        for row in range(rows):
            for col in range(columns):
                if not visited_arr[row][col] and grid[row][col] == 'o' and (
                        row == rows - 1 or row == 0 or col == 0 or col == columns - 1):
                    self.__dfs__(visited_arr, final_ans, grid[row][col], row, col, rows, columns)
        for i in range(rows):
            for j in range(columns):
                if final_ans[i][j] == 'o' and not visited_arr[i][j]:
                    final_ans[i][j] = 'x'
        return final_ans


if __name__ == "__main__":
    obj = Solution()
    ques = [
        ['o', 'x', 'x', 'o'],
        ['x', 'o', 'o', 'x'],
        ['o', 'x', 'x', 'x']
    ]
    print(obj.convert_o_with_x(ques))
