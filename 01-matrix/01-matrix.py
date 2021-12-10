class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        q=[]
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    q.append([i,j])
                else:
                    mat[i][j]=-1
        dx=[0,0,-1,1]
        dy=[1,-1,0,0]
        while len(q)>0:
            ele=q.pop(0)
            
            for i in range(len(dx)):
                row=ele[0]+dx[i]
                col=ele[1]+dy[i]
                
                if row>=0 and row<len(mat) and col>=0 and col<len(mat[0]) and mat[row][col]<0:
                    q.append([row,col])
                    mat[row][col]=mat[ele[0]][ele[1]]+1
        return mat
        