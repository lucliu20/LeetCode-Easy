# https://leetcode.com/problems/valid-perfect-square/

"""
Example 1:
Input: num = 16
Output: true

Example 2:
Input: num = 14
Output: false
"""

# num = 16
num = 14

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        while left <= right:
            mid = left + (right-left) // 2
            if mid*mid == num:
                return True
            elif mid*mid < num:
                left = mid + 1
            else:
                right = mid - 1
        return False


# Runtime: 28 ms, faster than 85.85% of Python3 online submissions for Valid Perfect Square.
# Memory Usage: 14.3 MB, less than 43.34% of Python3 online submissions for Valid Perfect Square.

solution = Solution()
print(solution.isPerfectSquare(num))


