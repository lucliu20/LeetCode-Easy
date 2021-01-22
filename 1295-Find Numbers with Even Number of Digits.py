# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

"""
Example 1:
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.

Example 2:
Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.
"""

# nums = [12,345,2,6,7896]
# nums = [555,901,482,1771]
nums = [437,315,322,431,686,264,442]

class Solution:
    def findNumbers(self, nums: list()) -> int:
        r, c = 0, 0
        for i in range(len(nums)):
            t = nums[i]
            while t > 0:
                t //= 10
                c += 1
            if c%2 == 0:
                r += 1
            c = 0
        return r

solution = Solution()
print(solution.findNumbers(nums))

# Runtime: 56 ms, faster than 44.50% of Python3 online submissions for Find Numbers with Even Number of Digits.
# Memory Usage: 14.3 MB, less than 45.21% of Python3 online submissions for Find Numbers with Even Number of Digits.

