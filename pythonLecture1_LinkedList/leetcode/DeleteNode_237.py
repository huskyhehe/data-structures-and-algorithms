from leetcode.ListNode import ListNode


class Solution237:
    def deleteNode(self, node: ListNode):
        succ = node.next
        node.val = succ.val

        node.next = succ.next
        succ.next = None


if __name__ == "__main__":

    solution = Solution237()

    def printLinkedList(head: ListNode):
        while head:
            print(str(head.val) + " -> ", end="")
            head = head.next
        print("None")

    # head = [4,5,1,9], node = 5
    head1 = ListNode(4)
    node_to_delete1 = ListNode(5)
    head1.next = node_to_delete1
    head1.next.next = ListNode(1)
    head1.next.next.next = ListNode(9)
    printLinkedList(head1)
    solution.deleteNode(node_to_delete1)
    printLinkedList(head1)


