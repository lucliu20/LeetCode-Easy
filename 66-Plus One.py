# https://leetcode.com/problems/plus-one/

"""
Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

Example 3:
Input: digits = [0]
Output: [1]
"""

# digits = [1,2,3]
# digits = [4,3,2,1]
# digits = [0]
# digits = [9,9,9]
digits = [8,9,9,9]

class Solution:
    def plusOne(self, digits: list()) -> list():
        c = 0
        for i in range(len(digits)-1, -1, -1):
            if digits[i]+1 == 10:
                c = 1
                digits[i] = 0
            else:
                if c == 1:
                    digits[i] += c
                    c = 0
                else:
                    digits[i] += 1
                break
        if c == 1:
            digits.insert(0, c)
        return digits


solution = Solution()
print(solution.plusOne(digits))

# Runtime: 32 ms, faster than 69.29% of Python3 online submissions for Plus One.
# Memory Usage: 14.2 MB, less than 48.99% of Python3 online submissions for Plus One.


