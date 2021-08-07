# https://leetcode.com/problems/delete-characters-to-make-fancy-string/

"""
Example 1:
Input: s = "leeetcode"
Output: "leetcode"
Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".

Example 2:
Input: s = "aaabaaaa"
Output: "aabaa"
Explanation:
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".

Example 3:
Input: s = "aab"
Output: "aab"
Explanation: No three consecutive characters are equal, so return "aab".
"""

# s = "leeetcode"
# s = "aaabaaaa"
# s = "aab"
s = "a"


class Solution:
    def makeFancyString(self, s: str) -> str:
        res, l, cnt = s[0], 0, 0
        for i in range(1, len(s)):
            if s[i] != s[l]:
                res += s[i]
                cnt = 0
                l = i
            elif s[i] == s[l]:
                cnt += 1
                if cnt < 2:
                    res += s[i]
                else:
                    continue
            
        return res


# Runtime: 772 ms, faster than 25.00% of Python3 online submissions for Delete Characters to Make Fancy String.
# Memory Usage: 16.2 MB, less than 25.00% of Python3 online submissions for Delete Characters to Make Fancy String.

solution = Solution()
print(solution.makeFancyString(s))

