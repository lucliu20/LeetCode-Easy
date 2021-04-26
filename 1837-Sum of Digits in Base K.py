# https://leetcode.com/problems/sum-of-digits-in-base-k/

"""
Example 1:
Input: n = 34, k = 6
Output: 9
Explanation: 34 (base 10) expressed in base 6 is 54. 5 + 4 = 9.

Example 2:
Input: n = 10, k = 10
Output: 1
Explanation: n is already in base 10. 1 + 0 = 1.
"""


# n, k = 128, 6
# n, k = 10, 10
# n, k = 42, 2
n, k = 68, 2



class Solution:
    def sumBase(self, n: int, k: int) -> int:
        q, base = n, k
        res = 0
        while q > 0:
            res += q%base
            q = q//base
        return res



solution = Solution()
print(solution.sumBase(n, k))

# Runtime: 28 ms, faster than 100.00% of Python3 online submissions for Sum of Digits in Base K.
# Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Sum of Digits in Base K.


