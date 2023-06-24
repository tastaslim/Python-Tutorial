"""
There are a total of n tasks you have to pick, labeled from 0 to n-1. Some tasks may have prerequisites tasks, for
example to pick task 0 you have to first finish tasks 1, which is expressed as a pair: [0, 1]
Given the total number of n tasks and a list of prerequisite pairs of size m. Find an ordering of tasks you should pick
to finish all tasks.
Note: There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all tasks
, return an empty array. Returning any correct order will give the output as 1, whereas any invalid order will give the
output "No Ordering Possible".


Example 1:

Input:
n = 2, m = 1
prerequisites = {{1, 0}}
Output:
1
Explanation:
The output 1 denotes that the order is
valid. So, if you have, implemented
your function correctly, then output
would be 1 for all test cases.
One possible order is [0, 1].
Example 2:

Input:
n = 4, m = 4
prerequisites = {{1, 0},
                 {2, 0},
                 {3, 1},
                 {3, 2}}
Output:
1
Explanation:
There are a total of 4 tasks to pick.
To pick task 3 you should have finished
both tasks 1 and 2. Both tasks 1 and 2
should be picked after you finished task 0.
So one correct task order is [0, 1, 2, 3].
Another correct ordering is [0, 2, 1, 3].
Returning any of these order will result in
an Output of 1.

Your Task:
The task is to complete the function findOrder() which takes two integers n, and m and a list of lists of size m*2
denoting the prerequisite pairs as input and returns any correct order to finish all the tasks. Return an empty array if
it's impossible to finish all tasks.


Constraints:
1 ≤ n ≤ 104
0 ≤ m ≤ 105
0 ≤ prerequisites[i][0], prerequisites[i][1] ≤ 105
All prerequisite pairs are unique
prerequisites[i][0] ≠ prerequisites[i][1]

Expected Time Complexity: O(n+m).
Expected Auxiliary Space: O(n+m).
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
        if len(ans) != vertices:
            return []
        return ans

    def find_order(self, n2, m1, pre_req):
        adjacency_list = [[] for _ in range(n2)]
        for (node1, node2) in pre_req:
            adjacency_list[node2].append(node1)
        return self.topo_sort(adjacency_list, n2)


def check(graph, n1, res1):
    mp = [0] * n1
    for idx in range(n1):
        mp[res1[idx]] = i
    for index in range(n1):
        for vertex in graph[index]:
            if mp[index] > mp[vertex]:
                return False
    return True


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, m = list(map(int, input().strip().split()))
        adj = [[] for _ in range(n)]
        prerequisites = []

        for _ in range(m):
            u, v = map(int, input().split())
            adj[v].append(u)
            prerequisites.append([u, v])

        ob = Solution()

        res = ob.find_order(n, m, prerequisites)

        if not len(res):
            print("No Ordering Possible")
        else:
            if check(adj, n, res):
                print(1)
            else:
                print(0)
# } Driver Code Ends
