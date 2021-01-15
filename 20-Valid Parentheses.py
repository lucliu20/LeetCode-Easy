# https://leetcode.com/problems/valid-parentheses/

"""
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "([)]"
Output: true
"""

# s = "()"
s = "()[]{}"
# s = "(]"
# s = "([)]"
# s = "([)]"
# s = "]"
# s = "(])"

class Solution:
    def isValid(self, s: str) -> bool:
        p = ["()", "[]", "{}"]
        c = ")]}"
        stack = list()
        for char in s:
            if char in c and len(stack) >= 1:
                t = stack[-1] + char
                if t in p:
                    stack.pop()
                    continue
            stack.append(char)
        return True if not stack else False

solution = Solution()
print(solution.isValid(s))

# Runtime: 28 ms, faster than 84.75% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 14.3 MB, less than 63.01% of Python3 online submissions for Valid Parentheses.

