# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

"""
Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
"""

# numbers, target = [2,7,11,15], 9
# numbers, target = [2,3,4], 6
# numbers, target = [-1,0], -1
# numbers, target = [5,25,75], 100
numbers, target = [1,2,3,4,4,9,56,90], 8


# Two-pointer
# class Solution:
#     def twoSum(self, numbers: list(), target: int) -> list():
#         i, j = 0, len(numbers)-1
#         while i < j:
#             if numbers[i] + numbers[j] < target:
#                 i += 1
#             elif numbers[i] + numbers[j] > target:
#                 j -= 1
#             else:
#                 return [i+1, j+1]

# Runtime: 60 ms, faster than 85.45% of Python3 online submissions for Two Sum II - Input array is sorted.
# Memory Usage: 14.6 MB, less than 61.15% of Python3 online submissions for Two Sum II - Input array is sorted.


# Binary Search
# Note that the searching left boundary changes in every for loop
# Time complexity: O(nlogn)
class Solution:
    def twoSum(self, numbers: list(), target: int) -> list():
        for i in range(len(numbers)):
            n = target - numbers[i]
            left, right = i+1, len(numbers)-1
            while left <= right:
                mid = left + (right-left) // 2
                if numbers[mid] == n:
                    return [i+1, mid+1]
                elif numbers[mid] > n:
                    right = mid - 1
                else:
                    left = mid + 1


# Runtime: 96 ms, faster than 17.21% of Python3 online submissions for Two Sum II - Input array is sorted.
# Memory Usage: 14.7 MB, less than 62.55% of Python3 online submissions for Two Sum II - Input array is sorted.

solution = Solution()
print(solution.twoSum(numbers, target))




