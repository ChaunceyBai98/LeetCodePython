# Given a list of non-negative integers nums, arrange them such that they form 
# the largest number and return it. 
# 
#  Since the result may be very large, so you need to return a string instead 
# of an integer. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [10,2]
# Output: "210"
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [3,30,34,5,9]
# Output: "9534330"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 100 
#  0 <= nums[i] <= 10⁹ 
#  
#  Related Topics String Greedy Sorting 👍 4847 👎 408

from typing import List
from functools import cmp_to_key


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        key = cmp_to_key(lambda x, y: int(y + x) - int(x + y))
        # map(str, nums) 把nums元素类型转换为str
        res = ''.join(sorted(map(str, nums), key=key)).lstrip('0')
        print(nums)
        a = list(map(str, nums))
        print(a)
        return res or '0'


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    a.largestNumber([0, 0, 10, 12, 233, 434])
