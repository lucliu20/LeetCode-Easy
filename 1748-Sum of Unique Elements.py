# https://leetcode.com/problems/sum-of-unique-elements/

"""
Example 1:
Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.

Example 2:
Input: nums = [1,1,1,1,1]
Output: 0
Explanation: There are no unique elements, and the sum is 0.

Example 3:
Input: nums = [1,2,3,4,5]
Output: 15
Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.
"""

# nums = [1,2,3,2]
# nums = [1,1,1,1,1]
nums = [1,2,3,4,5]

import collections
class Solution:
    def sumOfUnique(self, nums: list()) -> int:
        d= collections.Counter(nums)
        res = 0
        for key, val in d.items():
            if val == 1:
                res += key
        return res


solution = Solution()
print(solution.sumOfUnique(nums))

# Runtime: 36 ms, faster than 68.56% of Python3 online submissions for Sum of Unique Elements.
# Memory Usage: 13.9 MB, less than 98.46% of Python3 online submissions for Sum of Unique Elements.

