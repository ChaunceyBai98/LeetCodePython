# Suppose an array of length n sorted in ascending order is rotated between 1 
# and n times. For example, the array nums = [0,1,2,4,5,6,7] might become: 
# 
#  
#  [4,5,6,7,0,1,2] if it was rotated 4 times. 
#  [0,1,2,4,5,6,7] if it was rotated 7 times. 
#  
# 
#  Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results 
# in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]]. 
# 
#  Given the sorted rotated array nums of unique elements, return the minimum 
# element of this array. 
# 
#  You must write an algorithm that runs in O(log n) time. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 
# times.
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
# 
#  
# 
#  
#  Constraints: 
# 
#  
#  n == nums.length 
#  1 <= n <= 5000 
#  -5000 <= nums[i] <= 5000 
#  All the integers of nums are unique. 
#  nums is sorted and rotated between 1 and n times. 
#  
#  Related Topics Array Binary Search 👍 6922 👎 397

from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while hi > lo:
            mid = lo + (hi - lo) // 2
            # 关键条件是 当 mid比hi大 时，最小数在mid右边，如果mid小于hi：最小数可能在mid以及mid以左，
            if nums[mid] < nums[hi]:
                # 如果mid小于hi：最小数可能在mid以及mid以左
                hi = mid
            else:
                # 当 mid比hi大 时，最小数在mid右边
                lo = mid + 1
        # lo 和 hi 都行
        return nums[hi]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    print(a.findMin(nums=[11, 13, 15, 17]))
    print(a.findMin(nums=[4, 5, 6, 7, 0, 1, 2]))
