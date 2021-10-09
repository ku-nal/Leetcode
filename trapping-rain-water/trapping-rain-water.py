class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        suf=[0]*len(height)
        pref=[0]*len(height)
        
        pref[0],suf[-1]=height[0],height[-1]
        
        for i in range(1,len(height)):
            if pref[i-1]>=height[i]:
                pref[i]=pref[i-1]
            else:
                pref[i]=height[i]
        
        for i in reversed(range(len(height)-1)):
            if suf[i+1]<=height[i]:
                suf[i]=height[i]
            else:
                suf[i]=suf[i+1]
        ans=0
        for i in range(1,len(height)-1):
            ans+=min(pref[i],suf[i])-height[i]
        return ans