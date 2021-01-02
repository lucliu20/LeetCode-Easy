# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

# Example 1:
# Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
# Output: 2
# Explanation: 
# For arr1[0]=4 we have: 
# |4-10|=6 > d=2 
# |4-9|=5 > d=2 
# |4-1|=3 > d=2 
# |4-8|=4 > d=2 
# For arr1[1]=5 we have: 
# |5-10|=5 > d=2 
# |5-9|=4 > d=2 
# |5-1|=4 > d=2 
# |5-8|=3 > d=2
# For arr1[2]=8 we have:
# |8-10|=2 <= d=2
# |8-9|=1 <= d=2
# |8-1|=7 > d=2
# |8-8|=0 <= d=2

# Example 2:
# Input: arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
# Output: 2

# Example 3:
# Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
# Output: 1

# arr1 = [4,5,8]
# arr2 = [10,9,1,8]
# d = 2

# arr1 = [1,4,2,3]
# arr2 = [-4,-3,6,10,20,30]
# d = 3

arr1 = [2,1,100,3]
arr2 = [-5,-2,10,-3,7] # [-5, -3, -2, 7, 10]
d = 6

# Two-pointer, sorted
# Refer to the following post:
# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/discuss/546501/Python-two-pointers-O(n-log-n)
class Solution:
    def findTheDistanceValue(self, arr1: list(), arr2: list(), d: int) -> int:
        arr1.sort()
        arr2.sort()
        ans = i = j = 0
        while i < len(arr1) and j < len(arr2): 
            if arr1[i] <= arr2[j] + d: 
                if arr1[i] < arr2[j] - d: ans += 1
                i += 1
            else: j += 1
        return ans + len(arr1) - i

# Runtime: 68 ms, faster than 98.75% of Python3 online submissions for Find the Distance Value Between Two Arrays.
# Memory Usage: 14.2 MB, less than 94.83% of Python3 online submissions for Find the Distance Value Between Two Arrays.



# My initial approach:
# class Solution:
#     def findTheDistanceValue(self, arr1: list(), arr2: list(), d: int) -> int:
#         res = 0
#         arr1.sort()
#         arr2.sort()
#         tmp = arr1[0]
#         for i in range(len(arr2)):
#             if tmp <= arr1[i-1]:
#                 if arr1[0] - arr2[i] >= 0 and arr1[0] - arr2[i] <= d:
#                     continue
#                 elif arr1[0] - arr2[i] >= 0 and arr1[0] - arr2[i] > d:
#                     res += 1
#                 elif arr1[0] - arr2[i] < 0 and arr1[0] - arr2[i] >= -d:
#                     continue
#                 elif arr1[0] - arr2[i] < 0 and arr1[0] - arr2[i] < -d:
#                     res += 1
#                     tmp = arr1[i-1] + (abs(arr1[i-1] - arr2[i] + d) + 1)
#             else: break
#         return res

solution = Solution()
print(solution.findTheDistanceValue(arr1, arr2, d))

