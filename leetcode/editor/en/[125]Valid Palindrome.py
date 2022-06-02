# A phrase is a palindrome if, after converting all uppercase letters into 
# lowercase letters and removing all non-alphanumeric characters, it reads the same 
# forward and backward. Alphanumeric characters include letters and numbers. 
# 
#  Given a string s, return true if it is a palindrome, or false otherwise. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#  
# 
#  Example 3: 
# 
#  
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric 
# characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
# 
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 2 * 10⁵ 
#  s consists only of printable ASCII characters. 
#  
#  Related Topics Two Pointers String 👍 3791 👎 5288

from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        start, e = 0, len(s) - 1
        while start < e:
            if s[start] == s[e]:
                start += 1
                e -= 1
            elif not s[start].isalnum():
                start += 1
            elif not s[e].isalnum():
                e -= 1
            else:
                return False
        return True

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    print(a.isPalindrome("aba"))