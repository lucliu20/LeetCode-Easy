# https://leetcode.com/problems/squares-of-a-sorted-array/

"""
Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""

nums = [-4,-1,0,3,10]
# nums = [-7,-3,2,3,11]
# nums = [0,1,2,3,11]
# nums = [-1]
# nums = [-10000,-9999,-7,-5,0,0,10000]
# nums = [-10000,-9999,-5,-5,0,10000]

# Two pointers
# Time complexity: O(n)
class Solution:
    def sortedSquares(self, nums: list()) -> list():
        res = []
        i = 0
        while  i in range(len(nums)) and nums[i] < 0:
            i += 1
        j = i-1
        while i < len(nums) or j >= 0:
            if i in range(len(nums)) and j in range(len(nums)):
                if nums[i] < abs(nums[j]):
                    res.append(nums[i]*nums[i])
                    i += 1
                else:
                    res.append(nums[j]*nums[j])
                    j -= 1
            elif i not in range(len(nums)):
                res.append(nums[j]*nums[j])
                j -= 1
            elif j not in range(len(nums)):
                res.append(nums[i]*nums[i])
                i += 1
        return res

solution = Solution()
print(solution.sortedSquares(nums))

# Runtime: 276 ms, faster than 17.88% of Python3 online submissions for Squares of a Sorted Array.
# Memory Usage: 16 MB, less than 79.33% of Python3 online submissions for Squares of a Sorted Array.


