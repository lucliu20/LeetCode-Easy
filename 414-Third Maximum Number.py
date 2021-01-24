# https://leetcode.com/problems/third-maximum-number/


"""
Example 1:
Input: nums = [3,2,1]
Output: 1
Explanation: The third maximum is 1.

Example 2:
Input: nums = [1,2]
Output: 2
Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

Example 3:
Input: nums = [2,2,3,1]
Output: 1
Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
"""

# nums = [3,2,1]
# nums = [1,2]
nums = [2,2,3,1]
# nums = [5,2,2]
# nums = [1,-2147483648,2]

# Keep track of the top 3 distinct numbers
class Solution:
    def thirdMax(self, nums: list()) -> int:
        fir = sec = thi = -float("inf")
        for n in nums:
            if n in (fir, sec, thi):
                continue
            if n > fir:
                fir, n = n, fir
            if n > sec:
                sec, n = n, sec
            if n > thi:
                thi, n = n, thi
        return thi if -float("inf") not in (fir, sec, thi) else fir

solution = Solution()
print(solution.thirdMax(nums))

# Runtime: 48 ms, faster than 88.04% of Python3 online submissions for Third Maximum Number.
# Memory Usage: 15.2 MB, less than 70.97% of Python3 online submissions for Third Maximum Number.


