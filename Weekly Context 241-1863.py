# https://leetcode.com/problems/sum-of-all-subset-xor-totals/

# nums = [5,1,6]
nums = [3,4,5,6,7,8]

import itertools
from typing import List
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = sum(nums)
        for i in range(2, len(nums)+1):
            for j in itertools.combinations(nums, i):
                tmp = 0
                for k in range(len(j)):
                    tmp = tmp^j[k]
                res += tmp
        return res


solution = Solution()
print(solution.subsetXORSum(nums))

# Runtime: 96 ms
# Memory Usage: 14.1 MB

