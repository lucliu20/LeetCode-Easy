# https://leetcode.com/problems/find-the-highest-altitude/

"""
Example 1:
Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

Example 2:
Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.
"""

gain = [-5,1,5,0,-7]
# gain = [-4,-3,-2,-1,4,3,2]

import operator
import itertools
class Solution:
    def largestAltitude(self, gain: list()) -> int:
        gain.insert(0, 0)
        t = list(itertools.accumulate(gain, operator.add))
        return max(t)

solution = Solution()
print(solution.largestAltitude(gain))


# Runtime: 28 ms, faster than 97.27% of Python3 online submissions for Find the Highest Altitude.
# Memory Usage: 14.1 MB, less than 72.00% of Python3 online submissions for Find the Highest Altitude.

