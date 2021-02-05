# https://leetcode.com/problems/guess-number-higher-or-lower/

"""
Example 1:
Input: n = 10, pick = 6
Output: 6

Example 2:
Input: n = 1, pick = 1
Output: 1

Example 3:
Input: n = 2, pick = 1
Output: 1

Example 4:
Input: n = 2, pick = 2
Output: 2
"""

n, pick = 10, 6

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            mid = left + (right - left) // 2
            tmp = guess(mid)
            if tmp == 1:
                left = mid + 1
            elif tmp == -1:
                right = mid - 1
            elif tmp == 0:
                return mid

solution = Solution()
print(solution.guessNumber(n))

# Runtime: 32 ms, faster than 56.47% of Python3 online submissions for Guess Number Higher or Lower.
# Memory Usage: 14 MB, less than 91.58% of Python3 online submissions for Guess Number Higher or Lower.
