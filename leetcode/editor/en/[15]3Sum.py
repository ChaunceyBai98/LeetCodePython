# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[
# k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. 
# 
#  Notice that the solution set must not contain duplicate triplets. 
# 
#  
#  Example 1: 
#  Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
#  Example 2: 
#  Input: nums = []
# Output: []
#  Example 3: 
#  Input: nums = [0]
# Output: []
#  
#  
#  Constraints: 
# 
#  
#  0 <= nums.length <= 3000 
#  -10⁵ <= nums[i] <= 10⁵ 
#  
#  Related Topics Array Two Pointers Sorting 👍 17299 👎 1663

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        nlen = len(nums)
        for i in range(nlen):
            if nums[i] > 0:
                break
            # find the first one of duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            resOf2 = self.twoSum(nums, i + 1, nlen - 1, -nums[i])
            if resOf2:
                for ele in resOf2:
                    res.append([nums[i], ele[0], ele[1]])
        return res

    def twoSum(self, nums: List[int], start: int, end: int, target) -> list[list[int]]:
        res = []
        # nums是有序的
        while start < end:
            if nums[start] > target / 2:
                return res
            if nums[start] + nums[end] == target:
                res.append([nums[start], nums[end]])
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
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    print(a.threeSum([-1,0,1,2,-1,-4]))
