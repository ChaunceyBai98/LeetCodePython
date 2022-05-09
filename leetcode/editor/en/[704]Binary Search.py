# Given an array of integers nums which is sorted in ascending order, and an 
# integer target, write a function to search target in nums. If target exists, then 
# return its index. Otherwise, return -1. 
# 
#  You must write an algorithm with O(log n) runtime complexity. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  -10⁴ < nums[i], target < 10⁴ 
#  All the integers in nums are unique. 
#  nums is sorted in ascending order. 
#  
#  Related Topics Array Binary Search 👍 4603 👎 107

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = -1, len(nums)
        while left < right - 1:
            middle = left + (right - left) // 2
            if nums[middle] > target:
                right = middle
            elif nums[middle] < target:
                left = middle
            else:
                return middle
        return -1


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    print(a.search([-1,0,3,5,9,12], 2))
