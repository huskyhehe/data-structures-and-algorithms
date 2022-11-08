# https://leetcode.com/problems/inorder-successor-in-bst/
# use BST properties, skip half subtree
# time: O(n)
# space: O(1)

from typing import Optional

from Node import TreeNode


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        suc = None

        while root:
            if p.val >= root.val:
                root = root.right
            else:
                suc = root
                root = root.left

        return suc
