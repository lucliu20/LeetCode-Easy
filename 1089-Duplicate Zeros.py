# https://leetcode.com/problems/duplicate-zeros/

"""
Example 1:
Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:
Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]
"""

# arr = [1,0,2,3,0,4,5,0]
# arr = [1,0,2,3,9,0,5,0] # [1, 0, 0, 2, 3, 9, 0, 0]
# arr = [1,2,3]
# arr = [0]
# arr = [0,0]
# arr = [0,1]
# arr = [1,0]
arr = [8,4,5,0,0,0,0,7] # [8,4,5,0,0,0,0,0]

# class Solution:
#     def duplicateZeros(self, arr: list()) -> None:
#         """
#         Do not return anything, modify arr in-place instead.
#         """
#         i = 0
#         while i < len(arr)-1:
#             if arr[i] == 0:
#                 for j in range(len(arr)-2, i, -1):
#                     arr[j+1] = arr[j]
#                 arr[i+1] = 0
#                 i += 2
#             else:
#                 i += 1

# Runtime: 1136 ms, faster than 8.20% of Python3 online submissions for Duplicate Zeros.
# Memory Usage: 14.8 MB, less than 67.56% of Python3 online submissions for Duplicate Zeros.

class Solution:
    def duplicateZeros(self, arr: list()) -> None:
        i, j = 0, len(arr)-1
        z = 0 # No. of duplicated zeros to be processed later
        while i < j:
            if arr[i] == 0:
                z += 1
                j -= 1
            i += 1
        
        if i == j and arr[i] == 0: # cover the cases like [8,4,5,0,0,0,0,7] or [1,0]
            arr[i+z] = 0
            k = i - 1
        else:
            k = len(arr) - 1 - z
        while k >= 0:
            if arr[k] == 0:
                arr[k+z] = 0
                arr[k+z-1] = 0
                k -= 1
                z -= 1
            else:
                arr[k+z] = arr[k]
                k -= 1

# Runtime: 68 ms, faster than 82.64% of Python3 online submissions for Duplicate Zeros.
# Memory Usage: 14.9 MB, less than 67.56% of Python3 online submissions for Duplicate Zeros.

solution = Solution()
solution.duplicateZeros(arr)
print(arr)


