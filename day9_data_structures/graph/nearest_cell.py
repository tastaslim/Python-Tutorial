"""
Distance of nearest cell having 1
Given a binary grid of n*m. Find the distance of the nearest 1 in the grid for each cell.
The distance is calculated as |i1  - i2| + |j1 - j2|, where i1, j1 are the row number and column number of the current
cell, and i2, j2 are the row number and column number of the nearest cell having value 1. There should be at least one
1 in the grid.

Input: grid = {{0,1,1,0},{1,1,0,0},{0,0,1,1}}
Output: {{1,0,0,1},{0,0,1,1},{1,1,0,0}}
Explanation: The grid is-
0 1 1 0
1 1 0 0
0 0 1 1
0's at (0,0), (0,3), (1,2), (1,3), (2,0) and
(2,1) are at a distance of 1 from 1's at (0,1),
(0,2), (0,2), (2,3), (1,0) and (1,1)
respectively.

Output:
[
[1, 0, 0, 1]
[0, 0, 1, 1]
[1, 1, 0, 0]
]



Input: grid = {{1,0,1},{1,1,0},{1,0,0}}
Output: {{0,1,0},{0,0,1},{0,1,2}}
Explanation: The grid is-
1 0 1
1 1 0
1 0 0
0's at (0,1), (1,2), (2,1) and (2,2) are at a
distance of 1, 1, 1 and 2 from 1's at (0,0),
(0,2), (2,0) and (1,1) respectively.

Output:
[
[0, 1, 0]
[0, 0, 1]
[0, 1, 2]
]

"""

from queue import Queue
from typing import List


class Solution:
    @staticmethod
    def __bfs__(visited: List[List[int]], final_ans: List[List[int]], rows: int, columns: int):

        q = Queue()
        for i in range(rows):
            for j in range(columns):
                if final_ans[i][j] == 1:
                    final_ans[i][j] = 0
                    q.put((i, j, 0))
                    visited[i][j] = True
                else:
                    final_ans[i][j] = -1

        while not q.empty():
            row, col, count = q.get()
            adjacent = [(row - 1, col), (row + 1, col), (row, col + 1), (row, col - 1)]
            for (temp_row, temp_col) in adjacent:
                if rows > temp_row >= 0 and 0 <= temp_col < columns and not visited[temp_row][temp_col]:
                    final_ans[temp_row][temp_col] = count + 1
                    q.put((temp_row, temp_col, count + 1))
                    visited[temp_row][temp_col] = True

    def nearest_cell(self, grid: list) -> List[List[int]]:
        final_ans = [row[:] for row in grid]
        rows = len(grid)
        columns = len(grid[0])
        visited_arr = [[False for _ in range(columns)] for _ in range(rows)]
        self.__bfs__(visited_arr, final_ans, rows, columns)
        return final_ans


if __name__ == "__main__":
    obj = Solution()
    ques = [
        [0, 1, 1, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 1]
    ]
    print(obj.nearest_cell(ques))
