# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # Base Case 
        if not l1 and not l2: 
            return None
        elif l1 and not l2:
            return l1 
        elif not l1 and l2: 
            return l2
        
        centinal = ListNode(-1)
        curr = centinal
        
        while l1 and l2: 
            if l1.val < l2.val: 
                temp = l1.next
                curr.next = l1
                l1.next = None
                l1 = temp
            else: 
                temp = l2.next
                curr.next = l2
                l2.next = None
                l2 = temp
            curr = curr.next
        
        if l1: curr.next = l1
        else: curr.next = l2
        
        return centinal.next
                
                
        
                    
            
 
                    
                    
                    
        