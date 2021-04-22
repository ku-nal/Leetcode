class Solution(object):
    def wiggleMaxLength(self, li):
        """
        :type nums: List[int]
        :rtype: int
        """
        def sgn(n):
            if n>0:
                return 1
            elif n==0:
                return 0
            else:
                return -1
        ans=1
        prev=0
        for i in range(1,len(li)):
            curr=sgn(li[i]-li[i-1])
            
            if curr!=prev and curr!=0:
                ans+=1
                prev=curr
        return ans
            