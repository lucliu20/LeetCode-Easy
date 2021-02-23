# https://leetcode.com/problems/merge-strings-alternately/
# 1768. Merge Strings Alternately

# word1, word2 = "abc", "pqr"
word1, word2 = "abcd", "pq"

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        l1, l2 = len(word1), len(word2)
        for i, j in zip(range(len(word1)), range(len(word2))):
            res += word1[i]
            res += word2[j]
        
        if l1 > l2:
            res += word1[i+1:]
        if l1 < l2:
            res += word2[j+1:]
        return res

solution = Solution()
print(solution.mergeAlternately(word1, word2))

