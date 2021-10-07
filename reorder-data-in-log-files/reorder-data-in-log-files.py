class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        num,alp=[],[]
        for i in range(len(logs)):
            arr=logs[i].split()
            if arr[1].isnumeric():
                num.append(i)
            else:
                alp.append([arr[1:],arr[0],i])
        alp.sort()
        ans=[]
        for i in alp:
            ans.append(logs[i[-1]])
        for i in num:
            ans.append(logs[i])
        
        return ans
            
                
                
        