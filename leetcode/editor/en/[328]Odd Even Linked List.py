# Given the head of a singly linked list, group all the nodes with odd indices 
# together followed by the nodes with even indices, and return the reordered list. 
# 
# 
#  The first node is considered odd, and the second node is even, and so on. 
# 
#  Note that the relative order inside both the even and odd groups should 
# remain as it was in the input. 
# 
#  You must solve the problem in O(1) extra space complexity and O(n) time 
# complexity. 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]
#  
# 
#  Example 2: 
# 
#  
# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the linked list is in the range [0, 10⁴]. 
#  -10⁶ <= Node.val <= 10⁶ 
#  
#  Related Topics Linked List 👍 5311 👎 385

from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 自己画图做出来的！
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        oddList = head
        pOddList = oddList
        evenList = head.next
        pEvenList = evenList
        while pOddList.next and pEvenList.next:
                pOddList.next = pEvenList.next
                pEvenList.next = pOddList.next.next
                pOddList = pOddList.next
                pEvenList = pEvenList.next
        pOddList.next = evenList
        return oddList


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    b = a.oddEvenList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, None))))))))
    while b:
        print(b.val,',')
        b = b.next