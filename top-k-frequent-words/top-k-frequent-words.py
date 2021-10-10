from collections import Counter
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        omap=Counter(words)
        li=[]
        for key,v in omap.items():
            li.append([v,key])
        li.sort(key=lambda x:(-x[0],x[1]))
        ans=[]
        for i in range(k):
            ans.append(li[i][1])
        return ans
        
        