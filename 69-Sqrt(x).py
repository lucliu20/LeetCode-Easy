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

from typing import NoReturn


x = 0

# class Solution:
#     def mySqrt(self, x: int) -> int:
#         left, right = 0, x
#         while left <= right:
#             mid = left + (right-left)//2
#             if (mid*mid < x and (mid+1)*(mid+1) > x) or mid*mid == x:
#                 return mid
#             elif mid*mid > x:
#                 right = mid-1
#             elif mid*mid < x:
#                 left = mid+1

# Runtime: 36 ms, faster than 65.13% of Python3 online submissions for Sqrt(x).
# Memory Usage: 14.2 MB, less than 44.05% of Python3 online submissions for Sqrt(x).


# Attempt to implement with the LeetCode Template II
# Note that the "right" starts as "x+1", and the post-processing needs some tweaks as well to decide whether to return "left" or "left-1".
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x + 1
        while left < right:
            mid = left + (right-left)//2
            if mid*mid >= x:
                right = mid
            else:
                left = mid + 1

        # Post-processing:
        # End Condition: left == right
        if left != x + 1:
            if left*left == x:
                return left
            elif left*left > x:
                return left - 1

# Runtime: 36 ms, faster than 65.16% of Python3 online submissions for Sqrt(x).
# Memory Usage: 14.2 MB, less than 72.82% of Python3 online submissions for Sqrt(x).


solution = Solution()
print(solution.mySqrt(x))



