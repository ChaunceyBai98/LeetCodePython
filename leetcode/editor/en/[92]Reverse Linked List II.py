# Given the head of a singly linked list and two integers left and right where 
# left <= right, reverse the nodes of the list from position left to position 
# right, and return the reversed list. 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
#  
# 
#  Example 2: 
# 
#  
# Input: head = [5], left = 1, right = 1
# Output: [5]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is n. 
#  1 <= n <= 500 
#  -500 <= Node.val <= 500 
#  1 <= left <= right <= n 
#  
# 
#  
# Follow up: Could you do it in one pass? Related Topics Linked List 👍 6117 👎 
# 290

from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        dummyHead = ListNode(-1, head)
        pre1 = dummyHead
        # find the node before left
        for i in range(left - 1):
            pre1 = pre1.next
        pre2 = pre1.next
        cur = pre1.next.next
        for i in range(right - left):
            tail = cur.next
            cur.next = pre2
            pre2 = cur
            cur = tail
        pre1.next.next = cur
        pre1.next = pre2
        return dummyHead.next


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    b = a.reverseBetween(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, None))))))), 3,
                     6)
    while b:
        print(b.val,',')
        b = b.next
