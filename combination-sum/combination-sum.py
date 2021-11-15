class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans=[]
        path=[]
        self.dfs(candidates,target,path,ans)
        return ans
    
    def dfs(self,arr,target,path,ans):
        if target < 0:
            return
        if target==0:
            ans.append(path)
            
        for i in range(len(arr)):
            self.dfs(arr[i:],target-arr[i],path+[arr[i]],ans)
            
        