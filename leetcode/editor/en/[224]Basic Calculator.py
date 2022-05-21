# Given a string s representing a valid expression, implement a basic 
# calculator to evaluate it, and return the result of the evaluation. 
# 
#  Note: You are not allowed to use any built-in function which evaluates 
# strings as mathematical expressions, such as eval(). 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "1 + 1"
# Output: 2
#  
# 
#  Example 2: 
# 
#  
# Input: s = " 2-1 + 2 "
# Output: 3
#  
# 
#  Example 3: 
# 
#  
# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 3 * 10⁵ 
#  s consists of digits, '+', '-', '(', ')', and ' '. 
#  s represents a valid expression. 
#  '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid). 
# 
#  '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid). 
# 
#  There will be no two consecutive operators in the input. 
#  Every number and running calculation will fit in a signed 32-bit integer. 
#  
#  Related Topics Math String Stack Recursion 👍 3611 👎 296

from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # 思路是修改括号里的正负号
    def calculate(self, s: str) -> int:
        st= []
        ans, num, op = 0, 0, 1
        st.append(op)
        for c in s:
            if c == ' ':
                continue
            elif (c >= '0'):
                num = num * 10 + int(c)
            else:
                ans += op * num
                num = 0
                if c == '+':
                    op = st[-1]
                elif c == '-':
                    op = - st[-1]
                elif c == '(':
                    st.append(op)
                else:
                    st.pop()
        return ans + op * num


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    a.calculate("3-(6+8)")