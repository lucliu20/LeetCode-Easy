# https://leetcode.com/problems/first-unique-character-in-a-string/

"""
Examples:
s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
"""

# s = "leetcode"
s = "loveleetcode"

import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = collections.Counter(s)
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1

solution = Solution()
print(solution.firstUniqChar(s))

# Runtime: 88 ms, faster than 90.53% of Python3 online submissions for First Unique Character in a String.
# Memory Usage: 14.4 MB, less than 69.91% of Python3 online submissions for First Unique Character in a String.

