class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        def func(arr):
            return arr[1]
        
        pairs=sorted(pairs,key=func)
        ans=1
        ele=pairs[0]
        
        for i in range(1,len(pairs)):
            
            if pairs[i][0]>ele[1]:
                ele[1]=pairs[i][1]
                ans+=1
        return ans