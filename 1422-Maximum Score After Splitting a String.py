# Maximum Score After Splitting a String
# https://leetcode.com/problems/maximum-score-after-splitting-a-string/

# My post:
# https://leetcode.com/problems/maximum-score-after-splitting-a-string/discuss/994612/Python-3-One-pass-Explained-O(n)


# Example 1:
# Input: s = "011101"
# Output: 5 
# Explanation: 
# All possible ways of splitting s into two non-empty substrings are:
# left = "0" and right = "11101", score = 1 + 4 = 5 
# left = "01" and right = "1101", score = 1 + 3 = 4 
# left = "011" and right = "101", score = 1 + 2 = 3 
# left = "0111" and right = "01", score = 1 + 1 = 2 
# left = "01110" and right = "1", score = 2 + 1 = 3

# Example 2:
# Input: s = "00111"
# Output: 5
# Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5

# Example 3:
# Input: s = "1111"
# Output: 3

s = "011101"
# s = "00111"
# s = "1111"
# s = "101"
# s = "00"
# s = "11"

class Solution:
    def maxScore(self, s: str) -> int:
        res, co, cl = 0, 0, s.count("1")
        for i in range(len(s)-1):
            if s[i] == "0": co += 1
            else: cl -= 1
            res = max(co+cl, res)
        return res

solution = Solution()
print(solution.maxScore(s))

# Runtime: 24 ms, faster than 97.69% of Python3 online submissions for Maximum Score After Splitting a String.
# Memory Usage: 14.2 MB, less than 65.29% of Python3 online submissions for Maximum Score After Splitting a String.

# Runtime: 28 ms, faster than 90.08% of Python3 online submissions for Maximum Score After Splitting a String.
# Memory Usage: 14 MB, less than 98.18% of Python3 online submissions for Maximum Score After Splitting a String.
