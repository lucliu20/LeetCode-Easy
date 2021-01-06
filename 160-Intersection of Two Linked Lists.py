# https://leetcode.com/problems/intersection-of-two-linked-lists/
# My post:
# https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/1004084/Python-3-Intuitive-Explained-O(n)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

headA = ListNode(4)
hA2 = ListNode(1)
hA3 = ListNode(8)
hA4 = ListNode(4)
hA5 = ListNode(5)
headA.next = hA2
hA2.next = hA3
hA3.next = hA4
hA4.next = hA5

headB = ListNode(5)
headB.next = ListNode(6)
hB2 = ListNode(1)
# hB4 = ListNode(8)
# hB5 = ListNode(4)
# hB6 = ListNode(5)
headB.next.next = hB2
# hB2.next = hB3
hB2.next = hA3

# headA = ListNode(2)
# hA2 = ListNode(6)
# hA3 = ListNode(4)
# headA.next = hA2
# hA2.next = hA3

# headB = ListNode(1)
# hB2 = ListNode(5)
# headB.next = hB2

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ca, cb = 0, 0
        nodeA, nodeB = headA, headB
        while nodeA:
            nodeA = nodeA.next
            ca += 1
        while nodeB:
            nodeB = nodeB.next
            cb += 1
        nodeA, nodeB = headA, headB
        if ca > cb:
            i = ca - cb
            while i > 0:
                nodeA = nodeA.next
        else:
            i = cb - ca
            while i > 0:
                nodeB = nodeB.next
                i -= 1
        while nodeA:
            if nodeA == nodeB:
                return nodeA
            nodeA = nodeA.next
            nodeB = nodeB.next
        return None

solution = Solution()
print(solution.getIntersectionNode(headA, headB))

# Runtime: 152 ms, faster than 94.06% of Python3 online submissions for Intersection of Two Linked Lists.
# Memory Usage: 29.2 MB, less than 92.56% of Python3 online submissions for Intersection of Two Linked Lists.
