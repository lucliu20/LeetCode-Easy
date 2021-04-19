# https://leetcode.com/problems/check-if-the-sentence-is-pangram/

"""
Example 1:
Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.

Example 2:
Input: sentence = "leetcode"
Output: false
"""

sentence = "thequickbrownfoxjumpsoverthelazydog"
# sentence = "leetcode"



import collections
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        count = collections.Counter(sentence)
        if len(count) >= 26:
            return True
        return False

solution = Solution()
print(solution.checkIfPangram(sentence))

# Runtime: 48 ms
# Memory Usage: 14.4 MB
