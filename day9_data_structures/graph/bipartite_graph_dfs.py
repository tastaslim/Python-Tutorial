"""
Given an adjacency list of a graph adj  of V no. of vertices having 0 based index. Check whether the graph is bipartite or not.


Example 1:

Input:

Output: 1
Explanation: The given graph can be colored
in two colors so, it is a bipartite graph.
Example 2:

Input:

Output: 0
Explanation: The given graph cannot be colored
in two colors such that color of adjacent
vertices differs.


Your Task:
You don't need to read or print anything. Your task is to complete the function isBipartite() which takes V denoting no. of vertices and adj denoting adjacency list of the graph and returns a boolean value true if the graph is bipartite otherwise returns false.


Expected Time Complexity: O(V + E)
Expected Space Complexity: O(V)

"""
from typing import List


# Strangely , The BFS solution gives TLE on GFG for last 20 odd cases but BFS passes. GFG is weirdo

class Solution:
    def __dfs__(self, adjacency_list: List[List[int]], root, color_array: List[int], color: int) -> bool:
        color_array[root] = color
        for ele in adjacency_list[root]:
            if color_array[ele] == color_array[root]:
                return False
            if color_array[ele] == -1:
                bipartite = self.__dfs__(adjacency_list, ele, color_array, 1 - color_array[root])
                if not bipartite:
                    return False
        return True

    def is_bipartite(self, vertices: int, adjacency_list: List[List[int]]) -> bool:
        color_array = [-1 for _ in range(vertices)]
        for index in range(vertices):
            if color_array[index] == -1:
                bipartite = self.__dfs__(adjacency_list, index, color_array, 0)
                if not bipartite:
                    return False
        return True


# {
# Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        V, E = map(int, input().strip().split())
        adj = [[] for _ in range(V)]
        for _ in range(E):
            u, v = map(int, input().strip().split())
            adj[u].append(v)
            adj[v].append(u)
        obj = Solution()
        ans = obj.is_bipartite(V, adj)
        if ans:
            print("1")
        else:
            print("0")
