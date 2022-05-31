# (This problem is an interactive problem.) 
# 
#  You may recall that an array arr is a mountain array if and only if: 
# 
#  
#  arr.length >= 3 
#  There exists some i with 0 < i < arr.length - 1 such that:
#  
#  arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
#  arr[i] > arr[i + 1] > ... > arr[arr.length - 1] 
#  
#  
#  
# 
#  Given a mountain array mountainArr, return the minimum index such that 
# mountainArr.get(index) == target. If such an index does not exist, return -1. 
# 
#  You cannot access the mountain array directly. You may only access the array 
# using a MountainArray interface: 
# 
#  
#  MountainArray.get(k) returns the element of the array at index k (0-indexed).
#  
#  MountainArray.length() returns the length of the array. 
#  
# 
#  Submissions making more than 100 calls to MountainArray.get will be judged 
# Wrong Answer. Also, any solutions that attempt to circumvent the judge will 
# result in disqualification. 
# 
#  
#  Example 1: 
# 
#  
# Input: array = [1,2,3,4,5,3,1], target = 3
# Output: 2
# Explanation: 3 exists in the array, at index=2 and index=5. Return the 
# minimum index, which is 2. 
# 
#  Example 2: 
# 
#  
# Input: array = [0,1,2,4,2,1], target = 3
# Output: -1
# Explanation: 3 does not exist in the array, so we return -1.
#  
# 
#  
#  Constraints: 
# 
#  
#  3 <= mountain_arr.length() <= 10⁴ 
#  0 <= target <= 10⁹ 
#  0 <= mountain_arr.get(index) <= 10⁹ 
#  
#  Related Topics Array Binary Search Interactive 👍 1226 👎 57

from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:
class Solution:
    # 自己用二分的模板改的
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # 首先根据mountainArray的特性用二分找峰值
        l, r = -1, mountain_arr.length()
        while l < r - 1:
            m = l + (r - l) // 2
            if mountain_arr.get(m + 1) > mountain_arr.get(m):
                l = m
            else:
                r = m
        peak = r

        # 在左侧用二分找
        # print(peak)
        def b1(l, r):
            l -= 1
            r += 1
            while l < r - 1:
                m = l + (r - l) // 2
                if mountain_arr.get(m) < target:
                    l = m
                else:
                    r = m
            if mountain_arr.get(r) == target:
                return r
            return -1

        # 在右侧用二分找
        def b2(l, r):
            l -= 1
            r += 1
            while l < r - 1:
                m = l + (r - l) // 2
                if mountain_arr.get(m) > target:
                    l = m
                else:
                    r = m
            # if not exist on the right side, the r will exceed board
            if r == mountain_arr.length():
                return -1
            if mountain_arr.get(r) == target:
                return r
            return -1

        left = b1(0, peak)
        if left != -1:
            return left
        right = b2(peak + 1, mountain_arr.length() - 1)
        return right


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    # print(a.findInMountainArray(0, [1, 5, 2]))
    # print(a.findInMountainArray(2, [1, 5, 2]))
