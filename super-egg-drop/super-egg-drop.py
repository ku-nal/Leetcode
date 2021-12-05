# class Solution(object):
#     def superEggDrop(self, k, n):
#         """
#         :type k: int
#         :type n: int
#         :rtype: int
#         """
#         dp=[[0 for _ in range(n+1)] for _ in range(k+1)]
        
#         for i in range(1,k+1):
#             for j in range(1,n+1):
#                 if i==1:
#                     dp[i][j]=j
#                 elif j==1:
#                     dp[i][j]=1
#                 else:
#                     a,b=0,j-1
#                     mi=float('inf')
#                     while a<=j-1:
#                         ma=max(dp[i-1][a],dp[i][b])
#                         mi=min(mi,ma)
#                         a+=1
#                         b-=1
#                     dp[i][j]=mi
#         print(dp)
#         return dp[k][n]
class Solution(object):
    def superEggDrop(self, K, N):
        def f(x):
            ans = 0
            r = 1
            for i in range(1, K+1):
                r *= x-i+1
                r //= i
                ans += r
                if ans >= N: break
            return ans

        lo, hi = 1, N
        while lo < hi:
            mi = (lo + hi) // 2
            if f(mi) < N:
                lo = mi + 1
            else:
                hi = mi
        return lo       
        