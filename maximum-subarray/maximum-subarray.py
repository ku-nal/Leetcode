class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ma=float('-inf')
        add=0
        for i in range(len(nums)):
            add+=nums[i]
            
            ma=max(add,ma)
            if add<0:
                add=0
        return ma
        