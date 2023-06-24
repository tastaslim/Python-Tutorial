"""

"""

from queue import Queue


class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.adjacency_list = [[] for _ in range(0, vertices)]
        for (source, destination) in edges:
            self.adjacency_list[source].append(destination)
            self.adjacency_list[destination].append(source)

    def breath_first_search(self, root):
        if not self.adjacency_list or len(self.adjacency_list) == 0:
            return
        q = Queue()
        visited_array = [False for _ in range(0, self.vertices)]
        visited_array[root] = True
        q.put(root)
        while not q.empty():
            front = q.get()
            print(front)
            for ele in self.adjacency_list[front]:
                if not visited_array[ele]:
                    q.put(ele)
                    visited_array[ele] = True


if __name__ == '__main__':
    n, m = int(input("Enter number of vertices: ")), int(input("Enter number of edges: "))
    edge_list = list()
    for i in range(0, m):
        node1, node2 = int(input("Enter node1: ")), int(input("Enter node2: "))
        edge_list.append((node1, node2))
    graph = Graph(vertices=n, edges=edge_list)
    graph.breath_first_search(1)
