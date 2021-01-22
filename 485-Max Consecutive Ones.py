# https://leetcode.com/problems/max-consecutive-ones/

"""
Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
"""

nums = [1,1,0,1,1,1,0,1,1,0]

class Solution:
    def findMaxConsecutiveOnes(self, nums: list()) -> int:
        res, c = 0, 0
        for i in range(len(nums)):
            if nums[i]:
                c += 1
            else:
                res = max(res, c)
                c = 0
        return max(res, c)

solution = Solution()
print(solution.findMaxConsecutiveOnes(nums))

# Runtime: 340 ms, faster than 87.94% of Python3 online submissions for Max Consecutive Ones.
# Memory Usage: 14.4 MB, less than 51.20% of Python3 online submissions for Max Consecutive Ones.


