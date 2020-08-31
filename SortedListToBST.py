# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:        
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        
        # Base case
        if not head: return None
        
        nodes = list()
        
        while head: 
            nodes.append(head.val)
            head = head.next
        
        def buildTree(nodes):
        
            n = len(nodes)

            # Base case 
            if n == 0: return None

            start = 0
            end = n
            mid = (start+end)//2

            root = TreeNode(nodes[mid])
            root.left = buildTree(nodes[:mid])
            root.right = buildTree(nodes[mid+1:])

            return root
    
        return buildTree(nodes)
    
            
        
        
       