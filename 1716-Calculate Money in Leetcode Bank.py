# https://leetcode.com/problems/calculate-money-in-leetcode-bank/

"""
Example 1:
Input: n = 4
Output: 10
Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.

Example 2:
Input: n = 10
Output: 37
Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.

Example 3:
Input: n = 20
Output: 96
Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.
"""

# n = 4
# n = 10
n = 20

import itertools
import operator
class Solution:
    def totalMoney(self, n: int) -> int:
        q = n//7
        r = n%7
        base = 28
        res = 0
        for i in range(q):
            res = res + (base + 7*i)
        for j in range(r):
            res = res + (q+1+j)
        return res

solution = Solution()
print(solution.totalMoney(n))

# Runtime: 32 ms, faster than 82.03% of Python3 online submissions for Calculate Money in Leetcode Bank.
# Memory Usage: 14 MB, less than 98.21% of Python3 online submissions for Calculate Money in Leetcode Bank.

