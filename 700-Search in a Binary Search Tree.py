# https://leetcode.com/problems/search-in-a-binary-search-tree/


# Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.
# 
# For example, 
# 
# Given the tree:
#         4
#        / \
#       2   7
#      / \
#     1   3
# 
# And the value to search: 2
# You should return this subtree:
# 
#       2     
#      / \   
#     1   3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

val = 5

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return root
        if root.val == val:
            return root
        if root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)


solution = Solution()
solution.searchBST(root, val)

# Runtime: 80 ms
# Memory Usage: 16.1 MB

