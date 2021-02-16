# https://leetcode.com/problems/decode-xored-array/

"""
Example 1:
Input: encoded = [1,2,3], first = 1
Output: [1,0,2,1]
Explanation: If arr = [1,0,2,1], then first = 1 and encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3]

Example 2:
Input: encoded = [6,2,7,3], first = 4
Output: [4,2,0,7,4]
"""

# encoded, first = [1,2,3], 1
encoded, first = [6,2,7,3], 4

import operator
import itertools
class Solution:
    def decode(self, encoded: list(), first: int) -> list():
        encoded.insert(0, first)
        return list(itertools.accumulate(encoded, operator.xor))

solution = Solution()
print(solution.decode(encoded, first))

# Runtime: 220 ms, faster than 92.55% of Python3 online submissions for Decode XORed Array.
# Memory Usage: 15.8 MB, less than 64.84% of Python3 online submissions for Decode XORed Array.


