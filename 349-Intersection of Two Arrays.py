# https://leetcode.com/problems/intersection-of-two-arrays/

"""
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
"""

# nums1, nums2 = [1,2,2,1], [2,2]
nums1, nums2 = [4,9,5], [9,4,9,8,4]

import collections
class Solution:
    def intersection(self, nums1: list(), nums2: list()) -> list():
        d1 = collections.Counter(nums1)
        d2 = collections.Counter(nums2)
        res = []
        for key in d1.keys():
            if key in d2.keys():
                res.append(key)
        return res

solution = Solution()
print(solution.intersection(nums1, nums2))

# Runtime: 44 ms, faster than 78.37% of Python3 online submissions for Intersection of Two Arrays.
# Memory Usage: 14.6 MB, less than 13.91% of Python3 online submissions for Intersection of Two Arrays.


