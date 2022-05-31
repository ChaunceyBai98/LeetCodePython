# Write an efficient algorithm that searches for a value target in an m x n 
# integer matrix matrix. This matrix has the following properties: 
# 
#  
#  Integers in each row are sorted in ascending from left to right. 
#  Integers in each column are sorted in ascending from top to bottom. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[1
# 8,21,23,26,30]], target = 5
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[1
# 8,21,23,26,30]], target = 20
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= n, m <= 300 
#  -10⁹ <= matrix[i][j] <= 10⁹ 
#  All the integers in each row are sorted in ascending order. 
#  All the integers in each column are sorted in ascending order. 
#  -10⁹ <= target <= 10⁹ 
#  
#  Related Topics Array Binary Search Divide and Conquer Matrix 👍 7422 👎 123

from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        start = [0, n - 1]
        while start[0] < m and start[1] > -1:
            if matrix[start[0]][start[1]] > target:
                start[1] -= 1
            elif matrix[start[0]][start[1]] < target:
                start[0] += 1
            else:
                return True
        return False


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
