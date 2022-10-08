import collections
from typing import List, Optional

from BinaryTree import TreeNode


# what is different with basic level order:
# instead of res.append(level), res.append(level[0])
def left_side_view_bfs(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    res = []
    queue = collections.deque()
    queue.append(root)

    while queue:
        size = len(queue)
        level = []

        for _ in range(size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        res.append(level[0])
    return res


# what is different with basic level order:
# instead of res.append(level), res.append(level[-1])
def right_side_view_bfs(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    res = []
    queue = collections.deque()
    queue.append(root)

    while queue:
        size = len(queue)
        level = []

        for _ in range(size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        res.append(level[-1])
    return res


def left_side_view_dfs(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    left_side = []

    def dfs(node, level: int) -> None:
        if level == len(left_side):
            left_side.append(node.val)

        if node.left:
            dfs(node.left, level + 1)
        if node.right:
            dfs(node.right, level + 1)

    dfs(root, 0)
    return left_side


def right_side_view_dfs(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    right_side = []

    def dfs(node, level: int) -> None:
        if level == len(right_side):
            right_side.append(node.val)

        if node.right:
            dfs(node.right, level + 1)
        if node.left:
            dfs(node.left, level + 1)

    dfs(root, 0)
    return right_side


# bfs
# The idea is that we keep a hash table (let's denote it as columnTable<key, value>),
# where we keep the node values grouped by the column index.
# time: O(N)
# space: O(N)
def vertical_order(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    column_map = collections.defaultdict(list)
    queue = collections.deque()
    queue.append((root, 0))

    min_col = 0
    max_col = 0

    while queue:
        size = len(queue)

        for _ in range(size):
            node, col = queue.popleft()

            if node:
                column_map[col].append(node.val)

                min_col = min(min_col, col)
                max_col = max(max_col, col)

                queue.append((node.left, col - 1))
                queue.append((node.right, col + 1))

    return [column_map[x] for x in range(min_col, max_col + 1)]


if __name__ == "__main__":
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(8)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(0)
    root1.right.left = TreeNode(1)
    root1.right.right = TreeNode(7)
    '''
               3
            /     \
           9       8
          /   \  /   \
         4    0 1     7
    '''
    print(left_side_view_bfs(root1))
    print(left_side_view_dfs(root1))
    print(right_side_view_bfs(root1))
    print(right_side_view_dfs(root1))
    print(vertical_order(root1))
