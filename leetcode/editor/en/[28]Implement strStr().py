# Implement strStr(). 
# 
#  Given two strings needle and haystack, return the index of the first 
# occurrence of needle in haystack, or -1 if needle is not part of haystack. 
# 
#  Clarification: 
# 
#  What should we return when needle is an empty string? This is a great 
# question to ask during an interview. 
# 
#  For the purpose of this problem, we will return 0 when needle is an empty 
# string. This is consistent to C's strstr() and Java's indexOf(). 
# 
#  
#  Example 1: 
# 
#  
# Input: haystack = "hello", needle = "ll"
# Output: 2
#  
# 
#  Example 2: 
# 
#  
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= haystack.length, needle.length <= 10⁴ 
#  haystack and needle consist of only lowercase English characters. 
#  
#  Related Topics Two Pointers String String Matching 👍 3972 👎 3645

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
#         // 方法一
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a = len(needle)
        b = len(haystack)
        if a == 0:
            return 0
        next = self.getnext(a, needle)
        p = -1
        for j in range(b):
            while p >= 0 and needle[p + 1] != haystack[j]:
                p = next[p]
            if needle[p + 1] == haystack[j]:
                p += 1
            if p == a - 1:
                return j - a + 1
        return -1

    # 获取next数组
    def getnext(self, a, needle):
        next = ['' for i in range(a)]
        k = -1
        next[0] = k  # 只有一个字符的情况下认为是-1
        # k指向前缀终止位置(严格来说是终止位置减一的位置)
        for i in range(1, a):  # 计算剩下的位置
            # i指向后缀终止位置（与k同理）。
            while (k > -1 and needle[k + 1] != needle[i]): # 前后缀不同，向前回溯
                k = next[k] #
            if needle[k + 1] == needle[i]: # 前后缀相同
                k += 1
            next[i] = k # 将j（前缀的长度）赋给next[i]
        return next


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    print(a.strStr('hello', 'llo'))
    a.getnext('hello','llo')
