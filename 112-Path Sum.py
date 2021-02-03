# https://leetcode.com/problems/path-sum/

"""
Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false

Example 3:
Input: root = [1,2], targetSum = 0
Output: false
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Expected: True
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.right = TreeNode(1)
targetSum = 22

# Expected: False
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# targetSum = 5

# Expected: False
# root = TreeNode(1)
# root.left = TreeNode(2)
# targetSum = 0

# Expected: False
# [1,-2,-3,1,3,-2,null,-1], 3
# root = TreeNode(1)
# root.left = TreeNode(-2)
# root.right = TreeNode(-3)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)
# root.right.left = TreeNode(-2)
# root.left.left.left = TreeNode(-1)
# targetSum = 3

# Iteratively
# DFS
# 2 HashTables to track which nodes have been visisted and which node values have been counted/added.
# class Solution:
#     def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
#         if not root: return False
#         s = 0
#         stack = [root]
#         added = set()
#         visisted = set()
#         while stack:
#             t = stack[-1]
#             if t not in added:
#                 s += t.val
#                 added.add(t)
#             else:
#                 s -= t.val
#                 visisted.add(stack.pop())
#             if t.left == None and t.right == None:
#                 if s == targetSum:
#                     return True
#                 else:
#                     s -= t.val
#                     visisted.add(stack.pop())
#             if t.right and t.right not in visisted:
#                 stack.append(t.right)
#             if t.left and t.left not in visisted:
#                 stack.append(t.left)
#         return False

# Runtime: 44 ms, faster than 62.17% of Python3 online submissions for Path Sum.
# Memory Usage: 17.3 MB, less than 23.30% of Python3 online submissions for Path Sum.


# Iteratively
# DFS + tuple
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root: return False
        stack = [(root, targetSum)]
        while stack:
            curr, val = stack.pop()
            if curr.left == None and curr.right == None and val == curr.val:
                return True
            if curr.right:
                stack.append((curr.right, val-curr.val))
            if curr.left:
                stack.append((curr.left, val-curr.val))
        return False

# Runtime: 40 ms, faster than 84.37% of Python3 online submissions for Path Sum.
# Memory Usage: 15.8 MB, less than 82.20% of Python3 online submissions for Path Sum.


# Recursively
# Top-down
"""
Can you determine some parameters to help the node know its answer?
Can you use these parameters and the value of the node itself to determine 
what should be the parameters passed to its children? 
If the answers are both yes, 
try to solve this problem using a "top-down" recursive solution.
"""
# class Solution:
#     def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
#         if not root: return False
#         if root.left == None and root.right == None:
#             if (targetSum-root.val) == 0:
#                 return True
#             else:
#                 return False
#         return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)

# Runtime: 44 ms, faster than 62.17% of Python3 online submissions for Path Sum.
# Memory Usage: 16 MB, less than 54.47% of Python3 online submissions for Path Sum.


solution = Solution()
print(solution.hasPathSum(root, targetSum))



