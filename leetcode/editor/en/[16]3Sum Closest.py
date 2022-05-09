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
        n = len(nums)
        ans = sys.maxsize

        # 根据差值的绝对值来更新答案
        def update(cur):
            nonlocal ans
            if abs(cur - target) < abs(ans - target):
                ans = cur

        for i in range(n):
            # 保证和上一次枚举的元素不相等
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 使用双指针枚举 b 和 c
            l, r = i + 1, n - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                # 如果和为 target 直接返回答案
                if sum == target:
                    return target
                # 每次都要更新
                update(sum)
                if sum > target:
                    while l < r and nums[r - 1] == nums[r]:
                        r -= 1
                    r -= 1
                else:
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1

        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    print(a.threeSumClosest([11, 1, 1], 123))
