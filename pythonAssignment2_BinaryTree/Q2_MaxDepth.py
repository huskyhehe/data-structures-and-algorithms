# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# DFS
# time: O(n)
# space: O(n)

from typing import Optional

from TreeNode import TreeNode


class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1


if __name__ == "__main__":
    solution2 = Solution2()

    # test case 1
    '''
               3
            /     \
          9         20
                   /   \
                  15    7
    '''
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    # expected output: 3
    print(solution2.maxDepth(root1))

    # test case 2
    '''
           2
            \
             3
    '''
    root2 = TreeNode(2)
    root2.right = TreeNode(3)
    # expected output: 2
    print(solution2.maxDepth(root2))
