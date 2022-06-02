# You are given an integer array nums consisting of n elements, and an integer 
# k. 
# 
#  Find a contiguous subarray whose length is greater than or equal to k that 
# has the maximum average value and return this value. Any answer with a 
# calculation error less than 10⁻⁵ will be accepted. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation:
# - When the length is 4, averages are [0.5, 12.75, 10.5] and the maximum 
# average is 12.75
# - When the length is 5, averages are [10.4, 10.8] and the maximum average is 1
# 0.8
# - When the length is 6, averages are [9.16667] and the maximum average is 9.16
# 667
# The maximum average is when we choose a subarray of length 4 (i.e., the sub 
# array [12, -5, -6, 50]) which has the max average 12.75, so we return 12.75
# Note that we do not consider the subarrays of length < 4.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [5], k = 1
# Output: 5.00000
#  
# 
#  
#  Constraints: 
# 
#  
#  n == nums.length 
#  1 <= k <= n <= 10⁴ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  
#  Related Topics Array Binary Search 👍 542 👎 61
from itertools import accumulate
from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        def check(mid):
            pre=[0]+list(accumulate([v-mid for v in nums]))
            minv=0
            for i in range(k,n+1):
                # 这里不能pre[i]-pre[i-k]>=0
                # [-1,2,-3,-2,3]
                if pre[i]-minv>=0:return True
                # 必须保持距离大于等于k
                minv=min(minv,pre[i-k+1])
            return False

        l,r=min(nums),max(nums)
        # 二分
        while r-l>1e-5:
            mid=(l+r)/2
            if check(mid):
                l=mid
            else:
                r=mid
        return r
        
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()