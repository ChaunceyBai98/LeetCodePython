# Given a string s and an integer k, return the length of the longest substring 
# of s such that the frequency of each character in this substring is greater 
# than or equal to k. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "aaabb", k = 3
# Output: 3
# Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "ababbc", k = 2
# Output: 5
# Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 
# 'b' is repeated 3 times.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s consists of only lowercase English letters. 
#  1 <= k <= 10⁵ 
#  
#  Related Topics Hash Table String Divide and Conquer Sliding Window 👍 4000 👎
#  329

from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # 这代码太牛逼了
    # def longestSubstring(self, s: str, k: int) -> int:
    #     maxLength = 0
    #     if len(s) < k:
    #         return 0
    #     setOfs = set(s)
    #     for aChar in setOfs:
    #         # 如果所有字符都大于k，那就直接返回len(s)
    #         if s.count(aChar) < k:
    #             seperations = s.split(aChar)
    #             for seperation in seperations:
    #                 if seperation:
    #                     length = self.longestSubstring(seperation,k)
    #                     if length > maxLength:
    #                         maxLength = length
    #             return maxLength
    #     return len(s)
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        maxLength = 0
        setOfs = set(s)
        for aChar in setOfs:
            if s.count(aChar) < k:
                seperations = s.split(aChar)
                for sep in seperations:
                    length = self.longestSubstring(sep, k)
                    if length > maxLength:
                        maxLength = length
                return maxLength
        return len(s)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    # print(a.longestSubstring(s="abacbbc", k=3))
    print(a.longestSubstring(s="aaaabbbbqqddweeriiiiirrroooweedd", k=3))
