# Basic  #######################################################################
# 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/

# 653. Two Sum IV - Input is a BST
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/


import sys
from typing import Optional

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

    # 653. Two Sum IV - Input is a BST
    # dfs + hashset
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        val_set = set()

        def find(node: TreeNode):
            if not node:
                return False
            if (k - node.val) in val_set:
                return True

            val_set.add(node.val)
            return find(node.left) or find(node.right)

        return find(root)
