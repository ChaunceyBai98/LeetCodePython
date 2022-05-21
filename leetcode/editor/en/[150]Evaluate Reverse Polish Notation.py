# Evaluate the value of an arithmetic expression in Reverse Polish Notation. 
# 
#  Valid operators are +, -, *, and /. Each operand may be an integer or 
# another expression. 
# 
#  Note that division between two integers should truncate toward zero. 
# 
#  It is guaranteed that the given RPN expression is always valid. That means 
# the expression would always evaluate to a result, and there will not be any 
# division by zero operation. 
# 
#  
#  Example 1: 
# 
#  
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
#  
# 
#  Example 2: 
# 
#  
# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
#  
# 
#  Example 3: 
# 
#  
# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= tokens.length <= 10⁴ 
#  tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the 
# range [-200, 200]. 
#  
#  Related Topics Array Math Stack 👍 3076 👎 633

from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for token in tokens:
            if token == '+':
                nums.append(nums.pop() + nums.pop())
            elif token == '-':
                num1 = nums.pop()
                num2 = nums.pop()
                nums.append(num2 - num1)
            elif token == '*':
                nums.append(nums.pop() * nums.pop())
            elif token == '/':
                num1 = nums.pop()
                num2 = nums.pop()
                nums.append(int(num2 / num1))
            else:
                nums.append(int(token))
        return nums[0]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    print(a.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
