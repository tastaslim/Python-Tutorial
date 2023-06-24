"""
Given an undirected graph with V vertices and E edges, check whether it contains any cycle or not. Graph is in the form
of adjacency list where adj[i] contains all the nodes ith node is having edge with.

NOTE: The adjacency list denotes the edges of the graph where edges[i] stores all other vertices to which ith vertex is
connected.
"""

from typing import List


class Solution:
    def __detect__(self, vertices: int, adjacency_list: List[List[int]], visited_array: List[bool], root: int,
                   parent_node: int) -> bool:
        visited_array[root] = True
        for ele in adjacency_list[root]:
            if not visited_array[ele]:
                res = self.__detect__(vertices, adjacency_list, visited_array, ele, root)
                if res:
                    return True
            elif ele != parent_node:
                return True
        return False

    # Function to detect cycle in an undirected graph. Graph can be in form of multiple connected components
    def is_cycle(self, vertices: int, adjacency_list: List[List[int]]) -> bool:
        if len(adjacency_list) == 0:
            return False
        visited_array = [False for _ in range(vertices)]
        for root in range(vertices):
            if not visited_array[root]:
                ans1 = self.__detect__(vertices, adjacency_list, visited_array, root, -1)
                if ans1:
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
