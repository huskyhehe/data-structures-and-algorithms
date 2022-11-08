# https://leetcode.com/problems/recover-binary-search-tree/

from Node import TreeNode


class Solution:
    def recoverTree(self, root):
        x = y = pred = None

        def find_two_swapped(node: TreeNode):
            nonlocal x, y, pred
            if node is None:
                return
            find_two_swapped(node.left)
            if pred and node.val < pred.val:
                y = node
                if x is None:
                    x = pred
                else:
                    return
            pred = node
            find_two_swapped(node.right)

        find_two_swapped(root)
        x.val, y.val = y.val, x.val
