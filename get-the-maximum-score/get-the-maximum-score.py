class Solution(object):
    def maxSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        mod=(10**9)+7
        pt1,pt2=0,0
        s1,s2=0,0
        ans=0
        while pt1<len(nums1) and pt2<len(nums2):
            
            if nums1[pt1]<nums2[pt2]:
                s1+=nums1[pt1]
                pt1+=1
            elif nums2[pt2]==nums1[pt1]:
                ans+=max(s1,s2)+nums1[pt1]
                pt1+=1
                pt2+=1
                s1,s2=0,0
            else:
                s2+=nums2[pt2]
                pt2+=1
        
        while pt1<len(nums1):
            s1+=nums1[pt1]
            pt1+=1
        while pt2<len(nums2):
            s2+=nums2[pt2]
            pt2+=1
        
        ans+=max(s1,s2)
        
        return ans%mod
        