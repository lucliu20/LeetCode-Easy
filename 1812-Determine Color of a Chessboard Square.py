# https://leetcode.com/problems/determine-color-of-a-chessboard-square/

"""
Example 1:
Input: coordinates = "a1"
Output: false
Explanation: From the chessboard above, the square with coordinates "a1" is black, so return false.

Example 2:
Input: coordinates = "h3"
Output: true
Explanation: From the chessboard above, the square with coordinates "h3" is white, so return true.

Example 3:
Input: coordinates = "c7"
Output: false
"""



# coordinates = "a1"
# coordinates = "h3"
coordinates = "c7"


class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x = {"a":False, "b":True, "c":False, "d":True, "e":False, "f":True, "g":False, "h":True}
        y = {"1":False, "2":True, "3":False, "4":True, "5":False, "6":True, "7":False, "8":True}
        return False if x[coordinates[0]] == y[coordinates[1]] else True

solution = Solution()
print(solution.squareIsWhite(coordinates))

# Runtime: 32 ms, faster than 66.65% of Python3 online submissions for Determine Color of a Chessboard Square.
# Memory Usage: 14.2 MB, less than 71.24% of Python3 online submissions for Determine Color of a Chessboard Square.

