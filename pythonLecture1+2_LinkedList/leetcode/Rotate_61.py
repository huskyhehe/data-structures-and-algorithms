from typing import Optional

from leetcode.ListNode import ListNode


class Solution61:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        old_tail = head
        n = 1
        while old_tail.next:
            n += 1
            old_tail = old_tail.next

        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next

        old_tail.next = head
        new_head = new_tail.next
        new_tail.next = None

        return new_head


if __name__ == "__main__":
    solution = Solution61()

    def printLinkedList(head: ListNode):
        while head:
            print(str(head.val) + " -> ", end="")
            head = head.next
        print("None")

    # [1,2,3,4,5], k = 2
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(3)
    head1.next.next.next = ListNode(4)
    head1.next.next.next.next = ListNode(5)
    printLinkedList(head1)
    printLinkedList(solution.rotateRight(head1, 2))

    # [0,1,2], k = 4
    head2 = ListNode(0)
    head2.next = ListNode(1)
    head2.next.next = ListNode(2)
    printLinkedList(head2)
    printLinkedList(solution.rotateRight(head2, 4))


