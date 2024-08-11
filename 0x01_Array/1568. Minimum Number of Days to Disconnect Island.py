class Solution:
    def minDays(self, grid):
        def count_islands(g):
            seen = set()
            def dfs(i, j):
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < len(g) and 0 <= ny < len(g[0]) and g[nx][ny] == 1 and (nx, ny) not in seen:
                            seen.add((nx, ny))
                            stack.append((nx, ny))

            count = 0
            for i in range(len(g)):
                for j in range(len(g[0])):
                    if g[i][j] == 1 and (i, j) not in seen:
                        seen.add((i, j))
                        dfs(i, j)
                        count += 1
            return count

        if count_islands(grid) != 1:
            return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count_islands(grid) != 1:
                        return 1
                    grid[i][j] = 1

        return 2


    
if __name__ == "__main__":
    one = Solution()
    grid1 = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
    grid2 = [[1,1]]
    print(one.minDays(grid1))  # Output: 2
    print(one.minDays(grid2))  # Output: 2