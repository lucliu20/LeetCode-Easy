# https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/
# My post:
# https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/discuss/1270113/Python-3-Brute-Force-Easy-Understanding


"""
Example 1:
Input: ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5
Output: true
Explanation: Every integer between 2 and 5 is covered:
- 2 is covered by the first range.
- 3 and 4 are covered by the second range.
- 5 is covered by the third range.

Example 2:
Input: ranges = [[1,10],[10,20]], left = 21, right = 21
Output: false
Explanation: 21 is not covered by any range.
"""


ranges, left, right = [[1,2],[3,4],[5,6]], 2, 5
# ranges, left, right = [[1,10],[10,20]], 21, 21
# Test case #97:
# ranges, left, right = [[37,49],[5,17],[8,32]], 29, 49 # it requires every numbers from 29 to 49 inclusive are in the ranges, expected: False




# Brute Force
from typing import List
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for n in range(left, right+1):
            found= False    
            for s, e in ranges:
                if n in range(s, e+1):
                    found = True
                    break
            if found == False:
                return False
        return True

# Runtime: 44 ms, faster than 66.67% of Python3 online submissions for Check if All the Integers in a Range Are Covered.
# Memory Usage: 14.3 MB, less than 66.67% of Python3 online submissions for Check if All the Integers in a Range Are Covered.


solution = Solution()
print(solution.isCovered(ranges, left, right))



