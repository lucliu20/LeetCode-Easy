# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/


"""
Example 1:
Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.

Example 2:
Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
Output: false
Explanation: It is impossible to make mat equal to target by rotating mat.

Example 3:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.
"""


# mat, target = [[0,1],[1,0]], [[1,0],[0,1]]
# mat, target = [[0,1],[1,1]], [[1,0],[0,1]]
mat, target = [[0,0,0],[0,1,0],[1,1,1]], [[1,1,1],[0,1,0],[0,0,0]]
# mat, target = [[0,0],[0,1]], [[0,0],[1,0]]



# Refer to the LeetCode post:
# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/discuss/1253880/Python3-rotate-matrix
# https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
from typing import List
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4): 
            if mat == target: return True
            # print(mat[::-1])
            mat = [list(x) for x in zip(*mat[::-1])]
        return False


# Runtime: 28 ms, faster than 100.00% of Python3 online submissions for Determine Whether Matrix Can Be Obtained By Rotation.
# Memory Usage: 14.2 MB, less than 50.00% of Python3 online submissions for Determine Whether Matrix Can Be Obtained By Rotation.


solution = Solution()
print(solution.findRotation(mat, target))



