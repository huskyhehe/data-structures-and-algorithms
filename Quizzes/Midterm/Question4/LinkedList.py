"""
Question 4
Sorted insert in a Link list.
"""

# time: O(n)

from Question4.ListNode import ListNode


class LinkedList:
    def __init__(self, head=None, length=0):
        self.head = head
        self.length = 0

    def insert(self, data: int) -> None:
        newNode = ListNode(data)
        if not self.head:
            self.head = newNode
            return
        if data < self.head.val:
            newNode.next = self.head
            self.head = newNode
            return

        pre, cur = ListNode(-1), self.head
        while cur and data > cur.val:
            pre = cur
            cur = cur.next
        pre.next = newNode
        newNode.next = cur


if __name__ == "__main__":

    def printLinkedList(linkedls):
        if not linkedls.head:
            return
        cur = linkedls.head
        while cur:
            print(cur.val, end=", ")
            cur = cur.next
        print()

    testList = LinkedList()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(5)
    testList.head = head

    # before insert
    printLinkedList(testList)
    # insert
    testList.insert(4)
    # after insert
    printLinkedList(testList)


