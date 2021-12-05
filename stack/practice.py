from stack.stack import Stack


class Tree:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right


def levelWisePrint(root):
    if not root:
        return
    s = Stack()
    s.push(root)
    while not s.empty():
        front = s.top()
        s.pop()
        print(front.data)
        if front.left:
            s.push(front.left)
        if front.right:
            s.push(front.right)


def printData(root):
    if not root:
        return
    print(root.data, end=" ")
    printData(root.left)
    printData(root.right)


head = Tree(1)
child1 = Tree(2)
head.left = child1
child2 = Tree(3)
head.right = child2
# printData(head)
levelWisePrint(head)
