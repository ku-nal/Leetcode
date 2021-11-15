class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ans=[]
        if len(nums)==1:
            return [[nums[0]]]
        def helper(nums,idx,li):
            if idx>=len(nums):
                self.ans.append(li[::])
                return
            for i in range(len(nums)):
                if li[i]==11:
                    li[i]=nums[idx]
                    helper(nums,idx+1,li)
                    li[i]=11
        li=[11]*len(nums)
        helper(nums,0,li)
        return self.ans