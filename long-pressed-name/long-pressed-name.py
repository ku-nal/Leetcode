class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        if name[0]!=typed[0]:
            return False
        j=0
        for i in range(len(typed)):
            if j!=len(name) and typed[i]==name[j]:
                j+=1
            elif typed[i]!=name[j-1]:
                return False
        if j==len(name):return True
        return False