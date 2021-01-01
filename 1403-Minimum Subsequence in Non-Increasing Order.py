# https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/

# Example 1:
# Input: nums = [4,3,10,9,8]
# Output: [10,9] 
# Explanation: The subsequences [10,9] and [10,8] are minimal such that the sum of their elements is strictly greater than
# the sum of elements not included, however, the subsequence [10,9] has the maximum total sum of its elements. 

# Example 2:
# Input: nums = [4,4,7,6,7]
# Output: [7,7,6] 
# Explanation: The subsequence [7,7] has the sum of its elements equal to 14 which is not strictly greater than
# the sum of elements not included (14 = 4 + 4 + 6). Therefore, the subsequence [7,6,7] is the minimal satisfying the conditions.
# Note the subsequence has to returned in non-decreasing order.  

# Example 3:
# Input: nums = [6]
# Output: [6]

nums = [4,3,10,9,8]
# nums = [4,4,7,6,7]
# nums = [6]
# nums = [4,6,4,4,8,5,1,7,9]
# nums = [8,8]

# Sort: [10, 9, 8, 4, 3]
# Split the array to two parts, using t and s respectively to track the sum of the two parts
# t = 10, s = 24
# t = 10 + 9, s = 24 - 9
class Solution:
    def minSubsequence(self, nums: list()) -> list():
        nums.sort(reverse=True)
        print(nums)
        s = sum(nums[1:])
        t = nums[0]
        res = [nums[0]]
        for i in range(1, len(nums)):
            if t > s: break
            else:
                s -= nums[i]
                t += nums[i]
                res.append(nums[i])
        return res

solution = Solution()
print(solution.minSubsequence(nums))

# Runtime: 52 ms, faster than 98.08% of Python3 online submissions for Minimum Subsequence in Non-Increasing Order.
# Memory Usage: 14.4 MB, less than 24.01% of Python3 online submissions for Minimum Subsequence in Non-Increasing Order.


