"""
Eventual Safe States

A directed graph of V vertices and E edges is given in the form of an adjacency list adj. Each node of the graph is
labelled with a distinct integer in the range 0 to V - 1.
A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from
that node leads to a terminal node.
You have to return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

Expected Time Complexity: O(V + E)
Expected Space Complexity: O(V)

Constraints:
1 <= V <= 104
0 <= E <= 104
The graph won't contain self loops.
Each node in the graph has a distinct value in the range 0 to V - 1.

"""
# User function Template for python3

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
    def eventual_safe_nodes(self, vertices: int, adjacency_list: List[List[int]]) -> List[int]:
        visited_array = [False for _ in range(vertices)]
        tracker_arr = [False for _ in range(vertices)]
        for root in range(vertices):
            if not visited_array[root]:
                self.__detect__(adjacency_list, visited_array, root, tracker_arr)
        return [i for i in range(len(tracker_arr)) if not tracker_arr[i]]


if __name__ == "__main__":
    T = int(input())
    for t in range(T):

        V, E = map(int, input().strip().split())
        adj = [[] for _ in range(V)]
        for _ in range(E):
            u, v = map(int, input().strip().split())
            adj[u].append(v)
        obj = Solution()
        ans = obj.eventual_safe_nodes(V, adj)
        for nodes in ans:
            print(nodes, end=' ')
        print()

# } Driver Code Ends
