# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/

"""
Example 1:
Input: nums = [90], k = 1
Output: 0
Explanation: There is one way to pick score(s) of one student:
- [90]. The difference between the highest and lowest score is 90 - 90 = 0.
The minimum possible difference is 0.

Example 2:
Input: nums = [9,4,1,7], k = 2
Output: 2
Explanation: There are six ways to pick score(s) of two students:
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 1 = 8.
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 7 = 2.
- [9,4,1,7]. The difference between the highest and lowest score is 4 - 1 = 3.
- [9,4,1,7]. The difference between the highest and lowest score is 7 - 4 = 3.
- [9,4,1,7]. The difference between the highest and lowest score is 7 - 1 = 6.
The minimum possible difference is 2.
"""

# nums, k = [90], 1
# nums, k = [9,4,1,7], 2
nums, k = [9,4,1,5], 3


from typing import List
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        res = float("inf")
        for i in range(len(nums) - k + 1):
            j = i + k - 1
            res = min(res, nums[j] - nums[i])
        return res


# Runtime: 100 ms, faster than 91.01% of Python3 online submissions for Minimum Difference Between Highest and Lowest of K Scores.
# Memory Usage: 14.4 MB, less than 85.80% of Python3 online submissions for Minimum Difference Between Highest and Lowest of K Scores.

solution = Solution()
print(solution.minimumDifference(nums, k))
