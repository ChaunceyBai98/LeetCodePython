# You are a product manager and currently leading a team to develop a new 
# product. Unfortunately, the latest version of your product fails the quality check. 
# Since each version is developed based on the previous version, all the versions 
# after a bad version are also bad. 
# 
#  Suppose you have n versions [1, 2, ..., n] and you want to find out the 
# first bad one, which causes all the following ones to be bad. 
# 
#  You are given an API bool isBadVersion(version) which returns whether 
# version is bad. Implement a function to find the first bad version. You should 
# minimize the number of calls to the API. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 1, bad = 1
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= bad <= n <= 2³¹ - 1 
#  
#  Related Topics Binary Search Interactive 👍 4707 👎 1764

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # left = 1
        # right = n
        low, high = 0, n+1
        while low < high - 1:
            mid = (high - low) // 2 + low
            if isBadVersion(mid):
                high = mid
            else:
                low = mid
        return high
        # findSeperation = False
        # while not findSeperation:
        #     middle = int(left+(right-left)/2)
        #     isMiddleBad = isBadVersion(middle)
        #     if isMiddleBad :
        #         right = middle - 1
        #         findSeperation = not isBadVersion(right)
        #         if(findSeperation):
        #             return right + 1
        #     else:
        #         left = middle + 1
        #         findSeperation = isBadVersion(left)
        #         if(findSeperation):
        #             return left


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()