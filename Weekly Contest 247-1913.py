# https://leetcode.com/problems/maximum-product-difference-between-two-pairs/

"""
Example 1:
Input: nums = [5,6,2,7,4]
Output: 34
Explanation: We can choose indices 1 and 3 for the first pair (6, 7) and indices 2 and 4 for the second pair (2, 4).
The product difference is (6 * 7) - (2 * 4) = 34.

Example 2:
Input: 
Output: 64
Explanation: We can choose indices 3 and 6 for the first pair (9, 8) and indices 1 and 5 for the second pair (2, 4).
The product difference is (9 * 8) - (2 * 4) = 64.
"""

nums = [5,6,2,7,4]
# nums = [4,2,5,9,7,4,8]


from typing import List
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)-1
        return nums[l]*nums[l-1] - nums[0]*nums[1]


# Runtime: 184 ms
# Memory Usage: 15.4 MB

solution = Solution()
print(solution.maxProductDifference(nums))
