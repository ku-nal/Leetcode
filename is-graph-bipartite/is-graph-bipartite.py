class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        color=[-1]*len(graph)
        
        def bfs(ele):
            color[ele]=1
            q=[ele]
            
            while len(q):
                p=q.pop(0)
                
                for neigh in graph[p]:
                    if color[neigh]==-1:
                        color[neigh]=1-color[p]
                        q.append(neigh)
                    elif color[neigh]==color[p]:
                        return False
            
            return True
        
        for i in range(len(graph)):
            if color[i]==-1:
                if not bfs(i):return False
        return True