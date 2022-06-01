# You are given a sorted array consisting of only integers where every element 
# appears exactly twice, except for one element which appears exactly once. 
# 
#  Return the single element that appears only once. 
# 
#  Your solution must run in O(log n) time and O(1) space. 
# 
#  
#  Example 1: 
#  Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
#  Example 2: 
#  Input: nums = [3,3,7,7,10,11,11]
# Output: 10
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  0 <= nums[i] <= 10⁵ 
#  
#  Related Topics Array Binary Search 👍 5234 👎 111

from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        def ifSingleOnLeft(idx: int) -> bool:
            # 个例不面向测试想不到
            if idx == len(nums) - 1:
                return True

            if idx % 2 == 0:
                if nums[idx] == nums[idx + 1]:
                    return False
            else:
                if nums[idx] == nums[idx - 1]:
                    return False
            return True

        l, r = -1, len(nums)
        while l < r - 1:
            mid = l + (r - l) // 2
            if not ifSingleOnLeft(mid):
                l = mid
            else:
                r = mid
        # 个例不面向测试想不到
        if r == len(nums):
            return nums[-1]
        return nums[r]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    print(a.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
