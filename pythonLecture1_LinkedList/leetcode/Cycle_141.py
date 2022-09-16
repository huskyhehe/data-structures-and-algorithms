from typing import Optional

from leetcode.ListNode import ListNode


class Solution141:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head:
            return False

        slow = head
        fast = head.next

        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next

        return False


if __name__ == "__main__":

    solution141 = Solution141()

    # [3,2,0,-4] pos=1
    head1 = ListNode(3)
    cycle_pos1 = ListNode(2)
    head1.next = cycle_pos1
    head1.next.next = ListNode(0)
    head1.next.next.next = ListNode(-4)
    head1.next.next.next.next = cycle_pos1
    print(solution141.hasCycle(head1))

    # [1,2] pos=0
    head2 = ListNode(1)
    head2.next = ListNode(2)
    head2.next.next = head2
    print(solution141.hasCycle(head2))

    # [1] pos=-1
    head3 = ListNode(1)
    print(solution141.hasCycle(head3))





