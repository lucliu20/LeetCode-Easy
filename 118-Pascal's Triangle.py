# https://leetcode.com/problems/pascals-triangle/

"""
Example:
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

numRows = 5

class Solution:
    def generate(self, numRows: int) -> list(list()):
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        res = [[1], [1,1]]
        for i in range(2, numRows):
            for j in range(i+1): # i.e., range(numRows-(numRows-i)+1)
                if j == 0:
                    res.append([1])
                elif j == i:
                    res[i].append(1)
                else:
                    res[i].append(res[i-1][j-1] + res[i-1][j])
        return res

solution = Solution()
print(solution.generate(numRows))

# Runtime: 24 ms, faster than 95.79% of Python3 online submissions for Pascal's Triangle.
# Memory Usage: 14.2 MB, less than 59.67% of Python3 online submissions for Pascal's Triangle.

