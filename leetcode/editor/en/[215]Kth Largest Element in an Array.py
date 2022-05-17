# Given an integer array nums and an integer k, return the kᵗʰ largest element 
# in the array. 
# 
#  Note that it is the kᵗʰ largest element in the sorted order, not the kᵗʰ 
# distinct element. 
# 
#  
#  Example 1: 
#  Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
#  Example 2: 
#  Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
#  
#  
#  Constraints: 
# 
#  
#  1 <= k <= nums.length <= 10⁴ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  
#  Related Topics Array Divide and Conquer Sorting Heap (Priority Queue) 
# Quickselect 👍 9155 👎 490
import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # # nums：数组，k:第k大
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     n = len(nums)
    #     # 构建最大堆
    #     self.buildMaxHeap(nums)
    #     # 构建完后 pop k-1 次
    #     for i in range(k - 1):
    #         nums[0], nums[n - 1 - i] = nums[n - 1 - i], nums[0]
    #         self.adjustDown(nums, 0, n - 1 - i - 1)
    #     return nums[0]
    #
    # # 构建最大堆
    # def buildMaxHeap(self, nums: List[int]) -> None:
    #     n = len(nums)
    #     # 对前一半进行下沉 从n//2到0（从后往前，对非叶子节点进行下沉）
    #     for root in range(n // 2, -1, -1):
    #         self.adjustDown(nums, root, n - 1)
    #
    # # 对root进行下沉操作
    # def adjustDown(self, nums: List[int], root: int, hi: int) -> None:
    #     if root > hi:
    #         return
    #     t = nums[root]
    #     child = 2 * root + 1  # root的左子
    #     # root为非叶子节点时（叶子节点无法下沉）
    #     while child <= hi:
    #         # 选它比较大的那个孩子
    #         if child + 1 <= hi and nums[child] < nums[child + 1]:
    #             child += 1
    #         # 如果要下沉的元素比最大的子不小，跳出循环，当前的根等于要下沉的元素（下沉到位置了）
    #         if t >= nums[child]:
    #             break
    #         # 如果根比子小，把子的值赋予根（子上浮）
    #         nums[root] = nums[child]
    #         # 根指向子
    #         root = child
    #         # 子指向新的根的子
    #         child = 2 * root + 1
    #     # 叶子节点赋为最开始的root的值（子上浮结束，下沉元素的位置为root）
    #     nums[root] = t

    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        while True:
            idx = self.partition(nums, l, r)
            if idx == k - 1:
                return nums[idx]
            elif idx < k - 1:
                l = idx + 1
            else:
                r = idx - 1

    # ----左右挖坑互填
    def partition(self, nums: List[int], l: int, r: int) -> int:
        pivot = nums[l]
        while l < r:
            # 从右往左找比pivot大的
            while l < r and nums[r] <= pivot:
                r -= 1
            # 大的挪到左边
            nums[l] = nums[r]
            # 从左往右找比pivot小的
            while l < r and nums[l] >= pivot:
                l += 1
            # 小的挪到右边
            nums[r] = nums[l]
        # l在的位置就是pivot应该在的位置
        nums[l] = pivot
        return l


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    print(a.findKthLargest([1, 2, 3, 4, 5, 6, 7, 8], 8))
