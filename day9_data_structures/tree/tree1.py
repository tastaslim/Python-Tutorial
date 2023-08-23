from collections import defaultdict
from queue import Queue


class BinaryTree:
    def __init__(self, data, left=None, right=None) -> None:
        self.data, self.left, self.right = data, left, right


# def take_input():
#     value = int(input("Enter data: "))
#     root = None
#     while value != -1:
#         newNode = BinaryTree(value)


def sum_of_leaf_nodes(root: BinaryTree) -> int:
    if not root:
        return 0
    q = Queue()
    sum = 0
    q.put(root)
    while not q.empty():
        front = q.get()
        if not front.left and not front.right:
            sum += front.data
        if front.left:
            q.put(front.left)
        if front.right:
            q.put(front.right)
        
    return sum


def print_tree(head):
    if not head:
        return
    print(head.data, end=" ")
    print_tree(head.left)
    print_tree(head.right)


def find_node(head, value):
    if not head:
        return head
    if head.data == value:
        return head
    find_node(head.left, value)
    find_node(head.right, value)


def level_wise_traversal(head: BinaryTree) -> None:
    if not head:
        return
    queue = [head]
    while len(queue) > 0:
        front = queue[0]
        queue.pop(0)
        print(front.data)
        if front.left:
            queue.append(front.left)
        if front.right:
            queue.append(front.right)


def iterative_preorder_traversal(head: BinaryTree) -> None:
    if not head:
        return
    stack = [head]
    while len(stack) > 0:
        pass


mp = defaultdict(list)


def action(head, distance):
    if not head:
        return
    mp[distance].append(head.data)
    action(head.left, distance + 1)
    action(head.right, distance + 1)


def vertical_order_traversal_helper(head: BinaryTree, distance: int, mp1) -> None:
    if not head:
        return
    mp1.setdefault(distance, []).append(head.data)
    left_view_helper(head.left, distance - 1, mp1)
    left_view_helper(head.right, distance + 1, mp1)


def vertical_order_traversal(head: BinaryTree) -> None:
    temp_map = {}
    vertical_order_traversal_helper(head, 0, temp_map)
    for key in sorted(temp_map.keys()):
        print(
            temp_map.get(key))  # print(temp_map[key]) does the job, but it is not recommended. Better to use .get(key)


"""
Left view of Binary tree
"""


def left_view_helper(head: BinaryTree, distance: int, mp1) -> None:
    if not head:
        return
    mp1.setdefault(distance, []).append(head.data)
    left_view_helper(head.left, distance + 1, mp1)
    left_view_helper(head.right, distance + 1, mp1)


def left_view(head: BinaryTree) -> None:
    temp_map = {}
    left_view_helper(head, 0, temp_map)
    for key in sorted(temp_map.keys()):
        print(temp_map.get(key)[
                  0])  # print(temp_map[key]) does the job, but it is not recommended. Better to use .get(key)


"""
 Right view 
"""


def right_view_helper(head: BinaryTree, distance: int, mp1: dict) -> None:
    if not head:
        return
    mp1.setdefault(distance, []).append(head.data)
    right_view_helper(head.left, distance + 1, mp1)
    right_view_helper(head.right, distance + 1, mp1)


def right_view(head: BinaryTree) -> None:
    temp_map = {}
    left_view_helper(head, 0, temp_map)
    for key in sorted(temp_map.keys()):
        lst = temp_map.get(key)
        print(lst[len(lst) - 1])
        # print(temp_map.get(key)[
        #           len(temp_map.get(
        #               key) - 1)])


"""s
LCA
"""


def lca(head: BinaryTree, node1: int, node2: int) -> BinaryTree:
    if not head:
        return head
    if head.data == node1 or head.data == node2:
        return head
    left_part = lca(head.left, node1, node2)
    right_part = lca(head.right, node1, node2)
    if left_part and right_part:
        return head
    if left_part:
        return left_part
    if right_part:
        return right_part


def lca1(head: BinaryTree, mp1: dict, prev) -> None:
    if not head:
        return
    mp1[head.data] = prev.data
    prev = head
    lca1(head.left, mp1, prev)
    lca1(head.right, mp1, prev)


def root_node_path(head: BinaryTree, node: int):
    prev = BinaryTree(-1)
    mp1 = {}
    lca1(head, mp1, prev)
    temp = mp1[node]
    print(node, end=" ")
    while temp != -1:
        print(temp, end=" ")
        temp = mp1[temp]


def search_node(arr: list, node: int) -> int:
    index = 0
    for element in arr:
        if element == node:
            return index
        index += 1
    return -1


def distance_between_two_nodes(head: BinaryTree, node1: int, node2: int):
    prev = BinaryTree(-1)
    mp1 = {}
    lca1(head, mp1, prev)
    lca_node = lca(head, node1, node2)
    lst1, lst2 = [], []
    temp = mp1[node1]
    lst1.append(node1)
    while temp != -1:
        lst1.append(temp)
        temp = mp1[temp]

    temp = mp1[node2]
    lst2.append(node2)
    while temp != -1:
        lst2.append(temp)
        temp = mp1[temp]
    print(lst1)
    print(lst2)
    data = lca_node.data
    index1 = search_node(lst1, data)
    index2 = search_node(lst2, data)
    return index1 - lst1.index(node1) + index2 - lst2.index(node2)


def iterative_inorder_traversal(head: BinaryTree) -> None:
    if not head:
        return
    arr = [head]
    while len(arr) != 0:
        top = arr[0]
        if not top.left:
            arr.pop(0)
            print(top.data, end=" ")
        if top.right:
            arr.insert(top.right, 0)
        if top.left:
            arr.insert(top.left, 0)


root = BinaryTree(1)
l1 = BinaryTree(2)
r1 = BinaryTree(3)
l2 = BinaryTree(4)
r2 = BinaryTree(5)
l3 = BinaryTree(6)
r3 = BinaryTree(7)

root.left, root.right = l1, r1
l1.left, l1.right = l2, None
r1.left, r1.right = l3, r2
r2.left, r2.right = r3, None

ans = sum_of_leaf_nodes(root)
print(ans)
# ans: BinaryTree = lca(root, 3, 1)
# print(ans.data)
# root_node_path(root, 7)
# print()
# root_node_path(root, 6)

# print(distance_between_two_nodes(root, 4, 6))
"""
            1
          /    \
         2        3 
        /  \     /  \ 
       4   91   6    5
                    /  
                   7  
      1 2 4 91 3 6 5 7
"""
# vertical_order_traversal(root)
# left_view(root)
# right_view(root)
# levelWise(root)

# action(root, 0)
# print(mp)
# level_wise_traversal(root)
