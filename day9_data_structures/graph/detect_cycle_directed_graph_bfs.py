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
from queue import Queue


class Solution:
    @staticmethod
    def in_degree_nodes(adjacency_list, vertices):
        in_degree_arr = [0 for _ in range(vertices)]
        for element in adjacency_list:
            for node in element:
                in_degree_arr[node] += 1
        return in_degree_arr

    @staticmethod
    def __kahn_algorithm__(adjacency_list, ans, in_degree_arr):
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

    def topo_sort(self, adjacent, vertices):
        in_degree_arr = self.in_degree_nodes(adjacent, vertices)
        ans = []
        self.__kahn_algorithm__(adjacent, ans, in_degree_arr)
        return ans

    """
    Since we know that Topological sorting is only valid for DAG (means no cycle). We will find topological sorting of 
    a given graph, if it contains cycle, we would not get valid topo sort and length of topo sorted array would be less
    than the count of vertices (which means if there is a cycle in the graph, topo sort would never return all elements)
    """

    def is_cyclic(self, vertices, adjacency_list):
        if len(self.topo_sort(adjacency_list, vertices)) != vertices:
            return True
        return False


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
# } Driver Code Ends
