# We are given an array asteroids of integers representing asteroids in a row. 
# 
#  For each asteroid, the absolute value represents its size, and the sign 
# represents its direction (positive meaning right, negative meaning left). Each 
# asteroid moves at the same speed. 
# 
#  Find out the state of the asteroids after all collisions. If two asteroids 
# meet, the smaller one will explode. If both are the same size, both will explode. 
# Two asteroids moving in the same direction will never meet. 
# 
#  
#  Example 1: 
# 
#  
# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never 
# collide.
#  
# 
#  Example 2: 
# 
#  
# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.
#  
# 
#  Example 3: 
# 
#  
# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide 
# resulting in 10.
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= asteroids.length <= 10⁴ 
#  -1000 <= asteroids[i] <= 1000 
#  asteroids[i] != 0 
#  
#  Related Topics Array Stack 👍 3512 👎 280

from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = 0
        while i < len(asteroids):
            integer = asteroids[i]
            if integer > 0:
                stack.append(integer)
            elif stack:
                if stack[-1] * integer > 0:
                    stack.append(integer)
                else:
                    if stack[-1] < abs(integer):
                        stack.pop()
                        i -= 1
                    elif stack[-1] == abs(integer):
                        stack.pop()
            else:
                stack.append(integer)
            i += 1
        return stack

        # def asteroidCollision(self, asteroids):
        #     ans = []
        #     for new in asteroids:
        #         while ans and new < 0 < ans[-1]:
        #             if ans[-1] < -new:
        #                 ans.pop()
        #                 continue
        #             elif ans[-1] == -new:
        #                 ans.pop()
        #             break
        #         else:
        #             ans.append(new)
        #     return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    print(a.asteroidCollision([-2, -2, 1, -2]))
    print(a.asteroidCollision([5, 10, -5]))
