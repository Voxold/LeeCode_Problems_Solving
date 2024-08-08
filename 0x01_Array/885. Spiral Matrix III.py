from collections import List


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
        result = []
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        steps = 1
        r, c = rStart, cStart
        result.append([r, c])
        dir_idx = 0
    
        while len(result) < rows * cols:
            for _ in range(2):
                for _ in range(steps):
                    r += direction[dir_idx][0]
                    c += direction[dir_idx][1]
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])
                dir_idx = (dir_idx + 1) % 4
            steps += 1
        
        return result