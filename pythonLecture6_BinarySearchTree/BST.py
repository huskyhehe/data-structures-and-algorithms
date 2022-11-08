import sys
from typing import Optional

from TreeNode import TreeNode


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    # validate
    # https://leetcode.com/problems/validate-binary-search-tree/
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def inorder(node: Optional[TreeNode], low: int, high: int) -> bool:
            # Empty trees are valid BSTs.
            if not node:
                return True
             # The current node's value must be between low and high.
            if node.val <= low or node.val >= high:
                return False
            # The left and right subtree must also be valid.
            return inorder(node.left, low, node.val) and inorder(node.right, node.val, high)

        return inorder(root, -sys.maxsize, sys.maxsize)


    # basic operation:
    # search
    # insert
    # delete

    # search
    def searchInBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

    # insert
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

    # delete
    def deleteNodeInBST(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:





