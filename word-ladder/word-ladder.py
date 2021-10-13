from collections import Counter
class Solution(object):
    def ladderLength(self, begin, end, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        omap=Counter(list(set(wordList)))
        if end not in omap:
            return 0
        q=deque([begin])
        depth=0
        while len(q):
            depth+=1
            size=len(q)
            
            while size:
                size-=1
                
                word=q.popleft()
                for i in range(len(word)):
                    for j in range(97,123):
                        temp=word[:i]+chr(j)+word[i+1:]
                        if temp!=word:
                            if temp in omap:
                                if temp==end:
                                    return depth+1
                                q.append(temp)
                                del(omap[temp])
                            
        return 0