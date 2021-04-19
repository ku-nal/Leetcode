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
    
   

'''''Approach'''''''
So the question is solved using Dynamic Programming.

So if we want to increase the length of our square we want to check our previous state also. So the states that are contributing to the current state is the previous cell in the
same row, previous cell in the same columns ans the state [i-1][j-1] (One Row up and one Column up). So if the current cell having value equals to 1 then we check these states.
So, we have to find the minimum value among these previous states. So the new produced square is of having side equals to 1+min(states([i-1][j],[i][j-1],[i-1][j-1])). 

For any query mail me at :
kunalmakwana18@gnu.ac.in
''''''''''''''''''''
