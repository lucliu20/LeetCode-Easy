# https://leetcode.com/problems/find-lucky-integer-in-an-array/
# My post:
# https://leetcode.com/problems/find-lucky-integer-in-an-array/discuss/997196/Python-3-Explained-2-approaches

# Example 1:
# Input: arr = [2,2,3,4]
# Output: 2
# Explanation: The only lucky number in the array is 2 because frequency[2] == 2.

# Example 2:
# Input: arr = [1,2,2,3,3,3]
# Output: 3
# Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.

# Example 3:
# Input: arr = [2,2,2,3,3]
# Output: -1
# Explanation: There are no lucky numbers in the array.

# Example 4:
# Input: arr = [5]
# Output: -1
# 
# Example 5:
# Input: arr = [7,7,7,7,7,7,7]
# Output: 7


# arr = [2,2,3,4]
# arr = [1,2,2,3,3,3]
# arr = [2,2,2,3,3]
# arr = [5]
# arr = [7,7,7,7,7,7,7]
# arr = [1,13,1,5,14,1,18,20,20,15,2,1,3,6,2,19,13,3,18,16,18,2,1,10,9,2,19,12,5,19,7,4,4,6,19,2,3,13,18,18,16,18,16,16,9,2,17,11,2,4,7,18,13,14,4,15,14,10,17,11,14,1,7,10,12,10,9,1,11]
# 4
arr = [3,19,18,2,9,4,7,11,15,7,14,10,11,9,8,5,4,14,11,4,16,3,13,14,14,15,8,19,3,5,20,15,14,10,16,11,17,20,11,20,15,3,20,5,12,2,15,12,14,16,20,17,15,8,18,9,8,5,12,3,5,15,14,10,2,20,20,3,13,9,1,3,16,18,14,16,13,9,18,13,9,3,5,19]
# 1

import collections
# Approach #1: Using a list or set to keep track of the candidates, and defaultdict, one-pass
# class Solution:
#     def findLucky(self, arr: list()) -> int:
#         res = []
#         # arr.sort()
#         md = collections.defaultdict(int)
#         for i in arr:
#             md[i] += 1
#             if i == md[i]:
#                 res.append(i)
#             elif i < md[i] and i in res:
#                 res.remove(i)
#         return max(res) if res else -1

# Without sort():
# Runtime: 52 ms, faster than 86.29% of Python3 online submissions for Find Lucky Integer in an Array.
# Memory Usage: 14.4 MB, less than 10.95% of Python3 online submissions for Find Lucky Integer in an Array.

# With sort():
# Runtime: 44 ms, faster than 99.41% of Python3 online submissions for Find Lucky Integer in an Array.
# Memory Usage: 14.4 MB, less than 10.95% of Python3 online submissions for Find Lucky Integer in an Array.

# Approach #2: Using sorted() function and Counter()
class Solution:
    def findLucky(self, arr: list()) -> int:
        md = collections.Counter(arr)
        for key, value in sorted(md.items(), reverse=True):
            if key == value: return key
        return -1

# Runtime: 44 ms, faster than 99.41% of Python3 online submissions for Find Lucky Integer in an Array.
# Memory Usage: 14.4 MB, less than 34.71% of Python3 online submissions for Find Lucky Integer in an Array.

solution = Solution()
print(solution.findLucky(arr))

