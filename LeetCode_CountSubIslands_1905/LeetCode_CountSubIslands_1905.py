class Solution:
    def countSubIslands(self, grid1, grid2) -> int:
        def dfs(r,c,coordinate):
            if grid2[r][c] == 1:
                coordinate.append((r,c))
                grid2[r][c] = 2
                if r >= 1: dfs(r-1, c, coordinate)     #движение вверх
                if r+1 < rows: dfs(r+1, c, coordinate) #движение вниз
                if c >= 1: dfs(r, c-1, coordinate)     #движение влево
                if c+1 < cols: dfs(r, c+1, coordinate) #движение вправо
        
        def check_islands(grid1, coords):
            for coord in coords:
                r,c = coord
                if grid1[r][c] != 1:
                    return False
            return True
                       
        rows, cols = len(grid2), len(grid2[0])
        coordinates = []   
        id_coord = 0
        i = 0
        while i < rows:
            j = 0
            while j < cols:
                if grid2[i][j] == 1:
                    coordinates.append([])
                    dfs(i,j,coordinates[id_coord])
                    id_coord += 1
                j += 1
            i +=1

        sub_islands = 0
        for i in coordinates:
            if check_islands(grid1, i):
                sub_islands += 1
        return sub_islands


grid1 = [[1,1,1,0,0],
         [0,1,1,1,1],
         [0,0,0,0,0],
         [1,0,0,0,0],
         [1,1,0,1,1]] 

grid2 = [[1,1,1,0,0],
         [0,0,1,1,1],
         [0,1,0,0,0],
         [1,0,1,1,0],
         [0,1,0,1,0]]

grid10 = [[1,0,1,0,1],
          [1,1,1,1,1],
          [0,0,0,0,0],
          [1,1,1,1,1],
          [1,0,1,0,1]]

grid20 = [[0,0,0,0,0],
          [1,1,1,1,1],
          [0,1,0,1,0],
          [0,1,0,1,0],
          [1,0,0,0,1]]

countSub = Solution()
print(countSub.countSubIslands(grid10, grid20))
