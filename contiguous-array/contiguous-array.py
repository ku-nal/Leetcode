class Solution(object):
    def findMaxLength(self, li):
        """
        :type nums: List[int]
        :rtype: int
        """
        omap={0:-1}
        ans=0
        pref=0
        for i in range(len(li)):
            if li[i]==0:
                pref-=1
            else:
                pref+=1
            if pref in omap:
                ans=max(ans,i-omap[pref])
            else:
                omap[pref]=i
        return ans
        