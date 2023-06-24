"""
Given a grid of dimension nxm where each cell in the grid can have values 0, 1 or 2 which has the following meaning:
0 : Empty cell
1 : Cells have fresh oranges
2 : Cells have rotten oranges

We have to determine what is the minimum time required to rot all oranges. A rotten orange at index [i,j] can rot other fresh orange at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] (up, down, left and right) in unit time.


Example 1:

Input: grid = {{0,1,2},{0,1,2},{2,1,1}}
Output: 1
Explanation: The grid is-
0 1 2
0 1 2
2 1 1
Oranges at positions (0,2), (1,2), (2,0)
will rot oranges at (0,1), (1,1), (2,2) and
(2,1) in unit time.
Example 2:

Input: grid = {{2,2,0,1}}
Output: -1
Explanation: The grid is-
2 2 0 1
Oranges at (0,0) and (0,1) can't rot orange at
(0,3).


Your Task:
You don't need to read or print anything, Your task is to complete the function orangesRotting() which takes grid as input parameter and returns the minimum time to rot all the fresh oranges. If not possible returns -1.


Expected Time Complexity: O(n*m)
Expected Auxiliary Space: O(n*m)
"""
import sys
from queue import Queue

sys.setrecursionlimit(10 ** 8)


class Solution:
    @staticmethod
    def __bfs__(grid: list, visited: list, final_ans: list) -> list:
        n = len(grid)
        m = len(grid[0])
        q = Queue()
        for i in range(n):
            for j in range(m):
                if final_ans[i][j] == 2:
                    q.put((i, j))
                    visited[i][j] = True
                    final_ans[i][j] = (final_ans[i][j], 0)
                else:
                    final_ans[i][j] = (final_ans[i][j], -1)
        while not q.empty():
            row, col = q.get()
            adjacent = [(row - 1, col), (row + 1, col), (row, col + 1), (row, col - 1)]
            for (temp_row, temp_col) in adjacent:
                if n > temp_row >= 0 and 0 <= temp_col < m and grid[temp_row][temp_col] == 1 and \
                        not visited[temp_row][temp_col]:
                    q.put((temp_row, temp_col))
                    final_ans[temp_row][temp_col] = (2, final_ans[row][col][1] + 1)
                    visited[temp_row][temp_col] = True
        return final_ans

    def rotten_oranges(self, grid: list) -> int:
        final_ans = [row[:] for row in grid]  # you can also use deepcopy(grid) to copy matrix elements.
        # final_ans = grid ==> Here final_ans variable will have reference to same address as in grid and changing
        # values in final_ans will change values in grid.
        visited_arr = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        ans = self.__bfs__(grid, visited_arr, final_ans)
        min_step = - sys.maxsize
        for arr in ans:
            for ele in arr:
                element, distance = ele
                if element == 1:
                    return distance
                min_step = max(min_step, distance)
        return min_step


if __name__ == "__main__":
    obj = Solution()
    ques = [[2, 1, 1, 1, 2, 1, 2, 0, 2],
            [1, 2, 1, 1, 2, 1, 1, 2, 2],
            [2, 2, 1, 2, 2, 1, 1, 2, 1],
            [1, 0, 2, 0, 1, 2, 2, 1, 0],
            [2, 0, 0, 2, 2, 2, 2, 0, 2],
            [2, 1, 1, 1, 2, 0, 2, 1, 2],
            [2, 2, 1, 1, 0, 0, 1, 2, 2],
            [0, 2, 0, 2, 2, 2, 2, 2, 1],
            [2, 0, 2, 0, 1, 2, 2, 2, 2],
            [1, 1, 1, 2, 0, 1, 2, 2, 2]]
    print(obj.rotten_oranges(ques))
