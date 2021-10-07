import heapq
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        arr=[]
        for i in range(len(points)):
            arr.append([abs(points[i][0])**2+abs(points[i][1])**2,i])
        heapq.heapify(arr)
        ans=[]
        for i in range(k):
            val=heapq.heappop(arr)
            ans.append(points[val[1]])
        print(ans)
        return ans
        