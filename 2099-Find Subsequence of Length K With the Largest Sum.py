# nums, k = [18,3,19,-8,30,22,-35,11,16,18,-21,32,-7,-6,38,25,-21,-1,26,-8,-37,-39,-34,6,-36,-3,26,-32,22,-20,35,-35,-30,-8,11,7,-23,-9,-22,1,33,-6,12,2,27,-27,28,-12,21,12,16,21,33], 50
nums, k = [2,1,3,3], 2


from typing import List
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        res = []
        test = sorted(nums, reverse=True)
        for i in range(length):
            if k > 0 and nums[i] in test[:k]:
                res.append(nums[i])
                test.remove(nums[i])
                k -= 1
        return res


solution = Solution()
print(solution.maxSubsequence(nums, k))
