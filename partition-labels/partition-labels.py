from collections import OrderedDict
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        omap=OrderedDict()
        for i in range(len(s)):
            if s[i] in omap:
                omap[s[i]].append(i)
            else:
                omap[s[i]]=[i]
        interval=[]
        for k,v in omap.items():
            interval.append([v[0],v[-1]])
        i=1
        while i<len(interval):
            if interval[i][0]>interval[i-1][1]:
                pass
            else:
                temp=[interval[i-1][0],max(interval[i-1][1],interval[i][1])]
                interval[i]=temp
                interval.pop(i-1)
                i-=1
            i+=1
        ans=[]
        
        for i in range(len(interval)):
            ans.append(interval[i][1]-interval[i][0]+1)
        return ans
            