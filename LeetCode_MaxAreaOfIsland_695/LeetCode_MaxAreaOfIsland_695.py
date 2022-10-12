class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        def dfs(r,c, area_island):
            if grid[r][c] == 1:
                area_island.append(1)
                grid[r][c] = 2
                if r >= 1: dfs(r-1, c, area_island)     #движение вверх
                if r+1 < rows: dfs(r+1, c, area_island) #движение вниз
                if c >= 1: dfs(r, c-1, area_island)     #движение влево
                if c+1 < cols: dfs(r, c+1, area_island) #движение вправо
        
        rows, cols = len(grid), len(grid[0])
        i = 0
        max_island = 0
        while i < rows:
            j = 0
            while j < cols:
                if grid[i][j] == 1:
                    area_island = []
                    dfs(i,j, area_island)
                    if len(area_island) > max_island: max_island = len(area_island)
                j += 1
            i +=1
        return max_island
    
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

grid2 = [[0,0,0,0,0,0,0,0]]

max_island = Solution()
print(max_island.maxAreaOfIsland(grid2))
