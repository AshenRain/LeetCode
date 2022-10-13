class Solution:
    def numEnclaves(self, grid) -> int:
        def dfs(r,c):
            if grid[r][c] == 1:
                grid[r][c] = 2
                if r >= 1: dfs(r-1, c)     #движение вверх
                if r+1 < rows: dfs(r+1, c) #движение вниз
                if c >= 1: dfs(r, c-1)     #движение влево
                if c+1 < cols: dfs(r, c+1) #движение вправо
        
        rows, cols = len(grid), len(grid[0])
        #Проход по краям
        i = 0
        while i < rows:
            if i == 0 or i == rows - 1:
                j = 0
                while j < cols:
                    if grid[i][j] == 1:
                        dfs(i,j)
                    j += 1
            else:
                if grid[i][0] == 1:
                    dfs(i,0)
                if grid[i][cols-1] == 1:
                    dfs(i,cols-1)                    
            i +=1
        
        #Подсчет островов, до которых мы не можем добраться      
        islands = 0
        i = 1
        while i < rows - 1:
            j = 1
            while j < cols - 1:
                if grid[i][j] == 1:
                    islands += 1
                j += 1
            i +=1
        return islands


grid = [[0,0,0,0],
        [1,0,1,0],
        [0,1,1,0],
        [0,0,0,0]]

grid1 = [[0,1,1,0],
        [0,0,1,0],
        [0,0,1,0],
        [0,0,0,0]]
count_enclaves = Solution()
print(count_enclaves.numEnclaves(grid1))



