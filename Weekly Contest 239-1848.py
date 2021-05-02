# 1848. Minimum Distance to the Target Element
# My post:
# https://leetcode.com/problems/minimum-distance-to-the-target-element/discuss/1186873/Python-3-Simple-Intuitive


"""
Example 1:
Input: nums = [1,2,3,4,5], target = 5, start = 3
Output: 1
Explanation: nums[4] = 5 is the only value equal to target, so the answer is abs(4 - 3) = 1.

Example 2:
Input: nums = [1], target = 1, start = 0
Output: 0
Explanation: nums[0] = 1 is the only value equal to target, so the answer is abs(0 - 0) = 1.

Example 3:
Input: nums = [1,1,1,1,1,1,1,1,1,1], target = 1, start = 0
Output: 0
Explanation: Every value of nums is 1, but nums[0] minimizes abs(i - start), which is abs(0 - 0) = 0.
"""


nums, target, start = [1,2,3,4,5], 5, 3
# nums, target, start = [1], 1, 0
# nums, target, start = [1,1,1,1,1,1,1,1,1,1], 1, 0


from typing import List
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res = float("inf")
        for i in range(len(nums)):
            if nums[i] == target:
                res = min(res, abs(i-start))
        return res


solution = Solution()
print(solution.getMinDistance(nums, target, start))

# Runtime: 92 ms
# Memory Usage: 14.5 MB


