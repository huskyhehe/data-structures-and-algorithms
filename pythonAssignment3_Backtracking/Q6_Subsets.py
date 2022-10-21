# https://leetcode.com/problems/subsets/

# time: O(2^n * n)
# space: O(n)

from typing import List


class Solution6:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(start: int, subset: List[int]) -> None:
            if len(subset) <= n:
                res.append(subset[:])

            for i in range(start, n):
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()

        backtrack(0, [])
        return res


