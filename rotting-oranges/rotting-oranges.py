class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q1,q2=[],[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q1.append([i,j])
        ans=0
                    
        while len(q1)!=0:
            ans+=1
            for i in q1:
                if i[0]-1>=0:
                    if grid[i[0]-1][i[1]]==1:
                        grid[i[0]-1][i[1]]=2
                        q2.append([i[0]-1,i[1]])
                if i[0]+1<len(grid):
                    if grid[i[0]+1][i[1]]==1:
                        grid[i[0]+1][i[1]]=2
                        q2.append([i[0]+1,i[1]])
                if i[1]+1<len(grid[0]):
                    if grid[i[0]][i[1]+1]==1:
                        grid[i[0]][i[1]+1]=2
                        q2.append([i[0],i[1]+1])
                if i[1]-1>=0:
                    if grid[i[0]][i[1]-1]==1:
                        grid[i[0]][i[1]-1]=2
                        q2.append([i[0],i[1]-1])
            q1=q2
            q2=[]
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return -1
        return max(0,ans-1)
            
                    
        