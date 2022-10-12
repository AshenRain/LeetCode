class Solution:
    def numIslands(self, grid) -> int:
        def dfs(r,c):
            if grid[r][c] == '1':
                grid[r][c] = '2'
                if r >= 1: dfs(r-1, c)     #движение вверх
                if r+1 < rows: dfs(r+1, c) #движение вниз
                if c >= 1: dfs(r, c-1)     #движение влево
                if c+1 < cols: dfs(r, c+1) #движение вправо
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        i = 0
        while i < rows:
            j = 0
            while j < cols:
                if grid[i][j] == '1':
                    dfs(i,j)
                    islands += 1
                j += 1
            i +=1
        return islands
                
            
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

count_Islands = Solution()
print(count_Islands.numIslands(grid2))

