# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

"""
Example 1:
Input: s = "iiii", k = 1
Output: 36
Explanation: The operations are as follows:
- Convert: "iiii" ➝ "(9)(9)(9)(9)" ➝ "9999" ➝ 9999
- Transform #1: 9999 ➝ 9 + 9 + 9 + 9 ➝ 36
Thus the resulting integer is 36.

Example 2:
Input: s = "leetcode", k = 2
Output: 6
Explanation: The operations are as follows:
- Convert: "leetcode" ➝ "(12)(5)(5)(20)(3)(15)(4)(5)" ➝ "12552031545" ➝ 12552031545
- Transform #1: 12552031545 ➝ 1 + 2 + 5 + 5 + 2 + 0 + 3 + 1 + 5 + 4 + 5 ➝ 33
- Transform #2: 33 ➝ 3 + 3 ➝ 6
Thus the resulting integer is 6.

Example 3:
Input: s = "zbax", k = 2
Output: 8
"""

s, k = "iiii", 1
# s, k = "leetcode", 2
# s, k = "zbax", 2


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        al = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":1,"k":2,"l":3,"m":4,"n":5,"o":6,"p":7,"q":8,"r":9,"s":10,"t":2,"u":3,"v":4,"w":5,"x":6,"y":7,"z":8}
        res, tmp = 0, 0
        for c in s:
            res += al[c]
        for _ in range(k-1):
            tmp = str(res)
            res = 0
            for char in tmp:
                res += int(char)
        return res


# 216 / 216 test cases passed.
# Status: Accepted
# Runtime: 37 ms
# Memory Usage: 14.3 MB


solution = Solution()
print(solution.getLucky(s, k))

