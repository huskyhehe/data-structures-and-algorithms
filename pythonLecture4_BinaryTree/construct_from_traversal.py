from typing import List, Optional

from BinaryTree import TreeNode


def build_tree_from_pre_in(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not preorder:
        return None

    root_val = preorder[0]
    root_index = inorder.index(root_val)

    inorder_left = inorder[:root_index]
    inorder_right = inorder[root_index + 1:]

    preorder_left = preorder[1: len(inorder_left) + 1]
    preorder_right = preorder[len(inorder_left) + 1:]

    root = TreeNode(root_val)
    root.left = build_tree_from_pre_in(preorder_left, inorder_left)
    root.right = build_tree_from_pre_in(preorder_right, inorder_right)

    return root


def build_tree_from_in_post(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    if not postorder:
        return None

    root_val = postorder[-1]
    root_index = inorder.index(root_val)

    inorder_left = inorder[:root_index]
    inorder_right = inorder[root_index + 1:]

    postorder_left = postorder[:len(inorder_left)]
    postorder_right = postorder[len(inorder_left):-1]

    root = TreeNode(root_val)
    root.left = build_tree_from_in_post(inorder_left, postorder_left)
    root.right = build_tree_from_in_post(inorder_right, postorder_right)

    return root


# def build_tree_from_pre_post(preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:


if __name__ == "__main__":
    preorder1 = [3, 9, 20, 15, 7]
    inorder1 = [9, 3, 15, 20, 7]
    postorder1 = [9, 15, 7, 20, 3]
    '''
                           3
                        /     \
                      9        20
                              /   \
                             15    7
    '''
    root1 = build_tree_from_pre_in(preorder1, inorder1)
    root1.print_level_order()

    root2 = build_tree_from_in_post(inorder1, postorder1)
    root2.print_level_order()
