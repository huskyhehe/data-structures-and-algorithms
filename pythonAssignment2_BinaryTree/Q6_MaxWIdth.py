# https://leetcode.com/problems/maximum-width-of-binary-tree/

# BFS + (node, index)
# notice: col (in vertical traversal) VS index (in width)
# time: O(N)
# space: O(N)

import collections
from typing import Optional

from TreeNode import TreeNode


class Solution6:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_width = 1
        queue = collections.deque()
        queue.append((root, 0))

        while queue:
            size = len(queue)
            head, head_index = queue[0]
            node_index = 0

            for _ in range(size):
                node, node_index = queue.popleft()

                if node.left:
                    queue.append((node.left, node_index * 2))
                if node.right:
                    queue.append((node.right, node_index * 2 + 1))

            max_width = max(max_width, node_index - head_index + 1)
        return max_width


if __name__ == "__main__":
    solution6 = Solution6()

    # test case 1
    '''
               1
            /     \
          3        2
         /        /  
        5        15
    '''
    root1 = TreeNode(1)
    root1.left = TreeNode(3)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(5)
    root1.right.left = TreeNode(15)
    # expected output: 3
    print(solution6.widthOfBinaryTree(root1))
