class Solution(object):
    def kClosest(self, points, K):
        
        # Base case
        if K == 0 or len(points) == 0: 
            return []
    
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        
        return points[:K]