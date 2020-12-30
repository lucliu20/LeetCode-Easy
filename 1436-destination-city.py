# https://leetcode.com/problems/destination-city/
# My post:
# https://leetcode.com/problems/destination-city/discuss/992846/Python-3-Hash-Explained-O(n)

# https://realpython.com/python-defaultdict/

# Example 1:
# Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
# Output: "Sao Paulo" 
# Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

# Example 2:
# Input: paths = [["B","C"],["D","B"],["C","A"]]
# Output: "A"
# Explanation: All possible trips are: 
# "D" -> "B" -> "C" -> "A". 
# "B" -> "C" -> "A". 
# "C" -> "A". 
# "A". 
# Clearly the destination city is "A".

# Example 3:
# Input: paths = [["A","Z"]]
# Output: "Z"

# paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
paths = [["B","C"],["D","B"],["C","A"]]
# paths = [["A","Z"]]

# My approach
# import collections
# class Solution:
#     def destCity(self, paths: list(list())) -> str:
#         myd = collections.defaultdict(list)
#         for i in range(len(paths)):
#             for j in range(len(paths[0])):
#                 myd[paths[i][j]].append([i,j])
#         for k, v in myd.items():
#             if len(v) == 1:
#                 if v[0][1] == len(paths[0])-1:
#                     return k

# Runtime: 48 ms, faster than 90.97% of Python3 online submissions for Destination City.
# Memory Usage: 14.3 MB, less than 56.98% of Python3 online submissions for Destination City.

# Approach #2. Referred to a discussion
# Explanation:
# Create a map where key,value = source, destination.
# Iterate over destinations and if it is not a key in map, return destination.
# class Solution:
#     def destCity(self, paths: list(list())) -> str:
#         outgoings = collections.defaultdict(int)
#         
#         for src, dst in paths:
#             outgoings[src] += 1
#         
#         for src, dst in paths:
#             if dst not in outgoings:
#                 return dst

# Runtime: 44 ms
# Memory Usage: 13.8 MB

# Approach #3. Referred to a discussion
# https://leetcode.com/problems/destination-city/discuss/609770/Clean-Python-3-Set-in-two-lines
class Solution:
    def destCity(self, paths: list(list())) -> str:
        # The post uses map() function
        # A, B = map(set, zip(*paths))
        # print(*zip(*paths))
        # print(A, B)
        # for x, y, z in zip(*paths):
        #     print(x, y, z)
        # Here using a generator expression
        # with Set constructor
        A, B = (set(x) for x in zip(*paths))
        # Note that using curly braces {} won't work
        # A, B = ({x} for x in zip(*paths))
        return (B - A).pop()
        # Set Difference (operator "-") of B and A is the set of all items that are in B but not in A.

solution = Solution()
print(solution.destCity(paths))

# 

