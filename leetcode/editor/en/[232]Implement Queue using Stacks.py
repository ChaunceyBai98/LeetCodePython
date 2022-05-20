# Implement a first in first out (FIFO) queue using only two stacks. The 
# implemented queue should support all the functions of a normal queue (push, peek, pop, 
# and empty). 
# 
#  Implement the MyQueue class: 
# 
#  
#  void push(int x) Pushes element x to the back of the queue. 
#  int pop() Removes the element from the front of the queue and returns it. 
#  int peek() Returns the element at the front of the queue. 
#  boolean empty() Returns true if the queue is empty, false otherwise. 
#  
# 
#  Notes: 
# 
#  
#  You must use only standard operations of a stack, which means only push to 
# top, peek/pop from top, size, and is empty operations are valid. 
#  Depending on your language, the stack may not be supported natively. You may 
# simulate a stack using a list or deque (double-ended queue) as long as you use 
# only a stack's standard operations. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 1, 1, false]
# 
# Explanation
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= x <= 9 
#  At most 100 calls will be made to push, pop, peek, and empty. 
#  All the calls to pop and peek are valid. 
#  
# 
#  
#  Follow-up: Can you implement the queue such that each operation is amortized 
# O(1) time complexity? In other words, performing n operations will take overall 
# O(n) time even if one of those operations may take longer. 
#  Related Topics Stack Design Queue 👍 3417 👎 229

from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    #push :O(n)
    # def push(self, x: int) -> None:
    #     if self.stack1:
    #         while self.stack1:
    #             self.stack2.append(self.stack1.pop())
    #         self.stack2.append(x)
    #         while self.stack2:
    #             self.stack1.append(self.stack2.pop())
    #     else:
    #         self.stack1.append(x)
    #
    # def pop(self) -> int:
    #     return self.stack1.pop()
    #
    # def peek(self) -> int:
    #     return self.stack1[-1]
    #
    # def empty(self) -> bool:
    #     return not self.stack1

    # amortized all O(1)
    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        self.peek()
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        return not (self.stack1 or self.stack2)

    # Your MyQueue object will be instantiated and called as such:


# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = MyQueue()
    a.push(1)
    a.push(2)
    print(a.peek())
    print(a.pop())
    a.push(3)
    print(a.peek())
    a.push(4)
