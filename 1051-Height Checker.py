# https://leetcode.com/problems/height-checker/

"""
Example 1:
Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation: 
Current array : [1,1,4,2,1,3]
Target array  : [1,1,1,2,3,4]
On index 2 (0-based) we have 4 vs 1 so we have to move this student.
On index 4 (0-based) we have 1 vs 3 so we have to move this student.
On index 5 (0-based) we have 3 vs 4 so we have to move this student.

Example 2:
Input: heights = [5,1,2,3,4]
Output: 5

Example 3:
Input: heights = [1,2,3,4,5]
Output: 0
"""

# heights = [1,1,4,2,1,3]
# heights = [5,1,2,3,4]
heights = [1,2,3,4,5]


class Solution:
    def heightChecker(self, heights: list()) -> int:
        res = 0
        c = [heights[i] for i in range(len(heights))]
        heights.sort()
        for i in range(len(heights)):
            if heights[i] != c[i]:
                res += 1
        return res

solution = Solution()
print(solution.heightChecker(heights))

# Runtime: 28 ms
# Memory Usage: 14.2 MB

