# Write an efficient algorithm that searches for a value target in an m x n 
# integer matrix matrix. This matrix has the following properties: 
# 
#  
#  Integers in each row are sorted from left to right. 
#  The first integer of each row is greater than the last integer of the 
# previous row. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 100 
#  -10⁴ <= matrix[i][j], target <= 10⁴ 
#  
#  Related Topics Array Binary Search Matrix 👍 7741 👎 273

from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        lo = -1
        hi = m * n

        def idx2Location(idx: int) -> List:
            if idx < n:
                return [0, idx]
            trow = idx // n
            tcol = idx - n * trow
            return [trow, tcol]

        while lo < hi - 1:
            mid = lo + (hi - lo) // 2
            mrow, mcol = idx2Location(mid)
            if matrix[mrow][mcol] < target:
                lo = mid
            else:
                hi = mid

        row, col = idx2Location(hi)
        if row == m:
            return False
        if matrix[row][col] == target:
            return True
        return False


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    print(a.searchMatrix([[1]], 2))
    # print(a.searchMatrix([[1, 1]], 2))
    print(a.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
