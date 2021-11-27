class Solution(object):
    def makeConnected(self, n, adj):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        if len(adj)<n-1:
            return -1
        
        visited=[False]*n
        ans=0
        omap={}
        for i in adj:
            if i[0] not in omap:
                omap[i[0]]=[i[1]]
            else:
                omap[i[0]].append(i[1])
            if i[1] not in omap:
                omap[i[1]]=[i[0]]
            else:
                omap[i[1]].append(i[0])
                
        for i in range(n):
            if visited[i]==False:
                stack=[i]
                ans+=1
                while len(stack):
                    ele=stack.pop(-1)
                    visited[ele]=True
                    
                    if ele in omap:
                        
                        for neigh in omap[ele]:
                            if visited[neigh]==False:
                                stack.append(neigh)
        return ans-1