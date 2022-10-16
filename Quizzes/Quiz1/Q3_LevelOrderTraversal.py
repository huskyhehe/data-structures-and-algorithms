import collections
from typing import Optional, List

from TreeNode import TreeNode


class Solution3:
    def level_order_traversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            size = len(queue)
            level = []

            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(level)
        return res


