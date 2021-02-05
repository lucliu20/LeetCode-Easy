# https://leetcode.com/problems/binary-search/

"""
Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""

# nums, target = [-1,0,3,5,9,12], 9
nums, target = [-1,0,3,5,9,12], 2

# Time complexity : O(logN)
# Compute time complexity with the help of master theorem:
# https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms)
class Solution:
    def search(self, nums: list(), target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2 # Prevent overflow
            """
            If you are setting mid= (left+right)/2, you have to be very careful.
            Unless you are using a language that does not overflow such as Python, 
            (left + right) could overflow. One way to fix this is to use left+(right−left)/2 instead.
            """
            if nums[mid] > target:
                right = mid-1
            elif nums[mid] < target:
                left = mid+1
            else:
                return mid
        return -1

solution = Solution()
print(solution.search(nums, target))

# Runtime: 228 ms, faster than 93.27% of Python3 online submissions for Binary Search.
# Memory Usage: 15.7 MB, less than 33.09% of Python3 online submissions for Binary Search.

