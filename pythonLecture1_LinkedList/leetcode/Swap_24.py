from typing import Optional

from leetcode.ListNode import ListNode


class Solution24:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        first_node = head
        second_node = head.next

        first_node = self.swapPairs(second_node.next)
        second_node = first_node.next

        return second_node
