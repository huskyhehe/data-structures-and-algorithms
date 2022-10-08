from typing import Optional

from BinaryTree import TreeNode


def preorder_traversal(root: Optional[TreeNode]):
    if not root:
        return
    print(root.val, end=" -> ")
    preorder_traversal(root.left)
    preorder_traversal(root.right)


def inorder_traversal(root: Optional[TreeNode]):
    if not root:
        return
    inorder_traversal(root.left)
    print(root.val, end=" -> ")
    inorder_traversal(root.right)


def postorder_traversal(root: Optional[TreeNode]):
    if not root:
        return
    inorder_traversal(root.left)
    inorder_traversal(root.right)
    print(root.val, end=" -> ")


if __name__ == "__main__":
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right.left = TreeNode(6)
    root1.right.right = TreeNode(7)
    root1.left.left.left = TreeNode(8)
    '''
                       1
                    /     \
                  2         3
                /   \     /   \
               4    5     6    7
             /
            8
    '''
    root2 = TreeNode(2)
    root2.right = TreeNode(3)
    root2.right.left = TreeNode(4)
    root2.right.left.right = TreeNode(5)
    '''
                   2
                    \
                     3
                    /   
                   4
                    \ 
                     5
    '''
    print("Inorder")
    inorder_traversal(root1)
    print("\nPreorder")
    preorder_traversal(root1)
    print("\nPostorder")
    postorder_traversal(root1)

    print("\nInorder")
    inorder_traversal(root2)
    print("\nPreorder")
    preorder_traversal(root2)
    print("\nPostorder")
    postorder_traversal(root2)
