"""
Question 2
Populate parent of each node. in the binary tree
"""

# time: O(n)
from Question2.Node import Node


class BinTree:
    def __init__(self, root=None):
        self.root = root

    def populateParent(self, root):
        if not root:
            return
        self.populateParent(root.left)
        if root.left:
            root.left.parent = root
        if root.right:
            root.right.parent = root
        self.populateParent(root.right)



