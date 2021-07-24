# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/

"""
Example 1:
Input: s = "abacbc"
Output: true
Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.

Example 2:
Input: s = "aaabb"
Output: false
Explanation: The characters that appear in s are 'a' and 'b'.
'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.
"""


s = "abacbc"
# s = "aaabb"



import collections
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        cnts = collections.Counter(s)
        tmp = cnts[s[0]]
        for c in cnts.values():
            if c != tmp:
                return False
            tmp = c
        return True

# Runtime: 36 ms, faster than 66.67% of Python3 online submissions for Check if All Characters Have Equal Number of Occurrences.
# Memory Usage: 14.2 MB, less than 33.33% of Python3 online submissions for Check if All Characters Have Equal Number of Occurrences.


solution = Solution()
print(solution.areOccurrencesEqual(s))
