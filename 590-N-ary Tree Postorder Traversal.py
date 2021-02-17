# https://leetcode.com/problems/n-ary-tree-postorder-traversal/
# My post:
# https://leetcode.com/problems/n-ary-tree-postorder-traversal/discuss/1069166/Python-3-Iterative-Stack-WO-Reversing-Visited

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


# Recursively
# DFS
# class Solution:
#     def postorder(self, root: 'Node') -> list():
#         if not root:
#             return None
#         res = []
#         for i in range(len(root.children)):
#             res.extend(self.postorder(root.children[i]))
#         res.append(root.val)
#         return res

# Runtime: 48 ms, faster than 84.04% of Python3 online submissions for N-ary Tree Postorder Traversal.
# Memory Usage: 16 MB, less than 91.57% of Python3 online submissions for N-ary Tree Postorder Traversal.


# Iteratively
# DFS
class Solution:
    def postorder(self, root: 'Node') -> list():
        if not root:
            return []
        res = []
        curr = []
        stack = [root]
        visited = set()
        while stack:
            curr = stack[-1]
            while curr.children:
                if curr.children[0] not in visited:
                    stack.extend(curr.children[::-1])
                else:
                    break
                curr = stack[-1]
            if curr not in visited:
                res.append(stack.pop().val)
                visited.add(curr)
        return res

# Runtime: 52 ms, faster than 64.31% of Python3 online submissions for N-ary Tree Postorder Traversal.
# Memory Usage: 16.1 MB, less than 28.41% of Python3 online submissions for N-ary Tree Postorder Traversal.

solution = Solution()
print(solution.postorder(root))

