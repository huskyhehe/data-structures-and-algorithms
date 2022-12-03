# [70. Climbing Stairs]
# (https://leetcode.com/problems/climbing-stairs/)

class Solution:
    # basic top-down time: O(2^n), because every call to dp creates 2 more calls to dp.
    def climbStairs_top_down_basic(self, n: int) -> int:
        def dp(i):
            if i <= 2:
                return i
            return dp(i - 1) + dp(i - 2)

        return dp(n)

    # with memoization, our top-down time complexity drops to O(n)
    def climbStairs_top_down_memo(self, n: int) -> int:
        memo = {}

        def dp(i):
            if i <= 2:
                return i
            if i in memo:
                return memo[i]
            memo[i] = dp(i - 1) + dp(i - 2)
            return memo[i]

        return dp(n)

    # bottom-up implementations usually use an array, so we will use an array dp,
    # where dp[i] represents the number of ways to climb to the ith step.
    # time & space: O(n)
    def climbStairs_bottom_up(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0] * (n + 1)      # An array that represents the answer to the problem for a given state
        dp[1] = 1               # Base cases
        dp[2] = 2               # Base cases

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]       # Recurrence relation

        return dp[n]



