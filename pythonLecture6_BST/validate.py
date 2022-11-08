# validate
# https://leetcode.com/problems/validate-binary-search-tree/
# Convert Sorted Array to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

import sys
from typing import Optional, List

from TreeNode import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def inorder(node: Optional[TreeNode], low: int, high: int) -> bool:
            # Empty trees are valid BSTs.
            if not node:
                return True
            # The current node's value must be between low and high.
            if node.val <= low or node.val >= high:
                return False
            # The left and right subtree must also be valid.
            return inorder(node.left, low, node.val) and inorder(node.right, node.val, high)

        return inorder(root, -sys.maxsize, sys.maxsize)

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None

            # always choose left middle node as a root
            p = (left + right) // 2

            # preorder traversal: node -> left -> right
            root = TreeNode(nums[p])
            root.left = helper(left, p - 1)
            root.right = helper(p + 1, right)
            return root

        return helper(0, len(nums) - 1)
