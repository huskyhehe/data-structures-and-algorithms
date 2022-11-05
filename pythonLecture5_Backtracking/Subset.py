# https://leetcode.com/problems/subsets/
# https://leetcode.com/problems/subsets-ii/

from typing import List


class Subset:
    ################## The set only contains unique elements ####################
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

    ################## What if the set contains duplicate elements?###############
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # what is diffrent from subsets:
        # sort the array
        # if equal to its prev, skip

        n = len(nums)
        ##################################
        nums.sort()
        ##################################
        res = []

        def backtrack(start, subset):
            if len(subset) <= n:
                res.append(subset[:])
            for i in range(start, n):
                ##################################################
                if i > start and nums[i] == nums[i - 1]:
                    continue
                ##################################################
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()

        backtrack(0, [])
        return res
