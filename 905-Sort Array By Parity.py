# https://leetcode.com/problems/sort-array-by-parity/

"""
Example 1:
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
"""

# A = [3,1,2,4]
A = [3,7,1,2,6,4]

class Solution:
    def sortArrayByParity(self, A: list()) -> list():
        j = 0
        for i in range(len(A)):
            if A[i]%2 == 0: # an even number
                A[j], A[i] = A[i], A[j]
                j += 1
        return A

solution = Solution()
print(solution.sortArrayByParity(A))

# Runtime: 76 ms, faster than 84.68% of Python3 online submissions for Sort Array By Parity.
# Memory Usage: 15 MB, less than 57.77% of Python3 online submissions for Sort Array By Parity.

