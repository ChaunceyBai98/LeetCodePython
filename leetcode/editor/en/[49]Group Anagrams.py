# Given an array of strings strs, group the anagrams together. You can return 
# the answer in any order. 
# 
#  An Anagram is a word or phrase formed by rearranging the letters of a 
# different word or phrase, typically using all the original letters exactly once. 
# 
#  
#  Example 1: 
#  Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#  Example 2: 
#  Input: strs = [""]
# Output: [[""]]
#  Example 3: 
#  Input: strs = ["a"]
# Output: [["a"]]
#  
#  
#  Constraints: 
# 
#  
#  1 <= strs.length <= 10⁴ 
#  0 <= strs[i].length <= 100 
#  strs[i] consists of lowercase English letters. 
#  
#  Related Topics Hash Table String Sorting 👍 9393 👎 318
import collections
from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = collections.defaultdict(list)
        for str in strs:
            counts = [0] * 26
            for ch in str:
                counts[ord(ch) - ord('a')] += 1
            # 需要将 list 转换成 tuple 才能进行哈希
            map[tuple(counts)].append(str)
        return list(map.values())


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
