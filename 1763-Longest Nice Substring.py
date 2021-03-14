# https://leetcode.com/problems/longest-nice-substring/

"""
Example 1:
Input: s = "YazaAay"
Output: "aAa"
Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
"aAa" is the longest nice substring.

Example 2:
Input: s = "Bb"
Output: "Bb"
Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.

Example 3:
Input: s = "c"
Output: ""
Explanation: There are no nice substrings.

Example 4:
Input: s = "dDzeE"
Output: "dD"
Explanation: Both "dD" and "eE" are the longest nice substrings.
As there are multiple longest nice substrings, return "dD" since it occurs earlier.
"""

s = "YazaAay"
# s = "Bb"
# s = "c"
# s = "dDzeE"
# s = "HkhBubUYy" # "BubUYy"
# s = "wknklgkiDfdkHWnFWqkwWfwdIWhnKTbMWhWMNhhKMmMNWaLfnnsbdBH" # "MmM"


import collections
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def helper(start, end):
            for i in range(start, end+1):
                if s[i].islower() and s[i].upper() not in s[start:end+1]:
                    return False
                elif s[i].isupper() and s[i].lower() not in s[start:end+1]:
                    return False
            return True
        
        missing = set()
        myset = set(s)
        for char in myset:
            if char.upper() not in myset:
                missing.add(char)
        i, j = 0, 0
        res = ""
        while i < len(s) and j < len(s):
            print(s[i:j+1])
            if s[j] in missing:
                i += 1
                j = i
            else:
                print(s[i], s[j])
                if helper(i, j):
                    if len(res) < j+1-i:
                        res = s[i:j+1]
                    j += 1
                else:
                    j += 1
                    if j >= len(s):
                        i += 1
                        j = i
                
        return res

solution = Solution()
print(solution.longestNiceSubstring(s))

# Runtime: 80 ms, faster than 100.00% of Python3 online submissions for Longest Nice Substring.
# Memory Usage: 14.3 MB, less than 50.00% of Python3 online submissions for Longest Nice Substring.


