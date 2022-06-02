# Given a string s, return the length of the longest repeating substrings. If 
# no repeating substring exists, return 0. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "abcd"
# Output: 0
# Explanation: There is no repeating substring.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "abbaba"
# Output: 2
# Explanation: The longest repeating substrings are "ab" and "ba", each of 
# which occurs twice.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "aabcaabdaab"
# Output: 3
# Explanation: The longest repeating substring is "aab", which occurs 3 times.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 2000 
#  s consists of lowercase English letters. 
#  
#  Related Topics String Binary Search Dynamic Programming Rolling Hash Suffix 
# Array Hash Function 👍 519 👎 33

from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def search(self, L: int, n: int, S: str) -> str:
        """
        Search a substring of given length
        that occurs at least 2 times.
        @return start position if the substring exits and -1 otherwise.
        """
        seen = set()
        for start in range(0, n - L + 1):
            tmp = S[start:start + L]
            if tmp in seen:
                return start
            seen.add(tmp)
        return -1

    def longestRepeatingSubstring(self, S: str) -> str:
        n = len(S)

        # binary search, L = repeating string length
        left, right = 1, n
        while left <= right:
            L = left + (right - left) // 2
            if self.search(L, n, S) != -1:
                left = L + 1
            else:
                right = L - 1

        return left - 1
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()