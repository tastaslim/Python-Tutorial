def adjacency_matrix_to_adjacency_list(adjacency_matrix: list, vertices: int):
    adjacency_list = [[] for _ in range(vertices)]
    for index in range(vertices):
        for j in range(index):
            if adjacency_matrix[index][j] == 1 and index != j:
                adjacency_list[index].append(j)
                adjacency_list[j].append(index)
    return adjacency_list


def adjacency_list_to_adjacency_matrix(adjacency_list: list, vertices: int):
    adjacency_matrix = [[0] * vertices for _ in range(vertices)]

    for index in range(vertices):
        arr = adjacency_list[index]
        adjacency_matrix[index][index] = 1
        for ele in arr:
            adjacency_matrix[index][ele] = 1

    return adjacency_matrix


if __name__ == '__main__':
    t = 1  # int(input())
    for _ in range(t):
        # V = int(input())
        adj_matrix = [[1, 1, 1, 1], [1, 1, 0, 1], [1, 0, 1, 0], [1, 1, 0, 1]]

        # for i in range(V):
        #     temp = list(map(int, input().split()))
        #     adj_matrix.append(temp)
        ans = adjacency_matrix_to_adjacency_list(adjacency_matrix=adj_matrix, vertices=4)
        print(ans)
        print(adjacency_list_to_adjacency_matrix(adjacency_list=ans, vertices=4))
