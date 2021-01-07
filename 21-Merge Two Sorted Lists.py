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

# l1 = ListNode(1)
# l1.next = ListNode(2)
# l1.next.next = ListNode(4)
# 
# l2 = ListNode(1)
# l2.next = ListNode(3)
# l2.next.next = ListNode(4)

l1 = None
l2 = ListNode(0)

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = tmp = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        tmp.next = l1 or l2
        return dummy.next

solution = Solution()
solution.mergeTwoLists(l1, l2)

# Runtime: 36 ms, faster than 73.59% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 14.2 MB, less than 54.27% of Python3 online submissions for Merge Two Sorted Lists.


