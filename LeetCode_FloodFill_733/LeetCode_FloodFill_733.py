class Solution:
    def floodFill(self, image, sr, sc, newColor):
        rows, cols = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        def dfs(r,c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: dfs(r-1, c)     #движение вверх
                if r+1 < rows: dfs(r+1, c) #движение вниз
                if c >= 1: dfs(r, c-1)     #движение влево
                if c+1 < cols: dfs(r, c+1) #движение вправо
        dfs(sr,sc)
        return image


image = [[1,1,1],[1,1,0],[1,0,1]]
sr,sc = 1,1 # координаты стартового пикселя image[sr][sc]
color = 2
color_fill = Solution()
print(color_fill.floodFill(image,sr,sc,color))









#Output:  [[2,2,2],[2,2,0],[2,0,1]]