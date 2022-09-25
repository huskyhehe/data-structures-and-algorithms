from typing import Optional

from ListNode import ListNode


class Solution5:
    # https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/
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

    # linked list traversal
    # time: O(n)
    # space: O(1)


if __name__ == "__main__":
    solution5 = Solution5()

    def print_linked_list(head: ListNode):
        if not head:
            print("None")
        print(str(head.val) + " -> ", end="")
        cur = head.next
        while cur and cur != head:
            print(str(cur.val) + " -> ", end="")
            cur = cur.next
        print("")


    # Test Case 1 (Edge Case)
    # input: None, 1
    # output: 1 ->
    head1 = None
    print_linked_list(solution5.insert(head1, 1))

    # Test Case 2 (Edge Case)
    # input: 1 ->, 0
    # output: 1 ->
    head2 = ListNode(1)
    print_linked_list(solution5.insert(head2, 0))

    # Test Case 3
    # input: 3 -> 4 -> 1 ->, 2
    # output: 1 -> End
    head3 = ListNode(3)
    head3.next = ListNode(4)
    head3.next.next = ListNode(1)
    head3.next.next.next = head3
    print_linked_list(solution5.insert(head3, 2))

    # Test Case 4
    # input: 3 -> 4 -> 1 ->, 7
    # output: 1 ->
    head4 = ListNode(3)
    head4.next = ListNode(4)
    head4.next.next = ListNode(1)
    head4.next.next.next = head4
    print_linked_list(solution5.insert(head4, 7))
