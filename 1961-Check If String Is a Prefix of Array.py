# https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/

"""
Example 1:
Input: s = "iloveleetcode", words = ["i","love","leetcode","apples"]
Output: true
Explanation:
s can be made by concatenating "i", "love", and "leetcode" together.

Example 2:
Input: s = "iloveleetcode", words = ["apples","i","love","leetcode"]
Output: false
Explanation:
It is impossible to make s using a prefix of arr.
"""


# s, words = "iloveleetcode", ["i","love","leetcode","apples"]
# s, words = "iloveleetcode", ["apples","i","love","leetcode"]
s, words = "ccccccccc", ["c","cc"] # False


from typing import List
class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        l = 0
        for string in words:
            for i in range(len(string)):
                if l < len(s):
                    if s[l] == string[i]:
                        l += 1
                    else:
                        return False
                else:
                    if i > 0:
                        return False
                    else:
                        return True
        return True if l == len(s) else False

# Runtime: 32 ms, faster than 87.50% of Python3 online submissions for Check If String Is a Prefix of Array.
# Memory Usage: 14.3 MB, less than 50.00% of Python3 online submissions for Check If String Is a Prefix of Array.


solution = Solution()
print(solution.isPrefixString(s, words))
