class Solution(object):
    def majorityElement(self, A):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        c1,c2=0,0
        num1,num2=float('inf'),float('inf')
        n=len(A)//3
        for i in range(len(A)):
            if A[i]==num1:
                c1+=1
            elif A[i]==num2:
                c2+=1
            elif c1==0:
                num1=A[i]
                c1+=1
            elif c2==0:
                num2=A[i]
                c2+=1
            else:
                c1-=1
                c2-=1
        
        c1,c2=0,0
        
        for i in range(len(A)):
            if A[i]==num1:
                c1+=1
            elif A[i]==num2:
                c2+=1
        
        if c1>n and c2>n:
            return[num1,num2]
        if c1>n:
            return [num1]
        if c2>n:
            return [num2]
        