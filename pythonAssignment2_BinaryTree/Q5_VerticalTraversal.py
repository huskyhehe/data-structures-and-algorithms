# https://leetcode.com/problems/binary-tree-vertical-order-traversal/

# BFS + hashmap
# time: O(N)
# space: O(N)

import collections
from typing import Optional, List

from TreeNode import TreeNode


class Solution5:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        col_map = collections.defaultdict(list)
        queue = collections.deque()
        queue.append((root, 0))
        min_col = 0
        max_col = 0

        while queue:
            size = len(queue)

            for _ in range(size):
                node, col = queue.popleft()
                col_map[col].append(node.val)

                min_col = min(min_col, col)
                max_col = max(max_col, col)

                if node.left:
                    queue.append((node.left, col - 1))
                if node.right:
                    queue.append((node.right, col + 1))

        return [col_map[col] for col in range(min_col, max_col + 1)]


if __name__ == "__main__":
    solution5 = Solution5()

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
    # expected output: [[9], [3, 15], [20], [7]]
    print(solution5.verticalOrder(root1))
