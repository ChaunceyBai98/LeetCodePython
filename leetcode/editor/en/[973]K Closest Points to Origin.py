# Given an array of points where points[i] = [xi, yi] represents a point on the 
# X-Y plane and an integer k, return the k closest points to the origin (0, 0). 
# 
#  The distance between two points on the X-Y plane is the Euclidean distance (
# i.e., √(x1 - x2)² + (y1 - y2)²). 
# 
#  You may return the answer in any order. The answer is guaranteed to be 
# unique (except for the order that it is in). 
# 
#  
#  Example 1: 
# 
#  
# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [
# [-2,2]].
#  
# 
#  Example 2: 
# 
#  
# Input: points = [[3,3],[5,-1],[-2,4]], k = 2
# Output: [[3,3],[-2,4]]
# Explanation: The answer [[-2,4],[3,3]] would also be accepted.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= k <= points.length <= 10⁴ 
#  -10⁴ < xi, yi < 10⁴ 
#  
#  Related Topics Array Math Divide and Conquer Geometry Sorting Heap (Priority 
# Queue) Quickselect 👍 5563 👎 206
import heapq
from typing import List, Optional
from dataStructure.ListNode import ListNode


# 四种解法：
# Approach 1: Sort with Custom Comparator O(N logN),O(logN)~O(N)
# Approach 2: Max Heap or Max Priority Queue O(N logk),O(k)
# Approach 3: Binary Search O(n),O(n)
# Approach 4: QuickSelect O(n),O(1)
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # 构建最小堆，然后pop()k次

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # heap 里是（距离平方， 索引），用前k个数构建了k大小的堆
        heap = [(-self.squared_distance(points[i]), i) for i in range(k)]
        # heapq 构建的是最小堆
        heapq.heapify(heap)

        # 把剩下的数加进最小堆
        for i in range(k, len(points)):
            dist = -self.squared_distance(points[i])
            if dist > heap[0][0]:
                heapq.heappushpop(heap, (dist, i))
        return [points[i] for (_, i) in heap]

    def squared_distance(self, point: List[int]) -> int:
        """Calculate and return the squared Euclidean distance."""
        return point[0] ** 2 + point[1] ** 2


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    print(a.kClosest(points=[[3, 3], [5, -1], [-2, 4]], k=2))
