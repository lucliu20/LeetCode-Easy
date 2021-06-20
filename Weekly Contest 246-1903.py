# https://leetcode.com/problems/largest-odd-number-in-string/

# num = "35427"
# num = "52"
num = "4206"


class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1, -1, -1):
            # print(num[i:i+1])
            if int(num[i:i+1])%2 != 0:
                return (num[:i+1])
        return ""


solution = Solution()
print(solution.largestOddNumber(num))


# Runtime: 92 ms
# Memory Usage: 15.2 MB

