from typing import Optional

from ListNode import ListNode


class Solution5:
    def insert(self, head: Optional[ListNode], insertVal: int) -> ListNode:

        new_node = ListNode(insertVal)

        if not head:
            new_node.next = new_node
            return new_node

        if not head.next:
            head.next = new_node
            new_node.next = head
            return head

        pre, cur = head, head.next
        while cur != head:
            if pre.val <= insertVal <= cur.val:
                break
            if pre.val > cur.val > insertVal:
                break
            if insertVal > pre.val > cur.val:
                break
            pre = pre.next
            cur = cur.next

        pre.next = new_node
        new_node.next = cur

        return head
