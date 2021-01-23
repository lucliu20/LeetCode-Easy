# https://leetcode.com/problems/check-if-n-and-its-double-exist/
# My post
# https://leetcode.com/problems/check-if-n-and-its-double-exist/discuss/1031467/Python-3-HashTable-One-pass-Explained-99-faster

"""
Example 1:
Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.

Example 2:
Input: arr = [7,1,14,11]
Output: true
Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.

Example 3:
Input: arr = [3,1,7,11]
Output: false
Explanation: In this case does not exist N and M, such that N = 2 * M.
"""

# arr = [10,2,5,3]
# arr = [7,1,14,11]
arr = [3,1,7,11]


class Solution:
    def checkIfExist(self, arr: list()) -> bool:
        h = dict()
        for i in range(len(arr)):
            if arr[i]*2 in h or arr[i] in h.values():
                return True
            else:
                h[arr[i]] = arr[i]*2
        return False

solution = Solution()
print(solution.checkIfExist(arr))

# Runtime: 40 ms
# Memory Usage: 14.2 MB

