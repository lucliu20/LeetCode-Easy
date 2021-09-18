# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

"""
Example 1:
Input: nums = [1,2,2,1], k = 1
Output: 4
Explanation: The pairs with an absolute difference of 1 are:
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]

Example 2:
Input: nums = [1,3], k = 3
Output: 0
Explanation: There are no pairs with an absolute difference of 3.

Example 3:
Input: nums = [3,2,1,5,4], k = 2
Output: 3
Explanation: The pairs with an absolute difference of 2 are:
- [3,2,1,5,4]
- [3,2,1,5,4]
- [3,2,1,5,4]

"""


nums, k = [1,2,2,1], 1
# nums, k = [1,3], 3
# nums, k = [3,2,1,5,4], 2



from typing import List
# Brute force
# Time complexity: O(N**2)
# Space complexity: O(1)
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    res += 1
        return res


# Runtime: 244 ms, faster than 20.00% of Python3 online submissions for Count Number of Pairs With Absolute Difference K.
# Memory Usage: 14.3 MB, less than 40.00% of Python3 online submissions for Count Number of Pairs With Absolute Difference K.


# Hash Map
# Time complexity: O(N)
# Space complexity: O(N)
import collections
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        res, mydict = 0, collections.defaultdict(int)
        for i in range(len(nums)):
            x1 = nums[i] - k
            x2 = nums[i] + k
            if x1 in mydict:
                res += mydict[x1]
            if x2 in mydict:
                res += mydict[x2]
            mydict[nums[i]] += 1
        return res

# Runtime: 64 ms, faster than 20.00% of Python3 online submissions for Count Number of Pairs With Absolute Difference K.
# Memory Usage: 14.2 MB, less than 40.00% of Python3 online submissions for Count Number of Pairs With Absolute Difference K.


solution = Solution()
print(solution.countKDifference(nums, k))
