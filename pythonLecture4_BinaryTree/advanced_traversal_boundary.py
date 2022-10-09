from typing import Optional, List

from BinaryTree import TreeNode


def boundary(root: Optional[TreeNode]) -> List[int]:
    right_res = []
    left_res = []
    bottom_res = []

    def is_leaves(node) -> bool:
        if node and not node.left and not node.right:
            return True
        return False

    # get the left boundary (notice: different from left side view)
    def get_left_boundary(node) -> None:
        if not node or is_leaves(node):
            return
        left_res.append(node.val)
        if node.left:
            get_left_boundary(node.left)
        else:
            get_left_boundary(node.right)

    # get the right boundary (notice: different from right side view)
    def get_right_boundary(node) -> None:
        if not node or is_leaves(node):
            return
        right_res.append(node.val)
        if node.right:
            get_right_boundary(node.right)
        else:
            get_right_boundary(node.left)

    def get_leaves(node) -> None:
        if not node:
            return
        if is_leaves(node):
            bottom_res.append(node.val)
            return
        if node.left:
            get_leaves(node.left)
        if node.right:
            get_leaves(node.right)

    get_left_boundary(root.left)
    get_leaves(root.left)
    get_leaves(root.right)
    get_right_boundary(root.right)

    return [root.val] + left_res + bottom_res + right_res[::-1]


if __name__ == "__main__":
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right.right = TreeNode(7)
    root1.left.left.left = TreeNode(8)
    '''
                       1
                    /     \
                  2         3
                /   \         \
               4    5          7
              /
             8
    '''
    boundary(root1)
    print(boundary(root1))
