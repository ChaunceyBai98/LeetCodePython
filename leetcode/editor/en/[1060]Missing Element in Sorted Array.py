# Given an integer array nums which is sorted in ascending order and all of its 
# elements are unique and given also an integer k, return the kᵗʰ missing number 
# starting from the leftmost number of the array. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [4,7,9,10], k = 1
# Output: 5
# Explanation: The first missing number is 5.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [4,7,9,10], k = 3
# Output: 8
# Explanation: The missing numbers are [5,6,8,...], hence the third missing 
# number is 8.
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [1,2,4], k = 3
# Output: 6
# Explanation: The missing numbers are [3,5,6,7,...], hence the third missing 
# number is 6.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 5 * 10⁴ 
#  1 <= nums[i] <= 10⁷ 
#  nums is sorted in ascending order, and all the elements are unique. 
#  1 <= k <= 10⁸ 
#  
# 
#  
# Follow up: Can you find a logarithmic time complexity (i.e., O(log(n))) 
# solution? Related Topics Array Binary Search 👍 1301 👎 51

from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # Return how many numbers are missing until nums[idx]
        # 如何知道idx前缺了多少个数的关键观察
        def missing(idx):
            return nums[idx] - nums[0] - idx

        n = len(nums)
        # If kth missing number is larger than
        # the last element of the array
        if k > missing(n - 1):
            return nums[-1] + k - missing(n - 1)

        left, right = 0, n - 1
        # find left = right index such that
        # missing(left - 1) < k <= missing(left)
        while left != right:
            pivot = left + (right - left) // 2

            if missing(pivot) < k:
                left = pivot + 1
            else:
                right = pivot

                # kth missing number is larger than nums[left - 1]
        # and smaller than nums[left]
        return nums[left - 1] + k - missing(left - 1)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    print(a.missingElement(nums=[1, 2, 4], k=3))
