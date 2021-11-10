class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1 or len(nums)==0:
            return len(nums)
        hash={}
        longest=0
        for i in nums:
            hash[i]=True
        for i in nums:
            if i-1 in hash:
                hash[i]=False
        for key,val in hash.items():
            if val==True:
                s=key+1
                c=1
                while s in hash:
                    s+=1
                    c+=1
                if c>longest:
                    longest=c
        return longest
        