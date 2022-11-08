# https://leetcode.com/problems/range-sum-of-bst/

from typing import Optional

from Node import TreeNode


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal res
            if not node:
                return res
            if low <= node.val <= high:
                res += node.val
            if low < node.val:
                dfs(node.left)
            if high > node.val:
                dfs(node.right)

        dfs(root)
        return res
