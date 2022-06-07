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
    # 自己的版本，稍微提升了一点效率
    # def moveZeroes(self, nums: List[int]) -> None:
    #     l, r = 0, 0
    #     nlen = len(nums)
    #     while l < nlen and nums[l] != 0:
    #         l += 1
    #     r = l
    #     while r < nlen:
    #         while l < nlen and nums[l] != 0:
    #             l += 1
    #         while r < nlen and nums[r] == 0:
    #             r += 1
    #         if r == nlen - 1 and nums[r] == 0 or r == nlen:
    #             break
    #         else:
    #             nums[l], nums[r] = nums[r], nums[l]
    #     # print(nums)

    #答案这么写没问题，但是我不理解为什么可以把代码写成这样？
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    a.moveZeroes([1, 2, 0, 3, 4])
    a.moveZeroes([0, 1, 0, 3, 12])
    a.moveZeroes([0])
    a.moveZeroes([1])
