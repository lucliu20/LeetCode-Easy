# https://leetcode.com/problems/climbing-stairs/

"""
Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

n = 4

# Recrusive with Memoization
# Same as Fibonacci Number logic
class Solution:
    def climbStairs(self, n: int) -> int:
        md = {}
        def helper(n):
            if n in md:
                return md[n]
            if n < 3:
                return n
            else:
                ways = helper(n-1) + helper(n-2)
            md[n] = ways
            return ways
        
        return helper(n)

solution = Solution()
print(solution.climbStairs(n))

# Runtime: 28 ms, faster than 80.06% of Python3 online submissions for Climbing Stairs.
# Memory Usage: 14.3 MB, less than 40.36% of Python3 online submissions for Climbing Stairs.

