# https://leetcode.com/problems/three-divisors/

"""
Example 1:
Input: n = 2
Output: false
Explantion: 2 has only two divisors: 1 and 2.

Example 2:
Input: n = 4
Output: true
Explantion: 4 has three divisors: 1, 2, and 4.
"""


n = 9

class Solution:
    def isThree(self, n: int) -> bool:
        if n < 4:
            return False
        tmp = 0
        for i in range(2, n):
            if n%i == 0:
                tmp += 1
            if tmp > 1:
                return False
        return True if tmp == 1 else False


# 227 / 227 test cases passed.
# Status: Accepted
# Runtime: 33 ms
# Memory Usage: 13.9 MB


solution = Solution()
print(solution.isThree(n))

