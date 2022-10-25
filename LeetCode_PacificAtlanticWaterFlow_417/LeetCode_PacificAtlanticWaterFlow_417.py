class Solution:
    def pacificAtlantic(self, heights):
        def dfs(r,c,p,a,coords):
            if (r,c) in coords: return
            coords.add((r,c))
            if r >= 1:          #движение вверх
                if heights[r-1][c] <= heights[r][c]: dfs(r-1,c,p,a,coords)
            else:
                p+=1
            if c >= 1:          #движение влево    
                if heights[r][c-1] <= heights[r][c]: dfs(r,c-1,p,a,coords)
            else:
                p+=1
            if r+1 < rows:      #движение вниз
                if heights[r+1][c] <= heights[r][c]: dfs(r+1,c,p,a,coords)
            else: 
                a+=1 
            if c+1 < cols:      #движение вправо
                if heights[r][c+1] <= heights[r][c]: dfs(r,c+1,p,a,coords)
            else:
                a+=1
                print(a)
        

        rows, cols = len(heights), len(heights[0])
        i = 0
        heights_pa = set()
        while i < rows:
            j = 0
            while j < cols:
                p,a,coords = 0, 0, set()
                dfs(i,j,p,a,coords)
                if p != 0 and a != 0: heights_pa.add((i,j))
                j += 1
            i +=1
        return heights_pa

heights = [[1,2,2,3,5],
           [3,2,3,4,4],
           [2,4,5,3,1],
           [6,7,1,4,5],
           [5,1,1,2,4]]

pA = Solution()
print(pA.pacificAtlantic(heights))
