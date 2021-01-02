# https://leetcode.com/problems/create-target-array-in-the-given-order/

# Example 1:
# Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
# Output: [0,4,1,3,2]
# Explanation:
# nums       index     target
# 0            0        [0]
# 1            1        [0,1]
# 2            2        [0,1,2]
# 3            2        [0,1,3,2]
# 4            1        [0,4,1,3,2]

# Example 2:
# Input: nums = [1,2,3,4,0], index = [0,1,2,3,0]
# Output: [0,1,2,3,4]
# Explanation:
# nums       index     target
# 1            0        [1]
# 2            1        [1,2]
# 3            2        [1,2,3]
# 4            3        [1,2,3,4]
# 0            0        [0,1,2,3,4]

# Example 3:
# Input: nums = [1], index = [0]
# Output: [1]

nums = [0,1,2,3,4]
index = [0,1,2,2,1]

# nums = [1,2,3,4,0]
# index = [0,1,2,3,0]

# nums = [1]
# index = [0]

# List comprehension way
# Note that if you do return [t.insert(i, n) for i, n in zip(index, nums)]; you will get [None, None, None, None, None].
# That's because insert() function returns "None" and modifies the list.
class Solution:
    def createTargetArray(self, nums: list(), index: list()) -> list():
        t = []
        [t.insert(i, n) for i, n in zip(index, nums)]
        return t


# Runtime: 28 ms, faster than 92.11% of Python3 online submissions for Create Target Array in the Given Order.
# Memory Usage: 14.3 MB, less than 37.59% of Python3 online submissions for Create Target Array in the Given Order.

# class Solution:
#     def createTargetArray(self, nums: list(), index: list()) -> list():
#         target = list()
#         for i in range(len(index)):
#             target.insert(index[i],nums[i])


solution = Solution()
print(solution.createTargetArray(nums, index))

# Runtime: 32 ms, faster than 69.15% of Python3 online submissions for Create Target Array in the Given Order.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Create Target Array in the Given Order.