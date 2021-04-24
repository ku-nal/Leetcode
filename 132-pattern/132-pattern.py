class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mini=nums[0]
        for i in range(len(nums)-1):
            mini=min(mini,nums[i])
            if mini!=nums[i]:
                for k in range(i+1,len(nums)):
                    if nums[i] > nums[k] and mini < nums[k]:
                        return True
        return False