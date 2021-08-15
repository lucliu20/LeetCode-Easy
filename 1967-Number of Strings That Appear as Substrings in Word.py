# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/

"""
Example 1:
Input: patterns = ["a","abc","bc","d"], word = "abc"
Output: 3
Explanation:
- "a" appears as a substring in "abc".
- "abc" appears as a substring in "abc".
- "bc" appears as a substring in "abc".
- "d" does not appear as a substring in "abc".
3 of the strings in patterns appear as a substring in word.

Example 2:
Input: patterns = ["a","b","c"], word = "aaaaabbbbb"
Output: 2
Explanation:
- "a" appears as a substring in "aaaaabbbbb".
- "b" appears as a substring in "aaaaabbbbb".
- "c" does not appear as a substring in "aaaaabbbbb".
2 of the strings in patterns appear as a substring in word.

Example 3:
Input: patterns = ["a","a","a"], word = "ab"
Output: 3
Explanation: Each of the patterns appears as a substring in word "ab".
"""


# patterns, word = ["a","abc","bc","d"], "abc"
# patterns, word = ["a","b","c"], "aaaaabbbbb"
patterns, word = ["a","a","a"], "ab"



from typing import List
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        res = 0
        for s in patterns:
            if s in word:
                res += 1
        return res

# Runtime: 32 ms, faster than 80.00% of Python3 online submissions for Number of Strings That Appear as Substrings in Word.
# Memory Usage: 14.3 MB, less than 80.00% of Python3 online submissions for Number of Strings That Appear as Substrings in Word.


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        res = 0
        for s in patterns:
            try:
                word.index(s)
            except ValueError:
                # print("Not found!")
                continue
            else:
                # print("Found!")
                res += 1
        return res


# Runtime: 32 ms, faster than 80.00% of Python3 online submissions for Number of Strings That Appear as Substrings in Word.
# Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Number of Strings That Appear as Substrings in Word.


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        res = 0
        for s in patterns:
            if word.find(s) != -1:
                res += 1
        return res

# Runtime: 36 ms, faster than 40.00% of Python3 online submissions for Number of Strings That Appear as Substrings in Word.
# Memory Usage: 14.4 MB, less than 20.00% of Python3 online submissions for Number of Strings That Appear as Substrings in Word.


solution = Solution()
print(solution.numOfStrings(patterns, word))
