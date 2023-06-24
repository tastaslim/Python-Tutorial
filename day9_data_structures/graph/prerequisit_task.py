"""
There are a total of N tasks, labeled from 0 to N-1. Some tasks may have prerequisites, for example to do task 0 you have to first complete task 1, which is expressed as a pair: [0, 1]
Given the total number of tasks N and a list of prerequisite pairs P, find if it is possible to finish all tasks.


Example 1:

Input:
N = 4, P = 3
prerequisites = {{1,0},{2,1},{3,2}}
Output:
Yes
Explanation:
To do task 1 you should have completed
task 0, and to do task 2 you should
have finished task 1, and to do task 3 you
should have finished task 2. So it is possible.


Example 2:

Input:
N = 2, P = 2
prerequisites = {{1,0},{0,1}}
Output:
No
Explanation:
To do task 1 you should have completed
task 0, and to do task 0 you should
have finished task 1. So it is impossible.

Your task:
You don’t need to read input or print anything. Your task is to complete the function isPossible() which takes the integer N denoting the number of tasks, P denoting the number of prerequisite pairs and prerequisite as input parameters and returns true if it is possible to finish all tasks otherwise returns false.


Expected Time Complexity: O(N + P)
Expected Auxiliary Space: O(N + P)


Constraints:
1 ≤ N ≤ 104
1 ≤ P ≤ 105

"""

from queue import Queue
from typing import List


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
        return len(ans) == vertices

    def is_possible(self, n, pre):
        adjacency_list = [[] for _ in range(n)]
        for (node1, node2) in pre:
            adjacency_list[node2].append(node1)
        return self.topo_sort(adjacency_list, n)


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        N = int(input())
        P = int(input())

        prerequisites = []
        for _ in range(P):
            pair = [int(x) for x in input().split()]
            prerequisites.append(pair)
        ob = Solution()
        if ob.is_possible(N, prerequisites):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends
