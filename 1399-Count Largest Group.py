# https://leetcode.com/problems/count-largest-group/
# My post
# https://leetcode.com/problems/count-largest-group/discuss/997020/Python-3-defaultdict()-One-pass-O(n)

# Example 1:
# Input: n = 13
# Output: 4
# Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
# [1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9]. There are 4 groups with largest size.

# Example 2:
# Input: n = 2
# Output: 2
# Explanation: There are 2 groups [1], [2] of size 1.

# Example 3:
# Input: n = 15
# Output: 6

# Example 4:
# Input: n = 24
# Output: 5
# Explanation: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24].
# 5 largest size are [[2, 11, 20], [3, 12, 21], [4, 13, 22], [5, 14, 23], [6, 15, 24]], i.e., '2=1+1=2+0', '3=1+2=2+1', '4=1+3=2+2', etc.

# One reference below
# https://leetcode.com/problems/count-largest-group/discuss/563838/Python-using-DictionaryHashmap-with-explanation

# Another reference
# https://leetcode.com/problems/count-largest-group/discuss/564417/Python-Using-defaultdict(list)

n = 13 # 4
# n = 2 # 2
# n = 15 # 6
# n = 24 # 5

# One-pass
import collections
class Solution:
    def countLargestGroup(self, n: int) -> int:
        md = collections.defaultdict(int)
        l, res = 0, 0
        for i in range(1, n+1):
            s = 0
            while i > 0:
                s += i%10
                i = i//10
            md[s] += 1
            if l == md[s]:
                res += 1
            elif l < md[s]:
                l = md[s]
                res = 1
        return res

solution = Solution()
print(solution.countLargestGroup(n))

# Runtime: 92 ms, faster than 80.98% of Python3 online submissions for Count Largest Group.
# Memory Usage: 14.3 MB, less than 52.85% of Python3 online submissions for Count Largest Group.
