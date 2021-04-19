from collections import Counter
class Solution(object):
    def canReorderDoubled(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n=len(arr)
        if n<2:
            return True
        omap=Counter(arr)
        pos,neg=[],[]
        for i in range(n):
            if arr[i]>=0:
                pos.append(arr[i])
            else:
                neg.append(arr[i])
                
        pos.sort()
        neg.sort(reverse=True)
        for i in range(len(pos)):
            if pos[i] in omap:
                omap[pos[i]]-=1
                if omap[pos[i]]==0:del omap[pos[i]]
                if 2*pos[i] in omap:
                    omap[2*pos[i]]-=1

                    if omap[2*pos[i]]==0: del omap[2*pos[i]]
                else:
                    return False

        for i in range(len(neg)):
            if neg[i] in omap:
                omap[neg[i]]-=1
                if omap[neg[i]]==0:del omap[neg[i]]
                if 2*neg[i] in omap:
                    omap[2*neg[i]]-=1

                    if omap[2*neg[i]]==0: del omap[2*neg[i]]
                else:
                    return False
        return True
        
        