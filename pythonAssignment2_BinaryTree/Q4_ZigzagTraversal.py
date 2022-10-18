# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# BFS + bool flag + deque
# time: O(N)
# space: O(N)

import collections
from typing import Optional, List

from TreeNode import TreeNode


class Solution4:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = collections.deque()
        queue.append(root)
        res = []
        left_to_right = True

        while queue:
            size = len(queue)
            level = collections.deque()

            for _ in range(size):
                node = queue.popleft()
                if left_to_right:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(list(level))
            left_to_right = not left_to_right
        return res


if __name__ == "__main__":
    solution4 = Solution4()

    # test case 1
    '''
               3
            /     \
          9        20
                  /  \
                 15   7
    '''
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    # expected output: [[3], [20, 9], [15, 7]]
    print(solution4.zigzagLevelOrder(root1))
