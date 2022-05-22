# Given a string s of '(' , ')' and lowercase English characters. 
# 
#  Your task is to remove the minimum number of parentheses ( '(' or ')', in 
# any positions ) so that the resulting parentheses string is valid and return any 
# valid string. 
# 
#  Formally, a parentheses string is valid if and only if: 
# 
#  
#  It is the empty string, contains only lowercase characters, or 
#  It can be written as AB (A concatenated with B), where A and B are valid 
# strings, or 
#  It can be written as (A), where A is a valid string. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "a)b(c)d"
# Output: "ab(c)d"
#  
# 
#  Example 3: 
# 
#  
# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s[i] is either'(' , ')', or lowercase English letter. 
#
#  Related Topics String Stack 👍 4801 👎 82

from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        global j
        stack = []
        i = 0
        for c in s:
            if c == '(':
                stack.append([c, i])
            elif c == ')':
                if stack and stack[-1][0] == '(':
                    stack.pop()
                else:
                    stack.append([c, i])
            i += 1
            j = 0
        for char, index in stack:
            s = s[:index - j] + s[index + 1 - j:]
            j += 1
        return s
        # leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    print(a.minRemoveToMakeValid(s="a))b(c)d"))
