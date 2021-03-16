# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

"""
Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e., max profit = 0.
"""

# prices = [7,1,5,3,6,4] # 7
# prices = [1,2,3,4,5] # 4
# prices = [7,6,4,3,1] # 0
prices = [1,7,4,2] # 6


# The key point is we need to consider every peak immediately following a valley to maximize the profit.
# In case we skip one of the peaks (trying to obtain more profit), 
# we will end up losing the profit over one of the transactions leading to an overall lesser profit.
# Time complexity: O(n)
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, i = 0, 0
        while i < len(prices): # note that (while i < len(prices)-1:) also works
            valley, peak = float("inf"), -float("inf")
            while i < len(prices) and prices[i] < valley:
                valley = prices[i]
                i += 1
            while i < len(prices) and prices[i] > peak:
                peak = prices[i]
                i += 1
            if valley != float("inf") and peak != -float("inf"):
                profit += (peak - valley)
        return profit

# Runtime: 60 ms, faster than 76.06% of Python3 online submissions for Best Time to Buy and Sell Stock II.
# Memory Usage: 15 MB, less than 67.47% of Python3 online submissions for Best Time to Buy and Sell Stock II.



solution = Solution()
print(solution.maxProfit(prices))

# 


