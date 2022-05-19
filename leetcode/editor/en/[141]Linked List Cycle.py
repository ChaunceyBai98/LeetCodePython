# Given head, the head of a linked list, determine if the linked list has a 
# cycle in it. 
# 
#  There is a cycle in a linked list if there is some node in the list that can 
# be reached again by continuously following the next pointer. Internally, pos is 
# used to denote the index of the node that tail's next pointer is connected to. 
# Note that pos is not passed as a parameter. 
# 
#  Return true if there is a cycle in the linked list. Otherwise, return false. 
# 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to 
# the 1st node (0-indexed).
#  
# 
#  Example 2: 
# 
#  
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to 
# the 0th node.
#  
# 
#  Example 3: 
# 
#  
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of the nodes in the list is in the range [0, 10⁴]. 
#  -10⁵ <= Node.val <= 10⁵ 
#  pos is -1 or a valid index in the linked-list. 
#  
# 
#  
#  Follow up: Can you solve it using O(1) (i.e. constant) memory? 
#  Related Topics Hash Table Linked List Two Pointers 👍 8109 👎 790

from typing import List, Optional
from dataStructure.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        slow, fast = head, head.next
        while fast != slow:
            if fast is None or fast.next is None:
                return False
            fast = fast.next.next
            slow = slow.next
        return True


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = Solution()
    t1 = ListNode(1,ListNode(2,None))
    print(a.hasCycle(t1))