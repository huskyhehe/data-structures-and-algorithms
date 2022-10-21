# https://leetcode.com/problems/word-search/

# time: O(3^L * N)  L = len(word), N = len(board) * len(board[0])
# space: O(L)

import collections
from typing import List


class Solution4:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def backtracking(r: int, c: int, idx: int) -> bool:
            if board[r][c] != word[idx]:
                return False
            if idx == len(word) - 1:
                return True
            board[r][c] = '#'

            for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_r = r + direction[0]
                new_c = c + direction[1]
                if 0 <= new_r < len(board) and 0 <= new_c < len(board[0]) and backtracking(new_r, new_c, idx + 1):
                    return True
            board[r][c] = word[idx]

        # To prevent TLE,
        # reverse the word if frequency of the first letter is more than the last letter's
        count = collections.defaultdict(int, sum(map(collections.Counter, board), collections.Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtracking(i, j, 0):
                    return True
        return False
