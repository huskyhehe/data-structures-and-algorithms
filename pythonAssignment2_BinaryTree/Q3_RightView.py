# https://leetcode.com/problems/binary-tree-right-side-view/

# BFS + two queues
# time: O(N)
# space: O(D)  D: diameter, <= n // 2

import collections
from typing import Optional, List

from TreeNode import TreeNode


class Solution3:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        next_level = collections.deque()
        next_level.append(root)

        while next_level:
            cur_level = next_level
            next_level = collections.deque()

            while cur_level:
                node = cur_level.popleft()
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(node.val)
        return res


if __name__ == "__main__":
    solution3 = Solution3()
    # test case 1
    '''
           1
        /     \
      2         2
       \         \
        3         3 
    '''
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(2)
    root1.left.right = TreeNode(3)
    root1.right.right = TreeNode(3)
    # expected output: [1, 2, 3]
    print(solution3.rightSideView(root1))
