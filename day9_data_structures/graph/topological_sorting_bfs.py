from queue import Queue
from typing import List

"""
Kahn's Algorithm:
1. Find InDegree of all vertices and save inside an array data structure (say in_degree_arr). 
2. Traverse through the in_degree_arr and put all vertices with InDegree 0 in a queue data structure.
3. Check adjacent vertices of current node and decrease their InDegree by 1 (As we have already
traversed the current node, so edge from current node to any adjacent node is taken care).
4. Check if InDegree of adjacent node is 0, if yes put it inside queue.
5. Repeat step 3 and 4 until queue is not empty (while not q.empty()).
"""


class Solution:
    @staticmethod
    def in_degree_nodes(adjacency_list: List[List[int]], vertices: int) -> List[int]:
        in_degree_arr = [0 for _ in range(vertices)]
        for element in adjacency_list:
            for node in element:
                in_degree_arr[node] += 1
        return in_degree_arr

    @staticmethod
    def __kahn_algorithm__(adjacency_list: List[List[int]], ans: List[int], in_degree_arr: List[int]):
        q = Queue()
        for index in range(len(in_degree_arr)):
            if in_degree_arr[index] == 0:
                q.put(index)
        while not q.empty():
            node = q.get()
            ans.append(node)
            for ele in adjacency_list[node]:
                in_degree_arr[ele] -= 1
                if in_degree_arr[ele] == 0:
                    q.put(ele)

    def topo_sort(self, adjacent: List[List[int]], vertices: int):
        in_degree_arr = self.in_degree_nodes(adjacent, vertices)
        ans = []
        self.__kahn_algorithm__(adjacent, ans, in_degree_arr)
        return ans


if __name__ == '__main__':
    e, N = list(map(int, input().strip().split()))
    adj = [[] for _ in range(N)]
    for _ in range(e):
        u, v = map(int, input().split())
        adj[u].append(v)
    s = Solution()
    s.topo_sort(adj, N)
