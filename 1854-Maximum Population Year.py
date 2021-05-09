# https://leetcode.com/problems/maximum-population-year/
# My post:
# https://leetcode.com/problems/maximum-population-year/discuss/1199810/Python-3-Sorted-using-stack-Explained


"""
Example 1:
Input: logs = [[1993,1999],[2000,2010]]
Output: 1993
Explanation: The maximum population is 1, and 1993 is the earliest year with this population.

Example 2:
Input: logs = [[1950,1961],[1960,1971],[1970,1981]]
Output: 1960
Explanation: 
The maximum population is 2, and it had happened in years 1960 and 1970.
The earlier year between them is 1960.
"""


# logs = [[1993,1999],[2000,2010]]
# logs = [[1950,1961],[1960,1971],[1970,1981]]
# logs = [[2012,2014],[2032,2038],[1989,2035],[1979,1981],[2010,2013],[1971,2036],[2024,2037],[2028,2047]]
logs = [[2008,2026],[2004,2008],[2034,2035],[1999,2050],[2049,2050],[2011,2035],[1966,2033],[2044,2049]] # Expected: 2011



from typing import List
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        bir = [logs[i][0] for i in range(len(logs))]
        dea = [logs[i][1] for i in range(len(logs))]
        bir.sort()
        dea.sort()
        res = 0
        stack, mpop = [], 0
        j = 0
        for i in range(len(bir)):
            if bir[i] < dea[j]:
                stack.append(bir[i])
            elif bir[i] >= dea[j]:
                length = len(stack)
                while dea[j] <= bir[i]:
                    tmp = stack.pop()
                    if length > mpop:
                        res = tmp
                        mpop = length
                    j += 1
                stack.append(bir[i])
        length = len(stack)
        if length > mpop:
            res = stack.pop()
        return res


solution = Solution()
print(solution.maximumPopulation(logs))


# Runtime: 40 ms, faster than 77.78% of Python3 online submissions for Maximum Population Year.
# Memory Usage: 14.3 MB, less than 44.44% of Python3 online submissions for Maximum Population Year.

