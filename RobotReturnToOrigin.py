class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        # Base case
        if moves == "": 
            return True
        
        if moves.count("R") == moves.count("L") and moves.count("U") == moves.count("D"):
            return True
        else: 
            return False
        
        
        