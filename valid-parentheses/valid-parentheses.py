class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        
        for i in range(len(s)):
            if s[i]=="{" or s[i]=="[" or s[i]=="(":
                stack.append(s[i])
            else:
                if len(stack)==0:
                    return False
                if s[i]=="}":
                    if stack[-1]!="{":
                        return False
                    stack.pop()
                if s[i]=="]":
                    if stack[-1]!="[":
                        return False
                    stack.pop()
                if s[i]==")":
                    if stack[-1]!="(":
                        return False
                    stack.pop()
        if len(stack)==0:return True
        return False