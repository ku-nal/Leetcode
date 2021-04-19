class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans=""
        n=len(strs)
        mi=float('inf')
        for i in strs:
            if mi > len(i):
                mi=len(i)
        if mi==float('inf'):
            return ""
        for i in range(mi):
            ss=strs[0][i]
            tr=False
            for j in range(1,n):
                if strs[j][i]!=ss:
                    tr=True
                    break
                      
            if tr:break
            else:
                ans+=ss
        return ans
                    