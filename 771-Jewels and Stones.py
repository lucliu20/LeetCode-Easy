# https://leetcode.com/problems/jewels-and-stones/

"""
Example 1:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Example 2:
Input: jewels = "z", stones = "ZZ"
Output: 0
"""

# jewels, stones = "aA", "aAAbbbb"
jewels, stones = "z", "ZZ"

import collections
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d = collections.Counter(stones)
        res = 0
        for char in jewels:
            if char in d:
                res += d[char]
        return res

solution = Solution()
print(solution.numJewelsInStones(jewels, stones))

# Runtime: 28 ms, faster than 85.59% of Python3 online submissions for Jewels and Stones.
# Memory Usage: 14 MB, less than 98.79% of Python3 online submissions for Jewels and Stones.

