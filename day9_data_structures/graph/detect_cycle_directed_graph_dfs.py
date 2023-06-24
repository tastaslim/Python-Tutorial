"""
Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not.
Your task:
You don't need to read input or print anything. Your task is to complete the function isCyclic() which takes the integer
V denoting the number of vertices and adjacency list as input parameters and returns a boolean value denoting if the
given directed graph contains a cycle or not.


Expected Time Complexity: O(V + E)
Expected Auxiliary Space: O(V)


Constraints:
1 ≤ V, E ≤ 105
"""
import sys
from typing import List

sys.setrecursionlimit(10 ** 6)


class Solution:
    def __detect__(self, adjacency_list: List[List[int]], visited_array: List[bool], root: int,
                   tracker_arr: List[int]) -> bool:
        visited_array[root] = True
        tracker_arr[root] = True
        for ele in adjacency_list[root]:
            if not visited_array[ele]:
                has_cycle = self.__detect__(adjacency_list, visited_array, ele, tracker_arr)
                if has_cycle:
                    return True
            elif tracker_arr[ele]:
                return True
        tracker_arr[root] = False
        return False

    # Function to detect cycle in a directed graph.
    def is_cyclic(self, vertices: int, adjacency_list: List[List[int]]):
        visited_array = [False for _ in range(vertices)]
        tracker_arr = [False for _ in range(vertices)]
        for root in range(vertices):
            if not visited_array[root]:
                self.__detect__(adjacency_list, visited_array, root, tracker_arr)
                # return True
        # return False
        print(tracker_arr)


# {
# Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V, E = list(map(int, input().strip().split()))
        adj = [[] for _ in range(V)]
        for _ in range(E):
            a, b = map(int, input().strip().split())
            adj[a].append(b)
        ob = Solution()

        if ob.is_cyclic(V, adj):
            print(1)
        else:
            print(0)
