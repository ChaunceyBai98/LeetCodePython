# Given an m x n integer matrix matrix, if an element is 0, set its entire row 
# and column to 0's. 
# 
#  You must do it in place. 
# 
#  
#  Example 1: 
# 
#  
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
#  
# 
#  Example 2: 
# 
#  
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
#  
# 
#  
#  Constraints: 
# 
#  
#  m == matrix.length 
#  n == matrix[0].length 
#  1 <= m, n <= 200 
#  -2³¹ <= matrix[i][j] <= 2³¹ - 1 
#  
# 
#  
#  Follow up: 
# 
#  
#  A straightforward solution using O(mn) space is probably a bad idea. 
#  A simple improvement uses O(m + n) space, but still not the best solution. 
#  Could you devise a constant space solution? 
#  
#  Related Topics Array Hash Table Matrix 👍 7126 👎 494

from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 用两个变量来保存第一行和第一列是否包含0， 如果非第一行第一列包含零，则将此0平移至其对应的第一行第一列
        # 最后根据第一行第一列的0和两个变量来给矩阵置零
        m = len(matrix)
        n = len(matrix[0])

        if1Col = False

        for j in range(m):
            if matrix[j][0] == 0:
                if1Col = True
                break

        for i in matrix[0]:
            if i == 0:
                matrix[0][0] = 0
                break

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0

        if if1Col:
            for i in range(m):
                matrix[i][0] = 0


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    a.setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
