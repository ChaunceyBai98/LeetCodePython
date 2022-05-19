# Given the head of a singly linked list, reverse the list, and return the 
# reversed list. 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
#  
# 
#  Example 2: 
# 
#  
# Input: head = [1,2]
# Output: [2,1]
#  
# 
#  Example 3: 
# 
#  
# Input: head = []
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is the range [0, 5000]. 
#  -5000 <= Node.val <= 5000 
#  
# 
#  
#  Follow up: A linked list can be reversed either iteratively or recursively. 
# Could you implement both? 
#  Related Topics Linked List Recursion 👍 11861 👎 205

from typing import List
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def reverseList(self, head: ListNode) -> ListNode:
    #     if head is None or head.next is None:
    #         return head
    #     pre = None
    #     cur = head
    #     while cur is not None:
    #         tail = cur.next
    #         cur.next = pre
    #         pre = cur
    #         cur = tail
    #     return pre

    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        if curr is None or curr.next is None:
            # The last node is returned by this to second node from last
            return curr
        p = self.reverseList(curr.next)
        curr.next.next = curr
        curr.next = None
        return p

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    t1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
    t2 = a.reverseList(t1)
    print(t2.val)
