"""
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image.

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value
newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel
of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same
color as the starting pixel), and so on. Replace the color of all the aforementioned pixels with the newColor.

Example 1:

Input: image = {{1,1,1},{1,1,0},{1,0,1}},
sr = 1, sc = 1, newColor = 2.
Output: {{2,2,2},{2,2,0},{2,0,1}}
Explanation: From the center of the image
(with position (sr, sc) = (1, 1)), all
pixels connected by a path of the same color
as the starting pixel are colored with the new
color.Note the bottom corner is not colored 2,
because it is not 4-directionally connected to
the starting pixel.


Your Task:
You don't need to read or print anything. Your task is to complete the function floodFill() which takes image, sr, sc
and newColor as input parameter and returns the image after flood filling.


Expected Time Complexity: O(n*m)
Expected Space Complexity: O(n*m)

"""
# User function Template for python3

import sys
from queue import Queue

sys.setrecursionlimit(10 ** 8)


class Solution:
    @staticmethod
    def __bfs__(grid: list, visited: list, grid_row: int, grid_col: int, final_ans: list, fill_color):
        n = len(grid)
        m = len(grid[grid_row])
        q = Queue()
        num = grid[grid_row][grid_col]
        visited[grid_row][grid_col] = True
        final_ans[grid_row][grid_col] = fill_color
        q.put((grid_row, grid_col))
        while not q.empty():
            row1, col1 = q.get()

            # top, bottom, left, right = (row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col)
            adjacent_nodes = [(row1, col1 - 1), (row1, col1 + 1), (row1 - 1, col1), (row1 + 1, col1)]
            for traversal in adjacent_nodes:
                temp_row, temp_col = traversal
                if n > temp_row >= 0 and 0 <= temp_col < m and \
                        not visited[temp_row][temp_col] and grid[temp_row][temp_col] == num:
                    q.put(traversal)
                    visited[temp_row][temp_col] = True
                    final_ans[temp_row][temp_col] = fill_color

    def flood_fill(self, grid: list, start_row: int, start_col: int, fill_color: int) -> list:
        final_ans = grid
        visited_arr = []
        for ele in grid:
            temp = []
            for j in range(len(ele)):
                temp.append(False)
            visited_arr.append(temp)

        self.__bfs__(grid, visited_arr, start_row, start_col, final_ans, fill_color)
        return final_ans


if __name__ == "__main__":
    obj = Solution()
    ques = [[2, 1, 2, 1, 3], [2, 3, 3, 3, 2], [2, 3, 1, 3, 2], [1, 2, 3, 2, 2]]
    row, col, color = (1, 1, 8)
    print(obj.flood_fill(ques, row, col, color))
