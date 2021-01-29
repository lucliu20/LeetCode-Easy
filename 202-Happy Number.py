# https://leetcode.com/problems/happy-number/

"""
Example 1:
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:
Input: n = 2
Output: false
"""

n = 2

# Hash Map & Hash Set
class Solution:
    def isHappy(self, n: int) -> bool:
        power = {0:0, 1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49, 8:64, 9:81}
        dup = set()
        t = n
        while True:
            s = 0
            while t > 0:
                q = t%10
                t = t//10
                s += power[q]
            if s not in dup:
                dup.add(s)
                t = s
            else:
                break
        return s == 1

solution = Solution()
print(solution.isHappy(n))

# Runtime: 32 ms, faster than 84.46% of Python3 online submissions for Happy Number.
# Memory Usage: 14.2 MB, less than 77.95% of Python3 online submissions for Happy Number.


