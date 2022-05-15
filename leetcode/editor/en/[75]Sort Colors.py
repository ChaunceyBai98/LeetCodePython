# Given an array nums with n objects colored red, white, or blue, sort them in-
# place so that objects of the same color are adjacent, with the colors in the 
# order red, white, and blue. 
# 
#  We will use the integers 0, 1, and 2 to represent the color red, white, and 
# blue, respectively. 
# 
#  You must solve this problem without using the library's sort function. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [2,0,1]
# Output: [0,1,2]
#  
# 
#  
#  Constraints: 
# 
#  
#  n == nums.length 
#  1 <= n <= 300 
#  nums[i] is either 0, 1, or 2. 
#  
# 
#  
#  Follow up: Could you come up with a one-pass algorithm using only constant 
# extra space? 
#  Related Topics Array Two Pointers Sorting 👍 9803 👎 415

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p20, p22 = 0, len(nums) - 1
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == 0:
                nums[i], nums[p20] = nums[p20], nums[i]
                p20 += 1
                if nums[i] == 1:
                    i += 1
            elif nums[i] == 2:
                if i >= p22:
                    break
                nums[i], nums[p22] = nums[p22], nums[i]
                p22 -= 1
                if nums[i] == 1:
                    i += 1
            else:
                i += 1
        print(nums)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    a.sortColors([2,0,2,1,1,0])
