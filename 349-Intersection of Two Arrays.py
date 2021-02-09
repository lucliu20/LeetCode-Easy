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

# import collections
# class Solution:
#     def intersection(self, nums1: list(), nums2: list()) -> list():
#         d1 = collections.Counter(nums1)
#         d2 = collections.Counter(nums2)
#         res = []
#         for key in d1.keys():
#             if key in d2.keys():
#                 res.append(key)
#         return res

# Runtime: 44 ms, faster than 78.37% of Python3 online submissions for Intersection of Two Arrays.
# Memory Usage: 14.6 MB, less than 13.91% of Python3 online submissions for Intersection of Two Arrays.


# Binary Search
class Solution:
    def intersection(self, nums1: list(), nums2: list()) -> list():
        if len(nums1) < len(nums2):
            nums1,nums2 = nums2,nums1
        res = []
        nums1 = sorted(nums1)
        nums2 = set(nums2)
        for i in nums2:
            l,r = 0,len(nums1)-1
            while l <=r:
                m = (l+r)>>1
                if nums1[m] == i:
                    res.append(i)
                    break
                else:
                    if nums1[m] < i:
                        l = m + 1
                    else:
                        r = m - 1
        return res


# Runtime: 48 ms, faster than 55.02% of Python3 online submissions for Intersection of Two Arrays.
# Memory Usage: 14.6 MB, less than 14.99% of Python3 online submissions for Intersection of Two Arrays.


solution = Solution()
print(solution.intersection(nums1, nums2))




