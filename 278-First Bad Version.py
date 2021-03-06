# https://leetcode.com/problems/first-bad-version/

"""
Example 1:
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:
Input: n = 1, bad = 1
Output: 1
"""


n, bad = 6, 4
# n, bad = 1, 1

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    if version >= bad: return True
    return False

# Time complexity : O(logn)
# class Solution:
#     def firstBadVersion(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         left, right = 1, n
#         while left <= right:
#             mid = left + ((right-left) // 2)
#             if isBadVersion(mid):
#                 if isBadVersion(mid-1): # Use the element's left neighbor to determine
#                     right = mid - 1
#                 else:
#                     return mid
#             else:
#                 left = mid + 1

# Runtime: 32 ms, faster than 54.73% of Python3 online submissions for First Bad Version.
# Memory Usage: 14 MB, less than 92.33% of Python3 online submissions for First Bad Version.


# Attempt to implement with the LeetCode template II
# Note that the "right" starts as "n+1", and the post-processing needs some tweaks as well in terms of the "if" condition is removed.
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n + 1
        while left < right:
            mid = left + ((right-left) // 2)
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        
        # Post-processing:
        # End Condition: left == right
        # if left != n + 1 and isBadVersion(left):
        return left

# Runtime: 20 ms, faster than 99.02% of Python3 online submissions for First Bad Version.
# Memory Usage: 14.2 MB, less than 77.39% of Python3 online submissions for First Bad Version.


solution = Solution()
print(solution.firstBadVersion(5))





