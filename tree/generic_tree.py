class GenericTree:
    def __init__(self, data: int):
        self.data = data
        self.children = []


def take_input() -> GenericTree:
    root_data = int(input("Enter data: "))
    root = GenericTree(root_data)
    num_child = int(input(f"Enter number of children of node{root.data}: "))
    index = 0
    for i in range(num_child):
        child = take_input()
        root.children.append(child)
    return root


def print_node(root: GenericTree) -> None:
    if not root:
        return
    print(root.data)
    for i in range(0, len(root.children)):
        print_node(root.children)


head = take_input()
print_node(head)
