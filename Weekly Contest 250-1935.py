# https://leetcode.com/problems/maximum-number-of-words-you-can-type/

"""
Example 1:
Input: text = "hello world", brokenLetters = "ad"
Output: 1
Explanation: We cannot type "world" because the 'd' key is broken.

Example 2:
Input: text = "leet code", brokenLetters = "lt"
Output: 1
Explanation: We cannot type "leet" because the 'l' and 't' keys are broken.

Example 3:
Input: text = "leet code", brokenLetters = "e"
Output: 0
Explanation: We cannot type either word because the 'e' key is broken.
"""


text, brokenLetters = "hello world", "ad"
# text, brokenLetters = "leet code", "e"


from typing import List
import collections
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        res = 0
        mytext = text.split()
        mybroken = collections.Counter(brokenLetters)
        for word in mytext:
            flag = False
            for i in range(len(word)):
                if word[i] in mybroken:
                    flag = True
                    break
            if flag == False:
                res += 1
        return res

# 20 / 20 test cases passed.
# Status: Accepted
# Runtime: 48 ms
# Memory Usage: 14.3 MB


solution = Solution()
print(solution.canBeTypedWords(text, brokenLetters))
