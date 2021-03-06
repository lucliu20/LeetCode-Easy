# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

s1, s2 = "bank", "kanb"
# s1, s2 = "x", "z"
# s1, s2 = "aa", "bb"
# s1, s2 = "attack", "defend"
# s1, s2 = "kelb", "kelb"
# s1, s2 = "abcd", "dcba"
# s1 = "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkyoooooooooooooooooooooooooooooooooooooooooooooooo"
# s2 = "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkfoooooooooooooooooooooooooooooooooooooooooooooooo"


import collections
# class Solution:
#     def areAlmostEqual(self, s1: str, s2: str) -> bool:
#         d = collections.defaultdict(list)
#         for i, chars in enumerate(zip(s1, s2)):
#             d[i].append(chars[0])
#             d[i].append(chars[1])
#         count = 0
#         mylist = []
#         for _, value in d.items():
#             if len(d.keys()) == 1 and value[0] != value[1]:
#                 return False
#             elif value[0] != value[1]:
#                 if not mylist:
#                     mylist = value[:]
#                 else:
#                     if value[0] != mylist[1] or value[1] != mylist[0]:
#                         return False
#                 count += 1
#                 if count > 2:
#                     return False
#         return False if count == 1 else True

# Runtime: 24 ms, faster than 100.00% of Python3 online submissions for Check if One String Swap Can Make Strings Equal.
# Memory Usage: 14.4 MB, less than 100.00% of Python3 online submissions for Check if One String Swap Can Make Strings Equal.

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        ml = []
        for chars in zip(s1, s2):
            if chars[0] != chars[1]:
                ml.append((chars[0], chars[1]))
        if len(ml) == 1 or len(ml) > 2:
            return False
        elif len(ml) == 0:
            return True
        else:
            if ml[0][0] != ml[1][1] or ml[0][1] != ml[1][0]:
                return False
        return True

# Runtime: 28 ms, faster than 100.00% of Python3 online submissions for Check if One String Swap Can Make Strings Equal.
# Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Check if One String Swap Can Make Strings Equal.

solution = Solution()
print(solution.areAlmostEqual(s1, s2))


