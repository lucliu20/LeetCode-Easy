# https://leetcode.com/problems/remove-element/

"""
Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2]
Explanation: Your function should return length = 2, with the first two elements of nums being 2.
It doesn't matter what you leave beyond the returned length. For example if you return 2 with nums = [2,2,3,3] or nums = [2,2,0,0], 
your answer will be accepted.

Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3]
Explanation: Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4. 
Note that the order of those five elements can be arbitrary. It doesn't matter what values are set beyond the returned length.
"""

# nums, val = [3,2,2,3], 3
# nums, val = [0,1,2,2,3,0,4,2], 2
# nums, val = [], 0 # None, []
# nums, val = [4,5], 4 # 1, [5,4]
# nums, val = [3,3], 3 # None, []
nums, val = [1], 1 # None, []

class Solution:
    def removeElement(self, nums: list(), val: int) -> int:
        if not nums: return None
        i, j = 0, len(nums)-1
        while i <= j:
            if nums[i] == val:
                if nums[j] == val:
                    j -= 1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
            else:
                i += 1
        if j < 0:
            nums.clear()
            return None
        elif nums[j] == val:
            return j
        else:
            return j+1

solution = Solution()
print(solution.removeElement(nums, val), nums)

# Runtime: 28 ms, faster than 92.93% of Python3 online submissions for Remove Element.
# Memory Usage: 14.3 MB, less than 48.61% of Python3 online submissions for Remove Element.

