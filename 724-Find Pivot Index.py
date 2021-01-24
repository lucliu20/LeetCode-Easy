# https://leetcode.com/problems/find-pivot-index/

"""
Example 1:
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.

Example 2:
Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
"""

# nums = [1,7,3,6,5,6]
nums = [1,2,3]

class Solution:
    def pivotIndex(self, nums: list()) -> int:
        r, l = sum(nums), 0
        for i in range(len(nums)):
            r -= nums[i]
            if r == l:
                return i
            l += nums[i]
        return -1

solution = Solution()
print(solution.pivotIndex(nums))

# Runtime: 136 ms, faster than 98.55% of Python3 online submissions for Find Pivot Index.
# Memory Usage: 15.5 MB, less than 41.84% of Python3 online submissions for Find Pivot Index.


