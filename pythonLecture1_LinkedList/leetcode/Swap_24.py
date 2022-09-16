from typing import Optional

from leetcode.ListNode import ListNode


class Solution24:
    #
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        first_node = head
        second_node = head.next

        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node

        return second_node


if __name__ == "__main__":

    solution = Solution24()

    def printLinkedList(head: ListNode):
        while head:
            print(str(head.val) + " -> ", end="")
            head = head.next
        print("None")

    # [1,2,3,4]
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(3)
    head1.next.next.next = ListNode(4)
    printLinkedList(head1)
    printLinkedList(solution.swapPairs(head1))

    # [] -- corner case
    head2 = None
    printLinkedList(head2)
    printLinkedList(solution.swapPairs(head2))

    # [1] -- corner case
    head3 = ListNode(1)
    printLinkedList(head3)
    printLinkedList(solution.swapPairs(head3))
