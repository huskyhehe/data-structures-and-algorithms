# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# time: O(4^n * n)
# space: O(n)

from typing import List


class Solution3:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []
        letters_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"}

        def backtracking(start: int, comb: List[str]):
            if len(comb) == len(digits):
                res.append("".join(comb))
                return
            possible_letters = letters_map[digits[start]]
            for letter in possible_letters:
                comb.append(letter)
                backtracking(start + 1, comb)
                comb.pop()

        backtracking(0, [])
        return res
