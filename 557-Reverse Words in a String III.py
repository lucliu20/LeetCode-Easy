# https://leetcode.com/problems/reverse-words-in-a-string-iii/

"""
Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
"""

s = "Let's take LeetCode contest"

class Solution:
    def reverseWords(self, s: str) -> str:
        t = s.split(" ")
        res = []
        for i in range(len(t)):
            res.append("".join(reversed(t[i])))
        return " ".join(res)

solution = Solution()
print(solution.reverseWords(s))

# Runtime: 44 ms, faster than 34.20% of Python3 online submissions for Reverse Words in a String III.
# Memory Usage: 15.1 MB, less than 29.77% of Python3 online submissions for Reverse Words in a String III.


