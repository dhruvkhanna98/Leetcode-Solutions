# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Examples: 

# Base case: [] : []
# Example 1: No repeating numbers: [1,2] : [1,2]
# Example 2: Repeating twice: [1,1,2] , [1,2,2]: [1,2]
# Example 3: Repeating thrice : [1,1,1,2] , [1,1,2,2,2] : [1,2]
# Example 4: Repeating 4 times ; [1,1,1,1] : [1]

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        # Base case
        if head is None:
            return head

        while curr and curr.next is not None: 
            if curr.val = curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
    