class Solution(object):
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp=[1]*(len(s)+1)
        omap={}
        mod=(10**9)+7
        for i in range(len(s)):
            dp[i+1]=(2*dp[i])
            
            if s[i] in omap:
                dp[i+1]-=dp[omap[s[i]]]
            omap[s[i]]=i
        return (dp[-1]-1)%mod