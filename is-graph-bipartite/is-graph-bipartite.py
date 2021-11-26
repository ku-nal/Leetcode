class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        visited=[-1]*len(graph)
        def isbipartite(src,graph,visited):
            queue=[]
            queue.append([src,0])
            while len(queue)>0:
                rem=queue.pop(0)
                if visited[rem[0]]!=-1:
                    if visited[rem[0]]!=rem[1]:
                        return False
                else:
                    visited[rem[0]]=rem[1]
                for i in graph[rem[0]]:
                    if visited[i]==-1:
                        queue.append([i,rem[1]+1])
            return True
            
        for i in range(len(graph)):
            if visited[i]==-1:
                boo=isbipartite(i,graph,visited)
                if not boo:
                    return False
                
        return True
                
        