class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # Base case 
        if grid == None or grid == []: 
            return 0
        
        num_islands = 0
        
        for i,n in enumerate(grid):
            for j,m in enumerate(n):
                
                if m == "1": 
                    num_islands += self.dfs(grid, i, j)
                    
        return num_islands
    
    def dfs(self, grid: List[List[str]], i, j):
        
        # Base case
        if (i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == "0"):
            return 0 
        
        grid[i][j] = "0"
        # right
        self.dfs(grid, i + 1, j)
        # left
        self.dfs(grid, i - 1, j)
        # down
        self.dfs(grid, i, j + 1)
        # up
        self.dfs(grid, i, j - 1)
        
        return 1
                    
                
        