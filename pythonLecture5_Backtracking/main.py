

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        res = []

        def backtrack(start, subset):
            if len(subset) <= n:
                res.append(subset[:])

            for i in range(start, n):
                subset.append(nums[i])
                # pay attention to: start + 1 or i + 1?
                backtrack(i + 1, subset)
                subset.pop()
        backtrack(0, [])
        return res
