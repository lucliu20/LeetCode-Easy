# https://leetcode.com/problems/largest-number-at-least-twice-of-others/

"""
Example 1:
Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.

Example 2:
Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.
"""

# nums = [3, 6, 1, 0]
nums = [1, 2, 3, 4]

class Solution:
    def dominantIndex(self, nums: list()) -> int:
        l = max(nums)
        h = l/2
        for n in nums:
            if n != l:
                if n > h:
                    return -1
        return nums.index(l)

solution = Solution()
print(solution.dominantIndex(nums))

# Runtime: 32 ms, faster than 87.61% of Python3 online submissions for Largest Number At Least Twice of Others.
# Memory Usage: 14.1 MB, less than 91.00% of Python3 online submissions for Largest Number At Least Twice of Others.


