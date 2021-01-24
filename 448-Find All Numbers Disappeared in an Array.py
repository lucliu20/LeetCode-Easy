# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

"""
Example:
Input: [4,3,2,7,8,2,3,1]
Output: [5,6]
"""

nums = [4,3,2,7,8,2,3,1]

# Refer to the post
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/discuss/344583/Python%3A-O(1)-space-solution
# Time: O(n); Space: O(1)
class Solution:
    def findDisappearedNumbers(self, nums: list()) -> list():
        res = []
        for i in range(len(nums)):
            t = abs(nums[i])-1
            if nums[t] > 0:
                nums[t] = -nums[t]
        
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res

solution = Solution()
print(solution.findDisappearedNumbers(nums))

# Runtime: 352 ms, faster than 65.98% of Python3 online submissions for Find All Numbers Disappeared in an Array.
# Memory Usage: 22.3 MB, less than 46.06% of Python3 online submissions for Find All Numbers Disappeared in an Array.


