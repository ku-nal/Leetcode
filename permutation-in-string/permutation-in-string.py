from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1)>len(s2):
            return False
        omap=Counter(s1)
        omap1={}
        ans=[]
        for i in range(len(s1)):
            if s2[i] in omap1:
                omap1[s2[i]]+=1
            else:
                omap1[s2[i]]=1
        if omap1==omap:
            return True
        j=0
        for i in range(len(s1),len(s2)):
            if s2[i] in omap1:
                omap1[s2[i]]+=1
            else:
                omap1[s2[i]]=1

            if omap1[s2[j]]==1:
                del omap1[s2[j]]
            else:
                omap1[s2[j]]-=1
            if omap1==omap:
                return True
            j+=1
        return False