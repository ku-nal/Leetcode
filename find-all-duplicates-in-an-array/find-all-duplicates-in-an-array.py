from collections import Counter
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        omap=Counter(nums)
        ans=[]
        for k,v in omap.items():
            if v>1:
                ans.append(k)
        return ans
        