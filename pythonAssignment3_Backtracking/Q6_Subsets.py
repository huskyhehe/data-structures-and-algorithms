# https://leetcode.com/problems/subsets/

# time: O(2^n * n)
# space: O(n)

from typing import List


class Solution6:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtracking(start: int, subset: List[int]):
            if len(subset) <= n:
                res.append(subset.copy())

            for i in range(start, n):
                subset.append(nums[i])
                backtracking(i + 1, subset)
                subset.pop()

        backtracking(0, [])
        return res


