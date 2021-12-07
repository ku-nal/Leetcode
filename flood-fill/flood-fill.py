class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        self.nc=newColor
        visited=[[False for _ in range(len(image[0]))] for _ in range(len(image))]
        def helper(row,col,val,image):
            
            if row<0 or row>=len(image) or col<0 or col>=len(image[0]) or image[row][col]!=val or visited[row][col]:
                return
           
            image[row][col]=self.nc
            visited[row][col]=True
            helper(row-1,col,val,image)
            helper(row,col-1,val,image)
            helper(row,col+1,val,image)
            helper(row+1,col,val,image)
        
        helper(sr,sc,image[sr][sc],image)
        return image
        
        
        