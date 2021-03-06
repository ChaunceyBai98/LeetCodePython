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
#  1 <= haystack.length, needle.length <= 10â´ 
#  haystack and needle consist of only lowercase English characters. 
#  
#  Related Topics Two Pointers String String Matching ð 3972 ð 3645

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
#         // æ¹æ³ä¸
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

    # è·ånextæ°ç»
    def getnext(self, a, needle):
        next = ['' for i in range(a)]
        k = -1
        next[0] = k  # åªæä¸ä¸ªå­ç¬¦çæåµä¸è®¤ä¸ºæ¯-1
        # kæååç¼ç»æ­¢ä½ç½®(ä¸¥æ ¼æ¥è¯´æ¯ç»æ­¢ä½ç½®åä¸çä½ç½®)
        for i in range(1, a):  # è®¡ç®å©ä¸çä½ç½®
            # iæååç¼ç»æ­¢ä½ç½®ï¼ä¸kåçï¼ã
            while (k > -1 and needle[k + 1] != needle[i]): # ååç¼ä¸åï¼åååæº¯
                k = next[k] #
            if needle[k + 1] == needle[i]: # ååç¼ç¸å
                k += 1
            next[i] = k # å°jï¼åç¼çé¿åº¦ï¼èµç»next[i]
        return next


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    print(a.strStr('hello', 'llo'))
    a.getnext('hello','llo')
