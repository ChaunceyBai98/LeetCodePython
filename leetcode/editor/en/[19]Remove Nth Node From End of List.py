# Given the head of a linked list, remove the nᵗʰ node from the end of the list 
# and return its head. 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
#  
# 
#  Example 2: 
# 
#  
# Input: head = [1], n = 1
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: head = [1,2], n = 1
# Output: [1]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is sz. 
#  1 <= sz <= 30 
#  0 <= Node.val <= 100 
#  1 <= n <= sz 
#  
# 
#  
#  Follow up: Could you do this in one pass? 
#  Related Topics Linked List Two Pointers 👍 9663 👎 460

from typing import Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(-1,head)
        left, right = dummy, dummy
        dis = 0
        while right.next is not None:
            right = right.next
            dis += 1
            if dis > n:
                left = left.next
                # dis -= 1
        left.next = left.next.next
        return dummy.next


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
