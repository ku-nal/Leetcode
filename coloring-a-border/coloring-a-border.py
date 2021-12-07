class Solution(object):
    def colorBorder(self, grid, row, col, color):
        """
        :type grid: List[List[int]]
        :type row: int
        :type col: int
        :type color: int
        :rtype: List[List[int]]
        """
        self.visited=[[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        c=[]
        def helper(row,col,val,color,grid):
            
            if row<0 or col<0 or row>=len(grid) or col>=len(grid[0]):
                return 0
            if abs(grid[row][col])==val:
                if grid[row][col]<0:return 1
            else:return 0
            
            grid[row][col]=-grid[row][col]
            
            u=helper(row-1,col,val,color,grid)
            l=helper(row,col-1,val,color,grid)
            d=helper(row+1,col,val,color,grid)
            r=helper(row,col+1,val,color,grid)
            
            if u+l+d+r!=4 or row==0 or col==0 or row==len(grid)-1 or col==len(grid[0])-1:
                c.append([row,col])
            grid[row][col]=abs(grid[row][col])
            return 1
        
        
        helper(row,col,grid[row][col],color,grid)
        for i in c:
            grid[i[0]][i[1]]=color
        return grid