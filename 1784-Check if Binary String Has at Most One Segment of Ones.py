# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/
# Contest 231: Q1


s = "1001"
# s = "110"
# s = "1" # True
# s = "10" # True

from typing import List
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        res = True
        # if s == "1": return True
        anchar = -1
        for i in range(len(s)):
            if s[i] == "1" and anchar == -1:
                anchar = i
            elif s[i] == "1" and i == anchar+1:
                anchar = i
            elif s[i] == "1" and i != anchar+1:
                return False
        return res

solution = Solution()
print(solution.checkOnesSegment(s))
