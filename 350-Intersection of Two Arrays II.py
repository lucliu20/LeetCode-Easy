# https://leetcode.com/problems/intersection-of-two-arrays-ii/

"""
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
"""

nums1, nums2 = [1,2,2,1], [2,2]
# nums1, nums2 = [4,9,5], [9,4,9,8,4]

# import collections
# class Solution:
#     def intersect(self, nums1: list(), nums2: list()) -> list():
#         d1 = collections.Counter(nums1)
#         d2 = collections.Counter(nums2)
#         res = []
#         for key, val in d1.items():
#             if key in d2:
#                 t = [key]*min(d2[key], val)
#                 res.extend(t)
#         return res

# Runtime: 48 ms
# Memory Usage: 14.4 MB


# Binary Search
# Keep track of the founded target lower boundary index. Next Binary Search left pointer is equal to that index.
# Time complexity: O(nlogm)
class Solution:
    def intersect(self, nums1: list(), nums2: list()) -> list():
        def helper(arr, lower, target):
            left, right = lower, len(arr)-1
            while left < right:
                mid = left + (right-left) // 2
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        nums1.sort()
        nums2.sort()
        lo = 0
        res = []
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        for i in range(len(nums1)):
            ind = helper(nums2, lo, nums1[i])
            if ind in range(len(nums2)) and nums2[ind] == nums1[i]:
                res.append(nums1[i])
                lo = ind + 1
        return res

# Runtime: 48 ms, faster than 67.95% of Python3 online submissions for Intersection of Two Arrays II.
# Memory Usage: 14.4 MB, less than 72.05% of Python3 online submissions for Intersection of Two Arrays II.

solution = Solution()
print(solution.intersect(nums1, nums2))




