# [198. House Robber]
# (https://leetcode.com/problems/house-robber/)

# [746. Min Cost Climbing Stairs]
# (https://leetcode.com/problems/min-cost-climbing-stairs/)

from typing import List


class Robber:
    # time: O(n)
    # space: O(n)
    def rob_top_down_memo(self, nums: List[int]) -> int:
        memo = {}

        def dp(i):
            if i == 0:
                return 0
            if i == 1:
                return nums[0]
            if i in memo:
                return memo[i]
            memo[i] = max(dp(i - 1), dp(i - 2) + nums[i - 1])
            return memo[i]

        return dp(len(nums))

    # time: O(n)
    # space: O(1)
    def rob_bottom_up(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        dp = [0] * (n + 1)
        dp[1] = nums[0]

        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])

        print(dp)
        return dp[n]

    # time: O(n)
    # space: O(1)
    def rob_bottom_up_optimized_space(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        pre = 0
        cur = 0

        for num in nums:
            pre, cur = cur, max(cur, pre + num)

        return cur


class Cost:
    # time: O(n)
    # space: O(n)
    def minCostClimbingStairs_bottom_up(self, cost: List[int]) -> int:
        # The array's length should be 1 longer than the length of cost
        # This is because we can treat the "top floor" as a step to reach
        n = len(cost)
        dp = [0] * (n + 1)                      # dp here means min cost at ith stair

        # Start iteration from step 2, since the minimum cost of reaching
        # step 0 and step 1 is 0
        for i in range(2, n + 1):
            one_step = dp[i - 1] + cost[i - 1]
            two_steps = dp[i - 2] + cost[i - 2]
            dp[i] = min(one_step, two_steps)

        return dp[n]

    # time: O(n)
    # space: O(n)
    def minCostClimbingStairs_top_down_memo(self, cost: List[int]) -> int:
        memo = {}

        def dp(i):                              # dp here means min cost
            if i <= 1:
                return 0
            if i in memo:
                return memo[i]
            one_step = dp(i - 1) + cost[i - 1]
            two_steps = dp(i - 2) + cost[i - 2]
            memo[i] = min(one_step, two_steps)
            return memo[i]

        dp(len(cost))
        return memo[len(cost)]


