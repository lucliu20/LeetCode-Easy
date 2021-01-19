# https://leetcode.com/problems/implement-stack-using-queues/

"""
Example 1:
Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
"""

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if self.q1:
            while self.q1:
                self.q2.append(self.q1.pop(0))
            self.q1.append(x)
            while self.q2:
                self.q1.append(self.q2.pop(0))
        else:
            self.q1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.q1:
            return self.q1.pop(0)
        else:
            print("Stack is empty!")

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.q1:
            return self.q1[0]
        else:
            print("Queue is empty!")

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return True if not self.q1 else False

myStack = MyStack()
myStack.push(1)
myStack.push(2)
print(myStack.top()) # return 2
print(myStack.pop()) # return 2
print(myStack.empty()) # return False


# Runtime: 32 ms, faster than 54.38% of Python3 online submissions for Implement Stack using Queues.
# Memory Usage: 14.4 MB, less than 12.88% of Python3 online submissions for Implement Stack using Queues.


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()