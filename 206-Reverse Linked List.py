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

"""
# Iterative way
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

# Runtime: 28 ms
# Memory Usage: 15.7 MB
"""

# Recursive way
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node):
            if not node or not node.next:
                return node
            tmp = reverse(node.next)
            node.next.next = node
            node.next = None
            return tmp
        
        return reverse(head)

solution = Solution()
solution.reverseList(head)

# Runtime: 40 ms, faster than 30.22% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 20.3 MB, less than 5.82% of Python3 online submissions for Reverse Linked List.
