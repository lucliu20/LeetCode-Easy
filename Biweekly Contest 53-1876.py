# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

"""
Example 1:
Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
The only good substring of length 3 is "xyz".

Example 2:
Input: s = "aababcabc"
Output: 4
Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc".
"""

s = "xyzzaz"
# s = "aababcabc"



class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0
        res = 0
        for i in range(2, len(s)):
            j = 2
            myset = set()
            while j >= 0:
                if s[i-j] not in myset:
                    myset.add(s[i-j])
                else:
                    break
                j -= 1
            if len(myset) == 3:
                res += 1
        return res

solution = Solution()
print(solution.countGoodSubstrings(s))


# 160 / 160 test cases passed.
# Status: Accepted
# Runtime: 32 ms
# Memory Usage: 14.3 MB

