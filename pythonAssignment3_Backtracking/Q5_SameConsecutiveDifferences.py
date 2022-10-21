# https://leetcode.com/problems/numbers-with-same-consecutive-differences/

# using set() to avoid duplicates
# time: O(2^n)
# space: O(2^n)

from typing import List


class Solution5:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        if N == 1:
            return [i for i in range(10)]

        res = []

        def dfs(start: int, num: int) -> None:
            if start == 0:
                return res.append(num)

            tail_digit = num % 10
            # using set() to avoid duplicates when K == 0
            next_digits = {tail_digit + K, tail_digit - K}

            for digit in next_digits:
                if 0 <= digit <= 9:
                    new_num = num * 10 + digit
                    dfs(start - 1, new_num)

        for i in range(1, 10):
            dfs(N - 1, i)

        return res
