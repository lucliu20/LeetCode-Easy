# https://leetcode.com/problems/implement-queue-using-stacks/

"""
Example 1:
Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
"""


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if self.s1:
            while self.s1:
                self.s2.append(self.s1.pop())
            self.s1.append(x)
            while self.s2:
                self.s1.append(self.s2.pop())
        else:
            self.s1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.s1:
            return self.s1.pop()
        else:
            print("Queue is empty!")

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.s1:
            return self.s1[-1]
        else:
            print("Queue is empty!")

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return True if not self.s1 else False

myQueue = MyQueue()
myQueue.push(1) # queue is: [1]
myQueue.push(2) # queue is: [1, 2] (leftmost is front of the queue)
print(myQueue.peek()) # return 1
print(myQueue.pop()) # return 1, queue is [2]
print(myQueue.empty()) # return false


# Runtime: 32 ms, faster than 52.71% of Python3 online submissions for Implement Queue using Stacks.
# Memory Usage: 14.2 MB, less than 91.10% of Python3 online submissions for Implement Queue using Stacks.

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()