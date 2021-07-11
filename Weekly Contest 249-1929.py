# https://leetcode.com/problems/concatenation-of-array/

"""
Example 1:
Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]

Example 2:
Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]
"""

nums = [1,3,2,1]


from typing import List
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = nums.copy()
        res.extend(res)
        return res


solution = Solution()
print(solution.getConcatenation(nums))


# 91 / 91 test cases passed.
# Status: Accepted
# Runtime: 108 ms
# Memory Usage: 14.4 MB