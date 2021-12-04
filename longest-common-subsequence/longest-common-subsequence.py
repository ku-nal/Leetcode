class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp=[[0 for _ in range(len(text1)+1)] for _ in range(len(text2)+1)]
        
        for i in reversed(range(len(text2))):
            for j in reversed(range(len(text1))):
                if text1[j]==text2[i]:
                    dp[i][j]=1+dp[i+1][j+1]
                dp[i][j]=max(dp[i][j],dp[i+1][j],dp[i][j+1])
        return dp[0][0]
        