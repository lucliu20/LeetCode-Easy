# https://leetcode.com/problems/decode-the-message/

"""
Example 1:

Input: key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"
Output: "this is a secret"
Explanation: The diagram above shows the substitution table.
It is obtained by taking the first appearance of each letter in "the quick brown fox jumps over the lazy dog".

Example 2:

Input: key = "eljuxhpwnyrdgtqkviszcfmabo", message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
Output: "the five boxing wizards jump quickly"
Explanation: The diagram above shows the substitution table.
It is obtained by taking the first appearance of each letter in "eljuxhpwnyrdgtqkviszcfmabo".
"""

key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"

import collections
import string
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        res, mydict = "", collections.defaultdict(chr)
        # https://www.adamsmith.haus/python/answers/how-to-make-a-list-of-the-alphabet-in-python
        alphabet_string = string.ascii_lowercase
        alphabet_list = list(alphabet_string)
        
        i, j = 0, 0
        while i < 26:
            if key[j] != " " and (key[j] not in mydict.keys()):
                mydict[key[j]] = alphabet_list[i]
                i += 1
            j += 1
        # for i in range(26):
        #     mydict[key[i]] = alphabet_list[i]
        print(mydict.keys())

        for c in message:
            if c == " ":
                res += " "
            else:
                # print(mydict[c])
                res += mydict[c]
        return res

solution = Solution()
print(solution.decodeMessage(key, message))

# Runtime: 68 ms, faster than 54.55% of Python3 online submissions for Decode the Message.
# Memory Usage: 13.9 MB, less than 72.73% of Python3 online submissions for Decode the Message.
