class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        src=0
        dest=len(graph)-1
        self.ans=[]
        def helper(src,dest,graph,path):
            if src==dest:
                self.ans.append(path)
                return
            for i in graph[src]:
                helper(i,dest,graph,path+[i])
        helper(src,dest,graph,[src])
        return self.ans
        