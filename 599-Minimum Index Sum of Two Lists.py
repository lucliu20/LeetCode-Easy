# https://leetcode.com/problems/minimum-index-sum-of-two-lists/

"""
Example 1:
Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".

Example 2:
Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

Example 3:
Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
Output: ["KFC","Burger King","Tapioca Express","Shogun"]

Example 4:
Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KNN","KFC","Burger King","Tapioca Express","Shogun"]
Output: ["KFC","Burger King","Tapioca Express","Shogun"]

Example 5:
Input: list1 = ["KFC"], list2 = ["KFC"]
Output: ["KFC"]
"""


# list1, list2 = ["Shogun","Tapioca Express","Burger King","KFC"], ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# list1, list2 = ["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Shogun","Burger King"]
# list1, list2 = ["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Burger King","Tapioca Express","Shogun"]
# list1, list2 = ["Shogun","Tapioca Express","Burger King","KFC"], ["KNN","KFC","Burger King","Tapioca Express","Shogun"]
list1, list2 = ["KFC"], ["KFC"]


import collections
class Solution:
    def findRestaurant(self, list1: list(), list2: list()) -> list():
        d1 = collections.defaultdict(list)
        res, m = [], float("inf")
        for i in range(len(list1)):
            d1[list1[i]].append(i)
        
        for i in range(len(list2)):
            d1[list2[i]].append(i)
        
        for key, values in d1.items():
            if len(values) > 1:
                if sum(values) < m:
                    res.clear()
                    res.append(key)
                    m = sum(values)
                elif sum(values) == m:
                    res.append(key)
        
        return res

solution = Solution()
print(solution.findRestaurant(list1, list2))

# Runtime: 152 ms, faster than 65.31% of Python3 online submissions for Minimum Index Sum of Two Lists.
# Memory Usage: 15 MB, less than 15.31% of Python3 online submissions for Minimum Index Sum of Two Lists.

