class Solution:
    def isMagicSquare(self, grid, r, c):
        s = set()
        for i in range(r, r+3):
            for j in range(c, c+3):
                if grid[i][j] < 1 or grid[i][j] > 9 or grid[i][j] in s:
                    return False
                s.add(grid[i][j])
    
        return (grid[r][c] + grid[r][c+1] + grid[r][c+2] == 
                grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] == 
                grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] == 
                grid[r][c] + grid[r+1][c] + grid[r+2][c] == 
                grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] == 
                grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] == 
                grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] == 
                grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c])

    def numMagicSquaresInside(self, grid):
        rows, cols = len(grid), len(grid[0])
        count = 0
        for r in range(rows - 2):
            for c in range(cols - 2):
                if self.isMagicSquare(grid, r, c):
                    count += 1
        return count
