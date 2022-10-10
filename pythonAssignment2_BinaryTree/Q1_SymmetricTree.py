# https://leetcode.com/problems/symmetric-tree/

# DFS
# time: O(n)
# space: O(n)

from typing import Optional

from TreeNode import TreeNode


class Solution1:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def isMirrored(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val == q.val and isMirrored(p.left, q.right) and isMirrored(p.right, q.left)

        return isMirrored(root, root)


if __name__ == "__main__":
    solution1 = Solution1()

    # test case 1
    '''
                   1
                /     \
              2         2
            /   \     /   \
           3    4     4    3
    '''
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(4)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(3)
    # expected output: True
    print(solution1.isSymmetric(root1))

    # test case 2
    '''
           1
        /     \
      2         2
       \         \
        3         3 
    '''
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.right = TreeNode(3)
    root2.right.right = TreeNode(3)
    # expected output: False
    print(solution1.isSymmetric(root2))
