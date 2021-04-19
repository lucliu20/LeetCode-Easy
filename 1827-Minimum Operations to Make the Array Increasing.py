# https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/

"""
Example 1:
Input: nums = [1,1,1]
Output: 3
Explanation: You can do the following operations:
1) Increment nums[2], so nums becomes [1,1,2].
2) Increment nums[1], so nums becomes [1,2,2].
3) Increment nums[2], so nums becomes [1,2,3].

Example 2:
Input: nums = [1,5,2,4,1]
Output: 14

Example 3:
Input: nums = [8]
Output: 0
"""

nums = [1,1,1]
# nums = [1,5,2,4,1]
# nums = [8]


from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)-1):
            if nums[i+1] <= nums[i]:
                res += (nums[i] - nums[i+1] + 1)
                nums[i+1] += (nums[i] - nums[i+1] + 1)
        return res


solution = Solution()
print(solution.minOperations(nums))

# Runtime: 156 ms, faster than 100.00% of Python3 online submissions for Minimum Operations to Make the Array Increasing.
# Memory Usage: 14.9 MB, less than 100.00% of Python3 online submissions for Minimum Operations to Make the Array Increasing.

