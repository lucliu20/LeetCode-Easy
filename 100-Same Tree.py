# https://leetcode.com/problems/same-tree/

"""
Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

p = TreeNode(0)
p.left = TreeNode(-5)
# p.right = TreeNode(3)

q = TreeNode(0)
q.left = TreeNode(-5)
# q.right = TreeNode(3)


# Recursively
# class Solution:
#     def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
#         if not p and not q:
#             return True
#         if not p or not q:
#             return False
#         if p.val != q.val:
#             return False
#         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Runtime: 28 ms, faster than 84.67% of Python3 online submissions for Same Tree.
# Memory Usage: 14.3 MB, less than 35.42% of Python3 online submissions for Same Tree.


# Iteratively
import collections
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        queue = collections.deque([(p,q)])

        def isEqual(s, t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            if s.val != t.val:
                return False
            return True
        
        while queue:
            s, t = queue.popleft()
            if not isEqual(s, t):
                return False
            if s:
                queue.append((s.left, t.left))
                queue.append((s.right, t.right))
        return True


# Runtime: 24 ms, faster than 95.56% of Python3 online submissions for Same Tree.
# Memory Usage: 14.2 MB, less than 66.05% of Python3 online submissions for Same Tree.


solution = Solution()
print(solution.isSameTree(p, q))

