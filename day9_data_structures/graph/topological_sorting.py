"""
Given a Directed Acyclic Graph (DAG) with V vertices and E edges, Find any Topological Sorting of that Graph.
Your Task:
You don't need to read input or print anything. Your task is to complete the function topoSort()  which takes the
integer V denoting the number of vertices and adjacency list as input parameters and returns an array consisting of the
vertices in Topological order. As there are multiple Topological orders possible, you may return any of them.

If your returned topo sort is correct then console output will be 1 else 0.
Expected Time Complexity: O(V + E).
Expected Auxiliary Space: O(V).


Constraints:
2 ≤ V ≤ 104
1 ≤ E ≤ (N*(N-1))/2
"""

import sys
from queue import LifoQueue

sys.setrecursionlimit(10 ** 6)

"""
Topo Sort is only valid for DAG and contains same number of elements as number of vertices.

Topological sorting is a sorting algorithm that is used to order nodes in a directed acyclic graph (DAG) such that for 
every directed edge from node A to node B, node A appears before node B in the ordering. In other words, it is a way to 
linearly order the vertices of a DAG so that for every directed edge (u, v), vertex u comes before vertex v in the 
ordering.
There can be multiple topo Topological sorting
Topological sorting has many practical applications, such as in scheduling tasks in a project management system, 
determining the order of compilation tasks in a software build system, and in dependency resolution in package managers.
"""


class Solution:
    def __dfs__(self, adjacency_list, visited, root, stk):
        visited[root] = True
        for ele in adjacency_list[root]:
            if not visited[ele]:
                self.__dfs__(adjacency_list, visited, ele, stk)
        stk.put(root)

    def topo_sort(self, vertices, adjacent):
        s = LifoQueue()
        visited = [False for _ in range(vertices)]
        for root in range(vertices):
            if not visited[root]:
                self.__dfs__(adjacent, visited, root, s)
        ans = []
        while not s.empty():
            ans.append(s.get())
        return ans


def check(graph, n, response):
    if n != len(res):
        return False
    mp = [0] * n
    for index in range(n):
        mp[response[index]] = index
    for j in range(n):
        for ver in graph[j]:
            if mp[j] > mp[ver]:
                return False
    return True


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        e, N = list(map(int, input().strip().split()))
        adj = [[] for _ in range(N)]
        for _ in range(e):
            u, v = map(int, input().split())
            adj[u].append(v)

        ob = Solution()
        res = ob.topo_sort(N, adj)
        print(res)
        print(1) if check(adj, N, res) else print(0)
