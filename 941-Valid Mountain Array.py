# https://leetcode.com/problems/valid-mountain-array/

"""
Example 1:
Input: arr = [2,1]
Output: false

Example 2:
Input: arr = [3,5,5]
Output: false

Example 3:
Input: arr = [0,3,2,1]
Output: true
"""

# arr = [2,1]
# arr = [3,5,5]
# arr = [0,3,2,1]
# arr = [0,1,2,1,2]
# arr = [0,1,2,3,4]
# arr = [3,2,1,0]
arr = [0,1,2,4,2,1]

class Solution:
    def validMountainArray(self, arr: list()) -> bool:
        if len(arr) < 3: return False
        toPeak = True
        p = max(arr)
        for i in range(1, len(arr)):
            if toPeak:
                if arr[i-1] >= arr[i]:
                    return False
                if arr[i] == p and i == len(arr)-1:
                    return False
                elif arr[i] == p:
                    toPeak = False
            else:
                if arr[i-1] <= arr[i]:
                    return False
        return True

solution = Solution()
print(solution.validMountainArray(arr))

# Runtime: 200 ms, faster than 71.38% of Python3 online submissions for Valid Mountain Array.
# Memory Usage: 15.6 MB, less than 56.02% of Python3 online submissions for Valid Mountain Array.

