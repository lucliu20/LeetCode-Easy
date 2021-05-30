# https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/

"""
Example 1:
Input: firstWord = "acb", secondWord = "cba", targetWord = "cdb"
Output: true
Explanation:
The numerical value of firstWord is "acb" -> "021" -> 21.
The numerical value of secondWord is "cba" -> "210" -> 210.
The numerical value of targetWord is "cdb" -> "231" -> 231.
We return true because 21 + 210 == 231.

Example 2:
Input: firstWord = "aaa", secondWord = "a", targetWord = "aab"
Output: false
Explanation: 
The numerical value of firstWord is "aaa" -> "000" -> 0.
The numerical value of secondWord is "a" -> "0" -> 0.
The numerical value of targetWord is "aab" -> "001" -> 1.
We return false because 0 + 0 != 1.

Example 3:
Input: firstWord = "aaa", secondWord = "a", targetWord = "aaaa"
Output: true
Explanation: 
The numerical value of firstWord is "aaa" -> "000" -> 0.
The numerical value of secondWord is "a" -> "0" -> 0.
The numerical value of targetWord is "aaaa" -> "0000" -> 0.
We return true because 0 + 0 == 0.
"""

firstWord, secondWord, targetWord = "acb", "cba", "cdb"
# firstWord, secondWord, targetWord = "aaa", "a", "aab"
# firstWord, secondWord, targetWord = "aaa", "a", "aaaa"



class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        mydict = {"a":"0", "b":"1", "c":"2", "d":"3", "e":"4", "f":"5", "g":"6", "h":"7", "i":"8", "j":"9"}
        fir, sec, tar = "", "", ""
        for s in firstWord:
            fir += mydict[s]
        myfir = int(fir)
        for s in secondWord:
            sec += mydict[s]
        mysec = int(sec)
        for s in targetWord:
            tar += mydict[s]
        mytar = int(tar)
        return (myfir+mysec) == mytar



# 99 / 99 test cases passed.
# Status: Accepted
# Runtime: 36 ms
# Memory Usage: 14.4 MB


solution = Solution()
print(solution.isSumEqual(firstWord, secondWord, targetWord))

