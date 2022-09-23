from typing import Optional

from leetcode.ListNode import ListNode


class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            temp = v1 + v2 + carry

            cur.next = ListNode(temp % 10)
            carry = temp // 10

            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


if __name__ == "__main__":
    solution = Solution2()

    def printLinkedList(head: ListNode):
        while head:
            print(str(head.val) + " -> ", end="")
            head = head.next
        print("None")

    # [2,4,3], [5,6,4]
    l1head1 = ListNode(2)
    l1head1.next = ListNode(4)
    l1head1.next.next = ListNode(3)
    l2head1 = ListNode(5)
    l2head1.next = ListNode(6)
    l2head1.next.next = ListNode(4)
    printLinkedList(solution.addTwoNumbers(l1head1, l2head1))

    # [0], [0]
    l1head2 = ListNode(0)
    l2head2 = ListNode(0)
    printLinkedList(solution.addTwoNumbers(l1head2, l2head2))

    # [9,9,9,9,9], [9,9]
    l1head3 = ListNode(9)
    l1head3.next = ListNode(9)
    l1head3.next.next = ListNode(9)
    l1head3.next.next.next = ListNode(9)
    l1head3.next.next.next.next = ListNode(9)
    l2head3 = ListNode(9)
    l2head3.next = ListNode(9)
    printLinkedList(solution.addTwoNumbers(l1head3, l2head3))







