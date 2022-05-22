# You are given a string s and an integer k, a k duplicate removal consists of 
# choosing k adjacent and equal letters from s and removing them, causing the left 
# and the right side of the deleted substring to concatenate together. 
# 
#  We repeatedly make k duplicate removals on s until we no longer can. 
# 
#  Return the final string after all such duplicate removals have been made. It 
# is guaranteed that the answer is unique. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "abcd", k = 2
# Output: "abcd"
# Explanation: There's nothing to delete. 
# 
#  Example 2: 
# 
#  
# Input: s = "deeedbbcccbdaa", k = 3
# Output: "aa"
# Explanation: 
# First delete "eee" and "ccc", get "ddbbbdaa"
# Then delete "bbb", get "dddaa"
# Finally delete "ddd", get "aa" 
# 
#  Example 3: 
# 
#  
# Input: s = "pbbcggttciiippooaais", k = 2
# Output: "ps"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁵ 
#  2 <= k <= 10⁴ 
#  s only contains lower case English letters. 
#  
#  Related Topics String Stack 👍 3909 👎 74

from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # 我自己的，超时了，原因是要回退来判断是否超时
    # def removeDuplicates(self, s: str, k: int) -> str:
    #     stack = []
    #     for c in s:
    #         if len(stack) >= k - 1:
    #             ifk = True
    #             for i in range(k - 1):
    #                 if stack[-1 - i] != c:
    #                     ifk = False
    #                     break
    #             if ifk:
    #                 for _ in range(k - 1):
    #                     stack.pop()
    #             else:
    #                 stack.append(c)
    #         else:
    #             stack.append(c)
    #     ans = ''
    #     for c in stack:
    #         ans += c
    #     return ans
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])
            if stack[-1][1] == k:
                stack.pop()
        ans = ''
        for char, num in stack:
            ans += char * num
        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    print(a.removeDuplicates(s="deeedbbcccbdaa", k=3))
    print(a.removeDuplicates(s="pbbcggttciiippooaais", k=2))
