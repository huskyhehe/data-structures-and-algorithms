"""
Question 1
In a Binary Tree, populate next left of a tree.
"""

# time: O(n)

from Question1.Node import Node


class BinTree:
    def __init__(self, root=None):
        self.root = root

    def populateNextLeft(self, root):
        if not root:
            return None

        rightmost = root
        while rightmost.right:
            head = rightmost
            while head:
                head.right.nextLeft = head.left
                if head.nextLeft:
                    head.left.nextLeft = head.nextLeft.right
                head = head.nextLeft
            rightmost = rightmost.left
        return root


if __name__ == "__main__":
    def getTree():
        tree = BinTree()
        tree.root = Node(1)
        tree.root.left = Node(2)
        tree.root.right = Node(3)
        tree.root.left.left = Node(4)
        tree.root.left.right = Node(5)
        tree.root.right.left = Node(6)
        tree.root.right.right = Node(7)
        tree.root.left.left.left = Node(8)
        tree.root.left.right.left = Node(9)
        tree.root.right.left.left = Node(10)
        tree.root.right.right.left = Node(11)
        return tree





