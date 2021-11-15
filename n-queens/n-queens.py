class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.result=[]
        def Print(board):
            s=""
            res=[]
            for i in board:
                for j in i:
                    s+=j
                res.append(s)
                s=""
            self.result.append(res)    
                
                

        def issafe(board, row, col,n):
            for j in range(n):
                if board[row][j]=='Q':
                    return False
            for j in range(n):
                if board[j][col]=='Q':
                    return False
            i=row
            j=col
            while i< n and j< n:
                if board[i][j]=='Q':
                    return False
                i+=1
                j+=1
            i=row
            j=col
            while i>= 0 and j>=0:
                if board[i][j]=='Q':
                    return False
                i-=1
                j-=1
            i=row
            j=col
            while i>=0 and j<n:
                if board[i][j]=='Q':
                    return False
                i-=1
                j+=1
            i=row
            j=col
            while i< n and j>0:
                if board[i][j]=='Q':
                    return False
                i+=1
                j-=1
            return True

        def solve(board,row,n):
            if row==n:
                Print(board)
                return
            for j in range(n):
                if issafe(board,row,j,n)==True:
                    board[row][j]='Q'
                    solve(board,row+1,n)
                board[row][j]='.'       
        board=[['.' for i in range(n) ] for i in range(n)]
        solve(board,0,n)
        return self.result