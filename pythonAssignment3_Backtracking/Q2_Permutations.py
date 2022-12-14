# https://leetcode.com/problems/permutations/

# time: O(n * n!)
# space: O(n)

from typing import List


class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(start: int) -> None:
            if start == n:
                res.append(nums[:])
            for i in range(start, n):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return res
