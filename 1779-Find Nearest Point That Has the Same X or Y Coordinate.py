# https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/

"""
Example 1:
Input: x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
Output: 2
Explanation: Of all the points, only [3,1], [2,4] and [4,4] are valid. Of the valid points, [2,4] and [4,4] have the smallest Manhattan distance from your current location, with a distance of 1. [2,4] has the smallest index, so return 2.

Example 2:
Input: x = 3, y = 4, points = [[3,4]]
Output: 0
Explanation: The answer is allowed to be on the same location as your current location.

Example 3:
Input: x = 3, y = 4, points = [[2,3]]
Output: -1
Explanation: There are no valid points.
"""

# x, y, points = 3, 4, [[1,2],[3,1],[2,4],[2,3],[4,4]]
# x, y, points = 3, 4, [[3,4]]
x, y, points = 3, 4, [[2,3]]

from typing import List
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        # abs(x1 - x2) + abs(y1 - y2)
        Manhattan = float("inf")
        res = -1
        for i in range(len(points)):
            a, b = points[i]
            if a == x or b == y:
                dis = abs(x-a)+abs(y-b)
                if Manhattan > dis:
                    Manhattan = dis
                    res = i
        return res


solution = Solution()
print(solution.nearestValidPoint(x, y, points))

# Runtime: 700 ms, faster than 100.00% of Python3 online submissions for Find Nearest Point That Has the Same X or Y Coordinate.
# Memory Usage: 19.4 MB, less than 50.00% of Python3 online submissions for Find Nearest Point That Has the Same X or Y Coordinate.

