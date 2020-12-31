# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

# Example 1:
# Input: nums = [-3,2,-3,4,2]
# Output: 5
# Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
#                 step by step sum
#                 startValue = 4 | startValue = 5 | nums
#                   (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
#                   (1 +2 ) = 3  | (2 +2 ) = 4    |   2
#                   (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
#                   (0 +4 ) = 4  | (1 +4 ) = 5    |   4
#                   (4 +2 ) = 6  | (5 +2 ) = 7    |   2
# 
# Example 2:
# Input: nums = [1,2]
# Output: 1
# Explanation: Minimum start value should be positive. 
# 
# Example 3:
# Input: nums = [1,-2,-3]
# Output: 5

nums = [-3,2,-3,4,2]
# nums = [1,-2,-3]
# nums = [1,2]
# nums = [2,3,5,-5,-1] # 1
# nums = [5,4,-5,-5,0] # 2

# Approach #1: Track the minimum of the sum. If the sum is less than 1, then return the gap betweeen 2 and the minimum.
# class Solution:
#     def minStartValue(self, nums: list()) -> int:
#         if min(nums) >= 0: return 1
#         init = 1
#         mini = float("inf")
#         for i in range(len(nums)):
#             init += nums[i]
#             mini = min(mini, init)
#         return (2 - mini) if mini < 1 else 1

# Runtime: 28 ms, faster than 87.46% of Python3 online submissions for Minimum Value to Get Positive Step by Step Sum.
# Memory Usage: 14.2 MB, less than 63.54% of Python3 online submissions for Minimum Value to Get Positive Step by Step Sum.


# Simplified approach #1
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        init = 0
        mini = float("inf")
        for i in nums:
            init += i
            mini = min(mini, init)
        return (1 - mini) if mini < 0 else 1

# Runtime: 24 ms, faster than 97.66% of Python3 online submissions for Minimum Value to Get Positive Step by Step Sum.
# Memory Usage: 14.2 MB, less than 63.54% of Python3 online submissions for Minimum Value to Get Positive Step by Step Sum.


# Approach #2
# class Solution:
#     def minStartValue(self, nums: list()) -> int:
#         res = 0 # final value
#         cur = 0 # keep track of the current sum value, if it's less than 1, then find the new final value 'res' and also update the current sum itself.
#         for num in nums:
#             cur += num
#             if cur < 1:
#                 res += 1 - cur
#                 cur += 1 - cur
#         if res == 0: return 1
#         return res

solution = Solution()
print(solution.minStartValue(nums))


# Runtime: 32 ms
# Memory Usage: 13.8 MB

# Info only:
# Bruce force way:
# startValue = 1
# 
# while startValue >= 1:
#     add_nums = []
#     add_nums.append(nums[0] + startValue)
#     for i in range(1, len(nums)):
#         add_nums.append(nums[i] + add_nums[i-1])
#     if min(add_nums) >= 1:
#         break
#     startValue +=1
# 
# print(startValue)
