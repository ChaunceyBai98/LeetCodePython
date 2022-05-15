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
    # nums：数组，k:第k大
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # 构建最大堆
        self.buildMaxHeap(nums)
        # 扔k-1个最大数，下沉k-1次
        for i in range(k - 1):
            nums[0], nums[n - 1 - i] = nums[n - 1 - i], nums[0]
            self.adjustDown(nums, 0, n - 1 - i - 1)
        return nums[0]

    def buildMaxHeap(self, nums: List[int]) -> None:
        n = len(nums)
        # 对前一半进行下沉操作 从n//2到0
        for root in range(n // 2, -1, -1):
            self.adjustDown(nums, root, n - 1)
            print(nums)

    #
    def adjustDown(self, nums: List[int], root: int, hi: int) -> None:
        if root > hi:
            return
        t = nums[root]
        child = 2 * root + 1  # 左子
        # 当还有孩子的时候
        while child <= hi:
            # 如果右子没出界，并且左子小于右子
            if child + 1 <= hi and nums[child] < nums[child + 1]:
                # 处理右子
                child += 1
            # 如果初始根不比当前的子小,跳出循环，当前的根等于初始根
            if t >= nums[child]:
                break
            # 如果根比子小，把子的值赋予根，
            nums[root] = nums[child]
            # 根指向子
            root = child
            # 子指向新的根的子
            child = 2 * root + 1
        # 叶子节点赋为最开始的root的值
        nums[root] = t


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    a.findKthLargest([123, 2, 3, 4,5,6,7,8], 4)