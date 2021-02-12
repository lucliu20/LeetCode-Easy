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

# Recursively
# DFS
# Top-down
# class Solution:
#     def searchBST(self, root: TreeNode, val: int) -> TreeNode:
#         if not root:
#             return root
#         if root.val == val:
#             return root
#         if root.val > val:
#             return self.searchBST(root.left, val)
#         else:
#             return self.searchBST(root.right, val)

# Runtime: 80 ms
# Memory Usage: 16.1 MB


# Iteratively
# DFS
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root: return None
        curr = root
        stack = []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if curr.val == val:
                return curr
            curr = curr.right
        return None

# Runtime: 68 ms, faster than 91.12% of Python3 online submissions for Search in a Binary Search Tree.
# Memory Usage: 16 MB, less than 98.07% of Python3 online submissions for Search in a Binary Search Tree.


solution = Solution()
print(solution.searchBST(root, val))



