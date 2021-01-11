# https://leetcode.com/problems/fibonacci-number/

"""
Example 1:
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
"""

n = 4

# Recrusive with Memoization
class Solution:
    def fib(self, n: int) -> int:
        md = {}
        def helper(n):
            if n in md:
                return md[n]
            if n < 2: return n
            else:
                val = helper(n-1) + helper(n-2)
            md[n] = val
            return val
        
        return helper(n)

solution = Solution()
print(solution.fib(n))

# Runtime: 32 ms
# Memory Usage: 14.3 MB


