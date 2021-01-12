# https://leetcode.com/problems/merge-two-sorted-lists/

"""
Example 1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: l1 = [], l2 = []
Output: []

Example 3:
Input: l1 = [], l2 = [0]
Output: [0]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l1 = ListNode(1)
l1.next = ListNode(3)
l1.next.next = ListNode(5)

l2 = ListNode(2)
l2.next = ListNode(4)
l2.next.next = ListNode(6)

# l1 = None
# l2 = ListNode(0)

# Iterate:
# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         dummy = tmp = ListNode(0)
#         while l1 and l2:
#             if l1.val < l2.val:
#                 tmp.next = l1
#                 l1 = l1.next
#             else:
#                 tmp.next = l2
#                 l2 = l2.next
#             tmp = tmp.next
#         tmp.next = l1 or l2
#         return dummy.next

# Runtime: 36 ms, faster than 73.59% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 14.2 MB, less than 54.27% of Python3 online submissions for Merge Two Sorted Lists.

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l2 or l1
        # if not l2:
        #     return l1
        if l2.val > l1.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        
solution = Solution()
solution.mergeTwoLists(l1, l2)

# Runtime: 40 ms, faster than 44.86% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 14.4 MB, less than 29.21% of Python3 online submissions for Merge Two Sorted Lists.



