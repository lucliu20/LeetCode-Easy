# https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/


"""
Example 1:
Input: words = ["abc","aabc","bc"]
Output: true
Explanation: Move the first 'a' in words[1] to the front of words[2],
to make words[1] = "abc" and words[2] = "abc".
All the strings are now equal to "abc", so return true.

Example 2:
Input: words = ["ab","a"]
Output: false
Explanation: It is impossible to make all the strings equal using the operation.
"""


words = ["abc","aabc","bc"]
# words = ["ab","a"]
# words = ["a","b"]
# words = ["asdf"]
# words = ["caaaaa","aaaaaaaaa","a","bbb","bbbbbbbbb","bbb","cc","cccccccccccc","ccccccc","ccccccc","cc","cccc","c","cccccccc","c"]
# {'c': 45, 'a':15, 'b': 15}
# words = ["acca","cca","c","aacc"] # False



from typing import List
import collections
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        if len(words) == 1:
            return True
        mydict = collections.defaultdict(int)
        total = 0
        for word in words:
            for c in word:
                mydict[c] += 1
                total += 1
        
        string = words[0][0]
        frequency = mydict[string]
        if frequency == 1: # case: ["a","b"]
            return len(mydict) == 1
        
        for _, val in mydict.items():
            if val%len(words) != 0:
                return False

        return True


# Runtime: 72 ms, faster than 50.00% of Python3 online submissions for Redistribute Characters to Make All Strings Equal.
# Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Redistribute Characters to Make All Strings Equal.


solution = Solution()
print(solution.makeEqual(words))


