from Q1_RotateArray import Solution1
from Q2_SameTree import Solution2
from Q3_LevelOrderTraversal import Solution3
from TreeNode import TreeNode

if __name__ == '__main__':
    # Question 1 --------------------------------------
    solution1 = Solution1()
    # Example 1:
    # Input: nums = [1,2,3,4,5,6,7], k = 3
    # Output: [5,6,7,1,2,3,4]
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    solution1.rotate_array(nums1, 3)
    print(nums1)
    # Example 2:
    # Input: nums = [-1,-100,3,99], k = 2
    # Output: [3,99,-1,-100]
    nums2 = [-1, -100, 3, 99]
    solution1.rotate_array(nums2, 2)
    print(nums2)

    # Question 2 --------------------------------------
    solution2 = Solution2()
    # Example 1:
    # Input: p = [1,2,3], q = [1,2,3]
    # Output: true
    p1 = TreeNode(1)
    p1.left = TreeNode(2)
    p1.right = TreeNode(3)
    q1 = TreeNode(1)
    q1.left = TreeNode(2)
    q1.right = TreeNode(3)
    print(solution2.is_same_tree(p1, q1))
    # Example 2:
    # Input: p = [1,2], q = [1,null,2]
    # Output: false
    p2 = TreeNode(1)
    p2.left = TreeNode(2)
    q2 = TreeNode(1)
    q2.right = TreeNode(2)
    print(solution2.is_same_tree(p2, q2))

    # Question 3 --------------------------------------
    solution3 = Solution3()
    # Example 1:
    # Input:
    #      1
    #    /   \
    #   2     3
    #  /     /
    # 4     5
    #  \
    #   6
    # Output: [[1], [2, 3], [4, 5], [6]]
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.right.left = TreeNode(5)
    root1.left.left.right = TreeNode(6)
    print(solution3.level_order_traversal(root1))
