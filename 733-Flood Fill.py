# https://leetcode.com/problems/flood-fill/

"""
Example 1:
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
"""

image = [[1,1,1],[1,1,0],[1,0,1]]
sr, sc, newColor = 1, 1, 2

class Solution:
    def floodFill(self, image: list(list()), sr: int, sc: int, newColor: int) -> list(list()):
        visited = set()
        stack = [(sr, sc)]
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        curColor = image[sr][sc]
        image[sr][sc] = newColor
        visited.add((sr, sc))
        while stack:
            r, c = stack.pop()
            for i, j in directions:
                if (r+i) in range(0, len(image)) and (c+j) in range(0, len(image[0])):
                    if (r+i, c+j) not in visited:
                        if image[r+i][c+j] == curColor:
                            image[r+i][c+j] = newColor
                            visited.add((r+i, c+j))
                            stack.append((r+i, c+j))
        return image

solution = Solution()
print(solution.floodFill(image, sr, sc, newColor))

# Runtime: 72 ms, faster than 85.19% of Python3 online submissions for Flood Fill.
# Memory Usage: 14.2 MB, less than 92.28% of Python3 online submissions for Flood Fill.


