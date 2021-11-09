class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c,ans=0,0
        
        for i in range(len(nums)):
            if c==0:
                ans=nums[i]
            if ans==nums[i]:
                c+=1
            else:c-=1
        return ans
        