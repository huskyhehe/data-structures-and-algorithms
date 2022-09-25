# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

from typing import Optional

from ListNode import ListNode


class Solution3:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        begin = head
        end = head
        for i in range(1, k):
            begin = begin.next
        for i in range(1, n - k + 1):
            end = end.next

        begin.val, end.val = end.val, begin.val
        return head

    # linked list traversal
    # time: O(n)
    # space: O(1)


if __name__ == "__main__":
    solution3 = Solution3()

    def print_linked_list(head: ListNode):
        while head:
            print(str(head.val) + " -> ", end="")
            head = head.next
        print("None")

    # Test Case 1
    # input: 1 -> 4 -> 3 -> 2 -> 5 -> None, 4
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(3)
    head1.next.next.next = ListNode(4)
    head1.next.next.next.next = ListNode(5)
    # output: 1 -> 2 -> 3 -> 4 -> 5 -> None
    print_linked_list(solution3.swapNodes(head1, 4))

    # Test Case 2
    # input: 1 -> 2 -> None, 2
    head2 = ListNode(1)
    head2.next = ListNode(2)
    # output: 2 -> 1 -> None
    print_linked_list(solution3.swapNodes(head2, 2))

    # Test Case 3 (Edge Case)
    # input: 5 -> None, 1
    head3 = ListNode(5)
    # output: 5 -> None
    print_linked_list(solution3.swapNodes(head3, 1))
