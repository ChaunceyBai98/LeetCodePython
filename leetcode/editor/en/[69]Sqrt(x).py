# Given a non-negative integer x, compute and return the square root of x. 
# 
#  Since the return type is an integer, the decimal digits are truncated, and 
# only the integer part of the result is returned. 
# 
#  Note: You are not allowed to use any built-in exponent function or operator, 
# such as pow(x, 0.5) or x ** 0.5. 
# 
#  
#  Example 1: 
# 
#  
# Input: x = 4
# Output: 2
#  
# 
#  Example 2: 
# 
#  
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part 
# is truncated, 2 is returned. 
# 
#  
#  Constraints: 
# 
#  
#  0 <= x <= 2³¹ - 1 
#  
#  Related Topics Math Binary Search 👍 3912 👎 3229

from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def mySqrt(self, x: int) -> int:
        # 根据红蓝模板改的
        lo = 0
        hi = x // 2
        # 跳出循环时，lo*lo是>=x的第一个元素
        while lo * lo < x:
            mid = lo + (hi - lo) // 2
            if lo == mid:
                # 当hi = lo + 1时，要能跳出循环
                lo += 1
            elif mid * mid <= x:
                lo = mid
            else:
                hi = mid
        return lo if lo * lo == x else lo - 1


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    print(a.mySqrt(100))
    print(a.mySqrt(99))
