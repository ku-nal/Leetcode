class Solution(object):
    def maxSubarraySumCircular(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(arr)
        s1,s2=0,0
        ma,mi=float('-inf'),float('inf')
        s=sum(arr)
        for i in range(n):
            s1+=arr[i]

            if s1>ma:ma=s1
            if s1<0:s1=0

            s2+=arr[i]
            if s2<mi:mi=s2
            if s2>0:s2=0

        if ma<0:return ma
        return max(ma,s-mi)