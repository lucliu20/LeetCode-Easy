# https://leetcode.com/problems/add-binary/

"""
Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
"""

# a, b = "11", "1"
# a, b = "1010", "1011"
# a, b = "1", "111"
a, b = "1111", "1111"

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        i, j, c = len(a)-1, len(b)-1, 0
        while i >= 0 or j >= 0:
            if i in range(len(a)) and j in range(len(b)):
                tmp = int(a[i]) + int(b[j]) + c
                i -= 1
                j -= 1
                if tmp == 2:
                    c = 1
                    res = "0" + res
                elif tmp == 3:
                    res = "1" + res
                else:
                    res = str(tmp) + res
                    c = 0
            elif j < 0:
                tmp = int(a[i]) + c
                i -= 1
                if tmp == 2:
                    c = 1
                    res = "0" + res
                else:
                    res = str(tmp) + res
                    c = 0
            elif i < 0:
                tmp = int(b[j]) + c
                j -= 1
                if tmp == 2:
                    c = 1
                    res = "0" + res
                else:
                    res = str(tmp) + res
                    c = 0
        if c:
            res = "1" + res
        return res

solution = Solution()
print(solution.addBinary(a, b))

# Runtime: 28 ms, faster than 91.70% of Python3 online submissions for Add Binary.
# Memory Usage: 14.2 MB, less than 82.60% of Python3 online submissions for Add Binary.

