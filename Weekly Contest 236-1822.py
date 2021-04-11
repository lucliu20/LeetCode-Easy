# https://leetcode.com/problems/sign-of-the-product-of-an-array/

"""
Example 1:
Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1
Explanation: The product of all values in the array is 144, and signFunc(144) = 1

Example 2:
Input: nums = [1,5,0,2,-3]
Output: 0
Explanation: The product of all values in the array is 0, and signFunc(0) = 0

Example 3:
Input: nums = [-1,1,-1,1,-1]
Output: -1
Explanation: The product of all values in the array is -1, and signFunc(-1) = -1
"""


nums = [-1,-2,-3,-4,3,2,1]


from typing import List
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        positive, negative, zero = 0, 0, 0
        for n in nums:
            if n == 0:
                return 0
            elif n < 0:
                negative += 1
        return 1 if negative%2 == 0 else -1


solution = Solution()
print(solution.arraySign(nums))

# Runtime: 56 ms
# Memory Usage: 14.5 MB