# https://leetcode.com/explore/learn/card/recursion-i/

s = 'Hello'
class Solution:
    def printReverse(self, s: str):
        def helper(index):
            if index == None or index == len(s): return
            helper(index+1)
            print(s[index])
        helper(0)

solution = Solution()
print(solution.printReverse(s))

# s = ["h","e","l","l","o"]
# class Solution:
#     def reverseString(self, s: list()) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         def helper(index, length):
#             if index == None or index == len(s)//2: return
#             helper(index+1, length-1)
#             s[index], s[length-1] = s[length-1], s[index]
#         helper(0, len(s))
# 
# solution = Solution()
# print(solution.reverseString(s))

