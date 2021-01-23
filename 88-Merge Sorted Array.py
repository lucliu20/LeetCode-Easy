# https://leetcode.com/problems/merge-sorted-array/

"""
Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
"""

# nums1, m, nums2, n = [1,2,3,0,0,0], 3, [2,5,6], 3
nums1, m, nums2, n = [1], 1, [], 0

# Two-pointer
# Iterate from both tails, insert from the num1 tail
class Solution:
    def merge(self, nums1: list(), m: int, nums2: list(), n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m-1, n-1
        for k in range(len(nums1)-1, -1, -1):
            if i in range(m) and j in range(n):
                if nums1[i] < nums2[j]:
                    nums1[k] = nums2[j]
                    j -= 1
                else:
                    nums1[k] = nums1[i]
                    i -= 1
            elif i in range(m):
                nums1[k] = nums1[i]
                i -= 1
            elif j in range(n):
                nums1[k] = nums2[j]
                j -= 1

solution = Solution()
solution.merge(nums1, m, nums2, n)
print(nums1)

# Runtime: 40 ms, faster than 45.59% of Python3 online submissions for Merge Sorted Array.
# Memory Usage: 14.2 MB, less than 65.17% of Python3 online submissions for Merge Sorted Array.

