# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']
# ', determine if the input string is valid. 
# 
#  An input string is valid if: 
# 
#  
#  Open brackets must be closed by the same type of brackets. 
#  Open brackets must be closed in the correct order. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: s = "()"
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: s = "()[]{}"
# Output: true
#  
# 
#  Example 3: 
# 
#  
# Input: s = "(]"
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s consists of parentheses only '()[]{}'. 
#  
#  Related Topics String Stack 👍 13091 👎 587

from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # 我自己写的
    # def isValid(self, s: str) -> bool:
    #     myStack = []
    #     for c in s:
    #         if myStack:
    #             if c == '[' or c == '(' or c == '{':
    #                 myStack.append(c)
    #             elif c == ']':
    #                 if myStack[-1] == '[':
    #                     myStack.pop()
    #                 else:
    #                     return False
    #             elif c == '}':
    #                 if myStack[-1] == '{':
    #                     myStack.pop()
    #                 else:
    #                     return False
    #             else:
    #                 if myStack[-1] == '(':
    #                     myStack.pop()
    #                 else:
    #                     return False
    #         else:
    #             myStack.append(c)
    #     return not myStack

    # 字典的使用方法：https://www.runoob.com/python/python-dictionary.html
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        pairs = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        myStack = []
        for c in s:
            if c in pairs:
                if not myStack or myStack[-1] != pairs[c]:
                    return False
                myStack.pop()
            else:
                myStack.append(c)
        return not myStack


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    print(a.isValid("()"))
    print(a.isValid("()[]{}"))
    print(a.isValid("(]"))
    print(a.isValid("(])"))
