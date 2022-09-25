# https://leetcode.com/problems/remove-linked-list-elements

from typing import Optional

from ListNode import ListNode


class Solution2:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        if not head:
            return None

        dummy = ListNode(-1)
        dummy.next = head

        pre = dummy
        cur = head

        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next

        return dummy.next

    # dummy head technique & linked list traversal
    # time: O(n)
    # space: O(1)


if __name__ == "__main__":
    solution2 = Solution2()

    def print_linked_list(head: ListNode):
        while head:
            print(str(head.val) + " -> ", end="")
            head = head.next
        print("None")

    # Test Case 1
    # input: 1 -> 2 -> 6 -> 3 -> 6 -> None, 6
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(6)
    head1.next.next.next = ListNode(3)
    head1.next.next.next.next = ListNode(6)
    # output: 1 -> 2 -> 3 -> None
    print_linked_list(solution2.removeElements(head1, 6))

    # Test Case 2
    # input: 7 -> 7 -> 7 -> None, 7
    head2 = ListNode(7)
    head2.next = ListNode(7)
    head2.next.next = ListNode(7)
    # output: None
    print_linked_list(solution2.removeElements(head2, 7))

    # Test Case 3 (Edge Case)
    # input: None, 1
    # output: None
    print_linked_list(solution2.removeElements(None, 1))
