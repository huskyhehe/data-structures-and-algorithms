from typing import Optional

from ListNode import ListNode


class Solution1:
    # https://leetcode.com/problems/rotate-list
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next
        tail.next = head

        new_tail = head
        for i in range(1, length - k % length):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head

    # linked list traversal
    # time: O(n)
    # space: O(1)


if __name__ == "__main__":
    solution1 = Solution1()

    def print_linked_list(head: ListNode):
        while head:
            print(str(head.val) + " -> ", end="")
            head = head.next
        print("None")

    # Test Case 1
    # input: 1 -> 2 -> 3 -> 4 -> 5 -> None, 2
    # output: 4 -> 5 -> 1 -> 2 -> 3 -> None
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(3)
    head1.next.next.next = ListNode(4)
    head1.next.next.next.next = ListNode(5)
    print_linked_list(solution1.rotateRight(head1, 2))

    # Test Case 2
    # input: 7 -> 8 -> 9 -> None
    # output: 8 -> 9 -> 7 -> None
    head2 = ListNode(7)
    head2.next = ListNode(8)
    head2.next.next = ListNode(9)
    print_linked_list(solution1.rotateRight(head2, 5))

    # Test Case 3 (Edge Case)
    # input: 3 -> None
    # output: 3 -> None
    head3 = ListNode(3)
    print_linked_list(solution1.rotateRight(head3, 3))
