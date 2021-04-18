class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr=[]
        for i in range(n):
            arr.append((2*i)+1)
        i,j=0,n-1
        ans=0
        while i<j:
            ans+=(arr[j]-arr[i])//2
            i+=1
            j-=1
        return int(ans)
            