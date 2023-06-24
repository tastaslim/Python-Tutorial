"""
Given a grid of size n*m (n is the number of rows and m is the number of columns in the grid) consisting of '0's (Water)
and '1's(Land). Find the number of islands.

Note: An island is either surrounded by water or boundary of grid and is formed by connecting adjacent lands
horizontally or vertically or diagonally i.e., in all 8 directions.

[[0,1,1,1,0,0,0], [0,0,1,1,0,1,0]]
"""
# User function Template for python3

import sys
from queue import Queue

sys.setrecursionlimit(10 ** 8)


class Solution:
    @staticmethod
    def __bfs__(grid: list, visited: list, grid_row: int, grid_col: int):
        n = len(grid)
        m = len(grid[grid_row])
        q = Queue()
        visited[grid_row][grid_col] = True
        q.put((grid_row, grid_col))
        while not q.empty():
            row, col = q.get()

            # top, bottom, left, right = (row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col)
            # dig_right_up, dig_right_down, dig_left_up, dig_left_down = (row + 1, col - 1), (row + 1, col + 1), (
            #     row - 1, col - 1), (row - 1, col + 1)

            adjacent_nodes = [(row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col), (row + 1, col - 1),
                              (row + 1, col + 1), (row - 1, col - 1), (row - 1, col + 1)]
            for traversal in adjacent_nodes:
                temp_row, temp_col = traversal
                if n > temp_row >= 0 and 0 <= temp_col < m and \
                        not visited[temp_row][temp_col] and grid[temp_row][temp_col] != 0:
                    q.put(traversal)
                    visited[temp_row][temp_col] = True

    def num_islands(self, grid: list) -> int:
        size_n, size_m = len(grid), len(grid[0])
        if not grid or size_n == 0:
            return 0
        visited = [[False for _ in range(size_m)] for _ in grid]

        count = 0
        for row in range(size_n):
            for col in range(size_m):
                if not visited[row][col] and grid[row][col] != 0:
                    self.__bfs__(grid, visited, row, col)
                    count = count + 1
        return count


if __name__ == "__main__":
    obj = Solution()
    print(obj.num_islands([[0, 1], [1, 0], [1, 1], [1, 0]]))
