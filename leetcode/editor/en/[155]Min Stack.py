# Design a stack that supports push, pop, top, and retrieving the minimum 
# element in constant time. 
# 
#  Implement the MinStack class: 
# 
#  
#  MinStack() initializes the stack object. 
#  void push(int val) pushes the element val onto the stack. 
#  void pop() removes the element on the top of the stack. 
#  int top() gets the top element of the stack. 
#  int getMin() retrieves the minimum element in the stack. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# 
# Output
# [null,null,null,null,-3,null,0,-2]
# 
# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
#  
# 
#  
#  Constraints: 
# 
#  
#  -2³¹ <= val <= 2³¹ - 1 
#  Methods pop, top and getMin operations will always be called on non-empty 
# stacks. 
#  At most 3 * 10⁴ calls will be made to push, pop, top, and getMin. 
#  
#  Related Topics Stack Design 👍 8086 👎 623

from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
class MinStack:

    def __init__(self):
        self.List = []

    def push(self, val: int) -> None:
        if self.List:
            minVal = min(val, self.List[len(self.List) - 1][1])
        else:
            minVal = val
        self.List.append((val, minVal))

    def pop(self) -> None:
        self.List.pop()

    def top(self) -> int:
        return self.List[len(self.List) - 1][0]

    def getMin(self) -> int:
        return self.List[len(self.List) - 1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = MinStack()
    a.push(3)
    a.push(4)
    print(a.top())
    print(a.getMin())
