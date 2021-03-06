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
#  1 <= arr.length <= 10â´ 
#  1 <= arr[i], target <= 10âµ 
#  
#  Related Topics Array Binary Search Sorting ð 784 ð 94
import bisect
from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        # æåº
        arr.sort()
        n = len(arr)
        # è®¡ç®åç¼å
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] + num)
        # l:0,r:æ°ç»éçæå¤§å¼
        l, r = -1, max(arr) + 1
        while l < r - 1:
            mid = l + (r - l) // 2
            # it ä¹åçæ°æ¯midå°, itåæ¬ä¹åçæ°æ¯midå¤§
            it = bisect.bisect_left(arr, mid)
            # åé¢æ°çå + åé¢æ°é½åæmidçå
            curSum = prefix[it] + (n - it) * mid
            if curSum <= target:
                l = mid
            else:
                r = mid

        # è®¡ç®ä¿®æ¹åçç»æ
        def check(x):
            #  ä¸é¢é£ä¸ªreturnçææ
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
