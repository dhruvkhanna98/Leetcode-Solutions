# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # Base case
        if l1 == None and l2 == None: 
            return None
        elif l1 == None and l2 != None: 
            return l2
        elif l1 != None and l2 == None: 
            return l1
        
        head = ListNode(0)
        curr = head
        carry = 0 

        while l1 or l2:
            
            if l1 and l2: 
                s = l1.val + l2.val + carry
            elif l1 and not l2: 
                s = l1.val + carry
            elif not l1 and l2: 
                s = l2.val + carry
                
            carry = 0

            if s >= 10: 
                s -= 10
                carry = 1

            curr.val = s

            if l1: l1 = l1.next
            if l2: l2 = l2.next

            if l1 or l2: 
                curr.next = ListNode(0)   
                curr = curr.next
        
        if carry == 1: curr.next = ListNode(1)
     
        return head

        
        
      
        