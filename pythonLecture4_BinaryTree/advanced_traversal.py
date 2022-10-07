import collections
from typing import Optional, List

from BinaryTree import TreeNode


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    res = []
    queue = collections.deque()
    queue.append(root)

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            cur_node = queue.popleft()
            level.append(cur_node.val)

            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)

        res.append(level)
    return res


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
    print(level_order(root1))
    print(level_order(root2))

