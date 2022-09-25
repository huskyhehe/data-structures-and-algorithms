# https://leetcode.com/problems/split-linked-list-in-parts/

from typing import Optional, List

from ListNode import ListNode


class Solution4:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next

        size = n // k
        larger_count = n % k

        res = []
        pre = None
        cur = head
        for i in range(k):
            res.append(cur)
            larger = 1 if i < larger_count else 0
            for j in range(size + larger):
                pre = cur
                cur = cur.next
            if pre:
                pre.next = None

        return res

    # two pointers + linked list traversal
    # time: O(n)
    # space: O(max(n, k))


if __name__ == "__main__":
    solution4 = Solution4()

    def linked_list_to_string(head: ListNode):
        list_str = ""
        while head:
            list_str += (str(head.val) + " -> ")
            head = head.next
        list_str += "None"
        return list_str

    def print_a_list_of_linkedlist(ls: List[Optional[ListNode]]):
        output = []
        for linkedlist in ls:
            output.append(linked_list_to_string(linkedlist))
        print(output)

    # Test Case 1
    # input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> None
    head1 = ListNode(1)
    cur = head1
    for i in range(2, 11):
        cur.next = ListNode(i)
        cur = cur.next
    # expected output: ['1 -> 2 -> 3 -> 4 -> None', '5 -> 6 -> 7 -> None', '8 -> 9 -> 10 -> None']
    print_a_list_of_linkedlist(solution4.splitListToParts(head1, 3))

    # Test Case 2
    # input: 1 -> 2 -> 3 -> None, 5
    head2 = ListNode(1)
    head2.next = ListNode(2)
    head2.next.next = ListNode(3)
    # expected output: ['1 -> None', '2 -> None', '3 -> None', 'None', 'None']
    print_a_list_of_linkedlist(solution4.splitListToParts(head2, 5))

    # Test Case 3
    # input: None, 3
    # expected output: ['None', 'None', 'None']
    print_a_list_of_linkedlist(solution4.splitListToParts(None, 3))
