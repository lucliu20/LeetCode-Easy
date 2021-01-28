# https://leetcode.com/problems/contains-duplicate/

"""
Example 1:
Input: [1,2,3,1]
Output: true

Example 2:
Input: [1,2,3,4]
Output: false

Example 3:
Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

# nums = [1,2,3,1]
# nums = [1,2,3,4]
nums = [1,1,1,3,3,4,3,2,4,2]

import collections
class Solution:
    def containsDuplicate(self, nums: list()) -> bool:
        d = collections.Counter(nums)
        for _, val in d.items():
            if val > 1:
                return True
        return False

solution = Solution()
print(solution.containsDuplicate(nums))

# Runtime: 108 ms, faster than 97.28% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 21.5 MB, less than 6.73% of Python3 online submissions for Contains Duplicate.


