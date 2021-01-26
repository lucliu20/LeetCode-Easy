# https://leetcode.com/problems/longest-common-prefix/

"""
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

strs = ["flower","flow","flight"]
# strs = ["dog","racecar","car"]
# strs = ["c","acc","ccc"]

# Refer to the below post:
# https://leetcode.com/problems/longest-common-prefix/discuss/354496/Python3-list(zip(*str))
"""
traditional scan vertically
 i      0  1  2  3  4  5
 0      f  l  o  w  e  r
 1	    f  l  o  w
 2	    f  l  i  g  h  t
		
We choose the first string in the list as a reference. in this case is str[0] = "flower"
the outside for-loop go through each character of the str[0] or "flower". f->l->o->w->e->r
the inside for-loop, go through the words, in this case is flow, flight.
strs[j][i] means the the i's character of the j words in the strs.

there are 3 cases when we proceed the scan:

case 1: strs[j][i] = c, strs[1][2] = 'o' and strs[0][2] = 'o';  keep going;
case 2: strs[j][i] != c, strs[2][2] = 'i' and strs[0][2] = 'o';  break the rule, we can return strs[j][:i]. when comes to slicing a string, [:i] won't include the index i;
case 3: i = len(strs[j]) which means current word at strs[j] doesn't have character at index i, since it's 0 based index. the lenght equals i, the index ends at i - 1; break the rule, we can return.
"""

# class Solution:
#     def longestCommonPrefix(self, strs: list()) -> str:
#         if len(strs) == 0: return ""
#         for i in range(len(strs[0])):
#             for j in range(1, len(strs)):
#                 if i == len(strs[j]) or strs[j][i] != strs[0][i]:
#                     return strs[0][:i]
#         return strs[0]

        # My initial approach; which doesn't work.
        # candi = ""
        # for char in strs[0]:
        #     for i in range(1, len(strs)):
        #         if candi+char not in strs[i]:
        #             return candi
        #     candi += char
        # return candi

# Runtime: 28 ms, faster than 93.49% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 14.4 MB, less than 57.68% of Python3 online submissions for Longest Common Prefix.


# Using built-in zip(), and unpacking "*"
class Solution:
    def longestCommonPrefix(self, strs: list()) -> str:
        res = ""
        t = list(zip(*strs))
        print(t)
        for s in t:
            if len(set(s)) == 1:
                res += str(s[0])
            else:
                break
        return res

# Runtime: 36 ms, faster than 55.13% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 14.7 MB, less than 28.36% of Python3 online submissions for Longest Common Prefix.

solution = Solution()
print(solution.longestCommonPrefix(strs))

# 


