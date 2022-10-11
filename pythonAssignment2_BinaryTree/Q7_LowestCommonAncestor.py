# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# DFS
# LCA conditions:
#     f(lson) and f(rson) or
#     isPorQ and ( f(lson) or f(rson)
# time: O(n)
# space: O(n)

from TreeNode import TreeNode


class Solution7:
    def __init__(self):
        self.res = None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def isAncestor(node: TreeNode) -> bool:
            if not node:
                return False

            left = isAncestor(node.left)
            right = isAncestor(node.right)
            isSame = (node.val == p.val or node.val == q.val)

            if (left and right) or (isSame and (left or right)):
                self.res = node
            return left or right or isSame

        isAncestor(root)
        return self.res


if __name__ == "__main__":
    solution7 = Solution7()

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
    # expected output: 3
    print(solution7.lowestCommonAncestor(root1, TreeNode(5), TreeNode(1)).val)
    # expected output: 5
    print(solution7.lowestCommonAncestor(root1, TreeNode(5), TreeNode(4)).val)

