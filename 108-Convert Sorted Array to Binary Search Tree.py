# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/


# Example:
# Given the sorted array: [-10,-3,0,5,9],
# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
# 
#       0
#      / \
#    -3   9
#    /   /
#  -10  5

nums = [-10,-3,0,5,9]

"""
For a sorted array, the left half will be in the left subtree, middle value as the root, right half in the right subtree. This holds true for every node:

[1, 2, 3, 4, 5, 6, 7] -> left: [1, 2, 3], root: 4, right: [5, 6, 7]
[1, 2, 3] -> left: [1], root: 2, right: [3]
[5, 6, 7] -> left: [5], root: 6, right: [7]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# array slicing is expensive, use the array indices instead.
class Solution:
    def sortedArrayToBST(self, nums: list()) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None
            mid = left + (right-left)//2
            node  = TreeNode(nums[mid])
            node.left = helper(left, mid-1)
            node.right = helper(mid+1, right)
            return node

        return helper(0, len(nums)-1)

solution = Solution()
print(solution.sortedArrayToBST(nums))

# Runtime: 60 ms, faster than 99.48% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
# Memory Usage: 16.3 MB, less than 90.81% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.

