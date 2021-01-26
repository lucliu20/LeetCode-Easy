# https://leetcode.com/problems/implement-strstr/

"""
Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Example 3:
Input: haystack = "", needle = ""
Output: 0
"""

haystack, needle = "hello", "ll"
# haystack, needle = "aaaaa", "bba"
# haystack, needle = "", ""
# haystack, needle = "ababc", "abc"
# haystack, needle = "ababc", "abcd"
# haystack, needle = "a", "a"
# haystack, needle = "aaa", "aaaa"
# haystack, needle = "aaa", "a"
# haystack, needle = "aaa", "aa"
# haystack, needle = "mississippi", "issip" # 4
# haystack, needle = "bbbbababbbaabbba", "abb" # 6

# The following approach iterating from the beginning to the end doesn't work with the case like "mississippi", "issip".
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         if len(needle) == 0: return 0
#         j, anchor = 0, -1
#         for i in range(len(haystack)):
#             if haystack[i] == needle[j]:
#                 if j == len(needle)-1:
#                     if anchor != -1:
#                         return anchor
#                     else:
#                         return i
#                 elif j == 0:
#                     anchor = i
#                 j += 1
#             elif anchor != -1:
#                 j = 0
#                 if haystack[i] == needle[j]:
#                     anchor = i
#                     j += 1
#                 else:
#                     anchor = -1
#         if j != len(needle):
#             anchor = -1
#         return anchor


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0: return 0
        i, j, res = len(haystack)-1, len(needle)-1, -1
        anchor = -1
        while i >= 0:
            if haystack[i] == needle[j]:
                if anchor == -1:
                    anchor = i
                if j == 0:
                    res = i
                    anchor = -1
                    if i > 0:
                        i = i + len(needle)-1
                        j = len(needle)-1
                else:
                    j -= 1
            else:
                if anchor != -1:
                    i = anchor-1
                    anchor = -1
                j = len(needle)-1
                if haystack[i] == needle[j]:
                    if anchor == -1:
                        anchor = i
                    if j == 0:
                        res = i
                        anchor = -1
                        if i > 0:
                            i = i + len(needle)-1
                            j = len(needle)-1
                    else:
                        j -= 1
            i -= 1
        return res

solution = Solution()
print(solution.strStr(haystack, needle))

# Runtime: 40 ms, faster than 34.87% of Python3 online submissions for Implement strStr().
# Memory Usage: 14.5 MB, less than 47.85% of Python3 online submissions for Implement strStr().


