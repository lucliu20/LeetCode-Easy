# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

"""
Example 1:
Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].

Example 2:
Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.

Example 3:
Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.

Example 4:
Input: nums = [1,1,1]
Output: true
Explanation: [1,1,1] is the original sorted array.
You can rotate any number of positions to make nums.

Example 5:
Input: nums = [2,1]
Output: true
Explanation: [1,2] is the original sorted array.
You can rotate the array by x = 5 positions to begin on the element of value 2: [2,1].
"""

nums = [3,4,5,1,2] # True
# nums = [2,1,3,4] # False
# nums = [1,2,3] # True
# nums = [1,1,1] # True
# nums = [2,1] # True

# Note that the first element and the last element are also connected.
# We need to check the element at the end of list with the first element as well
class Solution:
    def check(self, nums: list()) -> bool:
        # When i = 0, we are comparing the first and the last elements.
        return sum((nums[i-1] > nums[i]) for i in range(len(nums))) <= 1
                
# Runtime: 28 ms, faster than 100.00% of Python3 online submissions for Check if Array Is Sorted and Rotated.
# Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Check if Array Is Sorted and Rotated.

solution = Solution()
print(solution.check(nums))

# 

