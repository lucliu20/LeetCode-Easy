# https://leetcode.com/problems/single-number/

"""
Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
"""

nums = [2,2,1]
# nums = [4,1,2,1,2]
# nums = [1]

# Hash Table way
# import collections
# class Solution:
#     def singleNumber(self, nums: list()) -> int:
#         d = collections.Counter(nums)
#         for key, val in d.items():
#             if val == 1:
#                 return key

# Runtime: 124 ms, faster than 94.01% of Python3 online submissions for Single Number.
# Memory Usage: 16.8 MB, less than 23.19% of Python3 online submissions for Single Number.

# Bit Manipulation (LeetCode solution #4)
# Concept
# If we take XOR of zero and some bit, it will return that bit
# a⊕0=a
# If we take XOR of two same bits, it will return 0
# a⊕a=0
# a⊕b⊕a=(a⊕a)⊕b=0⊕b=b
# So we can XOR all bits together to find the unique number.
class Solution:
    def singleNumber(self, nums: list()) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a

solution = Solution()
print(solution.singleNumber(nums))



