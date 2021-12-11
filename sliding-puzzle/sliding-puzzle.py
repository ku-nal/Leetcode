class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        st="123450"
        temp=""
        idx=-1
        for i in range(len(board)):
            for j in range(len(board[0])):
                temp+=str(board[i][j])
        omap={0:[1,3],1:[0,2,4],2:[1,5],3:[0,4],4:[1,3,5],5:[2,4]}
        
        for i in range(len(temp)):
            if temp[i]=='0':
                idx=i
                break
        vis={}
        q=[[temp,idx]]
        level=0
        while len(q)>0:
            size=len(q)
            
            while size>0:
                ele=q.pop(0)
                if ele[0]==st:
                    return level
                
                idx1=ele[1]
                for i in omap[idx1]:
                    li=list(ele[0])
                    
                    li[idx1],li[i]=li[i],li[idx1]
                    fin=''.join(li)
                    
                    if fin not in vis:
                        vis[fin]=1
                        q.append([fin,i])
                size-=1
            level+=1
        
        return -1
                    
                