class Solution(object):
    def groupAnagrams(self, li):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans=[]
        omap={}
        for i in range(len(li)):
            temp=list(li[i])
            temp.sort()
            st=''.join(temp)
            if st in omap:
                omap[st].append(li[i])
            else:
                omap[st]=[li[i]]
        
        for k,v in omap.items():
            ans.append(v)
        return ans