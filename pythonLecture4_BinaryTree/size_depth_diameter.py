from typing import Optional

from BinaryTree import TreeNode


def get_size(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + get_size(root.left) + get_size(root.right)


# A binary tree's maximum depth (= height) is the number of nodes
# along the longest path from the root node down to the farthest leaf node.

def get_max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    left_depth = get_max_depth(root.left)
    right_depth = get_max_depth(root.right)
    return max(left_depth, right_depth) + 1


# The minimum depth is the number of nodes
# along the shortest path from the root node down to the nearest leaf node.

def get_min_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    left_depth = get_min_depth(root.left)
    right_depth = get_max_depth(root.right)

    if left_depth == 0:
        return right_depth + 1
    if right_depth == 0:
        return left_depth + 1
    return min(left_depth, right_depth) + 1


# the length of the longest path between any two nodes in a tree.
# This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.
def get_diameter(root: Optional[TreeNode]):
    diameter = 0

    def get_node_max_depth(node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        # recursively find the longest path in both left child and right child
        left_depth = get_node_max_depth(node.left)
        right_depth = get_node_max_depth(node.right)

        # update the diameter if left_path plus right_path is larger
        nonlocal diameter
        diameter = max(diameter, left_depth + right_depth)

        return max(left_depth, right_depth) + 1

    get_node_max_depth(root)
    return diameter


# def get_path_sum(root: Optional[TreeNode]):


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
    print("size: ")
    print(get_size(root1))
    print("max depth:")
    print(get_max_depth(root1))
    print("min depth:")
    print(get_min_depth(root1))
    print("diameter:")
    print(get_diameter(root1))

    print("size: ")
    print(get_size(root2))
    print("max depth:")
    print(get_max_depth(root2))
    print("min depth:")
    print(get_min_depth(root2))
    print("diameter:")
    print(get_diameter(root2))
