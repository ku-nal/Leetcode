class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        cache = defaultdict(int)
        
        for i in range(m):
            temp0 = ''
            temp1 = ''
            for j in range(n):
                if matrix[i][j] == 0:
                    temp0 += str(j)
                else:
                    temp1 += str(j)
            cache[temp0] += 1
            cache[temp1] += 1
        return max(cache.values())