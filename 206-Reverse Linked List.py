# https://leetcode.com/problems/reverse-linked-list/

"""
Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        r = node = head
        if not head: return None
        while node.next:
            tmp = node.next
            node.next = tmp.next
            tmp.next = r
            r = tmp
        return r

solution = Solution()
solution.reverseList(head)

# Runtime: 28 ms
# Memory Usage: 15.7 MB
