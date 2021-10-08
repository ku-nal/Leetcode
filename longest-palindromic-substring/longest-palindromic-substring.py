class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==1:
            return s
        l=0
        ans=""
        for i in range(len(s)):
            id1,id2=i,i
            c=1
            while id1-1>=0 and id2+1<len(s):
                if s[id1-1]==s[id2+1]:
                    if (2*c)+1>l:
                        l=(2*c)+1
                        ans=s[id1-1:id2+2]
                else:
                    break
                id1-=1
                id2+=1
                c+=1
        
        for i in range(len(s)):
            id1,id2=i,i
            c=1
            while id1>=0 and id2+1<len(s):
                if s[id1]==s[id2+1]:
                    if 2*c>l:
                        l=2*c
                        ans=s[id1:id2+2]
                else:
                    break
                id1-=1
                id2+=1
                c+=1
        if ans=="":
            return s[0]
        return ans
                