import sys
from typing import Optional

from TreeNode import TreeNode


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    #############################################################
    # basic operation:
    # search
    # insert
    # delete
    #############################################################

    # search  ########################################################################################################
    # time: O(h) - the height of BST
    # space: O(1)
    #   1. return the node if the target value is equal to the value of the node;
    #   2. continue searching in the left subtree if the target value is less than the value of the node;
    #   3. continue searching in the right subtree if the target value is larger than the value of the node.
    ##################################################################################################################
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            return root
        if root.val > val:
            return self.searchBST(root.left, val)
        return self.searchBST(root.right, val)

    # insert #######################################################################################
    # The main idea is to find out a proper leaf position for the target node and then insert the node as a leaf.
    #   1. search the left or right subtrees according to the relation of the value of the node and the value of our target node;
    #   2. repeat STEP 1 until reaching an external node;
    #   3. add the new node as its left or right child depending on the relation of the value of the node and the value of our target node.
    ######################################################################################################################################
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val, None, None)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root

    # delete ###############################################################################################################
    #   1. If the target node has no child, we can simply remove the node.
    #   2. If the target node has one child, we can use its child to replace itself.
    #   3. If the target node has two children, replace the node with its in-order successor or predecessor node and delete that node.
    #########################################################################################################################
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        # delete from the right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # delete from the left subtree
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # delete the current node
        else:
            # the node is a leaf
            if not (root.left or root.right):
                root = None
            # the node is not a leaf and has a right child
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            # the node is not a leaf, has no right child, and has a left child
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)

        return root

    # One step right and then always left
    def successor(self, root: TreeNode) -> int:
            root = root.right
            while root.left:
                root = root.left
            return root.val

    # One step left and then always right
    def predecessor(self, root: TreeNode) -> int:
        root = root.left
        while root.right:
            root = root.right
        return root.val
