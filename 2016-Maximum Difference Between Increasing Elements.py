# https://leetcode.com/problems/maximum-difference-between-increasing-elements/

"""
Example 1:
Input: nums = [7,1,5,4]
Output: 4
Explanation:
The maximum difference occurs with i = 1 and j = 2, nums[j] - nums[i] = 5 - 1 = 4.
Note that with i = 1 and j = 0, the difference nums[j] - nums[i] = 7 - 1 = 6, but i > j, so it is not valid.

Example 2:
Input: nums = [9,4,3,2]
Output: -1
Explanation:
There is no i and j such that i < j and nums[i] < nums[j].

Example 3:
Input: nums = [1,5,2,10]
Output: 9
Explanation:
The maximum difference occurs with i = 0 and j = 3, nums[j] - nums[i] = 10 - 1 = 9.
"""

nums = [7,1,5,4]
# nums = [9,4,3,2]
# nums = [1,5,2,10]


from typing import List

# Time complexity: O(N**2)
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = -1
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    res = max(res, nums[j] - nums[i])
        return res

# 54 / 54 test cases passed.
# Runtime: 360 ms
# Memory Usage: 14.4 MB


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res, m = -1, float("inf")
        for i, n in enumerate(nums):
            if i > 0 and n > m:
                res = max(res, n - m)
            m = min(m, n)
        return res

# Runtime: 36 ms, faster than 99.33% of Python3 online submissions for Maximum Difference Between Increasing Elements.
# Memory Usage: 14.4 MB, less than 41.09% of Python3 online submissions for Maximum Difference Between Increasing Elements.


solution = Solution()
print(solution.maximumDifference(nums))
