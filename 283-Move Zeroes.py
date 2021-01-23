# https://leetcode.com/problems/move-zeroes/

"""
Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
"""

# nums = [0,1,0,3,12]
nums = [1]

class Solution:
    def moveZeroes(self, nums: list()) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[j] = nums[i]
                j += 1
        for i in range(j, len(nums)):
            nums[i] = 0

solution = Solution()
solution.moveZeroes(nums)
print(nums)

# Runtime: 44 ms, faster than 92.97% of Python3 online submissions for Move Zeroes.
# Memory Usage: 15.4 MB, less than 20.59% of Python3 online submissions for Move Zeroes.


