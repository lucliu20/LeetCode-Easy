# https://leetcode.com/problems/array-partition-i/

"""
Example 1:
Input: nums = [1,4,3,2]
Output: 4
Explanation: All possible pairings (ignoring the ordering of elements) are:
1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4.

Example 2:
Input: nums = [6,2,6,5,1,2]
Output: 9
Explanation: The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.
"""

nums = [1,4,3,2]
# nums = [6,2,6,5,1,2]


class Solution:
    def arrayPairSum(self, nums: list()) -> int:
        nums.sort()
        s = 0
        for i in range(0, len(nums), 2):
            s += nums[i]
        return s

solution = Solution()
print(solution.arrayPairSum(nums))

# Runtime: 256 ms, faster than 87.17% of Python3 online submissions for Array Partition I.
# Memory Usage: 16.8 MB, less than 85.08% of Python3 online submissions for Array Partition I.


