# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

"""
Example 1:
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation: 
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.

Example 2:
Input: arr = [400]
Output: [-1]
Explanation: There are no elements to the right of index 0.
"""

arr = [17,18,5,4,6,1]
# arr = [400]

class Solution:
    def replaceElements(self, arr: list()) -> list():
        t = arr[-1]
        for i in range(len(arr)-1, -1, -1):
            if i == len(arr)-1:
                arr[i] = -1
            else:
                s = arr[i]
                arr[i] = t
                t = max(t, s)
        return arr

solution = Solution()
print(solution.replaceElements(arr))

# Runtime: 120 ms, faster than 83.44% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.
# Memory Usage: 15.1 MB, less than 98.02% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.


