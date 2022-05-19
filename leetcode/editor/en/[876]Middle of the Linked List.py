# Given the head of a singly linked list, return the middle node of the linked 
# list. 
# 
#  If there are two middle nodes, return the second middle node. 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
#  
# 
#  Example 2: 
# 
#  
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we 
# return the second one.
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is in the range [1, 100]. 
#  1 <= Node.val <= 100 
#  
#  Related Topics Linked List Two Pointers 👍 5347 👎 136

from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        mid, tail = head, head
        while tail.next is not None:
            tail = tail.next
            if tail.next is not None:
                tail = tail.next
            mid = mid.next
        return mid


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
