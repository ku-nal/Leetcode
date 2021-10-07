class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        omap={}
        for i in range(len(nums)):
            if nums[i] in omap:
                omap[nums[i]].append(i)
            else:omap[nums[i]]=[i]
        
        for i in range(len(nums)):
            if target-nums[i] in omap:
                if target==2*nums[i]:
                    if len(omap[target-nums[i]])>1:
                        return [i,omap[target-nums[i]][1]]
                else:
                    return [i,omap[target-nums[i]][0]]