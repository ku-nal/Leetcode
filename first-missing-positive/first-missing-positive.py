class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        
        while i<len(nums):
            cpos=nums[i]-1
            
            while 1<=nums[i]<=len(nums) and nums[cpos]!=nums[i]:
                nums[cpos],nums[i]=nums[i],nums[cpos]
                cpos=nums[i]-1
            i+=1
        
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        
        return len(nums)+1
        