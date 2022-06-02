# Given a string s which consists of lowercase or uppercase letters, return the 
# length of the longest palindrome that can be built with those letters. 
# 
#  Letters are case sensitive, for example, "Aa" is not considered a palindrome 
# here. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "abccccdd"
# Output: 7
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "a"
# Output: 1
#  
# 
#  Example 3: 
# 
#  
# Input: s = "bb"
# Output: 2
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 2000 
#  s consists of lowercase and/or uppercase English letters only. 
#  
#  Related Topics Hash Table String Greedy 👍 2752 👎 161
import collections
from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = collections.Counter(s)
        ans = 0
        for alp, num in count.items():
            if num % 2 == 0:
                ans += num
            else:
                ans += num - 1
        if len(s) == ans:
            return ans
        else:
            return ans + 1


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    print(a.longestPalindrome(s="abccccdd"))
