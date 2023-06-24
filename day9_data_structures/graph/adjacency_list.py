class Graph:
    def __init__(self, vertices: int, edges: list):
        self.adjacency_list = [[] for _ in range(vertices)]
        for (source, destination) in edges:
            self.adjacency_list[source].append(destination)
            self.adjacency_list[destination].append(source)

    def has_node(self, n1, n2):
        return n2 in self.adjacency_list[n1]

    def print_list(self) -> None:
        for element in self.adjacency_list:
            print(element)


class WeightedGraph:
    def __init__(self, vertices: int, weighted_edges: list):
        self.adjacency_list = [[] for _ in range(vertices)]
        for (source, destination, w) in weighted_edges:
            self.adjacency_list[source].append([destination, w])
            self.adjacency_list[destination].append([source, w])

    def print_list(self) -> None:
        for element in self.adjacency_list:
            print(element)

    def has_node(self, n1, n2):
        return n2 in self.adjacency_list[n1[0]]


if __name__ == '__main__':
    n, m = int(input("Enter number of vertices: ")), int(input("Enter number of edges: "))
    edge_list = list()
    for i in range(0, m):
        node1, node2 = int(input("Enter node1: ")), int(input("Enter node2: "))
        edge_list.append((node1, node2))
    print(edge_list)
    arr = Graph(vertices=n, edges=edge_list)
    print(arr.adjacency_list)
    print(arr.has_node(0, 1))
    print(arr.has_node(0, 4))
    print(arr.has_node(1, 2))
    print(arr.has_node(2, 1))
    print(arr.has_node(0, 0))

    # ------------------ Weighted Graph ------------------------
    # edge_list = list()
    # for i in range(0, m):
    #     node1, node2, weight = int(input("Enter node1: ")), int(input("Enter node2: ")), int(input("Enter weight: "))
    #     edge_list.append((node1, node2, weight))
    # print(edge_list)
    #
    # arr = WeightedGraph(vertices=n, weighted_edges=edge_list)
    # print(arr.adjacency_list)

# class ConnectedComponents:
#     def __init__(self, vertices, edges):
#         self.visited = [False for _ in range(0, vertices)]
#         self.adjacency_list = [[] for _ in range(vertices)]
#         for (source, destination, w) in edges:
#             self.adjacency_list[source].append([destination, w])
#             self.adjacency_list[destination].append([source, w])
#
#     def traverse(self, node):
#         pass
#
#     def connected_components(self):
#         for arr in self.adjacency_list:
#             self.traverse()
