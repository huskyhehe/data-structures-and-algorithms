# https://leetcode.com/problems/combination-sum/

# time: O( n ^ (t/m + 1))       t = target, n = len(candidates)
# space: O(t/m)

from typing import List


class Solution1:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtracking(start: int, remain: int, comb: List[int]) -> None:
            if remain == 0:
                res.append(comb[:])
                return

            if remain <= 0:
                return

            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                backtracking(i, remain - candidates[i], comb)
                comb.pop()

        backtracking(0, target, [])
        return res

