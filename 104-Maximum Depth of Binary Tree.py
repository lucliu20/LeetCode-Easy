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

# Approach when I was doing the Recursive Explore Card
# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if root is None:
#             return 0
#         return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # My initial way:
        # def depth(node, dep):
        #     if not node:
        #         return dep
        #     hl = depth(node.left, dep + 1)
        #     hr = depth(node.right, dep + 1)
        #     return max(hl, hr)
        # return depth(root, 0)

# Runtime: 40 ms, faster than 73.16% of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 16.5 MB, less than 10.17% of Python3 online submissions for Maximum Depth of Binary Tree.


# Approaches when I was doing the Binary Tree Explore Card on 02/02/2021
# Bottom up
# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if not root: return 0
#         left = self.maxDepth(root.left)
#         right = self.maxDepth(root.right)
#         return max(left, right) + 1

# Runtime: 56 ms, faster than 10.82% of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 16.1 MB, less than 38.83% of Python3 online submissions for Maximum Depth of Binary Tree.


# Top down
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.res = 0
        def helper(node, depth):
            if not node: return
            if node.left is None and node.right is None:
                self.res = max(self.res, depth)
            helper(node.left, depth+1)
            helper(node.right, depth+1)
        
        helper(root, 0)
        return self.res+1

# Runtime: 36 ms
# Memory Usage: 16.5 MB

solution = Solution()
print(solution.maxDepth(root))


