# https://leetcode.com/problems/generate-parentheses/

# time: O(4^n / n)
# space: O(4^n / n)

from typing import List


class Solution7:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def backtracking(left: int, right: int, combo: List[str]):
            if len(combo) == n * 2:
                res.append("".join(combo))
                return

            if left < n:
                combo.append("(")
                backtracking(left + 1, right, combo)
                combo.pop()

            if left > right:
                combo.append(")")
                backtracking(left, right + 1, combo)
                combo.pop()

        backtracking(0, 0, [])
        return res
