# Given an array of integers nums and an integer target, return indices of the 
# two numbers such that they add up to target. 
# 
#  You may assume that each input would have exactly one solution, and you may 
# not use the same element twice. 
# 
#  You can return the answer in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [3,3], target = 6
# Output: [0,1]
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= nums.length <= 10⁴ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  -10⁹ <= target <= 10⁹ 
#  Only one valid answer exists. 
#  
# 
#  
# Follow-up: Can you come up with an algorithm that is less than O(n²) time 
# complexity? Related Topics Array Hash Table 👍 32396 👎 1031

from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # hashmap
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     map = {}
    #     for i in range(len(nums)):
    #         if map.get(nums[i]) is not None:
    #             return [i, map.get(nums[i])]
    #         else:
    #             map.setdefault(target - nums[i],i)
    #     return []
    # 双指针
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        Nnums = nums.copy()
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                for i in range(len(Nnums)):
                    if Nnums[i] == nums[left] or Nnums[i] == nums[right]:
                        ans.append(i)
                return ans
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    print(a.twoSum([3, 2, 4], 6))
    print(a.twoSum(nums=[2, 7, 11, 15], target=9))
    print(a.twoSum(nums=[3, 3], target=6))
