# Given the head of a linked list, return the list after sorting it in 
# ascending order. 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
#  
# 
#  Example 2: 
# 
#  
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
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
#  The number of nodes in the list is in the range [0, 5 * 10⁴]. 
#  -10⁵ <= Node.val <= 10⁵ 
#  
# 
#  
#  Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.
# e. constant space)? 
#  Related Topics Linked List Two Pointers Divide and Conquer Sorting Merge 
# Sort 👍 7105 👎 230

from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def sortList(self, head: ListNode) -> ListNode:
        return self.sortFunc(head, None)

    def sortFunc(self, head: ListNode, tail: ListNode) -> ListNode:
        if not head:
            return head
        if head.next == tail:
            head.next = None
            return head
        slow = fast = head
        while fast != tail:
            slow = slow.next
            fast = fast.next
            if fast != tail:
                fast = fast.next
        mid = slow
        return self.merge(self.sortFunc(head, mid), self.sortFunc(mid, tail))

    def merge(self, head1: ListNode, head2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        temp, temp1, temp2 = dummyHead, head1, head2
        while head1 and head2:
            if head1.val < head2.val:
                temp.next = head1
                head1 = head1.next
            else:
                temp.next = head2
                head2 = head2.next
            temp = temp.next
        if head1:
            temp.next = head1
        else:
            temp.next = head2
        return dummyHead.next


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
