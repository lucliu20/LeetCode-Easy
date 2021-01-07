# https://leetcode.com/problems/palindrome-linked-list/

"""
Example 1:
Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# head = ListNode(1)
# head.next = ListNode(2)

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(1)

"""
Solution: Reversed first half == Second half?
Phase 1: Reverse the first half while finding the middle.
Phase 2: Compare the reversed first half with the second half.
"""
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        s = f = head
        if not head: return True
        while f and f.next:
            s = s.next
            f = f.next.next
        r = s
        while s.next:
            tmp = s.next
            s.next = tmp.next
            tmp.next = r
            r = tmp
        while r:
            if r.val != head.val:
                return False
            r = r.next
            head = head.next
        return True

solution = Solution()
print(solution.isPalindrome(head))

# Runtime: 60 ms, faster than 96.29% of Python3 online submissions for Palindrome Linked List.
# Memory Usage: 24.5 MB, less than 29.49% of Python3 online submissions for Palindrome Linked List.

