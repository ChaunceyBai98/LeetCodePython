# A peak element is an element that is strictly greater than its neighbors. 
# 
#  Given an integer array nums, find a peak element, and return its index. If 
# the array contains multiple peaks, return the index to any of the peaks. 
# 
#  You may imagine that nums[-1] = nums[n] = -∞. 
# 
#  You must write an algorithm that runs in O(log n) time. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index 
# number 2. 
# 
#  Example 2: 
# 
#  
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak 
# element is 2, or index number 5 where the peak element is 6. 
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 1000 
#  -2³¹ <= nums[i] <= 2³¹ - 1 
#  nums[i] != nums[i + 1] for all valid i. 
#  
#  Related Topics Array Binary Search 👍 6132 👎 3759

from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        lo, hi = -1, len(nums)
        while lo < hi - 1:
            mid = lo + (hi - lo) // 2
            if mid + 1 == len(nums) and nums[mid] > nums[mid - 1]:
                return mid
            if nums[mid] < nums[mid + 1]:
                lo = mid
            else:
                hi = mid
        if hi == len(nums):
            return len(nums) - 1
        return hi


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    a.findPeakElement([1, 2])
