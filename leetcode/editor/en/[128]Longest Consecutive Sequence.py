# Given an unsorted array of integers nums, return the length of the longest 
# consecutive elements sequence. 
# 
#  You must write an algorithm that runs in O(n) time. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. 
# Therefore its length is 4.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= nums.length <= 10⁵ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  
#  Related Topics Array Hash Table Union Find 👍 9501 👎 422

from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # 这思路 感觉没做过很难想到
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)
        for num in nums:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                longest_streak = max (longest_streak,current_streak)
        return longest_streak

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()