class LinkedList:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


def take_input() -> LinkedList:
    data = int(input("Enter node data: "))
    head, tail = None, None
    while data != -1:
        new_node = LinkedList(data)
        if not head:
            head, tail = new_node, new_node
        else:
            tail.next_node = new_node
            tail = tail.next_node
        data = int(input("Enter node data: "))
    return head


def print_node(head: LinkedList) -> None:
    if not head:
        return
    print(head.data, end=" ")
    print_node(head.next_node)


def insert_node(head: LinkedList, value: int, pos: int) -> LinkedList:
    if not head or pos < 0:
        return head
    if pos == 0:
        new_node = LinkedList(value)
        new_node.next_node = head
        head = new_node
        return head

    temp, prev = head, head
    count = 0
    while count < pos and temp:
        prev = temp
        temp = temp.next_node
        count += 1
    if temp or count == pos:
        new_node = LinkedList(value)
        prev.next_node = new_node
        new_node.next_node = temp
    return head


def insert_node_recursive(head: LinkedList, value: int, pos: int) -> LinkedList:
    if not head:
        if pos == 0:
            new_node = LinkedList(value)
            new_node.next_node = head
            head = new_node
            return head
        else:
            return head
    if pos == 0:
        new_node = LinkedList(value)
        new_node.next_node = head
        head = new_node
        return head
    recursion_part = insert_node_recursive(head.next_node, value, pos - 1)
    head.next_node = recursion_part
    return head


def delete_node(head: LinkedList, pos: int) -> LinkedList:
    if not head or pos < 0:
        return head
    if pos == 0:
        head = head.next_node
        return head

    temp, prev, count = head, None, 0
    while count < pos and temp:
        prev = temp
        temp = temp.next_node
        count += 1
    if temp or count == pos:
        if temp:
            prev.next_node = temp.next_node
        else:
            prev.next_node = temp
    return head


def length_list(head: LinkedList) -> int:
    if not head:
        return 0
    return 1 + length_list(head.next_node)


def find_node(head: LinkedList, value: int) -> bool:
    if not head:
        return False
    if head.data == value:
        return True
    return find_node(head.next_node, value)


def delete_node_recursive(head: LinkedList, pos: int) -> LinkedList:
    if not head:
        return head
    if pos == 0:
        head = head.next_node
        return head
    recursion_part = delete_node_recursive(head.next_node, pos - 1)
    head.next_node = recursion_part
    return head


def reverse_list_recursive(head: LinkedList):
    if not head.next_node:
        return head
    temp = reverse_list_recursive(head.next_node)
    temp1 = head.next_node
    temp1.next_node = head.next_node = None
    head = temp
    return head


def reverse_list(root):
    if not root:
        return root
    prev, current, next_node = None, root, None
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    root = prev
    return root


def next_larger_nodes(head):
    if not head:
        return head
    head = reverse_list(head)
    # print_node(head)
    max_val = head.val
    head.val = 0
    temp = head.next
    while temp:
        if max_val > temp.val:
            temp.val = max_val
        else:
            max_val = temp.val
            temp.val = 0
        temp = temp.next
    head = reverse_list(head)
    return head


def contains(self, key: int) -> bool:
    temp = self.root
    while temp:
        if temp.data == key:
            return True
        temp = temp.next
    return False


def middle_node(root):
    if not root:
        return root
    slow, fast = root, root
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    return slow


def append_last_n_to_first(head: LinkedList, n: int) -> LinkedList:
    if not head or n < 1:
        return head
    head = reverse_list(head)
    tail = head
    count, temp = 0, head
    while temp and count < n - 1:
        temp = temp.next_node
        count += 1
    if temp:
        new_node = temp.next_node
        temp.next_node = None
        head = reverse_list(head)
        new_node = reverse_list(new_node)
        tail.next_node = new_node
    return head


def eliminate_consecutive_duplicates(head: LinkedList) -> LinkedList:
    if not head:
        return head
    final_head, final_tail = None, None
    temp = head
    while temp.next_node:
        if not final_head:
            final_tail = temp
            final_head = temp
        else:
            if temp.data != temp.next_node.data:
                final_tail.next_node = temp
                final_tail = final_tail.next_node
        temp = temp.next_node
    if final_tail.data != temp.data:
        final_tail.next_node = temp
        final_tail = final_tail.next_node
    final_tail.next_node = None
    return final_head


def eliminate_duplicates(head: LinkedList) -> LinkedList:
    if not head:
        return head
    s = dict()
    s.setdefault(head.data, 1)
    temp = head.next_node
    final_head, final_tail = head, head
    while temp:
        if not s.get(temp.data):
            final_tail.next_node = temp
            final_tail = final_tail.next_node
        s[temp.data] = 1
        temp = temp.next_node
    final_tail.next_node = None
    return final_head


def detect_loop(head: LinkedList) -> bool:
    if not head:
        return False
    slow, fast = head, head.next_node
    while fast and fast.next_node:
        slow = slow.next_node
        fast = fast.next_node
        if slow == fast:
            return True
    return False


def find_loop_length(head: LinkedList) -> int:
    if not head:
        return 0
    slow, fast = head, head.next_node
    while fast and fast.next_node:
        slow = slow.next_node
        fast = fast.next_node
        if slow == fast:
            break
    slow, fast = head, fast.next_node
    count = 0
    while slow != fast:
        count += 1
        slow = slow.next_node
        fast = fast.next_node
    return count


def swap_nodes_with_data_swap(head: LinkedList, node1: int, node2: int) -> LinkedList:
    if not head:
        return head
    current, next1, next2 = head, None, None
    while current:
        if current.data == node1:
            next1 = current
        if current.data == node2:
            next2 = current
        current = current.next_node
    temp = next1.data
    next1.data = next2.data
    next2.data = temp
    return head


def swap_nodes_without_data_swap(head: LinkedList, node1: int, node2: int) -> LinkedList:
    if not head or node1 == node2:
        return head
    current1, current2, next1, next2, prev1, prev2 = None, None, None, None, None, None
    temp, prev = head, None
    while temp:
        if temp.data == node1:
            prev1 = prev
            current1 = temp
        if temp.data == node2:
            prev2 = prev
            current2 = temp
        prev = temp
        temp = temp.next_node
    # When one of the node is not in the list
    if not current2 or not current1:
        return head
    # When one of the node is head node
    if not prev1:
        head = current2
    else:
        prev1.next_node = current2
    if not prev2:
        head = current1
    else:
        prev2.next_node = current1
    next1 = current1.next_node
    next2 = current2.next_node
    current1.next_node = next2
    current2.next_node = next1
    return head


def merge_two_sorted_lists(list1: LinkedList, list2: LinkedList) -> LinkedList:
    if not list1:
        return list2
    if not list2:
        return list1
    final_head, final_tail = None, None
    temp1, temp2 = list1, list2
    while temp1 and temp2:
        if temp1.data > temp2.data:
            if not final_head:
                final_head = temp2
                final_tail = temp2
            else:
                final_tail.next_node = temp2
                final_tail = final_tail.next_node
            temp2 = temp2.next_node
        else:
            if not final_head:
                final_head = temp1
                final_tail = temp1
            else:
                final_tail.next_node = temp1
                final_tail = final_tail.next_node
            temp1 = temp1.next_node
    if not temp1:
        final_tail.next_node = temp2
    if not temp2:
        final_tail.next_node = temp1
    return final_head


def merge_sort_list(head: LinkedList) -> LinkedList:
    if not head or not head.next_node:
        return head
    mid_point = middle_node(head)
    part1 = head
    part2 = mid_point.next_node
    mid_point.next_node = None
    part1 = merge_sort_list(part1)
    part2 = merge_sort_list(part2)
    return merge_two_sorted_lists(part1, part2)


def reverse_circular_list(head: LinkedList) -> LinkedList:
    if head.next_node:
        current, prev, nex = head, None, None
        while current.next_node != head:
            nex = current.next_node
            current.next_node = prev
            prev = current
            current = nex
        current.next_node = prev
        head.next = current
        head = current
    return head


def print_circular_list(head: LinkedList) -> None:
    if not head.next_node:
        print(head.data, end=" ")
        return
    print(head.data, end=" ")
    temp = head.next_node
    while temp and temp != head:
        print(temp.data, end=" ")
        temp = temp.next_node


def count_triplet_sum(head: LinkedList, value: int) -> int:
    if not head:
        return 0
    temp = head
    arr = []
    while temp:
        arr.append(temp.data)
        temp = temp.next_node
    # print(arr)
    count = 0
    for i in range(len(arr) - 1):
        req_sum = value - arr[i]
        j, k = i + 1, len(arr) - 1
        while j < k:
            if arr[j] + arr[k] > req_sum:
                k -= 1
            elif arr[j] + arr[k] < req_sum:
                j += 1
            else:
                count += 1
                j += 1
                k -= 1
    return count


def union_list(head1: LinkedList, head2: LinkedList) -> LinkedList:
    if not head1 and not head2:
        return head1
    temp1, temp2, final_head, final_tail, un_map = head1, head2, None, None, dict()
    while temp1:
        if not un_map.get(temp1.data):
            if not final_head:
                final_head = temp1
                final_tail = temp1
            else:
                final_tail.next_node = temp1
                final_tail = final_tail.next_node
        un_map[temp1.data] = 1
        temp1 = temp1.next_node
    # final_tail.next_node = None
    # print_node(final_head)
    while temp2:
        if not un_map.get(temp2.data):
            if not final_head:
                final_head = temp2
                final_tail = temp2
            else:
                final_tail.next_node = temp2
                final_tail = final_tail.next_node
        un_map[temp2.data] = 1
        temp2 = temp2.next_node
    final_tail.next_node = None
    return merge_sort_list(final_head)


# Google's question to find happy number
def happy_number(num: int) -> bool:
    if num == 1:
        return True
    # Slow and fast pointer concept
    fast = find_square(num)
    slow = num
    while fast != slow:
        slow = find_square(slow)
        fast = find_square(find_square(fast))
    if slow == 1:
        return True
    return False


def find_square(num: int) -> int:
    if num == 0 or num == 1:
        return num
    ans = 0
    while num != 0:
        rem = num % 10
        ans += rem * rem
        num //= 10
    return ans


def bubble_sort(head: LinkedList) -> LinkedList:
    if not head:
        return head
    temp, fina_head, final_tail = head, None, None
    while temp:
        inner_temp = temp
        inner_temp_next = temp.next_node
        while inner_temp_next:
            if inner_temp.data > inner_temp_next.data:
                a = inner_temp.data
                inner_temp.data = inner_temp_next.data
                inner_temp_next.data = a
            inner_temp_next = inner_temp_next.next_node
        temp = temp.next_node
    return head


def reverse_list_part(head: LinkedList, start: int, end: int) -> LinkedList:
    if not head:
        return head
    temp = head
    prev, prev_start, temp_start, temp_end = None, None, None, None
    while temp:
        if temp.data == start:
            prev_start = prev
            temp_start = temp
        if temp.data == end:
            temp_end = temp
            break
        prev = temp
        temp = temp.next_node
    if not temp_start or not temp_end:
        return head
    if prev_start:
        prev_start.next_node = None
        h1 = temp_end.next_node
        h2 = temp_start
        temp_end.next_node = None
        temp_start = reverse_list(temp_start)
        prev_start.next_node = temp_start
        h2.next_node = h1
    else:
        h1 = temp_end.next_node
        h2 = temp_start
        temp_end.next_node = None
        temp_start = reverse_list(temp_start)
        h2.next_node = h1
        head = temp_start

    return head


def rearrange_list(head: LinkedList) -> LinkedList:
    if not head:
        return head
    middle_element = middle_node(head)
    next_mid = middle_element.next_node
    middle_element.next_node = None
    final_head, final_tail = None, None
    temp1, temp2 = head, reverse_list(next_mid)
    x, y = None, None
    while temp1 and temp2:
        x = temp1.next_node
        y = temp2.next_node
        if not final_head:
            final_head = temp1
            final_tail = temp1
            final_tail.next_node = temp2
            final_tail = final_tail.next_node
        else:
            final_tail.next_node = temp1
            final_tail = final_tail.next_node
            final_tail.next_node = temp2
            final_tail = final_tail.next_node
            pass
        temp1 = x
        temp2 = y
    if x:
        final_tail.next_node = x
        final_tail = final_tail.next_node
    final_tail.next_node = None
    return final_head


# 1-2-3-4-5-6-7-8-9
# 4-3-2-1
def reverse_k_nodes(head: LinkedList, k: int) -> LinkedList:
    if not head:
        return head
    prev, temp = None, head
    m = False
    while temp:
        h1 = None
        x = temp
        count = 0
        while count < k - 1 and temp:
            count += 1
            temp = temp.next_node
        if temp:
            h1 = temp.next_node
            temp.next_node = None
        temp = reverse_list(x)
        if not m:
            head = temp
            m = True
        else:
            prev.next_node = temp
        prev = x
        x.next_node = h1
        temp = h1
    return head


# https://leetcode.com/problems/reverse-nodes-in-even-length-groups/
def reverse_even_group(head: LinkedList) -> LinkedList:
    if not head:
        return head
    prev, temp = head.next_node, head
    count = 1
    while temp:
        count1, h1, x = 0, None, temp
        while temp and count1 < count - 1:
            count1 += 1
            temp = temp.next_node
        if count % 2 == 0:
            if not temp:
                h1 = temp.next_node
                temp.next_node = None
            temp = reverse_list(x)
            prev.next_node = temp
            prev = x
            x.next_node = h1
            temp = h1
        else:
            if count1 % 2 == 0 and not temp:
                temp = reverse_list(x)
                prev.next_node = temp
                return head
            prev = temp
            if temp:
                temp = temp.next_node
        count += 1
    return head


def rotate_list(head: LinkedList, k: int) -> LinkedList:
    list_len = length_list(head)
    if list_len == 0:
        return head
    k = k % list_len
    if not head or not head.next_node or k == 0:
        return head

    count = list_len - k
    temp = head
    while temp and count > 1:
        temp = temp.next_node
        count -= 1
    h1 = temp.next_node
    temp.next_node = None
    y1 = h1
    while y1.next_node:
        y1 = y1.next_node
    y1.next_node = head
    head = h1
    return head


def partition(head: LinkedList, x: int) -> LinkedList:
    if not head:
        return head
    arr1 = []
    arr2 = []
    temp = head
    while temp:
        if x > temp.data:
            arr1.append(temp.data)
        else:
            arr2.append(temp.data)
        temp = temp.next_node

    i, j = 0, 0
    temp = head
    while i < len(arr1):
        temp.data = arr1[i]
        temp = temp.next_node
        i += 1
    while j < len(arr2):
        temp.data = arr2[j]
        temp = temp.next_node
        j += 1
    return head


def intersection_point(head1: LinkedList, head2: LinkedList) -> int:
    if not head1 or not head2:
        return -1
    count1, count2 = 0, 0
    temp1, temp2 = head1, head2
    while temp1:
        count1 += 1
        temp1 = temp1.next_node
    while temp2:
        count2 += 1
        temp2 = temp2.next_node
    temp1, temp2 = head1, head2
    count = count1 - count2
    first_is_larger = True if count > 0 else False
    if first_is_larger:
        pass
    else:
        pass

# [1,1,0,6]
# root1 = take_input()
# root2 = take_input()
# ans: int = intersection_point(root1, root2)
# print(ans)
# print_node(root)
# root = partition(root, 2)
# root = reverse_list_part(root, 3, 8)
# print()
# print_node(root)
# ans = rearrange_list(root)
# print()
# print_node(ans)

# num1 = int(input("Enter number to check happy or not : "))
# print(happy_number(num1))
# root = LinkedList(0)
# node1 = LinkedList(1)
# node2 = LinkedList(2)
# node3 = LinkedList(3)
# node4 = LinkedList(4)
#
# root.next_node = node1
# node1.next_node = node2
# node2.next_node = node3
# node3.next_node = node4
# node4.next_node = root

# print_circular_list(root)
# print()
# root = reverse_circular_list(root)
# print_circular_list(root)
# root1 = take_input()
# root2 = take_input()
# print_node(union_list(root1, root2))
# root2 = take_input()1
# print_node(root1)
# print()
# print_node(root2)
# print()
# ans = merge_two_sorted_lists(root1, root2)
# print_node(ans)
# print()
# print_node(merge_sort_list(root1))
# root = swap_nodes_without_data_swap(root, 3, 2)
# root = append_last_n_to_first(root, 3)
# root = eliminate_duplicates(root)
# print_node(root)

# root = insert_node_recursive(root, 897, 0)
# root = delete_node_recursive(root, 2)
# print_node(root)
# print(find_node(root, 4))
