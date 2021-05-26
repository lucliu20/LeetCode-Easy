# https://leetcode.com/problems/counting-bits/

"""
Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
"""


# n = 2
# n = 5
# n = 32
n = 129


"""
Illustraion of n = 32:
power   2**power       Decimal	    Binary     dp[i]
-           -          0	        0           0       >> base case

0           1          1	        1           1       >> dp[0]+1

1           2          2	        10          1       >> dp[0]+1
                       3	        11          2       >> dp[1]+1

2           4          4	        100         1       >> dp[0]+1
                       5	        101         2       >> dp[1]+1
                       6	        110         2       >> dp[2]+1
                       7	        111         3       >> dp[3]+1

3           8          8	        1000        1       >> dp[0]+1
                       9	        1001        2       >> dp[1]+1
                       10	        1010        2       >> dp[2]+1
                       11	        1011        3       >> dp[3]+1
                       12	        1100        2       >> dp[4]+1
                       13	        1101        3       >> dp[5]+1
                       14	        1110        3       >> dp[6]+1
                       15	        1111        4       >> dp[7]+1

4           16         16	        10000       ... ...
                       17	        10001
                       18	        10010
                       19	        10011
                       20	        10100
                       21	        10101
                       22	        10110
                       23	        10111
                       24	        11000
                       25	        11001
                       26	        11010
                       27	        11011
                       28	        11100
                       29	        11101
                       30	        11110
                       31	        11111
5           32         32	        100000
"""


from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]*(n+1)
        power = 0
        for i in range(1, n+1):
            if i == 2**power:
                j = 0
            dp[i] = dp[j] + 1
            if (power == 0) or (i == 2**(power+1) - 1):
                power += 1
            j += 1
        return dp


# Runtime: 116 ms, faster than 29.06% of Python3 online submissions for Counting Bits.
# Memory Usage: 20.8 MB, less than 91.38% of Python3 online submissions for Counting Bits.


solution = Solution()
print(solution.countBits(n))


