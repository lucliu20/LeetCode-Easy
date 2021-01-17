# https://leetcode.com/contest/weekly-contest-224/
# 1725. Number Of Rectangles That Can Form The Largest Square
# https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/
# My post:
# https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/discuss/1020735/Python-3-Intuitive-Simple


"""
Example 1:
Input: rectangles = [[5,8],[3,9],[5,12],[16,5]]
Output: 3
Explanation: The largest squares you can get from each rectangle are of lengths [5,3,5,5].
The largest possible square is of length 5, and you can get it out of 3 rectangles.

Example 2:
rectangles = [[2,3],[3,7],[4,3],[3,7]]
Output: 3
"""

# rectangles = [[5,8],[3,9],[5,12],[16,5]]
rectangles = [[2,3],[3,7],[4,3],[3,7]]

class Solution:
    def countGoodRectangles(self, rectangles: list(list())) -> int:
        maxLen = []
        for i, j in rectangles:
            maxLen.append(min(i, j))
        t = max(maxLen)
        return maxLen.count(t)

solution = Solution()
print(solution.countGoodRectangles(rectangles))

# 


