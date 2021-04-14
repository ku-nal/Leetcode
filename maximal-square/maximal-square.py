class Solution(object):
    def maximalSquare(self, li):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m,n=len(li),len(li[0])
        dp=[[0 for i in range(n)] for j in range(m)]
        ans=0
        for i in range(m):
            for j in range(n):
                if li[i][j]=="1":
                    dp[i][j]=1
                    if i>0 and j>0:
                        dp[i][j]=dp[i][j]+min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])
                ans=max(ans,dp[i][j])
        print(dp)
        return ans*ans