"""
Question 5
Write a function where I pass a sorted integer array  and another array of integers
and the function returns me start indexes of those values in second array
"""

# I assumed that the index here begins with 0

# Time: O(m * logn)
# space: O(m)
# m = len(values), n = len(arr)


from typing import List


class Solution5:
    def getStartOfEachValues(self, arr: List[int], values: List[int]):
        res = [0] * len(values)

        def getFirstPos(nums, target) -> int:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left if (0 < left < len(nums) and nums[left] == target) else -1

        for i in range(len(values)):
            res[i] = getFirstPos(arr, values[i])

        return res


if __name__ == "__main__":
    solution5 = Solution5()
    arr = [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 5, 5, 5, 8, 9, 10, 11]
    values = [1, 4, 5, 10]
    print(solution5.getStartOfEachValues(arr, values))
