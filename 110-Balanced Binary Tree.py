# https://leetcode.com/problems/balanced-binary-tree/

"""
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(4)
root.left.left.right.left = TreeNode(5)
root.left.left.right.right = TreeNode(5)
root.left.left.right.left.right = TreeNode(6)

# root = None

# [1,2,2,3,null,null,3,4,null,null,4]
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(2)
# root.left.left = TreeNode(3)
# root.right.right = TreeNode(3)
# root.left.left.left = TreeNode(4)
# root.right.right.right = TreeNode(4)


# Recursively
# DFS
# Bottom-up
# class Solution:
#     def isBalanced(self, root: TreeNode) -> bool:
#         def helper(node):
#             if not node:
#                 return [0, True]
#             h_left, left_b = helper(node.left)
#             h_right, right_b = helper(node.right)
#             if abs(h_left - h_right) > 1 or left_b is False or right_b is False:
#                 return [max(h_left+1, h_right+1), False]
#             return [max(h_left+1, h_right+1), True]
#         height, isB = helper(root)
#         return isB

# Runtime: 56 ms, faster than 41.83% of Python3 online submissions for Balanced Binary Tree.
# Memory Usage: 19.4 MB, less than 16.45% of Python3 online submissions for Balanced Binary Tree.


# Iteratively
# DFS
# Bottom-up
# Post-order
# Dictionary
import collections
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = []
        curr, last = root, None
        depths = collections.defaultdict(int)
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack[-1]
                if not curr.right or last == curr.right:
                    curr = stack.pop()
                    left, right  = depths.get(curr.left, 0), depths.get(curr.right, 0)
                    if abs(left - right) > 1: return False
                    depths[curr] = 1 + max(left, right)
                    last = curr
                    curr = None
                else:
                    curr = curr.right
        return True

# Runtime: 48 ms, faster than 79.82% of Python3 online submissions for Balanced Binary Tree.
# Memory Usage: 15 MB, less than 98.69% of Python3 online submissions for Balanced Binary Tree.


solution = Solution()
print(solution.isBalanced(root))


