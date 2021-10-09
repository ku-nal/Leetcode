class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool"""
        
        reachable=0
        if len(nums)==1:
            return True
        for i in range(len(nums)-1):
            if reachable<i:
                return False
            reachable=max(reachable,i+nums[i])
            if reachable>=len(nums)-1:
                return True
        return False
            
                
                    
                
                
            