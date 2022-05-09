# Given an integer array nums, move all 0's to the end of it while maintaining 
# the relative order of the non-zero elements. 
# 
#  Note that you must do this in-place without making a copy of the array. 
# 
#  
#  Example 1: 
#  Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
#  Example 2: 
#  Input: nums = [0]
# Output: [0]
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  -2³¹ <= nums[i] <= 2³¹ - 1 
#  
# 
#  
# Follow up: Could you minimize the total number of operations done? Related 
# Topics Array Two Pointers 👍 8925 👎 241

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = right = 0

        # 如果不是0，left和right都+1，交换等于没交换，如果是0，right+1,left还指向0，可以交换，
        # 如果有多个零，left停在第一个零，right停在第一个非零
        for i in range(n):
            if nums[i] != 0:
                #交换为什么写在这个位置呢？
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
        print(nums)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    a.moveZeroes([1, 2, 0, 3, 4])
