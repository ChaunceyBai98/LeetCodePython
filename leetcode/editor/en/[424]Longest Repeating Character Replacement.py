# You are given a string s and an integer k. You can choose any character of 
# the string and change it to any other uppercase English character. You can perform 
# this operation at most k times. 
# 
#  Return the length of the longest substring containing the same letter you 
# can get after performing the above operations. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10âµ 
#  s consists of only uppercase English letters. 
#  0 <= k <= s.length 
#  
#  Related Topics Hash Table String Sliding Window ð 4614 ð 188

from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    # æä»¬æ±çæ¯æé¿ï¼å¦ææ¾ä¸å°æ´é¿çç»´æé¿åº¦ä¸åè¿åç»æä¸åå½±å
    def characterReplacement(self, s: str, k: int) -> int:
        num = [0] * 26
        n = len(s)
        # left: å·¦è¾¹çï¼ç¨äºæ»å¨æ¶åå»å¤´é¨æèè®¡ç®é¿åº¦
        # right: å³è¾¹çï¼ç¨äºå ä¸åçªå°¾å·´æèè®¡ç®é¿åº¦
        maxn = left = right = 0

        while right < n:
            num[ord(s[right]) - ord("A")] += 1
            # // æ±çªå£ä¸­æ¾åºç°æå­æ¯çæå¤§æ¬¡æ°
            # // è®¡ç®æå­æ¯åºç°å¨æçªå£ä¸­çæå¤§æ¬¡æ°ï¼çªå£é¿åº¦åªè½å¢å¤§æèä¸åï¼æ³¨æåé¢leftæéåªç§»å¨äº0 - 1
            # æ¬¡ï¼
            # // è¿æ ·åçæä¹ï¼æä»¬æ±çæ¯æé¿ï¼å¦ææ¾ä¸å°æ´é¿çç»´æé¿åº¦ä¸åè¿åç»æä¸åå½±å
            maxn = max(maxn, num[ord(s[right]) - ord("A")])
            # // é¿åº¦len = right - left + 1, ä»¥ä¸ç®ç§°len
            # // len - å­æ¯åºç°æå¤§æ¬¡æ° > æ¿æ¢æ°ç® = > len > å­æ¯åºç°æå¤§æ¬¡æ° + æ¿æ¢æ°ç®
            # // åæä¸ä¸ï¼æ¿æ¢æ°ç®æ¯ä¸åç = k, å­æ¯åºç°æå¤§æ¬¡æ°æ¯å¯è½ååçï¼å æ­¤ï¼åªæå­æ¯åºç°æå¤§æ¬¡æ°å¢å çæåµï¼lenæè½æ¿å°æå¤§å¼
            # // åä¸æ»¡è¶³æ¡ä»¶çæåµä¸ï¼leftårightä¸èµ·ç§»å¨, lenä¸åç
            if right - left + 1 - maxn > k:
                # // è¿éè¦åçï¼å ä¸ºleftè¶è¿è¯¥ç¹ï¼ä¼å¯¹æå¤§å¼æå½±å
                num[ord(s[left]) - ord("A")] -= 1
                left += 1
            #     //èµ°å®è¿éçæ¶åï¼å¶å®rightä¼å¤èµ°ä¸æ­¥
            right += 1
        # //å ä¸ºrightå¤èµ°ä¸æ­¥ï¼ç»æä¸º(right-1)-left+1==right-left
        return right - left

    # leetcode submit region end(Prohibit modification and deletion)
# å¤§å¼ç¼çï¼æ»å¨çªå£çè¿é¶çã æ»ç»äºä¸ï¼æ»å¨çªå£æä¸¤ç§ï¼ ä¸ç§æ¯rightæ¯æ¬¡å¾å³èµ°ï¼åªè¦ä¸æ»¡è¶³æ¡ä»¶ï¼leftå°±ä¸ç´æ¶æã å¦ä¸ç§æ¯ï¼rightæ¯æ¬¡å¾å³èµ°ï¼å¦æä¸æ»¡è¶³æ¡ä»¶ï¼leftæå¤æ¶æä¸æ¬¡ï¼è¿é¶ï¼ã


if __name__ == '__main__':
    a = Solution()
