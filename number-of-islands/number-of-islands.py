class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited=[[False for i in range(len(grid[0]))]for j in range(len(grid))]
        ans=0
        def visitisland(grid,i,j,visited):
            
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]=="0" or visited[i][j]==True:
                return
            visited[i][j]=True
            visitisland(grid,i-1,j,visited)
            visitisland(grid,i+1,j,visited)
            visitisland(grid,i,j-1,visited)
            visitisland(grid,i,j+1,visited)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and visited[i][j]==False:
                    visitisland(grid,i,j,visited)
                    ans+=1
        return ans