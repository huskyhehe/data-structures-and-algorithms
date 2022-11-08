# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
# inorder
# time: O(n)
# space: O(logn)

from typing import Optional

from Node import ListNode, TreeNode


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def getSize(node):
            cur = node
            size = 0
            while cur:
                size += 1
                cur = cur.next
            return size

        size = getSize(head)

        def convert(left, right):
            nonlocal head
            if left > right:
                return None

            mid = (left + right) // 2

            left = convert(left, mid - 1)
            node = TreeNode(head.val)
            node.left = left

            head = head.next

            right = convert(mid + 1, right)
            node.right = right
            return node

        return convert(0, size - 1)
