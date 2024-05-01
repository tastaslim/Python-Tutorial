from day9_data_structures.tree.templatetree import BinaryTree


def take_input() -> BinaryTree | None:
    value = int(input("Enter node data: "))
    if value == -1:
        return None
    root = BinaryTree(value)
