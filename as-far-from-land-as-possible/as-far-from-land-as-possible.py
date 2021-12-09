class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dx=[-1,1,0,0]
        dy=[0,0,-1,1]
        ans=0
        q=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    q.append([i,j])
        
        while len(q):
            ans+=1
            size=len(q)
            while size>0:
                ele=q.pop(0)
                
                for i in range(len(dx)):
                    row=ele[0]+dx[i]
                    col=ele[1]+dy[i]
                    
                    if row>=0 and row<len(grid) and col>=0 and col<len(grid[0]) and grid[row][col]==0:
                        grid[row][col]=1
                        q.append([row,col])
                size-=1
                      
        
        return ans-1 if ans-1>0 else -1
        