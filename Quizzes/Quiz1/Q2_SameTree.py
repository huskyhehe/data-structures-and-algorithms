from typing import Optional

from TreeNode import TreeNode


class Solution2:
    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)
