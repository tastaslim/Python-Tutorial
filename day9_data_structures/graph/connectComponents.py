class Graph:
    def __init__(self, vertices: int, edges: list):
        self.vertices = vertices
        self.visited_array = [False for _ in range(0, vertices)]
        self.adjacency_list = [[] for _ in range(0, vertices)]
        for (source, destination) in edges:
            self.adjacency_list[source].append(destination)
            self.adjacency_list[destination].append(source)

    def depth_first_search(self, root):
        if not self.adjacency_list or len(self.adjacency_list) == 0:
            return
        self.visited_array[root] = True
        print(root, end=' ')
        for ele in self.adjacency_list[root]:
            if not self.visited_array[ele]:
                self.depth_first_search(ele)

    def connected_components(self, vertices: int):
        for vertex in range(0, vertices):
            if not self.visited_array[vertex]:
                self.depth_first_search(vertex)
                print()


if __name__ == "__main__":
    n, m = int(input("Enter number of vertices: ")), int(input("Enter number of edges: "))
    edge_list = list()
    for i in range(0, m):
        node1, node2 = int(input("Enter source node: ")), int(input("Enter destination node: "))
        edge_list.append((node1, node2))
    graph = Graph(vertices=n, edges=edge_list)
    graph.connected_components(vertices=n)
