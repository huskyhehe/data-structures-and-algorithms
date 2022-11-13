"""
Question 3
In a Binary search tree print values which are inside of range.
Optimize it if possible
"""

# time: O(n)

from Question3.TreeNode import TreeNode


class Solution3:
    def printValInRange(self, root: TreeNode, low: int, high: int) -> None:
        if not root:
            return

        if root.val > low:
            self.printValInRange(root.left, low, high)

        if low <= root.val <= high:
            print(root.val)

        self.printValInRange(root.right, low, high)


if __name__ == "__main__":
    solution3 = Solution3()

    def getBST():
        root = TreeNode(8)
        root.left = TreeNode(3)
        root.right = TreeNode(10)

        root.left.left = TreeNode(1)
        root.left.right = TreeNode(6)

        root.right.right = TreeNode(14)
        root.left.right.left = TreeNode(4)
        root.left.right.right = TreeNode(17)

        root.right.right.left = TreeNode(13)
        return root


    testRoot = getBST()
    solution3.printValInRange(testRoot, 5, 8)
