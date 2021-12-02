class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # code here
        V,M=amount,len(coins)
        dp=[[float('inf') for _ in range(V+1)] for _ in range(M+1)]
        for i in range(M+1):
            dp[i][0]=0
    
        
        for i in range(1,M+1):
            for j in range(1,V+1):
                if coins[i-1]<=j:
                    dp[i][j]=min(dp[i-1][j],1+dp[i][j-coins[i-1]])
                else:
                    dp[i][j]=dp[i-1][j]
        #print(dp)
        return dp[M][V] if dp[M][V]!=float('inf') else -1
        