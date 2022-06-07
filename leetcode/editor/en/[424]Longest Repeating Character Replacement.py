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
#  1 <= s.length <= 10⁵ 
#  s consists of only uppercase English letters. 
#  0 <= k <= s.length 
#  
#  Related Topics Hash Table String Sliding Window 👍 4614 👎 188

from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    # 我们求的是最长，如果找不到更长的维持长度不变返回结果不受影响
    def characterReplacement(self, s: str, k: int) -> int:
        num = [0] * 26
        n = len(s)
        # left: 左边界，用于滑动时减去头部或者计算长度
        # right: 右边界，用于加上划窗尾巴或者计算长度
        maxn = left = right = 0

        while right < n:
            num[ord(s[right]) - ord("A")] += 1
            # // 求窗口中曾出现某字母的最大次数
            # // 计算某字母出现在某窗口中的最大次数，窗口长度只能增大或者不变（注意后面left指针只移动了0 - 1
            # 次）
            # // 这样做的意义：我们求的是最长，如果找不到更长的维持长度不变返回结果不受影响
            maxn = max(maxn, num[ord(s[right]) - ord("A")])
            # // 长度len = right - left + 1, 以下简称len
            # // len - 字母出现最大次数 > 替换数目 = > len > 字母出现最大次数 + 替换数目
            # // 分析一下，替换数目是不变的 = k, 字母出现最大次数是可能变化的，因此，只有字母出现最大次数增加的情况，len才能拿到最大值
            # // 又不满足条件的情况下，left和right一起移动, len不变的
            if right - left + 1 - maxn > k:
                # // 这里要减的，因为left越过该点，会对最大值有影响
                num[ord(s[left]) - ord("A")] -= 1
                left += 1
            #     //走完这里的时候，其实right会多走一步
            right += 1
        # //因为right多走一步，结果为(right-1)-left+1==right-left
        return right - left

    # leetcode submit region end(Prohibit modification and deletion)
# 大开眼界，滑动窗口的进阶版。 总结了下，滑动窗口有两种： 一种是right每次往右走，只要不满足条件，left就一直收敛。 另一种是，right每次往右走，如果不满足条件，left最多收敛一次（进阶）。


if __name__ == '__main__':
    a = Solution()
