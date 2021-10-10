class Solution(object):
    def searchMatrix(self,grid,target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in range(len(grid)):
            if grid[i][-1]>=target:
                left,right=0,len(grid[0])-1
                
                while left<=right:
                    mid=(left+right)//2
                    if grid[i][mid]==target:
                        return True
                    if grid[i][mid]>target:
                        right=mid-1
                    else:
                        left=mid+1
        return False
                    
        