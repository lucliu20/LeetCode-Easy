# https://leetcode.com/problems/maximum-depth-of-binary-tree/

"""
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Example 3:
Input: root = []
Output: 0

Example 4:
Input: root = [0]
Output: 1
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# root = TreeNode(1)
# root.right = TreeNode(2)

# root = None

# root = TreeNode(0)

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # My initial way:
        # def depth(node, dep):
        #     if not node:
        #         return dep
        #     hl = depth(node.left, dep + 1)
        #     hr = depth(node.right, dep + 1)
        #     return max(hl, hr)
        # return depth(root, 0)

solution = Solution()
print(solution.maxDepth(root))

# Runtime: 40 ms, faster than 73.16% of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 16.5 MB, less than 10.17% of Python3 online submissions for Maximum Depth of Binary Tree.

