"""
https://leetcode.com/problems/linked-list-cycle/

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# head = ListNode(3)
# head.next = ListNode(2)
# head.next.next = ListNode(0)
# head.next.next.next = ListNode(-4)
# head.next.next.next.next = head.next

# head = None

# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = head

head = ListNode(1)

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None: return False
        slow = head
        fast = head.next
        while (slow != fast):
            if fast == None or fast.next == None: # Here we use "==", not "!=", then no error.
                return False
            slow = slow.next
            fast = fast.next.next
        return True

        # if not head: return False
        # slow, fast = head, head.next
        """
        The system reports below error when "head = ListNode(1)"
        while fast != None or fast.next != None:
        ttributeError: 'NoneType' object has no attribute 'next'
        """
        # while fast != None or fast.next != None:
        #     if slow == fast:
        #         return True
        #     slow = slow.next
        #     if fast.next.next:
        #         fast = fast.next.next
        # return False

obj = Solution()
print(obj.hasCycle(head))

# 