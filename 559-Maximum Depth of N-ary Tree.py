# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]

Example 2:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
"""

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = []

# Set up the tree based on the example #1
root = Node(1)
root.children.append(Node(3))
root.children.append(Node(2))
root.children.append(Node(4))
root.children[0].children.append(Node(5))
root.children[0].children.append(Node(6))

# Set up the tree based on the example #2
# root = Node(1)
# root.children.append(Node(2))
# root.children.append(Node(3))
# root.children.append(Node(4))
# root.children.append(Node(5))
# root.children[1].children.append(Node(6))
# root.children[1].children.append(Node(7))
# root.children[2].children.append(Node(8))
# root.children[3].children.append(Node(9))
# root.children[3].children.append(Node(10))
# root.children[1].children[1].children.append(Node(11))
# root.children[2].children[1].children.append(Node(12))
# root.children[3].children[1].children.append(Node(13))
# root.children[1].children[1].children[0].children.append(Node(14))

# root = None


# Recursively
# DFS
# Top-down
# class Solution:
#     def maxDepth(self, root: 'Node') -> int:
#         def helper(node, depth):
#             if not node: return 0
#             res = depth
#             for i in range(len(node.children)):
#                 res = max(helper(node.children[i], depth+1), res)
#             return res
#         
#         return helper(root, 1)

# Runtime: 36 ms, faster than 98.25% of Python3 online submissions for Maximum Depth of N-ary Tree.
# Memory Usage: 16 MB, less than 50.62% of Python3 online submissions for Maximum Depth of N-ary Tree.


# Iteratively
# DFS
# Top-down
# class Solution:
#     def maxDepth(self, root: 'Node') -> int:
#         if not root: return 0
#         heigth = -float("inf")
#         stack = [(root,1)]
#         while stack:
#             curr, chight = stack.pop()
#             heigth = max(heigth, chight)
#             # Using extend doesn't work.
#             # stack.extend((root.children[::-1], chight+1))
#             # Note here we don't need to reverse the children (problem 589. N-ary Tree Preorder Traversal needs to)
#             # But it's still good if we reverse "for child in curr.children[::-1]:".
#             for child in curr.children:
#                 stack.append((child, chight+1))
#         return heigth

# Runtime: 40 ms, faster than 92.92% of Python3 online submissions for Maximum Depth of N-ary Tree.
# Memory Usage: 16 MB, less than 81.43% of Python3 online submissions for Maximum Depth of N-ary Tree.


# Iteratively
# BFS
# Top-down
# Layer-by-layer
import collections
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        heigth = 0
        queue = collections.deque([root])
        while queue:
            tmp = []
            length = len(queue)
            for _ in range(length):
                tmp = queue.popleft()
                queue.extend(tmp.children)
            heigth += 1
        return heigth

# Runtime: 36 ms, faster than 98.25% of Python3 online submissions for Maximum Depth of N-ary Tree.
# Memory Usage: 15.9 MB, less than 95.90% of Python3 online submissions for Maximum Depth of N-ary Tree.


solution = Solution()
print(solution.maxDepth(root))

