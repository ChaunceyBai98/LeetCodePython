# Given a sorted array of distinct integers and a target value, return the 
# index if the target is found. If not, return the index where it would be if it were 
# inserted in order. 
# 
#  You must write an algorithm with O(log n) runtime complexity. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,3,5,6], target = 5
# Output: 2
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,3,5,6], target = 2
# Output: 1
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [1,3,5,6], target = 7
# Output: 4
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  nums contains distinct values sorted in ascending order. 
#  -10⁴ <= target <= 10⁴ 
#  
#  Related Topics Array Binary Search 👍 7532 👎 403

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # https://www.bilibili.com/video/BV1d54y1q7k7?spm_id_from=333.337.search-card.all.click
    # left 指向比目标小的最后一个，right指向比目标大的第一个
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = -1, len(nums)
        #如果left==right -1,那么边界已经划分好了
        while left < right - 1:
            mid = left + (right - left)//2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid
            else:
                return mid
        return right


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    print(a.searchInsert([1, 3, 5, 6],5))
