# Given an m x n matrix, return all elements of the matrix in spiral order. 
# 
#  
#  Example 1: 
# 
#  
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
#  
# 
#  Example 2: 
# 
#  
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#  
# 
#  
#  Constraints: 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 10 
#  -100 <= matrix[i][j] <= 100 
#  
#  Related Topics Array Matrix Simulation 👍 7191 👎 840

from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if not matrix:
            return result
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        numEle = len(matrix) * len(matrix[0])
        while numEle >= 1:
            for i in range(left, right + 1):
                if numEle < 1:
                    break
                result.append(matrix[top][i])
                numEle -= 1
            top += 1
            for i in range(top, bottom + 1):
                if numEle < 1:
                    break
                result.append(matrix[i][right])
                numEle -= 1
            right -= 1
            for i in range(right, left - 1, -1):
                if numEle < 1:
                    break
                result.append(matrix[bottom][i])
                numEle -= 1
            bottom -= 1
            for i in range(bottom, top - 1, -1):
                if numEle < 1:
                    break
                result.append(matrix[i][left])
                numEle -= 1
            left += 1
        return result


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    print(a.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))