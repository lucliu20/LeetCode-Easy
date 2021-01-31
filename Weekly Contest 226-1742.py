
"""
Example 1:
Input: lowLimit = 1, highLimit = 10
Output: 2
Explanation:
Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
Ball Count:  2 1 1 1 1 1 1 1 1 0  0  ...
Box 1 has the most number of balls with 2 balls.
Example 2:
Input: lowLimit = 5, highLimit = 15
Output: 2
Explanation:
Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
Ball Count:  1 1 1 1 2 2 1 1 1 0  0  ...
Boxes 5 and 6 have the most number of balls with 2 balls in each.
Example 3:
Input: lowLimit = 19, highLimit = 28
Output: 2
Explanation:
Box Number:  1 2 3 4 5 6 7 8 9 10 11 12 ...
Ball Count:  0 1 1 1 1 1 1 1 1 2  0  0  ...
Box 10 has the most number of balls with 2 balls.
"""

# lowLimit, highLimit = 1, 10
# lowLimit, highLimit = 5, 15
# lowLimit, highLimit = 19, 28
lowLimit, highLimit = 11, 104

import collections
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d = collections.Counter()
        res = 0
        for n in range(lowLimit, highLimit+1):
            t = 0
            for c in str(n):
                t += int(c)
            d[t] += 1
            res = max(d[t], res)

        return res

solution = Solution()
print(solution.countBalls(lowLimit, highLimit))

# 

