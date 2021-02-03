# https://leetcode.com/problems/symmetric-tree/

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
# 
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#  
# 
# But the following [1,2,2,null,3,null,3] is not:
# 
#     1
#    / \
#   2   2
#    \   \
#    3    3


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Set up the tree
# Expected: True
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)


# Set up the tree
# Expected: False
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(2)
# root.left.right = TreeNode(3)
# root.right.right = TreeNode(3)


# [1,2,2,null,3,3]
# Set up the tree
# Expected: True
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(2)
# root.left.right = TreeNode(3)
# root.right.left = TreeNode(3)

# [1,2,2,2,null,2]
# Set up the tree
# Expected: False
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(2)
# root.left.left = TreeNode(2)
# root.right.left = TreeNode(2)

# [2,3,3,4,5,5,4,null,null,8,9,null,null,9,8]
# Set up the tree
# Expected: False
# root = TreeNode(2)
# root.left = TreeNode(3)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(5)
# root.right.right = TreeNode(4)
# root.left.right.left = TreeNode(8)
# root.left.right.right = TreeNode(9)
# root.right.right.left = TreeNode(9)
# root.right.right.right = TreeNode(8)

# Iteratively
# BFS traversal, then separate the list of this layer into two parts, compare.
# import collections
# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         queue = collections.deque([root])
#         while queue:
#             layer = []
#             qlen = len(queue)
#             for _ in range(qlen):
#                 curr = queue.popleft()
#                 if curr:
#                     layer.append(curr.val)
#                     queue.append(curr.left)
#                     queue.append(curr.right)
#                 else:
#                     layer.append("None")
#             if qlen > 1:
#                 first = layer[0:(len(layer)//2)]
#                 second = layer[len(layer)//2:]
#                 if first != second[::-1]:
#                     return False
#         return True

# Runtime: 40 ms
# Memory Usage: 14.6 MB


# Iteratively
# BFS similar, dequeue two elements at a time, then compare; then enqueue
import collections
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = collections.deque([root])
        queue.append(root)
        while queue:
            n1 = queue.popleft()
            n2 = queue.popleft()
            if n1 == None and n2 == None:
                continue
            if n1 == None or n2 == None:
                return False
            if n1.val != n2.val:
                return False
            queue.append(n1.left)
            queue.append(n2.right)
            queue.append(n1.right)
            queue.append(n2.left)
        return True

# Runtime: 56 ms, faster than 7.59% of Python3 online submissions for Symmetric Tree.
# Memory Usage: 14.2 MB, less than 91.85% of Python3 online submissions for Symmetric Tree.


# Recursively
# DFS
# Bottom up
# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         def helper(n1, n2):
#             if n1 == None and n2 == None: return True
#             if n1 == None or n2 == None: return False
#             return n1.val == n2.val and helper(n1.right, n2.left) and helper(n1.left, n2.right)
#         
#         return helper(root, root)


solution = Solution()
print(solution.isSymmetric(root))

# 

