# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

# Example 1:
# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true] 
# Explanation: 
# Kid 1 has 2 candies and if he or she receives all extra candies (3) will have 5 candies --- the greatest number of candies among the kids. 
# Kid 2 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids. 
# Kid 3 has 5 candies and this is already the greatest number of candies among the kids. 
# Kid 4 has 1 candy and even if he or she receives all extra candies will only have 4 candies. 
# Kid 5 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids. 

# Example 2:
# Input: candies = [4,2,1,1,2], extraCandies = 1
# Output: [true,false,false,false,false] 
# Explanation: There is only 1 extra candy, therefore only kid 1 will have the greatest number of candies among the kids regardless of who takes the extra candy.

# Example 3:
# Input: candies = [12,1,12], extraCandies = 10
# Output: [true,false,true]

candies, extraCandies = [2,3,5,1,3], 3
# candies, extraCandies = [4,2,1,1,2], 1
# candies, extraCandies = [12,1,12], 10

class Solution:
    def kidsWithCandies(self, candies: list(), extraCandies: int) -> list():
        great = max(candies)
        return [((candies[i]+extraCandies)>=great) for i in range(len(candies))]

solution = Solution()
print(solution.kidsWithCandies(candies, extraCandies))

# Runtime: 28 ms, faster than 98.25% of Python3 online submissions for Kids With the Greatest Number of Candies.
# Memory Usage: 14.1 MB, less than 90.33% of Python3 online submissions for Kids With the Greatest Number of Candies.

