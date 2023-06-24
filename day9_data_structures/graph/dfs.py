class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.visited_array = [False for _ in range(vertices)]
        self.adjacency_list = [[] for _ in range(vertices)]
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


if __name__ == '__main__':
    n, m = int(input("Enter number of vertices: ")), int(input("Enter number of edges: "))
    edge_list = list()
    for i in range(0, m):
        node1, node2 = int(input("Enter node1: ")), int(input("Enter node2: "))
        edge_list.append((node1, node2))
    graph = Graph(vertices=n, edges=edge_list)
    graph.depth_first_search(0)
