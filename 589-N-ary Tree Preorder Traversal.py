# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

"""
Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]

Example 2:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
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


# Recursively
# DFS
# Pre-order
# class Solution:
#     def preorder(self, root: 'Node') -> list():
#         if not root:
#             return None
#         res = [root.val]
#         for i in range(len(root.children)):
#             res.extend(self.preorder(root.children[i])) # res.append() would return the result like [1, [3, [5], [6]], [2], [4]].
#         return res

# Runtime: 52 ms, faster than 64.76% of Python3 online submissions for N-ary Tree Preorder Traversal.
# Memory Usage: 16 MB, less than 90.43% of Python3 online submissions for N-ary Tree Preorder Traversal.


# Iteratively
# Pre-order
# Push the children of the curr into the stack in reverse order
class Solution:
    def preorder(self, root: 'Node') -> list():
        if not root: return []
        res = []
        curr = []
        stack = [root]
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            # Push the children of the curr into the stack in reverse order.
            # children of 1 = [3,2,4], if not reveresed then 4 will be popped out first from the stack.
            # if reversed then stack = [4,2,3]. Here 3 will pop out first.
            # This continues till the stack is empty.
            stack.extend(curr.children[::-1])
        return res

# Runtime: 44 ms, faster than 94.73% of Python3 online submissions for N-ary Tree Preorder Traversal.
# Memory Usage: 16.2 MB, less than 23.40% of Python3 online submissions for N-ary Tree Preorder Traversal.

solution = Solution()
print(solution.preorder(root))


