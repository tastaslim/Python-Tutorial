from typing import List


def in_degree_nodes(adjacency_list: List[List[int]]) -> List[int]:
    in_degree_arr = [0 for _ in adjacency_list]
    for element in adjacency_list:
        for node in element:
            in_degree_arr[node] += 1
    return in_degree_arr


if __name__ == '__main__':
    e, N = list(map(int, input().strip().split()))
    adj = [[] for _ in range(N)]
    for _ in range(e):
        u, v = map(int, input().split())
        adj[u].append(v)
    ans = in_degree_nodes(adjacency_list=adj)
    print(ans)
