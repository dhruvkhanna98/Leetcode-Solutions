# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        
        curr = head
        
        # Base case
        if curr == None or curr.next == None: 
            return curr
        
        reversed_head = self.reverseList(curr.next)
        curr.next.next = curr
        curr.next = None
        
        return reversed_head
        

        
        