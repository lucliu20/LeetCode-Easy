# https://leetcode.com/problems/second-largest-digit-in-a-string/

"""
Example 1:
Input: s = "dfa12321afd"
Output: 2
Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.

Example 2:
Input: s = "abc1111"
Output: -1
Explanation: The digits that appear in s are [1]. There is no second largest digit. 
"""


# s = "dfa12321afd"
# s = "abc1111"
s = "sjhtz8344"


class Solution:
    def secondHighest(self, s: str) -> int:
        mylist = [-1,-1]
        largest = -float("inf")
        for i in range(len(s)):
            if s[i].isdigit():
                tmp = int(s[i])
                if tmp > largest:
                    mylist[1], mylist[0] = mylist[0], tmp
                    largest = tmp
                elif tmp < largest and tmp > mylist[1]:
                    mylist[1] = tmp
        return mylist[1]


solution = Solution()
print(solution.secondHighest(s))

# Runtime: 36 ms, faster than 80.51% of Python3 online submissions for Second Largest Digit in a String.
# Memory Usage: 14.3 MB, less than 51.82% of Python3 online submissions for Second Largest Digit in a String.

