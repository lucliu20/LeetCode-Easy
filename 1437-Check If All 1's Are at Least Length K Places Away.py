# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/


"""
Example 1:
Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.

Example 2:
Input: nums = [1,0,0,1,0,1], k = 2
Output: false
Explanation: The second 1 and third 1 are only one apart from each other.

Example 3:
Input: nums = [1,1,1,1,1], k = 0
Output: true

Example 4:
Input: nums = [0,1,0,1], k = 1
Output: true
"""

# nums, k = [1,0,0,0,1,0,0,1], 2
# nums, k = [1,0,0,1,0,1], 2
# nums, k = [1,1,1,1,1], 0
# nums, k = [0,1,0,1], 1
# nums, k = [0,1,0,0,0,1], 1
nums, k = [1], 1

class Solution:
    def kLengthApart(self, nums: list(), k: int) -> bool:
        anchor, diff = 0, float("inf")
        for i in range(len(nums)):
            if i == 0 and nums[i] == 1:
                anchor = 1
            elif nums[i] == 1:
                diff = i - anchor
                anchor = i + 1
            if diff < k:
                return False
        return True

solution = Solution()
print(solution.kLengthApart(nums, k))

# Runtime: 572 ms, faster than 54.18% of Python3 online submissions for Check If All 1's Are at Least Length K Places Away.
# Memory Usage: 17 MB, less than 65.42% of Python3 online submissions for Check If All 1's Are at Least Length K Places Away.


