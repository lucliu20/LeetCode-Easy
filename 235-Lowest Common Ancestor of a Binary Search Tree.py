# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

"""
Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# root = TreeNode(6)
# root.left = TreeNode(2)
# root.right = TreeNode(8)
# root.left.left = TreeNode(0)
# root.left.right = TreeNode(4)
# root.right.left = TreeNode(7)
# root.right.right = TreeNode(9)
# root.left.right.left = TreeNode(3)
# root.left.right.right = TreeNode(5)
# p, q = root.left, root.right
# p, q = root.left, root.left.right


# root = TreeNode(2)
# root.left = TreeNode(1)
# p, q = root, root.left

# [2,1,3], 3, 1
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
p, q = root.right, root.left


# Recursively
# DFS
# Top-down
# Note to consider both node p and node q as one factor.
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val and q.val > root.val or p.val > root.val and q.val < root.val:
            return root
        if p.val == root.val or q.val == root.val:
            return root
        if p.val < root.val and q.val < root.val:
            res = self.lowestCommonAncestor(root.left, p, q)
        else:
            res = self.lowestCommonAncestor(root.right, p, q)
        return res

solution = Solution()
print(solution.lowestCommonAncestor(root, p, q))

# Runtime: 80 ms, faster than 53.37% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
# Memory Usage: 18.3 MB, less than 32.00% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.

