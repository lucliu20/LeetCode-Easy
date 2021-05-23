# https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/
# My post:
# https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/discuss/1224799/Python-3-Readable-Intuitive


"""
Example 1:
Input: s = "1101"
Output: true
Explanation:
The longest contiguous segment of 1s has length 2: "1101"
The longest contiguous segment of 0s has length 1: "1101"
The segment of 1s is longer, so return true.

Example 2:
Input: s = "111000"
Output: false
Explanation:
The longest contiguous segment of 1s has length 3: "111000"
The longest contiguous segment of 0s has length 3: "111000"
The segment of 1s is not longer, so return false.

Example 3:
Input: s = "110100010"
Output: false
Explanation:
The longest contiguous segment of 1s has length 2: "110100010"
The longest contiguous segment of 0s has length 3: "110100010"
The segment of 1s is not longer, so return false.
"""


# s = "1101"
# s = "111000"
s = "110100010"


class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        cnt1, cnt0 = 0, 0
        res1, res0 = 0, 0
        for i in range(len(s)):
            if i == 0:
                if s[i] == "1":
                    cnt1 += 1
                else:
                    cnt0 += 1
            else:
                if s[i-1] == "1":
                    if s[i] == "1":
                        cnt1 += 1
                    elif s[i] == "0":
                        res1 = max(res1, cnt1)
                        cnt1 == 0
                        cnt0 = 0
                        cnt0 += 1
                elif s[i-1] == "0":
                    if s[i] == "0":
                        cnt0 += 1
                    elif s[i] == "1":
                        res0 = max(res0, cnt0)
                        cnt0 = 0
                        cnt1 = 0
                        cnt1 += 1
            res1 = max(res1, cnt1)
            res0 = max(res0, cnt0)
            
        return res1 > res0


# Runtime: 36 ms
# Memory Usage: 14.3 MB


solution = Solution()
print(solution.checkZeroOnes(s))

