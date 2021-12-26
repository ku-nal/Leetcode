class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        maxcl=0
        min=float('inf')
        for i in range(len(nums)-1):
            left=i+1
            right=len(nums)-1
        
            while left < right:
                su=nums[i]+nums[left]+nums[right]
                if(su==target):
                    return target
                elif(su<target):
                    left+=1
                else:
                    right-=1
                if abs(su-target) < min:
                    min=abs(su-target)
                    maxcl=su
                elif abs(su-target) == min:
                    if su>maxcl:
                        maxcl=su
        return maxcl       