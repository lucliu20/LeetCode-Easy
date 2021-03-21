# https://leetcode.com/problems/maximum-ascending-subarray-sum/

nums = [10,20,30,5,10,50]
# nums = [10,20,30,40,50]
# nums = [12,17,15,13,10,11,12]
# nums = [100,10,1]


from typing import List
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = nums[0]
        tmp = nums[0]
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                tmp += nums[i+1]
            else:
                res = max(res, tmp)
                tmp = nums[i+1]
        return max(res, tmp)


solution = Solution()
print(solution.maxAscendingSum(nums))

