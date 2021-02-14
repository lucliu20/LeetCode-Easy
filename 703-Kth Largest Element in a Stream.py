# https://leetcode.com/problems/kth-largest-element-in-a-stream/
# Posted to query the solution
# https://leetcode.com/problems/kth-largest-element-in-a-stream/discuss/1064437/Python-3-Binary-Search-Tree-TLE-Any-idea-to-optimize

"""
Example 1:
Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]).
We are finding 3rd number from highest to lowest.
After kthLargest.add(3);, all the elements inside this instance is [4, 5, 8, 2, 3], and it return the 3rd largest element, so it returns 4.
After kthLargest.add(5);, all the elements inside this instance is [4, 5, 8, 2, 3, 5], and it return the 3rd largest element, so it returns 5.
After kthLargest.add(10);, all the elements inside this instance is [4, 5, 8, 2, 3, 5, 10], and it return the 3rd largest element, so it returns 5.
After kthLargest.add(9);, all the elements inside this instance is [4, 5, 8, 2, 3, 5, 10, 9], and it return the 3rd largest element, so it returns 8.
After kthLargest.add(4);, all the elements inside this instance is [4, 5, 8, 2, 3, 5, 10, 9, 4], and it return the 3rd largest element, so it returns 8.
"""

# Example 1
k = 3
nums = [4, 5, 8, 2]

# Example 2
# ["KthLargest","add","add","add","add","add"]
# [[1,[]],[-3],[-2],[-4],[0],[4]]
# k = 1
# nums = []

# Example 3:
# ["KthLargest","add","add","add","add","add"]
# [[1,[-2]],[-3],[0],[2],[-1],[4]]
# Expected: [null,-2,0,2,2,4]
# k = 1
# nums = [-2]

# Example 4:
# ["KthLargest","add","add","add","add","add"]
# [[2,[0]],[-1],[1],[-2],[-4],[3]]
# Expected: [null,-1,0,0,0,1]
# k = 2
# nums = [0]



# Binary Search Tree
# Refer to the Explore Card:
# https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/142/conclusion/1009/
# TLE
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None, count=0):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.count = count
# 
# 
# class KthLargest:
# 
#     def __init__(self, k: int, nums: list()):
#         self.k = k
#         if len(nums) == 0:
#             self.root = None
#         else:
#             self.root = TreeNode(nums[0],None,None,1)
#             for i in range(1, len(nums)):
#                 self.insertBST(self.root, nums[i])
#     
#     def insertBST(self, root: TreeNode, val: int):
#         """Inserts a node to the BST.
#         
#         :type root: TreeNode
#         :type val: int
#         """
#         if not root:
#             root = TreeNode(val,None,None,1)
#             return root
#         if val <= root.val:
#             root.left = self.insertBST(root.left, val)
#         else:
#             root.right = self.insertBST(root.right, val)
#         root.count += 1
#         return root
#     
#     def searchBST(self, root: TreeNode, n: int) -> int:
#         """Searches the kth largest element.
#         
#         :type root: TreeNode
#         :type n: int
#         :rtype: int
#         """
#         if n == 1 and root.count == 1:
#             return root.val
#         if n <= root.count:
#             if root.right and n <= root.right.count:
#                 res = self.searchBST(root.right, n)
#             else:
#                 if not root.right:
#                     n -= 1
#                 else:
#                     n = n - root.right.count - 1
#                 if n == 0:
#                     return root.val
#                 if root.left:
#                     res = self.searchBST(root.left, n)
#         else:
#             n = n - root.right.count - 1
#             if n == 0:
#                 return root.val
#             if root.left:
#                 res = self.searchBST(root.left, n)
#         return res
# 
#     def add(self, val: int) -> int:
#         tmp = self.insertBST(self.root, val)
#         if not self.root:
#             self.root = tmp
#         return self.searchBST(self.root, self.k)

import heapq
class KthLargest:

    def __init__(self, k: int, nums: list()):
        self.myheap = []
        self.k = k
        # The idea here is to maintain the top k elements in the array self.myheap
        for i in nums:
            if len(self.myheap) < self.k:
                heapq.heappush(self.myheap, i)
            else:
                if i > self.myheap[0]:
                    heapq.heappushpop(self.myheap, i) # Equivalent to heappush() followed by heappop()

    def add(self, val: int) -> int:
        if len(self.myheap) < self.k:
            heapq.heappush(self.myheap, val)
        else:
            if val > self.myheap[0]:
                heapq.heappushpop(self.myheap, val)
        return self.myheap[0]

# Runtime: 100 ms, faster than 59.29% of Python3 online submissions for Kth Largest Element in a Stream.
# Memory Usage: 18.2 MB, less than 92.43% of Python3 online submissions for Kth Largest Element in a Stream.

# heapq test:
# test = [4, 5, 8, 2]
# heapq.heapify(test) # output [2, 4, 8, 5]
# print(heapq.nlargest(1, test))

kthLargest = KthLargest(k, nums)
# Example 1
print(kthLargest.add(3))   # return 4
print(kthLargest.add(5))   # return 5
print(kthLargest.add(10))  # return 5
print(kthLargest.add(9))   # return 8
print(kthLargest.add(4))   # return 8

# Example 2
# print(kthLargest.add(-3))   # return -3
# print(kthLargest.add(-2))   # return -2
# print(kthLargest.add(-4))  # return -2
# print(kthLargest.add(0))   # return 0
# print(kthLargest.add(4))   # return 4

# Example 3, [-3],[0],[2],[-1],[4]
# print(kthLargest.add(-3))   # return -2
# print(kthLargest.add(0))   # return 0
# print(kthLargest.add(2))  # return 2
# print(kthLargest.add(-1))   # return 2
# print(kthLargest.add(4))   # return 4

# Example 4, [-1],[1],[-2],[-4],[3]
# print(kthLargest.add(-1))   # return -1
# print(kthLargest.add(1))   # return 0
# print(kthLargest.add(-2))  # return 0
# print(kthLargest.add(-4))   # return 0
# print(kthLargest.add(3))   # return 1


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)