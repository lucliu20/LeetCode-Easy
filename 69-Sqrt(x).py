# https://leetcode.com/problems/sqrtx/

"""
Example 1:
Input: x = 4
Output: 2

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
"""

x = 9

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            mid = left + (right-left)//2
            if (mid*mid < x and (mid+1)*(mid+1) > x) or mid*mid == x:
                return mid
            elif mid*mid > x:
                right = mid-1
            elif mid*mid < x:
                left = mid+1

    
solution = Solution()
print(solution.mySqrt(x))

# Runtime: 36 ms, faster than 65.13% of Python3 online submissions for Sqrt(x).
# Memory Usage: 14.2 MB, less than 44.05% of Python3 online submissions for Sqrt(x).

