from collections import deque
class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        que=deque()
        que.append(0)
        for i in range(len(s)):
            if s[i]=="0":
                while len(que) and que[0]<i-maxJump:
                    que.popleft()
                
                if len(que) and i>=que[0]+minJump and i<=que[0]+maxJump:
                    que.append(i)
                    if i==len(s)-1:
                        return True
            if len(que)==0:
                return False
                
        return False
            
        