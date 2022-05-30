# Given an array of integers nums sorted in non-decreasing order, find the 
# starting and ending position of a given target value. 
# 
#  If target is not found in the array, return [-1, -1]. 
# 
#  You must write an algorithm with O(log n) runtime complexity. 
# 
#  
#  Example 1: 
#  Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
#  Example 2: 
#  Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
#  Example 3: 
#  Input: nums = [], target = 0
# Output: [-1,-1]
#  
#  
#  Constraints: 
# 
#  
#  0 <= nums.length <= 10⁵ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  nums is a non-decreasing array. 
#  -10⁹ <= target <= 10⁹ 
#  
#  Related Topics Array Binary Search 👍 10793 👎 295

from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo, hi = -1, len(nums)
        while lo + 1 != hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < target:
                lo = mid
            else:
                hi = mid
        firstOne = hi
        if firstOne == len(nums):
            return [-1, -1]
        lo, hi = -1, len(nums)
        while lo + 1 != hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] <= target:
                lo = mid
            else:
                hi = mid
        secondOne = lo
        if nums[firstOne] == nums[secondOne] == target:
            return [firstOne, secondOne]
        return [-1, -1]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    print(a.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
    print(a.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6))
    print(a.searchRange([2, 2], 3))
