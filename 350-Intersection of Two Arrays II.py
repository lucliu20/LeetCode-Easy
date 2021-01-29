# https://leetcode.com/problems/intersection-of-two-arrays-ii/

"""
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
"""

# nums1, nums2 = [1,2,2,1], [2,2]
nums1, nums2 = [4,9,5], [9,4,9,8,4]

import collections
class Solution:
    def intersect(self, nums1: list(), nums2: list()) -> list():
        d1 = collections.Counter(nums1)
        d2 = collections.Counter(nums2)
        res = []
        for key, val in d1.items():
            if key in d2:
                t = [key]*min(d2[key], val)
                res.extend(t)
        return res

solution = Solution()
print(solution.intersect(nums1, nums2))

# Runtime: 48 ms
# Memory Usage: 14.4 MB


