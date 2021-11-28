class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mi=nums.index(min(nums))
        ma=nums.index(max(nums))
        
        ans=min(max(mi,ma)+1,len(nums)-min(mi,ma),len(nums)-mi+ma+1,len(nums)-ma+mi+1)
        
        return ans
        