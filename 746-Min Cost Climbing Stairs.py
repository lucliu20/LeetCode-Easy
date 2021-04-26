# https://leetcode.com/problems/min-cost-climbing-stairs/
# My post:
# https://leetcode.com/problems/min-cost-climbing-stairs/discuss/1176657/Python-3-Recursion-and-iteration-DP-Memorization-Explained


"""
Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: Cheapest is: start on cost[1], pay that cost, and go to the top.

Example 2:
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: Cheapest is: start on cost[0], and only step on 1s, skipping cost[3].
"""


# cost = [10,15,20]
cost = [1,100,1,1,1,100,1,1,100,1]


# DP iteratively
from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # the array dp is initialized with one more element space, the last space represents the top of the floor
        # i.e. [10,15,20,top]
        dp = [-1 for _ in range(len(cost)+1)]
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)+1):
            if i < len(cost):
                dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
            else:
                dp[i] = min(dp[i-1], dp[i-2])
        return dp[len(cost)]


# Runtime: 56 ms, faster than 70.14% of Python3 online submissions for Min Cost Climbing Stairs.
# Memory Usage: 14.6 MB, less than 18.61% of Python3 online submissions for Min Cost Climbing Stairs.



# DP recursively
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def helper(memo, length):
            if length == 0 or length == 1: # Base cases
                memo[length] = cost[length]
                return memo[length]
            if memo[length] != -1: # memorization kicks in
                return memo[length]
            if length < len(cost):
                memo[length] = min(helper(memo, length-1), helper(memo, length-2)) + cost[length]
            else: # compute the last element ("top" position), there's no cost at the "top" position 
                memo[length] = min(helper(memo, length-1), helper(memo, length-2))
            return memo[length]
        
        # the array memo is initialized with one more element space, the last space represents the top of the floor
        # i.e. memo = [-1,-1,-1,"top"]
		# at the end, return the last element of array memo
        memo = [-1 for _ in range(len(cost)+1)]
        return helper(memo, len(cost))


# Runtime: 56 ms, faster than 70.14% of Python3 online submissions for Min Cost Climbing Stairs.
# Memory Usage: 15.7 MB, less than 7.11% of Python3 online submissions for Min Cost Climbing Stairs.


solution = Solution()
print(solution.minCostClimbingStairs(cost))


