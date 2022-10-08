import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def print_level_order(self) -> List[List[int]]:
        if not self:
            return None

        res = []
        queue = collections.deque()
        queue.append(self)

        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                cur_node = queue.popleft()
                res.append(cur_node.val)

                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
        print(res)


class BinaryTree:
    def __init__(self, root=None):
        self.root = root


