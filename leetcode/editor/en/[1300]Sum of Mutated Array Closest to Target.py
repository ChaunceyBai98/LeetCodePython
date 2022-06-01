# Given an integer array arr and a target value target, return the integer 
# value such that when we change all the integers larger than value in the given array 
# to be equal to value, the sum of the array gets as close as possible (in 
# absolute difference) to target. 
# 
#  In case of a tie, return the minimum such integer. 
# 
#  Notice that the answer is not neccesarilly a number from arr. 
# 
#  
#  Example 1: 
# 
#  
# Input: arr = [4,9,3], target = 10
# Output: 3
# Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's 
# the optimal answer.
#  
# 
#  Example 2: 
# 
#  
# Input: arr = [2,3,5], target = 10
# Output: 5
#  
# 
#  Example 3: 
# 
#  
# Input: arr = [60864,25176,27249,21296,20204], target = 56803
# Output: 11361
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= arr.length <= 10⁴ 
#  1 <= arr[i], target <= 10⁵ 
#  
#  Related Topics Array Binary Search Sorting 👍 784 👎 94
import bisect
from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        # 排序
        arr.sort()
        n = len(arr)
        # 计算前缀和
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] + num)
        # l:0,r:数组里的最大值
        l, r = -1, max(arr) + 1
        while l < r - 1:
            mid = l + (r - l) // 2
            # it 之前的数比mid小, it包括之后的数比mid大
            it = bisect.bisect_left(arr, mid)
            # 前面数的和 + 后面数都变成mid的和
            curSum = prefix[it] + (n - it) * mid
            if curSum <= target:
                l = mid
            else:
                r = mid

        # 计算修改后的结果
        def check(x):
            #  下面那个return的意思
            # sum = 0
            # for num in arr:
            #     if num >= x:
            #         sum += x
            #     else:
            #         sum += num
            # return sum
            return sum(x if num >= x else num for num in arr)

        choose_small = check(l)
        choose_big = check(r)
        return l if abs(choose_small - target) <= abs(choose_big - target) else r


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    print(a.findBestValue([4, 9, 3], 10))
