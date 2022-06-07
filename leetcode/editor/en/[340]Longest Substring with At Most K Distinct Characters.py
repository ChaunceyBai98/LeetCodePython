# Given a string s and an integer k, return the length of the longest substring 
# of s that contains at most k distinct characters. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "eceba", k = 2
# Output: 3
# Explanation: The substring is "ece" with length 3. 
# 
#  Example 2: 
# 
#  
# Input: s = "aa", k = 1
# Output: 2
# Explanation: The substring is "aa" with length 2.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 5 * 10⁴ 
#  0 <= k <= 50 
#  
#  Related Topics Hash Table String Sliding Window 👍 2313 👎 70
from collections import defaultdict
from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        if k == 0 or n == 0:
            return 0
        left, right = 0, 0
        max_len = 1
        hashmap = defaultdict()
        while right < n:
            # 有多个e时，记录的是最右边的，因为删左边的不会减少字母种类
            hashmap[s[right]] = right
            right += 1

            if len(hashmap) == k + 1:
                del_idx = min(hashmap.values())
                del hashmap[s[del_idx]]

                left = del_idx + 1

            max_len = max(max_len,right-left)

        return max_len


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    a.lengthOfLongestSubstringKDistinct(s = "eceba", k = 2)
