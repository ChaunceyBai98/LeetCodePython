# Given an integer array nums of length n and an integer target, find three 
# integers in nums such that the sum is closest to target. 
# 
#  Return the sum of the three integers. 
# 
#  You may assume that each input would have exactly one solution. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0,0,0], target = 1
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  3 <= nums.length <= 1000 
#  -1000 <= nums[i] <= 1000 
#  -10⁴ <= target <= 10⁴ 
#  
#  Related Topics Array Two Pointers Sorting 👍 5690 👎 242

from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
import sys


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        nlen = len(nums)
        ans = 10000000

        def updateAns(curSum: int, ans: int)->int:
            if abs(curSum - target) < abs(ans - target):
                ans = curSum
            return ans

        for i in range(nlen - 2):
            if nums[i] > target / 3:
                ans = updateAns(nums[i] + nums[i + 1] + nums[i + 2], ans)
                break
            start = i + 1
            end = nlen - 1
            while start < end:
                curSum = nums[i] + nums[start] + nums[end]
                ans = updateAns(curSum, ans)
                if curSum == target:
                    return curSum
                elif curSum < target:
                    start += 1
                else:
                    end -= 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    print(a.threeSumClosest([11, 1, 1], 123))
    print(a.threeSumClosest(nums = [-1,2,1,-4], target = 1))
    print(a.threeSumClosest(nums = [0,0,0], target = 1))
    print(a.threeSumClosest([1, 1, 1, 1], 0))
