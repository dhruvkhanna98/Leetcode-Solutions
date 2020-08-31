class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        n = len(nums1)
        m = len(nums2)
        
        # Base case 
        if n == 0 or m == 0: return []
     
        res = list(set(nums1) & set(nums2))
        
        return res