class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        for i in range(n):
            if nums[i]>=0:
                break
        ans=[]
        if i==0:
            for i in range(n):
                ans.append(nums[i]**2)
            return ans
        # elif i==n-1:
        #     for i in reversed(range(n)):
        #         ans.append(nums[i]**2)
        #     return ans
        else:
            pt1,pt2=i-1,i
            while pt1>=0 and pt2<len(nums):
                sq1,sq2=nums[pt1]**2,nums[pt2]**2
                if sq1<sq2:
                    ans.append(sq1)
                    pt1-=1
                else:
                    ans.append(sq2)
                    pt2+=1
            while pt1>=0:
                ans.append(nums[pt1]**2)
                pt1-=1
            while pt2<len(nums):
                ans.append(nums[pt2]**2)
                pt2+=1
            return ans