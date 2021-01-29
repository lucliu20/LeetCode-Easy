# https://leetcode.com/problems/contains-duplicate-ii/

"""
Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""

# nums, k = [1,2,3,1], 3
# nums, k = [1,0,1,1], 1
nums, k = [1,2,3,1,2,3], 2

import collections
class Solution:
    def containsNearbyDuplicate(self, nums: list(), k: int) -> bool:
        d = collections.defaultdict(list)
        for i in range(len(nums)):
            d[nums[i]].append(i)
            if len(d[nums[i]]) > 1:
                t = d[nums[i]][-1] - d[nums[i]][-2]
                if t <= k:
                    return True
        return False

solution = Solution()
print(solution.containsNearbyDuplicate(nums, k))

# Runtime: 132 ms, faster than 7.48% of Python3 online submissions for Contains Duplicate II.
# Memory Usage: 26.1 MB, less than 6.60% of Python3 online submissions for Contains Duplicate II.


