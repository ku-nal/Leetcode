class Solution(object):
    def findTargetSumWays(self, li, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.ans=0
        self.dp=[[float('-inf') for i in range(2001)]for j in range(len(li))]
        def helper(li,S,idx,su):
            if su==S and idx==len(li):
                self.ans+=1
                return 1
            if idx==len(li):
                return 0
            if self.dp[idx][su+1000]!=float('-inf'):
                return self.dp[idx][su+1000]
            
            plus=helper(li,S,idx+1,su+li[idx])
            minus=helper(li,S,idx+1,su-li[idx])
            self.dp[idx][su+1000]=plus+minus
            return self.dp[idx][su+1000]
         
    
            
        helper(li,S,0,0)
        return self.dp[0][1000]
            