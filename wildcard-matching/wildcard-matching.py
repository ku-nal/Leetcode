class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp=[[False for i in range(len(s)+1)] for _ in range(len(p)+1)]
        
        for i in reversed(range(len(p)+1)):
            for j in reversed(range(len(s)+1)):
                if i==len(p) and j==len(s):
                    dp[i][j]=True
                elif i==len(p):
                    continue
                elif j==len(s):
                    if p[i]=="*":
                        dp[i][j]=dp[i+1][j]
                else:
                    if p[i]=="?":
                        dp[i][j]=dp[i+1][j+1]
                    elif p[i]=="*":
                        dp[i][j]=dp[i+1][j] | dp[i][j+1]
                    else:
                        if p[i]==s[j]:
                            dp[i][j]=dp[i+1][j+1]
        return dp[0][0]
            