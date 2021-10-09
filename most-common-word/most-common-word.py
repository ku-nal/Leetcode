from collections import Counter
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        punc="!?',;."
        paragraph=paragraph.lower()
        for i in punc:
            paragraph=paragraph.replace(i," ")
        
        arr=paragraph.split()
        omap=Counter(arr)
        freq=0
        ans=""
        for key,val in omap.items():
            if key not in banned:
                if val>freq:
                    ans=key
                    freq=val
        return ans
                    
        