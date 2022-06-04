# Given an array nums of n integers, return an array of all the unique 
# quadruplets [nums[a], nums[b], nums[c], nums[d]] such that: 
# 
#  
#  0 <= a, b, c, d < n 
#  a, b, c, and d are distinct. 
#  nums[a] + nums[b] + nums[c] + nums[d] == target 
#  
# 
#  You may return the answer in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 200 
#  -10⁹ <= nums[i] <= 10⁹ 
#  -10⁹ <= target <= 10⁹ 
#  
#  Related Topics Array Two Pointers Sorting 👍 6170 👎 698

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        nlen = len(nums)
        first = 0
        while first < nlen - 3:
            if nums[first] > target / 4:
                return ans
            second = first + 1
            while second < nlen - 2:
                if nums[second] > (target - nums[first]) / 3:
                    break
                ansOf2 = self.twoSum(nums, second + 1, nlen - 1, target - nums[first] - nums[second])
                if ansOf2:
                    for ele in ansOf2:
                        ans.append([nums[first], nums[second], ele[0], ele[1]])
                    while second < nlen - 2 and nums[second] == nums[second + 1]:
                        second += 1
                    second += 1
                else:
                    second += 1
            while first < nlen - 3 and nums[first] == nums[first + 1]:
                first += 1
            first += 1
        return ans

    def twoSum(self, nums: List[int], start: int, end: int, target: int) -> List[List[int]]:
        ans = []
        while start < end:
            if nums[start] > target / 2:
                return ans
            if nums[start] + nums[end] == target:
                ans.append([nums[start], nums[end]])
                while start < end and nums[start] == nums[start + 1]:
                    start += 1
                while start < end and nums[end] == nums[end - 1]:
                    end -= 1
                start += 1
                end -= 1
            elif nums[start] + nums[end] < target:
                start += 1
            else:
                end -= 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    print(a.twoSum([1, 1], 0, 1, 2))
    print(a.fourSum([1, 1, 2, 3, 4, 5, 6], 7))
    print(a.fourSum([-3, -1, 0, 2, 4, 5], 1))
