class LinkedList:
    def __init__(self, data=0, next_node=None, child_node=None):
        self.val = data
        self.next = next_node
        self.child = child_node


def mergeTwoSortedLL(head1: LinkedList, head2: LinkedList) -> LinkedList:
    if not head1:
        return head2
    if not head2:
        return head1
    temp1, temp2 = head1, head2
    finalHead, finalTail = None, None
    while temp1 and temp2:
        if temp1.val > temp2.val:
            if not finalHead:
                finalHead = temp2
                finalTail = temp2
            else:
                finalTail.next = temp2
                finalTail = finalTail.next
            temp2 = temp2.next
        else:
            if not finalHead:
                finalHead = temp1
                finalTail = temp1
            else:
                finalTail.next = temp1
                finalTail = finalTail.next
            temp1 = temp1.next
    if temp1:
        finalTail.next = temp1
    if temp2:
        finalTail.next = temp2

    return finalHead


def middleNode(head):
    if not head or not head.next:
        return head
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def sortList(head):
    if not head or not head.next:
        return head
    mid = middleNode(head)
    secondPart = mid.next
    mid.next = None
    head1 = sortList(head)
    head2 = sortList(secondPart)
    return mergeTwoSortedLL(head1, head2)


def deleteAllOccurrences(head: LinkedList, k: int) -> LinkedList:
    if not head:
        return head

    temp, prev = head, None

    while temp and temp.val == k:
        prev = temp
        temp = temp.next
        head = head.next
        del prev

    if not temp:
        return temp

    while temp:
        if temp.val == k:
            prev.next = temp.next
        prev = temp
        temp = temp.next
    return head


def length(head: LinkedList) -> int:
    count = 0
    temp = head
    while temp:
        temp = temp.next
        count += 1
    return count


def rotate(head: LinkedList, k: int) -> LinkedList:
    if not head or not head.next or k == 0:
        return head
    k = k % length(head)

    slow, fast, prev = head, head, None
    count = 0
    while count < k:
        count += 1
        fast = fast.next

    while fast:
        prev = slow
        slow = slow.next
        fast = fast.next

    temp = slow
    prev.next = None

    while temp and temp.next:
        temp = temp.next

    temp.next = head
    head = slow
    return head


def flattenLinkedList(head: LinkedList) -> LinkedList:
    if not head or not head.next:
        return head

    finalHead, finalTail = None, None
    temp = head
    while temp:
        nextNode = temp.next
        internalTemp = temp
        while internalTemp:
            if not finalHead:
                finalHead = internalTemp
                finalTail = internalTemp
            else:
                finalTail.child = internalTemp
                finalTail = finalTail.child
            internalTemp = internalTemp.child
        temp = nextNode
    return finalHead


def take_input() -> LinkedList:
    data = int(input("Enter node data: "))
    head, tail = None, None
    while data != -1:
        new_node = LinkedList(data)
        if not head:
            head, tail = new_node, new_node
        else:
            tail.next = new_node
            tail = tail.next
        data = int(input("Enter node data: "))
    return head


def take_special_input() -> LinkedList:
    data = int(input("Enter node data: "))
    head, tail = None, None
    while data != -1:
        new_node = LinkedList(data)
        if not head:
            head, tail = new_node, new_node
        else:
            tail.next = new_node
            tail = tail.next

        childData = int(input("Enter child data"))
        cTail = tail
        while childData != -1:
            child_new_node = LinkedList(childData)
            cTail.child = child_new_node
            cTail = cTail.child
            childData = int(input("Enter child data"))

        data = int(input("Enter node data: "))
    return head


def print_node(head: LinkedList) -> None:
    if not head:
        return
    print(head.val, end=" ")
    print_node(head.child)


class Solution:
    def insertAtFront(self, head: LinkedList) -> LinkedList:
        new_node = LinkedList()
        new_node.next = head
        head = new_node
        return head

    def countDifferenceInNodes(self, head1: LinkedList, head2: LinkedList) -> tuple[bool, int]:
        temp1, temp2 = head1, head2
        isFirstList, count = False, 0
        while temp1 and temp2:
            temp1 = temp1.next
            temp2 = temp2.next

        while temp1:
            temp1 = temp1.next
            isFirstList = True
            count += 1

        while temp2:
            temp2 = temp2.next
            count += 1

        return isFirstList, count

    def addTwoNumbersHelper(self, l1: LinkedList, l2: LinkedList, final_head, carry) -> \
            LinkedList:
        if l1 and l2:
            final_list_next = self.addTwoNumbersHelper(l1.next, l2.next, final_head, carry)
            sum_node = l1.val + l2.val + carry
            carry = sum_node // 10
            sum_node_modulo = sum_node % 10
            new_node = LinkedList(sum_node_modulo)
            final_head = new_node
            final_head.next = final_list_next

        return final_head

    def addTwoNumbers(self, l1: LinkedList, l2: LinkedList) -> LinkedList:
        isFirstList, count = self.countDifferenceInNodes(l1, l2)

        while count > 0:
            if isFirstList:
                l2 = self.insertAtFront(l2)
            else:
                l1 = self.insertAtFront(l1)
            count -= 1

        return self.addTwoNumbersHelper(l1, l2, None, 0)

    def length(self, head: LinkedList) -> int:
        count = 0
        temp = head
        while temp:
            temp = temp.next
            count += 1
        return count

    def splitListToParts(self, head: LinkedList, k: int) -> list[LinkedList]:
        answer = []
        final_ans = []
        length = self.length(head)
        rem = length % k
        dividend = length // k
        j = 0

        for i in range(dividend):
            answer.append(dividend)

        while rem > 0:
            answer[j] += 1
            j += 1
            rem -= 1

        temp = head
        for ele in range(len(answer)):
            temp_count = answer[ele]
            temp_arr = []
            prev = None
            final_head = temp
            while temp_count > 0 and temp:
                temp_arr.append(temp)
                prev = temp
                temp = temp.next
                temp_count -= 1
            prev.next = None
            final_ans.append(final_head)

        return final_ans


if __name__ == "__main__":
    head1 = take_special_input()
    head1 = flattenLinkedList(head1)
    print_node(head1)
    # sol = Solution()
    # ans = sol.splitListToParts(head1, 3)
    # for a in ans:
    #     print_node(a)
    #     print()
    # ans = sol.addTwoNumbers(head1, head2)
    # print_node(ans)
