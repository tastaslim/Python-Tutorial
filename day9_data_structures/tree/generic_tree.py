from queue import Queue


class GenericTree:
    def __init__(self, data: int) -> None:
        self.data = data
        self.children = []


def takeInput() -> GenericTree:
    value = int(input("Enter node data: "))
    root = GenericTree(value)
    numberOfChildren = int(input("Enter number of children: "))
    for i in range(numberOfChildren):
        children = takeInput()
        root.children.append(children)
    return root


def takeInputLevelWise() -> GenericTree:
    q = Queue()
    value = int(input("Enter root data: "))
    root = GenericTree(value)
    q.put(root)
    while not q.empty():
        front = q.get()
        numberOfChildren = int(input("Enter number of children: "))
        for i in range(numberOfChildren):
            value = int(input(f"Enter children{i} data: "))
            child = GenericTree(value)
            front.children.append(child)
            q.put(child)
    return root


def printNodes(root: GenericTree, parentNode: GenericTree | None) -> None:
    if not root:
        return
    print(f"{root.data} : {parentNode.data if parentNode else None}")
    for element in root.children:
        printNodes(element, root)


def printNodesLevelWise(root: GenericTree) -> None:
    if not root:
        return
    q = Queue()
    q.put(root)
    while not q.empty():
        front = q.get()
        print(front.data)
        for element in front.children:
            q.put(element)


if __name__ == "__main__":
    head = takeInputLevelWise()
    printNodesLevelWise(head)
