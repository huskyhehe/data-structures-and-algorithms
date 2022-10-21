# https://leetcode.com/problems/generate-parentheses/

# time: O(4^n / n)
# space: O(4^n / n)

from typing import List


class Solution7:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def backtracking(left: int, right: int, comb: List[str]):
            if len(comb) == n * 2:
                res.append("".join(comb))
                return

            if left < n:
                comb.append("(")
                backtracking(left + 1, right, comb)
                comb.pop()

            if left > right:
                comb.append(")")
                backtracking(left, right + 1, comb)
                comb.pop()

        backtracking(0, 0, [])
        return res
