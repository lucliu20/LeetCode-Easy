# https://leetcode.com/problems/find-center-of-star-graph/

"""
Example 1:
Input: edges = [[1,2],[2,3],[4,2]]
Output: 2
Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.

Example 2:
Input: edges = [[1,2],[5,1],[1,3],[1,4]]
Output: 1
"""


edges = [[1,2],[2,3],[4,2]]
# edges = [[1,2],[5,1],[1,3],[1,4]]



from typing import List
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        for i in range(len(edges)):
            if edges[i][0] == edges[i+1][0]:
                return edges[i][0]
            elif edges[i][0] == edges[i+1][1]:
                return edges[i][0]
            elif edges[i][1] == edges[i+1][0]:
                return edges[i][1]
            elif edges[i][1] == edges[i+1][1]:
                return edges[i][1]


# Runtime: 796 ms, faster than 66.48% of Python3 online submissions for Find Center of Star Graph.
# Memory Usage: 50.5 MB, less than 20.21% of Python3 online submissions for Find Center of Star Graph.


solution = Solution()
print(solution.findCenter(edges))

