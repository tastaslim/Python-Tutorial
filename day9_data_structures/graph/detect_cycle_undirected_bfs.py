"""
Given an undirected graph with V vertices and E edges, check whether it contains any cycle or not. Graph is in the form
of adjacency list where adj[i] contains all the nodes ith node is having edge with.

NOTE: The adjacency list denotes the edges of the graph where edges[i] stores all other vertices to which ith vertex is
connected.
"""

from queue import Queue
from typing import List


class Solution:
    @staticmethod
    def __detect__(vertices: int, adjacency_list: List[List[int]], visited_array: List[bool], root: int):
        if vertices == 0:
            return False
        q = Queue()
        visited_array[root] = True
        q.put((root, -1))
        while not q.empty():
            node, parent = q.get()
            for ele in adjacency_list[node]:
                if not visited_array[ele]:
                    q.put((ele, node))
                    visited_array[ele] = True
                elif ele != parent:
                    return True
        return False

    # Function to detect cycle in an undirected graph.
    def is_cycle(self, vertices: int, adjacency_list: List[List[int]]) -> bool:
        if len(adjacency_list) == 0:
            return False
        visited_array = [False for _ in range(vertices)]
        for root in range(vertices):
            if not visited_array[root]:
                if self.__detect__(vertices, adjacency_list, visited_array, root):
                    return True
        return False


# {
# Driver Code Starts
if __name__ == '__main__':

    T = int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for _ in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        obj = Solution()
        ans = obj.is_cycle(V, adj)
        if ans:
            print("1")
        else:
            print("0")

# } Driver Code Ends
