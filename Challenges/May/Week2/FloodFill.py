class Solution:
    def changeColor(self,matrix,sr,sc,newColor,initial,r,c):
        if sr <0 or sr >= r or sc < 0 or sc >=c :
            return 
        elif matrix[sr][sc] != newColor and matrix[sr][sc] == initial :
            matrix[sr][sc] = newColor
            self.changeColor(matrix,sr-1,sc,newColor,initial,r,c)
            self.changeColor(matrix,sr+1,sc,newColor,initial,r,c)
            self.changeColor(matrix,sr,sc+1,newColor,initial,r,c)
            self.changeColor(matrix,sr,sc-1,newColor,initial,r,c)           
        else:
            return
        
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        r = len(image)
        c = len(image[0])
        initial = image[sr][sc]
        self.changeColor(image,sr,sc,newColor,initial,r,c)
        return image
    
