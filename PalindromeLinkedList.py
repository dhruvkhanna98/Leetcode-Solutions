# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        # Base Case 
        if head == None: 
            return True
        
        curr = head
        stack = []
        
        while curr: 
            stack.append(curr.val)
            curr = curr.next
        
        while head: 
            if head.val != stack.pop():
                return False
            head = head.next
        
        
        return True