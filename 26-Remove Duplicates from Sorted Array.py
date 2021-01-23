# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

"""
Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2]
Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. 
It doesn't matter what you leave beyond the returned length.

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4]
Explanation: Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively. 
It doesn't matter what values are set beyond the returned length.
"""

# nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,4]

class Solution:
    def removeDuplicates(self, nums: list()) -> int:
        i = 0
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i+1

solution = Solution()
print(solution.removeDuplicates(nums))

# Runtime: 76 ms
# Memory Usage: 15.6 MB

