class Solution(object):
    def maxAscendingSum(self, li):
        """
        :type nums: List[int]
        :rtype: int
        """
        su=li[0]
        n=len(li)
        ans=0
        for i in range(1,n):
            if li[i]>li[i-1]:su+=li[i]
            else:
                ans=max(su,ans)
                su=li[i]
        return max(ans,su)