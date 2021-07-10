# https://leetcode.com/problems/count-square-sum-triples/

"""
Example 1:
Input: n = 5
Output: 2
Explanation: The square triples are (3,4,5) and (4,3,5).

Example 2:
Input: n = 10
Output: 4
Explanation: The square triples are (3,4,5), (4,3,5), (6,8,10), and (8,6,10).
"""



# n = 5
n = 250

class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        myset = set()
        for m in range(1, n+1):
            myset.add(m**2)
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                tmp = i**2 + j**2
                if tmp in myset:
                        res += 1
        return res*2

# 91 / 91 test cases passed.
# Status: Accepted
# Runtime: 540 ms
# Memory Usage: 14.3 MB


solution = Solution()
print(solution.countTriples(n))
