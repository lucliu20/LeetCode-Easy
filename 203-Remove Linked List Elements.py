# https://leetcode.com/problems/remove-linked-list-elements/

"""
Example:
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = ListNode(6)
h2 = ListNode(2)
h3 = ListNode(6)
h4 = ListNode(3)
h5 = ListNode(4)
h6 = ListNode(5)
h7 = ListNode(6)
head.next = h2
h2.next = h3
h3.next = h4
h4.next = h5
h5.next = h6
h6.next = h7

val = 6

# head = ListNode(1)
# h2 = ListNode(1)
# head.next = h2
# 
# val = 1

# head = ListNode(1)
# h2 = ListNode(2)
# h3 = ListNode(2)
# h4 = ListNode(1)
# head.next = h2
# h2.next = h3
# h3.next = h4
# 
# val = 2

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        r = node = head
        if not head: return None
        while node:
            if node.val == val:
                if r == node: # if the 1st node needs to be removed.
                    head = node.next
                    r = node.next
                    node = node.next
                else:
                    r.next = node.next
                    node = node.next
            else:
                r = node
                node = node.next
        return head

solution = Solution()
solution.removeElements(head, val)

# Runtime: 68 ms, faster than 70.16% of Python3 online submissions for Remove Linked List Elements.
# Memory Usage: 17 MB, less than 76.38% of Python3 online submissions for Remove Linked List Elements.

