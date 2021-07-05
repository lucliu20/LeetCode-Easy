# https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/

"""
Example 1:
Input: nums = [1,2,10,5,7]
Output: true
Explanation: By removing 10 at index 2 from nums, it becomes [1,2,5,7].
[1,2,5,7] is strictly increasing, so return true.

Example 2:
Input: nums = [2,3,1,2]
Output: false
Explanation:
[3,1,2] is the result of removing the element at index 0.
[2,1,2] is the result of removing the element at index 1.
[2,3,2] is the result of removing the element at index 2.
[2,3,1] is the result of removing the element at index 3.
No resulting array is strictly increasing, so return false.

Example 3:
Input: nums = [1,1,1]
Output: false
Explanation: The result of removing any element is [1,1].
[1,1] is not strictly increasing, so return false.

Example 4:
Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is already strictly increasing, so return true.
"""


# nums = [1,2,10,5,7]
# nums = [2,3,1,2]
# nums = [1,1,1]
# nums = [1,2,3]
# nums = [3,1]
# Test case: #103
nums = [100,21,100] # True
# Test case: #105
# nums = [962,23,27,555] # True



from typing import List
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        diff, cnt = [], 0
        if len(nums) == 2:
            return True
        for i in range(len(nums)-1):
            tmp = nums[i+1] - nums[i]
            if tmp <= 0:
                cnt += 1
            if cnt > 1:
                return False
            diff.append(tmp)
        for j in range(len(diff)):
            if diff[j] <= 0:
                if j == 0 or j == len(diff)-1:
                    return True
                elif diff[j-1] + diff[j] <= 0 and diff[j+1] + diff[j] <= 0:
                    return False
        return True


# 109 / 109 test cases passed.
# Runtime: 52 ms, faster than 77.07% of Python3 online submissions for Remove One Element to Make the Array Strictly Increasing.
# Memory Usage: 14.4 MB, less than 49.84% of Python3 online submissions for Remove One Element to Make the Array Strictly Increasing.



solution = Solution()
print(solution.canBeIncreasing(nums))

