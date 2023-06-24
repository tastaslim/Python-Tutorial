class GenericTree:
    def __init__(self, data: int):
        self.data = data
        self.children = []


def take_input() -> GenericTree:
    root_data = int(input("Enter data: "))
    root = GenericTree(root_data)
    num_child = int(input(f"Enter number of children of node{root.data}: "))
    for i in range(num_child):
        child = take_input()
        root.children.append(child)
    return root


def print_node(root: GenericTree, maxima) -> int:
    if not root:
        return -1
    for i in range(0, len(root.children)):
        maxima = max(maxima, root.children[i].data)
        print_node(root.children[i], maxima)
    return maxima


def find_max(root: GenericTree, maxima) -> int:
    if not root:
        return -1
    for i in range(0, len(root.children)):
        maxima = max(maxima, root.children[i].data)
        find_max(root.children[i], maxima)
    return maxima


head = take_input()
ans = print_node(head, head.data)
print(ans)
