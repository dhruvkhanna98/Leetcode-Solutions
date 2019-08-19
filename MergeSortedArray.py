class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        res = []
        i = 0
        j = 0
        
        while i < m or j < n: 
            if i < m and j < n:
                if nums1[i] <= nums2[j]: 
                    res.append(nums1[i])
                    i += 1
                else: 
                    res.append(nums2[j])
                    j += 1
            elif j < n: 
                res.append(nums2[j])
                j += 1
            else: 
                res.append(nums1[i])
                i += 1
        
        for i,n in enumerate(res): 
            nums1[i] = n