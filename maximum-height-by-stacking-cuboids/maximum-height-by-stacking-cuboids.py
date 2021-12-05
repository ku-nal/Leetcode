class Solution(object):
    def maxHeight(self, cub):
        """
        :type cuboids: List[List[int]]
        :rtype: int
        """
        for i in range(len(cub)):
            cub[i].sort()
        cub.sort()
        
        dp=[0]*len(cub)
        for i in range(len(dp)):
            dp[i]=cub[i][-1]
        
        for i in range(1,len(dp)):
            for j in range(i):
                if cub[i][0]>=cub[j][0] and cub[i][1]>=cub[j][1] and cub[i][2]>=cub[j][2]:
                    dp[i]=max(dp[i],dp[j]+cub[i][-1])
        
        return max(dp)
            