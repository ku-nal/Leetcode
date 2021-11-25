class Solution(object):
    def canFinish(self, num, pre):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if len(pre)==0:
            return True
        self.visited=[False]*num
        self.dfsvisited=[False]*num
        self.omap={}
        for i in pre:
            if i[0] in self.omap:
                self.omap[i[0]].append(i[1])
            else:
                self.omap[i[0]]=[i[1]]
            
        
        def dfs(ele):
            self.visited[ele]=True

            self.dfsvisited[ele]=True
            
            if ele in self.omap:
                for i in self.omap[ele]:
                    if self.visited[i]==False:
                        res=dfs(i)
                        if not res:return False
                    elif self.dfsvisited[i]:
                        return False
            self.dfsvisited[ele]=False
            return True
        
        for i in range(num):
            if i in self.omap and not self.visited[i]:
                result=dfs(i)
                if result==False:return False
        return True
            
        