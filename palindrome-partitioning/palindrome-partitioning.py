class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.ans=[]
        self.temp=[]
        if len(s)==1:
            return [[s[0]]]
        if len(s)==0:
            return [[]]
        def helper(s,ans,temp):
            if len(s)==0:
                self.ans.append(self.temp[::])
                return
            for i in range(len(s)):
                st=s[:i+1]
                if ispalindrome(st):
                    helper(s[i+1:],ans,self.temp.append(st))
                    self.temp.pop()
                    
        def ispalindrome(st):
            if st==st[::-1]:
                return True
            return False
        
        helper(s,self.ans,self.temp)
        return self.ans
        