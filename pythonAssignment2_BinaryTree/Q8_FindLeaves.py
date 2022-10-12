# https://leetcode.com/problems/find-leaves-of-binary-tree/

# DFS
# time: O(n)
# space: O(n)

from typing import Optional, List

from TreeNode import TreeNode


class Solution8:
    def __init__(self):
        self.res = []

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        def getHeight(node: Optional[TreeNode]) -> int:
            if not node:
                return -1

            left_depth = getHeight(node.left)
            right_depth = getHeight(node.right)
            height = max(left_depth, right_depth) + 1

            if height == len(self.res):
                self.res.append([])
            self.res[height].append(node.val)
            node.left = None
            node.right = None
            return height

        getHeight(root)
        return self.res


if __name__ == "__main__":
    solution8 = Solution8()

    # test case 1
    '''
                   3
                /     \
              5         1
            /  \       /  \
           6    2     0    8
               /  \
              7    4
    '''
    root1 = TreeNode(3)
    root1.left = TreeNode(5)
    root1.right = TreeNode(1)
    root1.left.left = TreeNode(6)
    root1.left.right = TreeNode(2)
    root1.right.left = TreeNode(0)
    root1.right.right = TreeNode(8)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(4)
    # expected output: [[6, 7, 4, 0, 8], [2, 1], [5], [3]]
    print(solution8.findLeaves(root1))

