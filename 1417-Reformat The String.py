# https://leetcode.com/problems/reformat-the-string/
# My post:
# https://leetcode.com/problems/reformat-the-string/discuss/994752/Python-3-Zip-Join-Explained

# Example 1:
# Input: s = "a0b1c2"
# Output: "0a1b2c"
# Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.

# Example 2:
# Input: s = "leetcode"
# Output: ""
# Explanation: "leetcode" has only characters so we cannot separate them by digits.

# Example 3:
# Input: s = "1229857369"
# Output: ""
# Explanation: "1229857369" has only digits so we cannot separate them by characters.

# Example 4:
# Input: s = "covid2019"
# Output: "c2o0v1i9d"

# Example 5:
# Input: s = "ab123"
# Output: "1a2b3"

# strings = ["a12b3cd","ab123","covid2019","1229857369","leetcode","a0b1c2","j","uu","8"]
# s = "a12b3cd"
# s = "ab123"
# s = "covid2019"
# s = "1229857369"
# s = "leetcode"
s = "a0b1c2"

class Solution:
    def reformat(self, s: str) -> str:
        # let = sum(_.isalpha() for _ in s)
        # num = sum(_.isdigit() for _ in s)
        # if abs(let-num) > 1: return ""
        al, dig, res = "", "", ""
        for c in s:
            if c.isalpha(): al += c
            else: dig += c
        if abs(len(al)-len(dig)) > 1: return ""
        if len(al) > len(dig):
            res = "".join([(l+n) for l, n in zip(al, dig)])
            # for l, n in zip(al, dig):
            #     res += (l+n)
            res += al[-1]
        elif len(al) < len(dig):
            res = "".join([(n+l) for n, l in zip(dig, al)])
            # for n, l in zip(dig, al):
            #     res += (n+l)
            res += dig[-1]
        else:
            res = "".join([(n+l) for n, l in zip(dig, al)])
            # for n, l in zip(dig, al):
            #     res += (n+l)
        return res

solution = Solution()
print(solution.reformat(s))

# Runtime: 36 ms, faster than 96.03% of Python3 online submissions for Reformat The String.
# Memory Usage: 14 MB, less than 99.24% of Python3 online submissions for Reformat The String.


