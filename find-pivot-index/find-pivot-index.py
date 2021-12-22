class Solution(object):
    def pivotIndex(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        N=len(A)
        if N==1:return 1
        s=sum(A)
        pt1=0
        
        for i in range(N):
            if pt1*2==s-A[i]:
                return i
            pt1+=A[i]
        return -1
        