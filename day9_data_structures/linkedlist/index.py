"""
So far, we have seen how lists store and organize data for us. Python does not have a built-in linked list structure, as
it isn’t required after the introduction of lists.
However, knowledge about linked lists can be very useful in coding interviews!
Learn about LL here:
Tut-1 :  https://dev.to/tastaslim/an-introduction-to-linked-list-1bmp
Tut-2 : https://dev.to/tastaslim/circular-linked-list-4ned


Note:
1. Insertion at tail for arrays like data structures is in O(n), but in python, the append method for lists is able
to do it in O(1) and in worst case O(n)
2. Deletion at tail for arrays like data structures is in O(n), but in python, the pop method for lists is able to
do it in O(1) but when we use pop for elements except last it takes O(n) to remove that element as we have to shift list
elements.

append function has constant time complexity i.e. O(1), because lists are randomly accessed so the last element can be
reached in O(1) time that's why the time taken to add the new element at the end of the list is O(1).

Also, when a list is created in python, it reserves 32 bits of the contiguous memory location. Whenever the combined size
of elements of that list exceeds the memory space of the original list, it acquires the contiguous memory at another
location of size double its previous size. In that scenario, the previous elements are copied to this new memory space,
and new elements are appended to the list. So, this is considered as the worst case for appending any element to the list
and the time complexity for this worst case is O(N) where N is the size of the original list.


"""

"""
The primary operations which are generally a part of the LinkedList class are listed below:

insert_at_tail(data) - inserts an element at the end of the linked list
insert_at_root(data) - inserts an element at the start/root of the linked list
delete(data) - deletes an element with your specified value from the linked list
delete_at_root() - deletes the first element of the list
search(data) - searches for an element with the specified value in the linked list
is_empty() - returns true if the linked list is empty
"""


class LinkedList:
    def __init__(self, data, next_element_address=None):
        self.data = data
        self.next_element_address = next_element_address


# T(n) = O(1), S(n)=O(1)
def is_empty(root: LinkedList) -> bool:
    if not root:
        return True
    return False


# T(n) = O(n), S(n)=O(1)
def search(root: LinkedList, data: int) -> int:
    temp = root
    while temp:
        if temp.data == data:
            return data
        temp = temp.next_element_address
    return -1


# T(n) = O(n), S(n)=O(1)
def insert_at_tail(root: LinkedList, data: int) -> LinkedList:
    if not root:
        return root
    temp = root
    while temp.next_element_address:
        temp = temp.next_element_address
    temp.next_element_address = LinkedList(data)
    return root


# T(n) = O(1), S(n)=O(1)
def insert_at_root(root: LinkedList, data: int) -> LinkedList:
    if not root:
        return root
    new_element = LinkedList(data)
    new_element.next_element_address = root
    root = new_element
    return root


# T(n) = O(1), S(n)=O(1)
def delete_at_root(root: LinkedList) -> LinkedList:
    if not root:
        return root
    root = root.next_element_address
    return root


# T(n) = O(n), S(n)=O(1)
def delete(root: LinkedList, data: int) -> LinkedList:
    if not root or root.data == data:
        return delete_at_root(root)  # Handle delete element at root or empty LL

    temp, prev = root, None
    while temp and temp.data != data:
        prev = temp
        temp = temp.next_element_address
    if temp:  # handle if element not found
        prev.next_element_address = temp.next_element_address
    return root


# T(n) = O(n), S(n)=O(1)
def length(root: LinkedList) -> int:
    temp, count = root, 0
    while temp:
        count += 1
        temp = temp.next_element_address
    return count


# T(n) = O(n), S(n)=O(n)
def take_input(number_of_element: int) -> LinkedList:
    root, tail = None, None
    while number_of_element > 0:
        node_value = input('Enter data: ')
        if not root:

            """
            Had to do this because you see in tail we are creating a new LL node with same value which will have a different
            address and hence if we don't write last 2 lines, it will always print head element. I showed it here, because
            most of us often end up doing this mistake
            
            root, tail = LinkedList(node_value), LinkedList(node_value)
            root.next_element_address = tail
            root = root.next_element_address
            """
            # correct way
            root = LinkedList(node_value)
            tail = root
        else:
            tail.next_element_address = LinkedList(node_value)
            tail = tail.next_element_address
        number_of_element -= 1
    return root


# T(n) = O(n), S(n)=O(1)
def print_element(root: LinkedList) -> None:
    temp = root
    while temp:
        print(temp.data, end=" ")
        temp = temp.next_element_address


# T(n) = O(n), S(n)=O(1)
def reverse(root: LinkedList) -> LinkedList:
    if not root or not root.next_element_address:
        return root
    prev, temp, next_node = None, root, None
    while temp:
        next_node = temp.next_element_address
        temp.next_element_address = prev
        prev = temp
        temp = next_node
    root = prev
    return root


# T(n) = O(n), S(n)=O(1)
def middle_node(root: LinkedList) -> int:
    ans = -1
    if not root:
        return ans
    slow, fast = root, root.next_element_address
    while fast and fast.next_element_address:
        slow = slow.next_element_address
        fast = fast.next_element_address.next_element_address
    return slow.data


# T(n) = O(n), S(n)=O(1)
def detect_cycle(root: LinkedList) -> bool:
    if not root or not root.next_element_address:
        return False
    slow, fast = root, root.next_element_address
    while fast and fast.next_element_address:
        # print(slow.data, fast.data)
        if slow is fast:
            return True
        slow = slow.next_element_address
        fast = fast.next_element_address.next_element_address
    return False


# Remove Duplicates from Linked List

def remove_duplicates(root: LinkedList) -> LinkedList:
    if not root:
        return root
    # T(n) = O(n), S(n)=O(n)
    dictionary = {}
    temp = root
    while temp:
        if dictionary.get(temp.data):
            dictionary[temp.data] = dictionary.get(temp.data) + 1
        else:
            dictionary[temp.data] = 1
        temp = temp.next_element_address
    temp, final_head, final_tail = root, None, None
    while temp:
        if dictionary.get(temp.data):
            if not final_head:
                final_head = temp
                final_tail = final_head
            else:
                final_tail.next_element_address = temp
                final_tail = final_tail.next_element_address
            dictionary[temp.data] = None
        temp = temp.next_element_address
    final_tail.next_element_address = None
    return final_head


# T(n) = O(m+n), S(n)=O(m+n)
def union(root1: LinkedList, root2: LinkedList) -> LinkedList:
    """
    We can also do it with remove duplicates method where we add the tail of root1 with head of
    root 2 and then perform remove duplicate on merged linked list but problem with that approach is
    when either of root 1 or root 2 has duplicates elements in it then it will remove those as well.
    """
    if not root1:
        return root2
    if not root2:
        return root1
    dictionary = {}
    temp1, temp2 = root1, root2
    final_head = None
    final_tail = None
    while temp1:
        if dictionary.get(temp1.data):
            dictionary[temp1.data] += 1
        else:
            dictionary[temp1.data] = 1
        if not final_head:
            final_head = temp1
            final_tail = final_head
        else:
            final_tail.next_element_address = temp1
            final_tail = final_tail.next_element_address
        temp1 = temp1.next_element_address

    while temp2:
        if not dictionary.get(temp2.data):
            final_tail.next_element_address = temp2
            final_tail = final_tail.next_element_address
        temp2 = temp2.next_element_address

    final_tail.next_element_address = None
    return final_head


# T(n) = O(m+n), S(n)=O(m+n)
def intersection(root1: LinkedList, root2: LinkedList) -> LinkedList:
    if not root1:
        return root1
    if not root2:
        return root2
    dictionary = {}
    temp1, temp2 = root1, root2
    final_head = None
    final_tail = None
    while temp1:
        if dictionary.get(temp1.data):
            dictionary[temp1.data] += 1
        else:
            dictionary[temp1.data] = 1
        temp1 = temp1.next_element_address

    while temp2:
        if dictionary.get(temp2.data):
            if not final_head:
                final_head = temp2
                final_tail = final_head
            else:
                final_tail.next_element_address = temp2
                final_tail = final_tail.next_element_address
        temp2 = temp2.next_element_address

    if final_tail:  # check for no common nodes
        final_tail.next_element_address = None
    return final_head


def merge_two_sorted_lists(root1: LinkedList, root2: LinkedList) -> LinkedList:
    if not root1:
        return root2
    if not root2:
        return root1
    temp1, temp2 = root1, root2
    final_head, final_tail, temp = None, None, None
    while temp1 and temp2:
        if temp1.data > temp2.data:
            temp = temp2
            temp2 = temp2.next_element_address
        else:
            temp = temp1
            temp1 = temp1.next_element_address
        if not final_head:
            final_head = temp
            final_tail = final_head
        else:
            final_tail.next_element_address = temp
            final_tail = final_tail.next_element_address
    if temp1:
        final_tail.next_element_address = temp1
    if temp2:
        final_tail.next_element_address = temp2
    return final_head


def return_nth_node_from_last(root: LinkedList, n: int) -> int:
    if not root:
        return -1
    """
    # By calculating length ==> T(n) = O(n), S(n) = O(1) ==> requires 2 iteration of ll
    length_ll = length(root)
    temp, count = root, length_ll - n
    if count < 0 or n < 0:
        return -1
    while temp and count > 0:
        temp = temp.next_element_address
        count -= 1

    if temp:
        return temp.data
    return -1
    """

    # By reversing the Linked List ==> T(n) = O(n), S(n) = O(1) ==> requires 2 iteration of ll
    """
    root = reverse(root)
    temp = root
    if n < 0:
        return -1
    while temp and n > 1:
        temp = temp.next_element_address
        n -= 1
    if temp:
        return temp.data
    return -1
    """

    # Two point approach ==> T(n) = O(n), S(n) = O(1) ==> requires only 1 iteration of ll
    if n < 0:
        return -1
    end_node, nth_node = root, root
    while end_node and n > 0:
        end_node = end_node.next_element_address
        n -= 1

    if not end_node:
        return -1

    while end_node:
        end_node = end_node.next_element_address
        nth_node = nth_node.next_element_address

    if nth_node:
        return nth_node.data
    return -1


def mergeTwoSortedLL(head1: LinkedList, head2: LinkedList) -> LinkedList:
    if not head1:
        return head2
    if not head2:
        return head1

    temp1, temp2 = head1, head2
    finalHead, finalTail = None, None
    while temp1 and temp2:
        if temp1.data > temp2.data:
            if not finalHead:
                finalHead = temp2
                finalTail = temp2
            else:
                finalTail.child = temp2
                finalTail = finalTail.child
            temp2 = temp2.child
        else:
            if not finalHead:
                finalHead = temp1
                finalTail = temp1
            else:
                finalTail.child = temp1
                finalTail = finalTail.child
            temp1 = temp1.child

    if not temp1:
        finalTail.child = temp1
    if not temp2:
        finalTail.child = temp2
    return finalHead


def flattenLinkedList(head: LinkedList) -> LinkedList:
    if not head or not head.next:
        return head
    rec = flattenLinkedList(head.next)
    head.next = None
    answer = mergeTwoSortedLL(head, rec)
    return answer


class Solution:
    @staticmethod
    def reverse(head: LinkedList) -> LinkedList:
        if not head or not head.next_element_address:
            return head
        prev, curr, nextNode = None, head, None
        while curr:
            nextNode = curr.next_element_address
            curr.next_element_address = prev
            prev = curr
            curr = nextNode
        return prev

    def reverseKGroup(self, head: LinkedList, k: int) -> LinkedList:
        if not head or not head.next_element_address or k <= 1:
            return head

        finalHead, finalTail = None, None

        prev, temp = None, head
        while temp:
            h1 = temp
            h2 = temp
            count = 0
            while temp and count != k:
                prev = temp
                temp = temp.next_element_address
                count += 1
            if prev:
                prev.next_element_address = None
                if temp:
                    h2 = self.reverse(h2)
            if not finalHead:
                finalHead = h2
                finalTail = h1
            else:
                finalTail.next_element_address = h2
                finalTail = h1
        return finalHead


size = int(input("Enter length of linkedlist: "))
head1 = take_input(size)
# head2 = take_input(2)
num = int(input("Enter size in which list to be reversed: "))
print_element(Solution().reverseKGroup(head1, num))
# 1 2 3 4 5 6
