# https://leetcode.com/problems/string-matching-in-an-array/
# My post
# https://leetcode.com/problems/string-matching-in-an-array/discuss/995859/Python-3-Multiple-approaches-Explained

# Example 1:
# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]
# Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
# ["hero","as"] is also a valid answer.

# Example 2:
# Input: words = ["leetcode","et","code"]
# Output: ["et","code"]
# Explanation: "et", "code" are substring of "leetcode".

# Example 3:
# Input: words = ["blue","green","bu"]
# Output: []

# words = ["mass","as","hero","superhero"]
# words = ["leetcode","et","code"]
# words = ["blue","green","bu"]
words = ["leetcoder","leetcode","od","hamlet","am"] # ["leetcode","od","am"]

# Approach #1: traditional nested loops
# class Solution:
#     def stringMatching(self, words: list()) -> list():
#         res = set()
#         for c in words:
#             for d in words:
#                 if c != d and d in c:
#                     res.add(d)
#         return res

# Runtime: 36 ms, faster than 74.37% of Python3 online submissions for String Matching in an Array.
# Memory Usage: 14.4 MB, less than 17.36% of Python3 online submissions for String Matching in an Array.

# Approach #2
# Using itertools.combinations() by C(n, 2) with math combination
# import itertools
# class Solution:
#     def stringMatching(self, words: list()) -> list():
#         res = set()
#         for c1, c2 in itertools.combinations(words, 2):
#             if c1 in c2: res.add(c1)
#             elif c2 in c1: res.add(c2)
#         return res

# Runtime: 32 ms, faster than 90.38% of Python3 online submissions for String Matching in an Array.
# Memory Usage: 14 MB, less than 92.47% of Python3 online submissions for String Matching in an Array.


# Approach #3: Sorted array
class Solution:
    def stringMatching(self, words: list()) -> list():
        res = set()
        words.sort(key=len)
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if words[i] in words[j]: res.add(words[i])
        return res

# Runtime: 28 ms, faster than 97.07% of Python3 online submissions for String Matching in an Array.
# Memory Usage: 14 MB, less than 92.47% of Python3 online submissions for String Matching in an Array.

solution = Solution()
print(solution.stringMatching(words))

