# https://leetcode.com/problems/isomorphic-strings/

"""
Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true
"""

# s, t = "egg", "add"
# s, t = "foo", "bar"
# s, t = "paper", "title"
s, t = "bbbaaaba", "aaabbbba"

import collections
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        ds = collections.defaultdict(set)
        dt = collections.defaultdict(set)
        for i, vals in enumerate(zip(s,t)):
            ds[vals[0]].add(i)
            dt[vals[1]].add(i)
            print(i, vals)
        if len(ds) == len(dt):
            for vals in ds.values():
                if vals not in dt.values():
                    return False
        else:
            return False
        return True

solution = Solution()
print(solution.isIsomorphic(s, t))

# Runtime: 44 ms
# Memory Usage: 21.3 MB


