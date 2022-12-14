class Solution:
    def closedIsland(self, grid) -> int:
        def dfs(r,c):
            if grid[r][c] == 0:
                grid[r][c] = 2
                a = 0
                if r >= 1: a += dfs(r-1, c)     #движение вверх
                else: a += 1
                if r+1 < rows: a += dfs(r+1, c) #движение вниз
                else: a += 1
                if c >= 1: a += dfs(r, c-1)     #движение влево
                else: a += 1
                if c+1 < cols: a += dfs(r, c+1) #движение вправо
                else: a += 1
                return a
            return 0

        rows, cols = len(grid), len(grid[0])
        closed_islands = 0
        i = 0
        while i < rows:
            j = 0
            while j < cols:
                if grid[i][j] == 0 and dfs(i,j) == 0:
                    #print('close', i,j)
                    closed_islands += 1
                j += 1
            i +=1
        return closed_islands


grid = [[1,1,1,1,1,1,1,0],
        [1,0,0,0,0,1,1,0],
        [1,0,1,0,1,1,1,0],
        [1,0,0,0,0,1,0,1],
        [1,1,1,1,1,1,1,0]]

grid2 = [[0,0,1,0,0],
         [0,1,0,1,0],
         [0,1,1,1,0]]

grid3 = [[1,1,1,1,1,1,1],
        [1,0,0,0,0,0,1],
        [1,0,1,1,1,0,1],
        [1,0,1,0,1,0,1],
        [1,0,1,1,1,0,1],
        [1,0,0,0,0,0,1],
        [1,1,1,1,1,1,1]]

grid4 = [[0,0,1,1,0,1,0,0,1,0],
         [1,1,0,1,1,0,1,1,1,0],
         [1,0,1,1,1,0,0,1,1,0],
         [0,1,1,0,0,0,0,1,0,1],
         [0,0,0,0,0,0,1,1,1,0],
         [0,1,0,1,0,1,0,1,1,1],
         [1,0,1,0,1,1,0,0,0,1],
         [1,1,1,1,1,1,0,0,0,0],
         [1,1,1,0,0,1,0,1,0,1],
         [1,1,1,0,1,1,0,1,1,0]]

grid5 = [[1,1,0,1,1,1,1,1,1,1],
         [0,0,1,0,0,1,0,1,1,1],
         [1,0,1,0,0,0,1,0,1,0],
         [1,1,1,1,1,0,0,1,0,0],
         [1,0,1,0,1,1,1,1,1,0],
         [0,0,0,0,1,1,0,0,0,0],
         [1,0,1,0,0,0,0,1,1,0],
         [1,1,0,0,1,1,0,0,0,0],
         [0,0,0,1,1,0,1,1,1,0],
         [1,1,0,1,0,1,0,0,1,0]]

closed = Solution()
print(closed.closedIsland(grid5))
print(grid5)