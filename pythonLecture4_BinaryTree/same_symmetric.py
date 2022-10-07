from typing import Optional

from BinaryTree import TreeNode


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    return p.val == q.val and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


def is_symmetric(root: Optional[TreeNode]) -> bool:
    def is_mirrored(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        return node1.val == node2.val \
               and is_mirrored(node1.left, node2.right) \
               and is_mirrored(node1.right, node2.left)


def mirror_tree(root: Optional[TreeNode]):
    if not root:
        return
    mirror_tree(root.left)
    mirror_tree(root.right)
    root.left, root.right = root.right, root.left


if __name__ == "__main__":
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(4)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(3)
    '''
                           1
                        /     \
                      2         2
                    /   \     /   \
                   3    4     4    3
    '''

    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.right = TreeNode(3)
    root4.left.left = TreeNode(4)
    root4.left.right = TreeNode(5)
