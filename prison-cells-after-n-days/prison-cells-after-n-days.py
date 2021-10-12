class Solution(object):
    def prisonAfterNDays(self, cells, n):
        """
        :type cells: List[int]
        :type n: int
        :rtype: List[int]
        """
        omap={tuple(cells):0}
        rem=0
        for i in range(1,65):
            b=cells[:]
            if i==1:
                b[0],b[-1]=0,0
            for j in range(1,7):
                if cells[j+1]==cells[j-1]:
                    b[j]=1
                else:
                    b[j]=0
            if tuple(b) in omap:
                fi=omap[tuple(b)]
                cycle=i-fi
                rem=(n-fi)%cycle
                cells=b[:]
                break
            else:
                omap[tuple(b)]=i
            cells=b[:]

        for i in range(rem):
            b=cells[:]
            for j in range(1,7):
                if cells[j+1]==cells[j-1]:
                    b[j]=1
                else:
                    b[j]=0
            cells=b[:]
        return cells
            
            
                
                    
                
                
                