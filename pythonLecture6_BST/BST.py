# [700. Search in a Binary Search Tree]
# (https://leetcode.com/problems/search-in-a-binary-search-tree/)

# [701. Insert into a Binary Search Tree]
# (https://leetcode.com/problems/insert-into-a-binary-search-tree/)

# [450. Delete Node in a BST]
# (https://leetcode.com/problems/delete-node-in-a-bst/)

from typing import Optional

from TreeNode import TreeNode


class BinarySearchTree:
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
    def search(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            return root
        if root.val > val:
            return self.search(root.left, val)
        return self.search(root.right, val)

    # insert #######################################################################################
    # The main idea is to find out a proper leaf position for the target node and then insert the node as a leaf.
    #   1. search the left or right subtrees according to the relation of the value of the node and the value of our target node;
    #   2. repeat STEP 1 until reaching an external node;
    #   3. add the new node as its left or right child depending on the relation of the value of the node and the value of our target node.
    ######################################################################################################################################
    def insert(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val, None, None)
        if val > root.val:
            root.right = self.insert(root.right, val)
        else:
            root.left = self.insert(root.left, val)
        return root

    # delete ###########################################################################################################################
    #   1. If the target node has no child, we can simply remove the node.
    #   2. If the target node has one child, we can use its child to replace itself.
    #   3. If the target node has two children, replace the node with its in-order successor or predecessor node and delete that node.
    # time: O(logN)
    # space: O(H)  H: tree height, H = logN if balanced tree
    ####################################################################################################################################
    def delete(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        # delete from the right subtree
        if key > root.val:
            root.right = self.delete(root.right, key)
        # delete from the left subtree
        elif key < root.val:
            root.left = self.delete(root.left, key)
        # delete the current node
        else:
            # the node is a leaf
            if not (root.left or root.right):
                root = None
            # the node is not a leaf and has a right child
            elif root.right:
                root.val = self.successor(root).val
                root.right = self.delete(root.right, root.val)
            # the node is not a leaf, has no right child, and has a left child
            else:
                root.val = self.predecessor(root).val
                root.left = self.delete(root.left, root.val)

        return root

    # One step right and then always left
    def successor(self, node: TreeNode) -> TreeNode:
            node = node.right
            while node.left:
                node = node.left
            return node

    # One step left and then always right
    def predecessor(self, node: TreeNode) -> TreeNode:
        node = node.left
        while node.right:
            node = node.right
        return node
