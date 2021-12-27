from collections import Counter
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        omap=Counter(nums)
        arr=[]
        for key,val in omap.items():
            arr.append([-val,key])
        heapq.heapify(arr)
        ans=[]
        for i in range(k):
            ele=heapq.heappop(arr)
            ans.append(ele[1])
        
        return ans
        