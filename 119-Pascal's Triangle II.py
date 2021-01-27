# https://leetcode.com/problems/pascals-triangle-ii/

"""
Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]
"""

rowIndex = 3

# Refer to post:
# https://leetcode.com/problems/pascals-triangle-ii/discuss/562371/Python-Recursion-Approach

# recurrence relation: use the previous row array element values to calculate the current row array element values;
# append [1] at either boarders of the row.
# class Solution:
#     def getRow(self, rowIndex: int) -> list():
#         if rowIndex == 0:
#             return [1]
#         lastRow = self.getRow(rowIndex-1)
#         res = [1]
#         for i in range(len(lastRow)-1):
#             res.append(lastRow[i]+lastRow[i+1])
#         res.append(1)
#         return res


# Runtime: 32 ms, faster than 60.64% of Python3 online submissions for Pascal's Triangle II.
# Memory Usage: 14.3 MB, less than 48.07% of Python3 online submissions for Pascal's Triangle II.


# Iterate way
class Solution:
    def getRow(self, rowIndex: int) -> list():
        res = [1]
        if rowIndex == 0: return res
        for n in range(1, rowIndex+1):
            t = [1]
            for i in range(n):
                if i == n-1:
                    t.append(1)
                else:
                    t.append(res[i] + res[(i+1)%n])
            res.clear()
            res = [k for k in t]

        return res

# Runtime: 32 ms, faster than 64.88% of Python3 online submissions for Pascal's Triangle II.
# Memory Usage: 14.3 MB, less than 24.75% of Python3 online submissions for Pascal's Triangle II.

# class Solution:
#     def getRow(self, rowIndex: int) -> list():
        # My initial recursive way: "Time Limit Exceeded"
        # def get(row, col):
        #     if row == col or col == 0:
        #         return 1
        #     return get(row-1, col-1) + get(row-1, col)
        # t = []
        # for i in range(rowIndex+1):
        #     t.append(get(rowIndex, i))
        # return t

solution = Solution()
print(solution.getRow(rowIndex))


