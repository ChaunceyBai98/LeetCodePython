# # You are given an integer array height of length n. There are n vertical 
# lines 
# # drawn such that the two endpoints of the iᵗʰ line are (i, 0) and (i, height[
# i]).
# # 
# # 
# # Find two lines that together with the x-axis form a container, such that 
# the 
# # container contains the most water. 
# # 
# # Return the maximum amount of water a container can store. 
# # 
# # Notice that you may not slant the container. 
# # 
# # 
# # Example 1: 
# # 
# # 
# # Input: height = [1,8,6,2,5,4,8,3,7]
# # Output: 49
# # Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,
# 8,
# # 3,7]. In this case, the max area of water (blue section) the container can 
# # contain is 49.
# # 
# # 
# # Example 2: 
# # 
# # 
# # Input: height = [1,1]
# # Output: 1
# # 
# # 
# # 
# # Constraints: 
# # 
# # 
# # n == height.length 
# # 2 <= n <= 10⁵ 
# # 0 <= height[i] <= 10⁴ 
# # 
# # Related Topics Array Two Pointers Greedy 👍 16507 👎 932
# 这题是贪心
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        hlen = len(height)
        max = 0
        l, r = 0, hlen - 1
        while l < r:
            cur = min(height[l], height[r]) * (r - l)
            if cur > max:
                max = cur
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    a = Solution()
    print(a.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(a.maxArea([1, 1]))
