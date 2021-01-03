# https://leetcode.com/problems/maximum-units-on-a-truck/
# My post:
# https://leetcode.com/problems/maximum-units-on-a-truck/discuss/999229/Python-3-Sorted-Simple

"""
Example 1:
Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.

Example 2:
Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
Output: 91
"""

boxTypes, truckSize = [[1,3],[2,2],[3,1]], 4 # 8
# boxTypes, truckSize = [[5,10],[2,5],[4,7],[3,9]], 10 # 91

class Solution:
    def maximumUnits(self, boxTypes: list(list()), truckSize: int) -> int:
        res, count = 0, 0
        boxTypes = sorted(boxTypes,key=lambda x: x[1],reverse=True)
        for i,j in boxTypes:
            if (count + i) <= truckSize:
                res += i * j
                count += i
            else:
                res += (truckSize - count) * j
                break
        return res

#         res, count = 0, 0
#         boxTypes = sorted(boxTypes,key=lambda x: x[1],reverse=True)
#         for i in range(len(boxTypes)):
#             if (count + boxTypes[i][0]) <= truckSize:
#                 res += boxTypes[i][0] * boxTypes[i][1]
#                 count += boxTypes[i][0]
#             else:
#                 res += (truckSize - count) * boxTypes[i][1]
#                 break
#         return res


solution = Solution()
print(solution.maximumUnits(boxTypes, truckSize))

# Runtime: 144 ms, faster than 100.00% of Python3 online submissions for Maximum Units on a Truck.
# Memory Usage: 14.6 MB, less than 100.00% of Python3 online submissions for Maximum Units on a Truck.