class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        visited=[[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dx=[-1,1,0,0]
        dy=[0,0,-1,1]
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and visited[i][j]==False:
                    
                    q=[[i,j]]
                    c=0
                    flag=False
                    while len(q):
                        
                        ele=q.pop(0)
                        if not visited[ele[0]][ele[1]]:
                            c+=1
                            visited[ele[0]][ele[1]]=True
                            if ele[0]==0 or ele[0]==len(grid)-1 or ele[1]==0 or ele[1]==len(grid[0])-1:
                                flag=True
                            
                            for k in range(len(dx)):
                                if ele[0]+dx[k]>=0 and ele[0]+dx[k]<len(grid) and ele[1]+dy[k]>=0 and ele[1]+dy[k]<len(grid[0]) and grid[ele[0]+dx[k]][ele[1]+dy[k]]==1:
                                    q.append([ele[0]+dx[k],ele[1]+dy[k]])
                   
                    if not flag:
                        ans+=c
        return ans
                                    
                                
                            
                            
                            
                    
        