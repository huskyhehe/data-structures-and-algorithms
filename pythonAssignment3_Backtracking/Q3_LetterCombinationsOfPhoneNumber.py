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

        def backtracking(start: int, combo: List[str]):
            if len(combo) == len(digits):
                res.append("".join(combo))
                return
            possible_letters = letters_map[digits[start]]
            for letter in possible_letters:
                combo.append(letter)
                backtracking(start + 1, combo)
                combo.pop()

        backtracking(0, [])
        return res
