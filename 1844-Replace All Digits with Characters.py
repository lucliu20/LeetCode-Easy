# https://leetcode.com/problems/replace-all-digits-with-characters/


"""
Example 1:
Input: s = "a1c1e1"
Output: "abcdef"
Explanation: The digits are replaced as follows:
- s[1] -> shift('a',1) = 'b'
- s[3] -> shift('c',1) = 'd'
- s[5] -> shift('e',1) = 'f'

Example 2:
Input: s = "a1b2c3d4e"
Output: "abbdcfdhe"
Explanation: The digits are replaced as follows:
- s[1] -> shift('a',1) = 'b'
- s[3] -> shift('b',2) = 'd'
- s[5] -> shift('c',3) = 'f'
- s[7] -> shift('d',4) = 'h'
"""

# s = "a1c1e1"
# s = "a1b2c3d4e"
# s = "a"
s = "a1"



class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(c, x):
            ind = lettersToDigits[c]
            return digitsToLetters[ind+int(x)]
        
        lettersToDigits = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9, "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16, "r":17, "s":18, "t":19, "u":20, "v":21, "w":22, "x":23, "y":24, "z":25}
        digitsToLetters = {0:"a", 1:"b", 2:"c", 3:"d", 4:"e", 5:"f", 6:"g", 7:"h", 8:"i", 9:"j", 10:"k", 11:"l", 12:"m", 13:"n", 14:"o", 15:"p", 16:"q", 17:"r", 18:"s", 19:"t", 20:"u", 21:"v", 22:"w", 23:"x", 24:"y", 25:"z"}

        for i in range(0, len(s), 2):
            if i+1 < len(s):
                replace = shift(s[i], s[i+1])
                s = s.replace(s[i+1], replace, 1)
        return s



solution = Solution()
print(solution.replaceDigits(s))

# Runtime: 32 ms
# Memory Usage: 14.1 MB
