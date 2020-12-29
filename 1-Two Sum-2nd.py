# https://leetcode.com/problems/two-sum/

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# nums, target = [2,7,11,15], 9
# nums, target = [3,2,4], 6
nums, target = [1,3,3], 6

# Approach #1: LeeCode solution #3
# class Solution:
#     def twoSum(self, nums: list(), target: int) -> list():
#         mydict = dict()
#         for i in range(len(nums)):
#             com = target - nums[i]
#             if com in mydict:
#                 return [mydict[com], i]
#             mydict[nums[i]] = i
#         return -1

# Runtime: 44 ms, faster than 91.07% of Python3 online submissions for Two Sum.
# Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Two Sum.

# Approach #2
"""
    nums = [2,7,11,15]  target = 9
    
    compliment = { 9-2  = 7  : "0",
                   9-7  = 2  : "1",
                   9-11 = -2 : "2",
                   9-15 = -6 : "3" 
    }
	nums[0] =2 not in complement:
			complement ={7:0}
	nums[1] =7 in complement:
			return [0,1]
"""
# class Solution:
#     def twoSum(self, nums: list(), target: int) -> list():
#         mydict = dict()
#         for i in range(len(nums)):
#             com = target - nums[i]
#             if nums[i] in mydict:
#                 return [mydict[nums[i]], i]
#             mydict[com] = i
#         return -1

# Runtime: 36 ms, faster than 99.42% of Python3 online submissions for Two Sum.
# Memory Usage: 14.4 MB, less than 100.00% of Python3 online submissions for Two Sum.

# Two-pass
class Solution:
    def twoSum(self, nums: list(), target: int) -> list():
        myd = {k: v for v, k in enumerate(nums)}
        # print(type(myd), myd, myd.keys(), type(myd.keys()))
        for i in range(len(nums)):
            if (target - nums[i]) in myd.keys():
                if myd[target - nums[i]] != i:
                    return [i, myd[target - nums[i]]]

solution = Solution()
print(solution.twoSum(nums, target))


# Runtime: 40 ms, faster than 96.30% of Python3 online submissions for Two Sum.
# Memory Usage: 14.7 MB, less than 33.34% of Python3 online submissions for Two Sum.

