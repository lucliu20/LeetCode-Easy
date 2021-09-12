# https://leetcode.com/problems/long-pressed-name/

"""
Example 1:
Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.

Example 2:
Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.

Example 3:
Input: name = "leelee", typed = "lleeelee"
Output: true

Example 4:
Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.
"""


# name, typed = "alex", "aaleex"
# name, typed = "saeed", "ssaaedd"
# name, typed = "leelee", "lleeelee"
# name, typed = "laiden", "laiden"
# Test case #93
# name, typed = "alex", "aaleexeex" # Expected: False
# Test case #69
name, typed = "vtkgn", "vttkgnn" # Expected: True


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name == typed:
            return True
        if typed[-1] != name[-1]:
            return False
        indice = -1
        prev = name[0]
        for char in name:
            if (char in typed):
                indice = typed.index(char)
                if indice > 0:
                    for i in range(0, indice):
                        if typed[i] != prev:
                            return False
                typed = typed[(indice+1):]
                prev = char
            else:
                return False
        for c in typed:
            if c != prev:
                return False
        return True

# 94 / 94 test cases passed.
# Status: Accepted
# Runtime: 16 ms, faster than 99.83% of Python3 online submissions for Long Pressed Name.
# Memory Usage: 14.1 MB, less than 84.04% of Python3 online submissions for Long Pressed Name.


solution = Solution()
print(solution.isLongPressedName(name, typed))

